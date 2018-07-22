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
import os
    
def database(a):
    try:
        conn = psycopg2.connect(dbname='study', user='quant', host='35.240.207.140', password='quant')
    except:
        print("I am unable to connect to the database")
    cur = conn.cursor()
    a()
    conn.commit()
    conn.close()


def create_table(b):
    b.execute("""
                CREATE TABLE Stocks (
                        date  date, 
                        open  real, 
                        high  real, 
                        low  real,
                        close  real,
                        volume  real
                        ); """)
    print ("Table create successful!")
    
def insert_value(b,df):
    df = pd.read_csv('C:/Users/Thinkpad/Desktop/SZ000021.csv', sep = ',' );    
    output = io.StringIO();
# ignore the index
    df.to_csv(output, sep='\t',index = False, header = False);
    output.getvalue();
# jump to start of stream
    output.seek(0);
    b.copy_from(output, 'sz_tocks', null='')
    print ("Data insert successful!")

def select_data(b):
    b.execute("""SELECT * from Stocks""")
    rows = b.fetchall()
    print ("\nShow me the databases:\n")
    for row in rows:
        print ("   ", row)

def read_csv():
    folder_path = 'C:/Users/Thinkpad/Desktop/2018-7 精英特训/sz_stock'
    file_list = os.listdir(folder_path)
    for name in file_list:
        file_path = folder_path + '/' + name
        df = pd.read_csv(file_path, sep = ',' )
        database(insert_value(cur,df))
    print ("All data insert successful")


database(create_table(cur))
database(insert_value(cur,df))
database(select_data(cur))

#cur.execute("""COPY Stock FROM 'C:/Users/Thinkpad/Desktop/SZ000021.txt'""")
