import sqlite3

def create_table(tablename):
    listings = sqlite3.connect('listings.db')
    listings.execute('''CREATE TABLE IF NOT EXISTS {table} (
                            url text PRIMARY KEY UNIQUE,
                            apartment text,
                            title text DEFAULT unknown,
                            neighborhood text DEFAULT unknown,
                            price number DEFAULT 0,
                            availDate text DEFAULT unknown,
                            bedrooms number DEFAULT 0,
                            bathrooms number DEFAULT 0,
                            sqft number DEFAULT 0,
                            parking text,
                            laundry text,
                            cats text,
                            dogs text,
                            furnished text,
                            postDatetime text DEFAULT unknown,
                            postid number DEFAULT 0
                        );'''.format(table = tablename))
    listings.commit()
    listings.close()

def insert_listing(record):
    listings = sqlite3.connect('listings.db')
    c = listings.cursor()

    c.execute('INSERT OR IGNORE INTO listings VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', record)

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
