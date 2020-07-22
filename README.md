# apartments
searching for apartments

api.py: basic Flask api for sqlite3 database, allows for CSV download\
website/download.html: the page with the download links\
craiglist.py: craigslist scraper which returns a python dictionary with the following structure:
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
sf.py: pulls in craigslist listing URLs for SF\
milwaukee.py: pulls in craigslist listing URLs for Milwaukee\
chicago.py: pulls in craigslist listing URLs for Chicago\
crawler.py: contains functions used by crawl.py\
requirements.txt: list of pip packages needed\
sql.py: sqlite access helper functions\
util.py: some utility functions (like the random interval pause function used after sending a request)
