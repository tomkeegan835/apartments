import sqlite3

def create_table():
    listings = sqlite3.connect('listings.db')
    listings.execute('''CREATE TABLE IF NOT EXISTS listings (
                            url text PRIMARY KEY UNIQUE,
                            price number,
                            title text,
                            neighborhood text,
                            bedrooms number DEFAULT 0,
                            bathrooms number DEFAULT 0,
                            sqft number DEFAULT 0,
                            availDate text DEFUALT unknown,
                            postid number,
                            postDatetime text
                        );''')
    listings.commit()
    listings.close()

def insert_record(record):
    listings = sqlite3.connect('listings.db')
    c = listings.cursor()

    c.execute('INSERT OR IGNORE INTO listings VALUES (?,?,?,?,?,?,?,?,?,?)', record)

    listings.commit()
    listings.close()

def dump_listings(filename):
    listings = sqlite3.connect('listings.db')
    c = listings.cursor()

    file = open(filename, 'w')

    for row in c.execute('SELECT * FROM listings'):
        file.write('|'.join([str(e) for e in row]) + '\n')

    file.close()

    listings.close()
