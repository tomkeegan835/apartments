import sqlite3, sys

def create_table():
    listings = sqlite3.connect('listings.db')
    listings.execute('''CREATE TABLE IF NOT EXISTS listings (
                            url text,
                            price number,
                            title text,
                            neighborhood text,
                            statsBedrooms number,
                            statsSqft number,
                            postid number,
                            postDatetime text
                        );''')
    listings.commit()
    listings.close()

def insert_record(record):
    listings = sqlite3.connect('listings.db')
    c = listings.cursor()

    c.execute('INSERT INTO listings VALUES (?,?,?,?,?,?,?,?)', record)

    print(record)

    listings.commit()
    listings.close()

def dump_listings():
    listings = sqlite3.connect('listings.db')
    c = listings.cursor()

    file = open('listings.txt', 'w')

    for row in c.execute('SELECT * FROM listings'):
        file.write(row)

    file.close()

    listings.close()
