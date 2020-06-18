import requests, string, dateutil.parser
from bs4 import BeautifulSoup
# custom
import util

def check_alive(url):
    r = requests.get(url)
    util.pause()
    page = BeautifulSoup(r.text, 'html.parser')

    return get_postid(page) != 0

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

def get_attributes(page):
    bedrooms = 0
    bathrooms = 0
    sqft = 0
    availDate = ''
    tags = set()

    attrGroups = page.find_all('p', {'class': 'attrgroup'})

    for attrGroup in attrGroups:
        if attrGroup != None:
            sharedLineBubbles = attrGroup.find_all('span', {'class': 'shared-line-bubble'})
            if len(sharedLineBubbles) > 0:
                for sharedLineBubble in sharedLineBubbles:
                    if sharedLineBubble != None:
                        bees = sharedLineBubble.find_all('b')
                        if len(bees) == 2:
                            bedrooms = bees[0].string.strip('BR')
                            bathrooms = bees[1].string.strip('Ba')
                        elif len(bees) == 1:
                            sqft = int(bees[0].string)
                        else:
                            availDate = sharedLineBubble['data-date']
            else:
                for tag in attrGroup.find_all('span'):
                    tags.add(tag.string)
    return {
        'bedrooms': bedrooms,
        'bathrooms': bathrooms,
        'sqft': sqft,
        'availDate': availDate,
        'tags': tags
    }

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
    util.pause()
    page = BeautifulSoup(r.text, 'html.parser')

    return {
        'url': url,
        'price': get_price(page),
        'title': get_title(page),
        'neighborhood': get_neighborhood(page),
        'attributes': get_attributes(page),
        'postid': get_postid(page),
        'postDatetime': get_postDatetime(page)
    }
