import requests, string, dateutil.parser
from bs4 import BeautifulSoup

def get_attributes(page):
    attributes = set()
    attributes_block = page.find_all('p', {'class': 'attrgroup'})[1]
    for attribute in attributes_block.find_all('span'):
        attributes.add(attribute.string)
    return attributes

def get_postDatetime(page):
    return page.find('div', {'class': 'postinginfos'}).find('p', {'class': 'postinginfo reveal'}).time['datetime']

def get_postid(page):
    return int(page.find('div', {'class': 'postinginfos'}).find('p').string[9:])

def get_price(page):
    return int(page.find('span', {'class': 'price'}).string[1:])

def get_stats(page):
    statsKeys = ['bedrooms', 'sqft']
    statsValues = []

    for bubble in page.find_all('span', {'class': 'shared-line-bubble'}):
        if bubble.find('b') != None: statsValues.append(int(bubble.find('b').string.strip(string.ascii_letters)))

    return dict(zip(statsKeys, statsValues))

def get_title(page):
    return page.find('span', {'id': 'titletextonly'}).string

def get_neighborhood(page):
    return page.find('span', {'class': 'postingtitletext'}).find('small').string.strip(' ()')

def main():
    r = requests.get('https://sfbay.craigslist.org/sfc/apa/d/san-francisco-beautiful-1-bedroom-and-1/7131533811.html')

    page = BeautifulSoup(r.text, 'html.parser')

    data = {
        'price': get_price(page),
        'title': get_title(page),
        'neighborhood': get_neighborhood(page),
        'stats': get_stats(page),
        'attributes': get_attributes(page),
        'postid': get_postid(page),
        'postDatetime': get_postDatetime(page)
    }

    print('DATA:',data)

if __name__=="__main__":
    main()
