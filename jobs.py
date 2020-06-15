import crawler

urls = crawler.crawl('https://sfbay.craigslist.org/search/sfc/apa?', 3000)
crawler.scrape_set(urls, 'listings')
