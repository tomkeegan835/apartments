import requests, string, dateutil.parser
from bs4 import BeautifulSoup

def getAttributes(page):
    attributes = set()
    attributes_block = page.find_all('p', {'class': 'attrgroup'})[1]
    for attribute in attributes_block.find_all('span'):
        attributes.add(attribute.string)
    return attributes

def getPostDateTime(page):
    return page.find('div', {'class': 'postinginfos'}).find('p', {'class': 'postinginfo reveal'}).time['datetime']

def getPostId(page):
    return int(page.find('div', {'class': 'postinginfos'}).find('p').string[9:])

def getPrice(page):
    return int(page.find('span', {'class': 'price'}).string[1:])

def getStats(page):
    stats_keys = ['bedrooms', 'sqft']
    stats_values = []

    for bubble in page.find_all('span', {'class': 'shared-line-bubble'}):
        if bubble.find('b') != None: stats_values.append(int(bubble.find('b').string.strip(string.ascii_letters)))

    return dict(zip(stats_keys, stats_values))

def getTitle(page):
    return page.find('span', {'id': 'titletextonly'}).string

def getNeighborhood(page):
    return page.find('span', {'class': 'postingtitletext'}).find('small').string.strip(' ()')

def scrape(url):
    r = requests.get(url)

    page = BeautifulSoup(r.text, 'html.parser')

    data = {
        'price': getPrice(page),
        'title': getTitle(page),
        'neighborhood': getNeighborhood(page),
        'stats': getStats(page),
        'attributes': getAttributes(page),
        'postid': getPostId(page),
        'post_datetime': getPostDateTime(page)
    }

    return data

if __name__=="__main__":
    main()
