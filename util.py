import time, random, sys

def tuplify_listing(data):
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

def pause():
    time.sleep(.5 + 2.5 * random.random())
