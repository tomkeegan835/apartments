import requests, sys
from bs4 import BeautifulSoup
# custom
import craigslist, sql, util

def crawl(url):
    r = requests.get(url)
    page = BeautifulSoup(r.text, 'html.parser')

    for result in page.find_all('p', {'class': 'result-info'}):
        listingUrl = result.a['href']
        listingUrls.add(listingUrl)

    nextRelUrlTag = page.find('a', {'class': 'button next'})
    if nextRelUrlTag != None:
        nextRelUrl = nextRelUrlTag['href']
        if len(nextRelUrl) > 0:
            nextUrl = baseUrl + nextRelUrl
            pageUrls.add(nextUrl)
            crawl(nextUrl)

    return

firstUrl = 'https://sfbay.craigslist.org/search/sfc/apa'
baseUrl = 'https://sfbay.craigslist.org'
pageUrls = {firstUrl}
listingUrls = set()
listings = []

# crawl all urls, starting with the first search result page
crawl(firstUrl)

i = 0
for listingUrl in listingUrls:
    listingInfo = craigslist.scrape(listingUrl)
    listings.append(listingInfo)
    print(i)
    i = i + 1

#for listing in listings:
#    sql.insert_record(tuplify(listing))
