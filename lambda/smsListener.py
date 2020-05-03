import json

def smsHandler(event, context):

    # get url from event
    url = json.loads(event['Records'][0]['Sns']['Message'])["messageBody"]

    

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
