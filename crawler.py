import requests, sys, time
from bs4 import BeautifulSoup
from progress.bar import ChargingBar
# custom
import craigslist, sql, util

def next(baseUrl, url, numRemaining):
    pageUrls = set()
    nextUrl = ''

    r = requests.get(url)
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
            pageUrls.add(next(baseUrl, nextUrl, numRemaining))

    return pageUrls

def scrape_set(urls, tablename):
    sql.create_table(tablename)
    results = set()
    scrapeBar = ChargingBar('Scraping urls', max = len(urls), suffix = '%(index)d/%(max)d')
    for url in urls:
        info = craigslist.scrape(url)
        sql.insert(util.tuplify_listing(info))
        scrapeBar.next()
    scrapeBar.finish()
    return

def crawl(firstUrl, numListingsRequested):
    baseUrl = 'https://sfbay.craigslist.org'

    # crawl all urls, starting with the first search result page
    listingUrls = next(baseUrl, firstUrl, numListingsRequested)
    return listingUrls
