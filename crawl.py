import crawler, sql

while(True):
    listingUrls = crawler.crawl('https://sfbay.craigslist.org/search/sfc/apa?', 3000)

    currentUrls = set()
    for row in sql.column('listings', 'url'):
        currentUrls.add(row[0])

    print('fetched urls: ', len(listingUrls))
    newUrls = listingUrls - currentUrls
    print('new urls: ', len(newUrls))

    if len(newUrls) > 0:
        crawler.scrape_set(newUrls, 'listings')
