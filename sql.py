import sqlite3
import pandas as pd

# rewrite this
def column(tablename, columnheader):
    db = sqlite3.connect('db.db')
    c = db.cursor()

    column = set()
    for row in c.execute('SELECT {col} FROM {table}'.format(col = columnheader, table = tablename)):
        column.add(row)

    db.close()

    return column

def copy_table(original, copy):
    db = sqlite3.connect('db.db')
    c = db.cursor()

    craigslist_create(copy)
    sql_args = (copy, original)
    c.execute('INSERT INTO {newTable} SELECT * FROM {oldTable}'.format(newTable = copy, oldTable = original))

    db.commit()
    db.close()

def craigslist_create(tablename):
    db = sqlite3.connect('db.db')
    db.execute('''CREATE TABLE IF NOT EXISTS {table} (
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
    db.commit()
    db.close()

def craigslist_insert(tablename, record):

    db = sqlite3.connect('db.db')
    c = db.cursor()

    c.execute('INSERT OR IGNORE INTO {table} VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'.format(table = tablename), record)

    db.commit()
    db.close()

def to_df(tablename):
    db = sqlite3.connect('db.db')

    df = pd.read_sql_query('SELECT * from {table}'.format(table = tablename), db)

    db.close()

    return df

def drop(tablename):
    db = sqlite3.connect('db.db')
    c = db.cursor()

    c.execute('DROP TABLE {table}'.format(table = tablename))

    db.commit()
    db.close()

def delete(tablename, columnheader, value):
    db = sqlite3.connect('db.db')
    c = db.cursor()

    c.execute('DELETE FROM {table} WHERE {column} = \'{val}\''.format(table = tablename, column = columnheader, val = value))

    db.commit()
    db.close()

def dump(tablename, filename):
    db = sqlite3.connect('db.db')

    df = pd.read_sql_query('SELECT * FROM {table}'.format(table = tablename), db)

    db.close()

    df.to_csv('{file}.csv'.format(file = filename), index = False)

def oldest(tablename):
    db = sqlite3.connect('db.db')
    c = db.cursor()

    urls = []
    for row in c.execute('SELECT * FROM {table} ORDER BY postDatetime ASC'.format(table = tablename)):
        urls.append(row[0])

    db.close()

    return urls

def select(tablename, columnheader, value):
    db = sqlite3.connect('db.db')
    c = db.cursor()

    rows = c.execute('SELECT * FROM {table} WHERE {column} = ?'.format(table = tablename, column = columnheader), value,)

    db.close()

    return rows
