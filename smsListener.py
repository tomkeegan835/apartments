import json, boto3

s3 = boto3.client('s3')

def smsHandler(event, context):

    print(event)

    url = (json.loads(event['Records'][0]['Sns']['Message'])["messageBody"])

    with open('listingUrls.txt', 'wb') as listingUrlsFile:
        s3.download_fileobj('com.tom.apartments', 'listingUrls.txt', listingUrlsFile)
        listingUrlsFile.write(url)
        s3.upload_fileobj(listingUrlsFile, 'com.tom.apartments', 'listingUrls.txt')

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
