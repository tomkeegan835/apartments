import json, boto3

# create s3 client
s3 = boto3.client('s3')

def smsHandler(event, context):

    # print event for logging purposes
    print(json.dumps(event))

    # get url from event
    url = (json.loads(event['Records'][0]['Sns']['Message'])["messageBody"])

    with open('listingUrls.txt', 'wb') as listingUrlsFile:
        s3.download_fileobj('com.tom.apartments', 'listingUrls.txt', listingUrlsFile)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
