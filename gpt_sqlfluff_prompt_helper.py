def create_sqlfluff_prompt(lint_errors, sql_content):
    prompt = f"""
Assign a virtual line number for each row/line of the SQL code below:

{sql_content}

Correct the formatting errors listed below on the specified lines of the SQL code above:

{lint_errors}.

Additional Notes:
This prompt combines the instructions for different issues into a single block.
Line numbers are highlighted for specific errors.
The prompt clarifies the desired outcome for the indentation issue.
Only fix the formatting errors and do not change anything else in the SQL code.
Return only code with no further explanation of the changes made."""
    return prompt
