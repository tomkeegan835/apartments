import craigslist, crawler, sql

while(True):
    fetchedUrls = crawler.crawl('https://sfbay.craigslist.org/search/sfc/apa?', 3000)

    sql.craigslist_create('listingsCrawlSanFrancisco')

    currentUrls = set()
    for row in sql.column('listingsCrawlSanFrancisco', 'url'):
        currentUrls.add(row[0])

    newUrls = fetchedUrls - currentUrls

    if(len(newUrls) > 0):
        craigslist.scrape_set(newUrls, 'listingsCrawlSanFrancisco')

    crawler.clean('listingsCrawlSanFrancisco')
