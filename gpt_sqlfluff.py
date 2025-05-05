import os
import subprocess
from pathlib import Path

import gpt_sqlfluff_prompt_helper as helper
import openai

openai.api_key = os.getenv("WEBEX_CI_API_KEY")
openai.api_type = "azure_ad"
openai.api_version = "2023-05-15"
openai.api_base = "https://llm-proxy.us-east-2.int.infra.intelligence.webex.com/azure/v1"


def get_directory():
    current_dir = Path(__file__).resolve().parent
    etl_root = current_dir.parent.parent
    directory = etl_root / "slido-dbt-transformations"
    return directory


def lint_sql_file(directory, file_name):
    # Navigate to the repository directory
    os.chdir(directory)
    # Build the full path to the SQL file
    sql_file_path = os.path.join(directory, file_name)

    try:
        # Read the content of the SQL file
        with open(sql_file_path, "r") as file:
            sql_content = file.read()

        # Construct the command to run
        command = f"sqlfluff lint {file_name}"
        # Run the command with the SQL content as input
        result = subprocess.run(command, shell=True, capture_output=True, text=True, cwd=directory)

        print(f"Successfully linted {file_name} using sqlfluff.")
        # Extract lint errors from the result
        # lint_errors = result.stdout.strip()

        lint_errors = [
            line.replace("L:", "Line").replace("P:", "Position")
            for line in result.stdout.split("\n")
            if line.strip()
            and not line.startswith("===")
            and not line.startswith("==")
            and not line.startswith("WARNING:")
            and not line.startswith("All")
        ]
        return "\n".join(lint_errors), sql_content

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return None, None


def sqlfluff_ai(lint_errors, sql_content):
    if lint_errors:
        prompt = helper.create_sqlfluff_prompt(lint_errors, sql_content)
        # print(prompt)
        completion = openai.ChatCompletion.create(
            deployment_id="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful coding assistant. "
                    "I need help with the following SQL code.",
                },
                {"role": "user", "content": prompt},
            ],
        )
        reply_content = completion.choices[0].message.content
        return reply_content

    else:
        print("No lint errors found. Nothing to fix.")
        return None


def update_sql_file(directory, file_name, corrected_content):
    updated_sql_file_path = os.path.join(directory, file_name)
    with open(updated_sql_file_path, "w") as file:
        file.write(corrected_content)
        print(f"Updated {file_name} with the corrected content.")


# Example usage
directory = get_directory()
file_name = "models/transformations/general/mv_typeform_responses_answers.sql"
lint_errors, sql_content = lint_sql_file(directory, file_name)
corrected_content = sqlfluff_ai(lint_errors, sql_content)

if corrected_content:
    update_sql_file(directory, file_name, corrected_content)
