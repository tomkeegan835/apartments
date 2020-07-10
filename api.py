import json
from flask import Flask, request, send_file, send_from_directory
# custom
import craigslist, sql, util

# create the flask api
api = Flask(__name__)

# create the urls table
sql.craigslist_create('listingsApi')

@api.route('/', methods=['GET'])
def hello():
    try:
        return send_from_directory('website','download.html')
    except Exception as e:
	    return str(e)

@api.route('/urls/', methods=['POST','GET'])
def write_url():
    if request.method == 'GET':
        sql.dump('listingsCrawlMilwaukee','mke')
        return send_file('mke.csv')

    # is there a better way to do this than nested json.loads()?
    url = json.loads(json.loads(request.data)['Message'])["messageBody"]

    data = craigslist.scrape(url)

    sql.craigslist_insert('listingsSMS', craigslist.tuplify(data))

    return "processed SMS with listing link"

if __name__ == '__main__':
    api.run(host="0.0.0.0", port=80, debug=True)
