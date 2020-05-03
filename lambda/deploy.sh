zip smsListener.zip smsListener.py
aws lambda update-function-code --function-name "smsListener" --zip-file fileb://smsListener.zip
