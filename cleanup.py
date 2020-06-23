import craigslist, sql
from progress.bar import ChargingBar

urls = set()
for row in sql.column('listings', 'url'):
    urls.add(row[0])

expiredUrls = set()
checkBar = ChargingBar('Checking for expired listings', max = len(urls), suffix = '%(index)d/%(max)d')
for url in urls:
    if !craigslist.check_alive(url):
        expiredUrls.add(url)
