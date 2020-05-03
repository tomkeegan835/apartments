from flask import Flask
import sqlite3

api = Flask(__name__)

@api.route('/', methods=['GET'])
def hello():
    return "Hello world"

@api.route('/urls/<url>', methods=['POST'])
def write_url(url):
    urls = sqlite3.connect('urls.db')
    cursor = urls.cursor()
    urls.execute('CREATE  TABLE [IF NOT EXISTS] urls')
    urls.execute('INSERT INTO urls VALUES ' + url)

if __name__ == '__main__':
     api.run()
