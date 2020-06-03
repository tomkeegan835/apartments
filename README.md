# apartments
searching for apartments

api.py: basic Flask api for sqlite3 database\
crawl.py: pulls in craigslist listing URLs\
craiglist.py: craiglist scraper which returns a dictionary with the following structure:
```
{
    'url': string url
    'price': int price,
    'title': string title,
    'neighborhood': string neighborhood,
    'attributes': {
        'bedrooms': int,
        'bathrooms': int,
        'sqft': int,
        'availDate' : string,
        'tags': set
    },
    'postid': int,
    'postDatetime': iso string
}
```
deploy.sh: packages and sftps files to ec2
