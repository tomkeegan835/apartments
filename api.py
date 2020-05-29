import json
from flask import Flask, request
# custom
import craigslist, sql, util

# create the flask api
api = Flask(__name__)

# create the urls table
sql.create_table()

@api.route('/', methods=['GET'])
def hello():
    return "Hello"

@api.route('/urls/', methods=['POST'])
def write_url():
    url = json.loads(json.loads(request.data)['Message'])["messageBody"]

    data = craigslist.scrape(url)

    sql.insert_record(util.tuplify(data))

    return "processed SMS with listing link"

if __name__ == '__main__':
     api.run(host="0.0.0.0", port=80, debug=True)
