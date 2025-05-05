# GPT_SQLFluff
###*This Project is specific to my work environment and rather serves as an insipiration than a ready-to-use product. Replicating it locally requires some adjustments*###

This script utilizes SQLFluff and OpenAI's GPT-3 to implement suggested linting and formatting for selected SQL code (`slido-dbt-transformation` table).

## How It Works

1. **Linting with SQLFluff**: The script lints a given SQL file using SQLFluff to identify and capture formatting errors.
2. **AI Correction**: It then uses GPT-3 via Webex API to generate corrections for the identified linting errors.
3. **File Update**: The script updates the original SQL file with the corrected formatting.

## How to Use

1. Obtain the Webex API token [link](https://developer-portal.int-first-general1.ciscospark.com/docs/getting-started)
2. `export WEBEX_CI_API_KEY=<your_webex_api_token>`
3. `cd ./slido-etl/utils/gpt_sqlfluff/`
4. `pip install -r requirements.txt`
5. Navigate to the `gpt_sqlfluff.py` and define your local path for the `slido-dbt-transformations` directory and the file you want to lint.
- directory = "`/local_path/`slido-etl/slido-dbt-transformations/"
- file_name = "models/reports/general/`file.sql`"
6. Run the script `python gpt_sqlfluff.py`

### Always check the output before committing the changes!

