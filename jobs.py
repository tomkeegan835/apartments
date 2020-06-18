import craigslist, sql

urls = sql.column('listings', 'url')

for i in range(10):
    url = urls.pop()[0]
    print(url, 'alive' if craigslist.check_alive(url) else 'dead')
