# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 10:56:03 2018

"""

# https://wiki.postgresql.org/wiki/Psycopg2_Tutorial
# http://initd.org/psycopg/docs/usage.html
# http://www.postgresqltutorial.com/postgresql-python/create-tables/

import psycopg2
import pandas as pd
import io

try:
    conn = psycopg2.connect(dbname='study', user='quant', host='35.240.207.140', password='quant')
except:
    print("I am unable to connect to the database")
    
print(conn)

cur = conn.cursor()

cur.execute("""SELECT * from Persons""")

rows = cur.fetchall()

print ("\nShow me the databases:\n")
for row in rows:
    print ("   ", row)

def create_table():
    try:
        conn = psycopg2.connect(dbname='study', user='quant', host='35.240.207.140', password='quant')
    except:
        print("I am unable to connect to the database")
    cur = conn.cursor()

    cur.execute("""
                CREATE TABLE Stocks (
                        date  date, 
                        open  real, 
                        high  real, 
                        low  real,
                        close  real,
                        volume  real
                        ); """)
    conn.commit()
    conn.close()
    print ("Table create successful!")
    
def insert_value():
    try:
        conn = psycopg2.connect(dbname='study', user='quant', host='35.240.207.140', password='quant')
    except:
        print("I am unable to connect to the database")
    cur = conn.cursor()
    df = pd.read_csv('C:/Users/Thinkpad/Desktop/SZ000021.csv', sep = ',' )    
    output = io.StringIO()
# ignore the index
    df.to_csv(output, sep='\t',index = False, header = False)
    output.getvalue()
# jump to start of stream
    output.seek(0)
    cur.copy_from(output, 'Stocks', null='')
    conn.commit()
    conn.close()
    print ("Data insert successful!")
    return 0

def select_data():
    try:
        conn = psycopg2.connect(dbname='study', user='quant', host='35.240.207.140', password='quant')
    except:
        print("I am unable to connect to the database")
    cur = conn.cursor()
    cur.execute("""SELECT * from Stocks""")
    rows = cur.fetchall()
    print ("\nShow me the databases:\n")
    for row in rows:
        print ("   ", row)
    conn.commit()
    conn.close()
    return 0



create_table()
insert_value()
select_data()

cur.execute("""COPY Stock FROM 'C:/Users/Thinkpad/Desktop/SZ000021.txt'""")
