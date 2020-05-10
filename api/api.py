from flask import Flask, request
import sqlite3, sys, json

# create the flask api
api = Flask(__name__)

# create the urls table
listings = sqlite3.connect('listings.db')
listings.execute('''CREATE TABLE IF NOT EXISTS listings (
                        url text
                    );''')
listings.commit()
listings.close()

@api.route('/', methods=['GET'])
def hello():
    return "Hello"

@api.route('/urls/', methods=['POST'])
def write_url():
    listingUrl = json.loads(json.loads(request.data)['Message'])["messageBody"]

    listings = sqlite3.connect('listings.db')
    c = listings.cursor()

    c.execute('INSERT INTO listings VALUES (?)', (listingUrl,))

    print('\nInserted', listingUrl, 'into listings database.\n\nThe current contents of the listings database are as follows:\n\n')
    for row in c.execute('SELECT * FROM listings'):
        print(row, file=sys.stdout)

    listings.commit()
    listings.close()

    return "processed SMS with listing link"

if __name__ == '__main__':
     api.run(host="0.0.0.0", port=80, debug=True)
