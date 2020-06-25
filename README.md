# apartments
searching for apartments

api.py: basic Flask api for sqlite3 database\
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
crawl.py: pulls in craigslist listing URLs\
crawler.py: contains functions used by crawl.py\
deploy.sh: packages and sftps files to ec2\
requirements.txt: list of pip packages needed\
sql.py: sqlite access helper functions\
util.py: some utility functions used throughout the codebase
