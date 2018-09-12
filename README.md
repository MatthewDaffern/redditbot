# redditbot
Bot that uses a reddit account to post in response to a query

<<<<<<< HEAD
It works with the Biblia REST API and ESV REST API to post verses in response to redditors.

## Setup

Make sure you have the necessary API keys. Put them in a file called `file name here` in `some sort of` format.

To upload to AWS and start running your function:

 1. Package everything together, including PRAW and other imported libraries
 2. Upload the resulting packaged file to S3
 3. Upload `scripture_bot_cfn.json` to S3
 4. Go to CloudFormation in the AWS console, and create a new cloudformation stack from a template
 5. Use the `scripture_bot_cfn.json` template you uploaded in step 3.
 6. When prompted, enter the S3 bucket and key for the code package that you uploaded in step 2.
 7. Choose the configuration for the Lambda function. If you don't know what you want to do, consider setting the memory to 256, the MaxRunTime to 180, and the RecurrenceTime to 5.
 8. Follow the prompts to finish setting up the bot.

 Alternately:

 1. Package everything together, including PRAW and other imported libraries
 2. Upload the resulting packaged file to S3
 3. Go to the CloudFormation visual editor
 4. Copy the content of `scripture_bot_cfn.json` to the text box in the visual editor, and run it.
 5. When prompted, enter the S3 bucket and key for the code package that you uploaded in step 2.
 6. Choose the configuration for the Lambda function. If you don't know what you want to do, consider setting the memory to 256, the MaxRunTime to 180, and the RecurrenceTime to 5.
 7. Follow the prompts to finish setting up the bot.
=======
It works with the Biblia REST API and ESV REST API to post verses in response to redditors and is designed for Lambda AWS
>>>>>>> queries
