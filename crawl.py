import craigslist, crawler, sql

while(True):
    fetchedUrls = crawler.crawl('https://sfbay.craigslist.org/search/sfc/apa?', 3000)

    currentUrls = set()
    for row in sql.column('listings', 'url'):
        currentUrls.add(row[0])

    newUrls = fetchedUrls - currentUrls

    if(len(newUrls) > 0):
        craiglist.scrape_set(newUrls, 'listings')

    crawler.clean('listings')
