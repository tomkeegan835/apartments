import craigslist, crawler, sql

while(True):
    fetchedUrls = crawler.crawl('https://chicago.craigslist.org', 'https://chicago.craigslist.org/search/chc/apa?', 3000)

    sql.craigslist_create('listingsCrawlChicago')

    currentUrls = set()
    for row in sql.column('listingsCrawlChicago', 'url'):
        currentUrls.add(row[0])

    newUrls = fetchedUrls - currentUrls

    if(len(newUrls) > 0):
        craigslist.scrape_set(newUrls, 'listingsCrawlChicago')

    crawler.clean('listingsCrawlChicago')
