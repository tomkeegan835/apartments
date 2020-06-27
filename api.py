import json
from flask import Flask, request
# custom
import craigslist, sql, util

# create the flask api
api = Flask(__name__)

# create the urls table
sql.craigslist_create('listingsSMS')

@api.route('/', methods=['GET'])
def hello():
    return "What are you doing here?"

@api.route('/urls/', methods=['POST'])
def write_url():
    # is there a better way to do this than nested json.loads()?
    url = json.loads(json.loads(request.data)['Message'])["messageBody"]

    data = craigslist.scrape(url)

    sql.craigslist_insert('listingsSMS', craigslist.tuplify(data))

    return "processed SMS with listing link"

if __name__ == '__main__':
     api.run(host="0.0.0.0", port=80, debug=True)
