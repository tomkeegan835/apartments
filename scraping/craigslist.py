import requests, string
from bs4 import BeautifulSoup

def getAttributes(page):
    attributes = []
    attributes_block = page.find_all('p', {'class': 'attrgroup'})[1]
    for tag in attributes_block.find_all('span'):
        attributes.append(tag.string)
    return attributes

def getPrice(page):
    return int(page.find('span', {'class': 'price'}).string[1:])

def getStats(page):
    stats_keys = ['bedrooms', 'sqft']
    stats_values = []

    for bubble in page.find_all('span', {'class': 'shared-line-bubble'}):
        stats_values.append(int(bubble.find('b').string.strip(string.ascii_letters)))

    return dict(zip(stats_keys, stats_values))

def getTitle(page):
    return page.find('span', {'id': 'titletextonly'}).string

def getNeighborhood(page):
    return page.find('span', {'class': 'postingtitletext'}).find('small').string.strip(' ()')

def main():
    r = requests.get('https://sfbay.craigslist.org/sfc/apa/d/san-francisco-furnished-smart-soma-1br/7130431659.html')

    page = BeautifulSoup(r.text, 'html.parser')

    data = {'price': getPrice(page), 'title': getTitle(page), 'neighborhood': getNeighborhood(page), 'stats': getStats(page), 'attributes': getAttributes(page)}

    print('DATA:', data)

if __name__=="__main__":
    main()
