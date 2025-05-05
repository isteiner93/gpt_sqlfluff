## GPT_SQLFluff
This script utilizes SQLFluff and OpenAI's GPT-3 to implement suggested linting and formatting for selected SQL code
(slido-dbt_transformation table).


### How to use
1. Obtain the Webex API token [link](https://developer-portal.int-first-general1.ciscospark.com/docs/getting-started)
2. `export WEBEX_CI_API_KEY=<your_webex_api_token>`
3. `cd ./slido-etl/utils/gpt_sqlfluff/`
4. `pip install -r requirements.txt`
5. Navigate to the `gpt_sqlfluff.py` and define your local path for the `slido-dbt-transformations` directory and the file you want to lint.
- directory = "`/local_path/`slido-etl/slido-dbt-transformations/"
- file_name = "models/reports/general/`file.sql`"
6. Run the script `python gpt_sqlfluff.py`

### Always check the output before committing the changes!
