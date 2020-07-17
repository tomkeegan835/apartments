from flask import Flask, send_file, send_from_directory
# custom
import sql

# create the flask api
api = Flask(__name__)

@api.route('/', methods=['GET'])
def hello():
    try:
        return send_from_directory('website','download.html')
    except Exception as e:
	    return str(e)

@api.route('/milwaukee/', methods=['GET'])
def download_mke():
    sql.dump('listingsCrawlMilwaukee','mke')
    return send_file('mke.csv', as_attachment=True)

@api.route('/sf/', methods=['GET'])
def download_sf():
    sql.dump('listingsCrawlSanFrancisco','sf')
    return send_file('sf.csv', as_attachment=True)

if __name__ == '__main__':
    api.run(host="0.0.0.0", port=80, debug=True)
