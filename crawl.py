import requests, sys, time
from bs4 import BeautifulSoup
from progress.bar import ChargingBar
from progress.spinner import Spinner
# custom
import craigslist, sql, util

def crawl(url, numRemaining):
    r = requests.get(url)
    util.pause()
    fetchSpinner.next()
    page = BeautifulSoup(r.text, 'html.parser')

    for result in page.find_all('p', {'class': 'result-info'}):
        if numRemaining == 0: return 0
        listingUrl = result.a['href']
        listingUrls.add(listingUrl)
        numRemaining = numRemaining - 1


    nextRelUrlTag = page.find('a', {'class': 'button next'})
    if nextRelUrlTag != None:
        nextRelUrl = nextRelUrlTag['href']
        if len(nextRelUrl) > 0:
            nextUrl = baseUrl + nextRelUrl
            pageUrls.add(nextUrl)
            numRemaining = crawl(nextUrl, numRemaining)

    return numRemaining

firstUrl = sys.argv[1]
numListings = numListingsRequested = int(sys.argv[2])
baseUrl = 'https://sfbay.craigslist.org'
pageUrls = {firstUrl}
listingUrls = set()
listings = []

# crawl all urls, starting with the first search result page
fetchSpinner = Spinner('Fetching lising URLs ')
numListings = numListingsRequested - crawl(firstUrl, numListingsRequested)
fetchSpinner.finish()

sql.create_table('listings')
scrapeBar = ChargingBar('Scraping listings and storing in sqlite', max = numListings, suffix = '%(index)d/%(max)d')
for listingUrl in listingUrls:
    listingInfo = craigslist.scrape(listingUrl)
    sql.insert_listing(util.tuplify_listing(listingInfo))
    scrapeBar.next()
scrapeBar.finish()
