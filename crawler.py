import requests, sys, time
from bs4 import BeautifulSoup
from progress.bar import ChargingBar
from progress.spinner import Spinner
# custom
import craigslist, sql, util

# recursive function to fetch all listing urls
def next(baseUrl, url, numRemaining, progress):
    pageUrls = set()
    nextUrl = ''

    r = requests.get(url)
    progress.next()
    util.pause()
    page = BeautifulSoup(r.text, 'html.parser')

    for result in page.find_all('p', {'class': 'result-info'}):
        if numRemaining == 0: return pageUrls
        pageUrl = result.a['href']
        pageUrls.add(pageUrl)
        numRemaining = numRemaining - 1

    nextRelUrlTag = page.find('a', {'class': 'button next'})
    if nextRelUrlTag != None:
        nextRelUrl = nextRelUrlTag['href']
        if len(nextRelUrl) > 0:
            nextUrl = baseUrl + nextRelUrl
            pageUrls.update(next(baseUrl, nextUrl, numRemaining, progress))

    return pageUrls

"""
____SCRAPE_SET____

RETURN: None

ARGS:
    urls: set of craiglist apartment posting URLs
    tablename: SQL table in which results will be stored
"""
def scrape_set(urls, tablename):
    sql.create_table(tablename)
    results = set()
    scrapeBar = ChargingBar('Scraping urls', max = len(urls), suffix = '%(index)d/%(max)d')
    for url in urls:
        info = craigslist.scrape(url)
        sql.insert(tablename, util.tuplify_listing(info))
        scrapeBar.next()
    scrapeBar.finish()

"""
____CRAWL____

RETURN: set

ARGS:
    firstUrl: url from which to start crawling
    numListingsRequested: how many results to fetch
"""
def crawl(firstUrl, numListingsRequested):
    baseUrl = 'https://sfbay.craigslist.org'
    spinner = Spinner('Fetching listing URLs ')

    # crawl all urls, starting with the first search result page
    listingUrls = next(baseUrl, firstUrl, numListingsRequested, spinner)

    spinner.finish()
    return listingUrls
