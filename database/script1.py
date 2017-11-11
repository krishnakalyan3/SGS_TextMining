#!/usr/bin/env python3
import pandas as pd
import psycopg2
import json
from sqlalchemy import create_engine
import csv

PATH = 'login.json'
PATH_CSV = '../data/titles_and_types.csv'

def read_json(path):
    with open(path) as data_file:
        db1 = json.load(data_file)
    return db1


def connect(db):
    conn = psycopg2.connect(database=db['database'], user=db['user'], password=db['password'], host=db['host'],
                            port=db['port'])
    return conn


def did_not_work():
    df = pd.read_csv('../data/titles_and_types.csv', sep='\t')
    df.columns = [c.lower() for c in df.columns]
    conn_str = 'postgresql://' + db['user'] + ':' + db['password'] + '@' + db['host'] + ':' + db['port'] + '/' + db[
    'database']
    engine = create_engine(conn_str)
    df.to_sql("sbs_raw_new", engine)
    return db


def insert_data(cursor, post_id, type, title):
    cursor.execute('update twitter.TITILES2 set post_id=%s where idd=%s', (post_id, type, title))


if __name__ == '__main__':
    db = read_json(PATH)
    conn = psycopg2.connect(database=db['database'], user=db['user'], password=db['password'],
                            host=db['host'], port=db['port'])

    with open(PATH_CSV, 'r', encoding='utf8') as f:
      for i, value in enumerate(f):
        if i != 0:
          line = value.strip().split('\t')
          insert_data(conn, line[0], line[1], line[2])

    conn.commit()
    conn.close()
