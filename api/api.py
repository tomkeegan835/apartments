from flask import Flask, request, url_for
import sqlite3, sys

# create the flask api
api = Flask(__name__)

# create the urls table
listings = sqlite3.connect('listings.db')
listings.execute('''CREATE TABLE IF NOT EXISTS listings (
                        url text PRIMARY KEY
                    );''')

@api.route('/', methods=['GET'])
def hello():

    return "Hello"

@api.route('/urls/<listingUrl>', methods=['POST'])
def write_url(listingUrl):
    print(listingUrl, file=sys.stdout)
    listings.execute('INSERT INTO listings VALUES ' + listingUrl)
    print('created record with url', file=sys.stdout)
    return 'created record with url'

with api.test_request_context():
    print(url_for('write_url', listingUrl='http://www.google.com'))

if __name__ == '__main__':
     api.run(host="0.0.0.0", port=80, debug=True)
