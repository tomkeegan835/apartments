import crawler, craigslist

craigslist.scrape_set(crawler.crawl('https://sfbay.craigslist.org/search/sfc/apa?', 200), 'listings')
