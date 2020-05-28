# apartments
searching for apartments, assembling a dataset about apartments in the areas we're interested

api.py: basic Flask api for sqlite3 database
craiglist.py: craiglist scraper which returns a dictionary with the following structure:
    {
        'price': 4100, 
        'title': 'Beautiful 1 Bedroom and 1 Bath Unit in Meticulously Restored Victorian',
        'neighborhood': 'alamo square / nopa',
        'stats': {
            'bedrooms': 1,
            'sqft': 684
        }, 
        'attributes': {
            'apartment',
            'laundry on site',
            'street parking',
            'no smoking'
        },
        'postid': 7131533811,
        'postDatetime': '2020-05-27T17:32:21-0700'
    }
delpoy.sh: sftps neccessary files to ec2
