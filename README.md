# apartments
searching for apartments, assembling a dataset about apartments in the areas we're interested

api:
  api.py: basic Flask api for sqlite3 database

lambda:
  smsListener.py: translates SNS message form Pinpoint into SNS message for Flask to process
  delpoy.sh: deploy to lambda
