import requests, sys, time
from bs4 import BeautifulSoup
from progress.spinner import Spinner
from progress.bar import ChargingBar
# custom
import craigslist, sql, util

"""
____CLEAN____

RETURN: None

ARGS: tablename: name of table to be cleaned
"""
def clean(tablename):
    urls = sql.oldest(tablename)

    checkBar = ChargingBar('Checking for expired listings', max = len(urls), suffix = '%(index)d/%(max)d')
    for url in urls:
        if craigslist.is_expired(url):
            sql.delete(tablename, 'url', url)
        checkBar.next()
    checkBar.finish()

"""
____CRAWL____

RETURN: set

ARGS:
    firstUrl: url from which to start crawling
    numListingsRequested: how many results to fetch
"""
def crawl(baseUrl, firstUrl, numListingsRequested):
    spinner = Spinner('Fetching listing URLs ')

    # crawl all urls, starting with the first search result page
    listingUrls = next(baseUrl, firstUrl, numListingsRequested, spinner)

    spinner.finish()
    return listingUrls

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
