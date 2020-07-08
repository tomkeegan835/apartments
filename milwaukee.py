import craigslist, crawler, sql

while(True):
    fetchedUrls = crawler.crawl('https://milwaukee.craigslist.org/search/apa?', 3000)

    sql.craigslist_create('listingsCrawlMilwaukee')

    currentUrls = set()
    for row in sql.column('listingsCrawlMilwaukee', 'url'):
        currentUrls.add(row[0])

    newUrls = fetchedUrls - currentUrls

    if(len(newUrls) > 0):
        craigslist.scrape_set(newUrls, 'listingsCrawlMilwaukee')

    crawler.clean('listingsCrawlMilwaukee')
