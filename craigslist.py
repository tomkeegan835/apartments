import requests, string
from bs4 import BeautifulSoup
from progress.bar import ChargingBar
# local
import util, sql

def is_expired(url):
    r = requests.get(url)
    util.pause()
    page = BeautifulSoup(r.text, 'html.parser')

    return get_postid(page) == 0

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

"""
____SCRAPE____

RETURN: tuple containing database record

ARGS:
    urls: set of craiglist apartment posting URLs
    tablename: SQL table in which results will be stored
"""

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

"""
____SCRAPE_SET____

RETURN: None

ARGS:
    urls: set of craiglist apartment posting URLs
    tablename: SQL table in which results will be stored
"""
def scrape_set(urls, tablename):
    sql.craigslist_create(tablename)
    results = set()
    scrapeBar = ChargingBar('Scraping urls', max = len(urls), suffix = '%(index)d/%(max)d')
    for url in urls:
        info = scrape(url)
        sql.craigslist_insert(tablename, tuplify(info))
        scrapeBar.next()
    scrapeBar.finish()

def tuplify(data):
    tags = data['attributes']['tags']

    cats = 'yes' if 'cats are OK - purrr' in tags else 'no'
    dogs = 'yes' if 'dogs are OK - wooof' in tags else 'no'
    furnished = 'yes' if 'furnished' in tags else 'no'
    apartment = 'yes' if 'apartment' in tags else 'no'

    laundryInBuilding = 'laundry in bldg' in tags
    laundryInUnit = 'w/d in unit' in tags

    laundry = ''
    if(laundryInBuilding): laundry = 'laundry in bldg'
    elif(laundryInUnit): laundry = 'w/d in unit'
    else: laundry = 'no laundry'

    offStreetParking = 'off-street parking' in tags
    garage = 'attached garage' in tags

    parking = ''
    if(offStreetParking): parking = 'off-street parking'
    elif(garage): parking = 'attached garage'
    else: parking = 'no parking'

    return (
        data['url'],
        apartment,
        data['title'],
        data['neighborhood'],
        data['price'],
        data['attributes']['availDate'],
        data['attributes']['bedrooms'],
        data['attributes']['bathrooms'],
        data['attributes']['sqft'],
        parking,
        laundry,
        cats,
        dogs,
        furnished,
        data['postDatetime'],
        data['postid']
    )
