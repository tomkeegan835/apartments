import sqlite3, sys, json, craigslist
from flask import Flask, request

# create the flask api
api = Flask(__name__)

# create the urls table
listings = sqlite3.connect('listings.db')
listings.execute('''CREATE TABLE IF NOT EXISTS listings (
                        url text
                        price number
                        title text
                        neighborhood text
                        statsBedrooms number
                        statsSqft number
                        postid number
                        postDatetime text
                    );''')
listings.commit()
listings.close()

@api.route('/', methods=['GET'])
def hello():
    return "Hello"

@api.route('/urls/', methods=['POST'])
def write_url():
    print(json.loads(request.data))

    url = json.loads(json.loads(request.data)['Message'])["messageBody"]

    data = craigslist.scrape(url)

    record = (url, data['price'], data['title'], data['neighborhood'], data['statsBedrooms'], data['statsSqft'], data['postid'], data['postDatetime'])

    listings = sqlite3.connect('listings.db')
    c = listings.cursor()

    c.execute('INSERT INTO listings VALUES (?)', record)

    print('\nInserted', listingUrl, 'into listings database.\n\nThe current contents of the listings database are as follows:\n\n')
    for row in c.execute('SELECT * FROM listings'):
        print(row, file=sys.stdout)

    listings.commit()
    listings.close()

    return "processed SMS with listing link"

if __name__ == '__main__':
     api.run(host="0.0.0.0", port=80, debug=True)
