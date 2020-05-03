# apartments
searching for apartments, assembling a dataset about apartments in the areas we're interested

labmda:
  smsListener.py: Lambda for handling events from PinPoint SNS queue
  deploy.sh: packages smsListener.py and deploys to Lambda
api:
  api.py: basic Flask api for sqlite3 database
