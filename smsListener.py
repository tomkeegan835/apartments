import json

def lambda_handler(event, context):
    
    print('EVENT:\n\n',event,'\n\n')
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
