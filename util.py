import time, random, sys

def tuplify(data):
    return (data['url'], data['price'], data['title'], data['neighborhood'], data['attributes']['bedrooms'], data['attributes']['bathrooms'], data['attributes']['sqft'], data['attributes']['availDate'], data['postid'], data['postDatetime'])

def pause():
    time.sleep(.5 + 2.5 * random.random())
