import json
import urllib3

def smsHandler(event, context):

    # get url from event
    listingUrl = json.loads(event['Records'][0]['Sns']['Message'])["messageBody"]

    print(listingUrl)

    http = urllib3.PoolManager()

    response = http.request(method='POST',url=f'http://54.188.29.69/urls/{listingUrl}')

    print(response.data)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
