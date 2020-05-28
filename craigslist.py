import requests, string, dateutil.parser
from bs4 import BeautifulSoup

def get_attributes(page):
    attributes = set()
    attributesGroups = page.find_all('p', {'class': 'attrgroup'})
    if len(attributesGroups) > 1:
        for attribute in attributesGroups[1].find_all('span'):
            attributes.add(attribute.string)
    return attributes

def get_postDatetime(page):
    postDatetime = ''
    postingInfoTag = page.find('div', {'class': 'postinginfos'})
    if postingInfoTag != None:
        postDatetimeWrapper = postingInfoTag.find('p', {'class': 'postinginfo reveal'})
        if postDatetimeWrapper != None:
            postDatetimeTag = postDatetimeWrapper.time
            if postDatetimeTag != None:
                postDatetime = postDatetimeTag['datetime']
    return postDatetime

def get_postid(page):
    postid = 0
    postingInfoTag = page.find('div', {'class': 'postinginfos'})
    if postingInfoTag != None:
        postidTag = postingInfoTag.p
        if postidTag != None:
            postid = int(postidTag.string[9:])
    return postid

def get_price(page):
    price = 0
    priceTag = page.find('span', {'class': 'price'})
    if priceTag != None:
        price = int(priceTag.string[1:])
    return price

def get_stats(page):
    statsKeys = ['bedrooms', 'sqft']
    statsValues = []

    for bubble in page.find_all('span', {'class': 'shared-line-bubble'}):
        if bubble.b != None: statsValues.append(int(bubble.b.string.strip(string.ascii_letters)))

    return dict(zip(statsKeys, statsValues))

def get_title(page):
    title = ''
    titleTag = page.find('span', {'id': 'titletextonly'})
    if titleTag != None:
        title = titleTag.string
    return title

def get_neighborhood(page):
    neighborhood = ''
    titleTag = page.find('span', {'class': 'postingtitletext'})
    if titleTag != None:
        neighborhoodTag = titleTag.small
        if neighborhoodTag != None:
            neighborhood = neighborhoodTag.string.strip(' ()')
    return neighborhood

def scrape(url):
    r = requests.get(url)
    page = BeautifulSoup(r.text, 'html.parser')

    return {
        'price': get_price(page),
        'title': get_title(page),
        'neighborhood': get_neighborhood(page),
        'stats': get_stats(page),
        'attributes': get_attributes(page),
        'postid': get_postid(page),
        'postDatetime': get_postDatetime(page)
    }
