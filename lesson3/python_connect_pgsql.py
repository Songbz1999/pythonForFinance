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
    
def database(db_command_func):
    try:
        conn = psycopg2.connect(dbname='study', user='quant', host='35.240.207.140', password='quant')
    except:
        print("I am unable to connect to the database")
        
    db_command_func(conn.cursor())
    
    conn.commit()
    conn.close()


def create_table_if_not_exist(cursor):
    cursor.execute("""
                CREATE TABLE IF NOT EXISTS sz_stock (
                        id SERIAL PRIMARY KEY,
                        stock_symbol VARCHAR(255) NOT NULL,
                        date  date, 
                        open  real, 
                        high  real, 
                        low  real,
                        close  real,
                        volume  real,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        ); """)
    #CURRENT_TIMESTAMP
    print ("Table create successful!")
    
def insert_value(cursor, df):
    output = io.StringIO();
# ignore the index
    df.to_csv(output, sep='\t',index = False, header = False);
    output.getvalue();
# jump to start of stream
    output.seek(0);
    cursor.copy_from(output, 'sz_tocks', null='')
    print ("Data insert successful!")
# df.to_sql('db_table2', engine, if_exists='replace')

def select_data(cursor):
    cursor.execute("""SELECT COUNT(*) from Stocks WHERE DATE(created_at) = TODAY()""")
    rows = cursor.fetchall()
    print ("\nShow me the databases:\n")
    # inserted line sum 5000 * 500, head(0) 
    for row in rows:
        print ("   ", row)

def read_csv():
    folder_path = 'C:/Users/Thinkpad/Desktop/2018-7 精英特训/sz_stock'
    file_list = os.listdir(folder_path)
    # file_list line sum -> 5000 * 500, head(0) random sample 
    for name in file_list:
        file_path = folder_path + '/' + name
        df = pd.read_csv(file_path, sep = ',' )
        df["stock_symbol"] = file_name
        database(insert_value(cur,df))
    print ("All data insert successful")


database(create_table_if_not_exist(cur))
database(insert_value(cur,df))
database(select_data(cur))


#cur.execute("""COPY Stock FROM 'C:/Users/Thinkpad/Desktop/SZ000021.txt'""")

"""
def get_connection(execute_sql):
    cur = 15
    execute_sql(cur)
    print("in foo: ", cur)

    
def select_sth(cur):
    print("select_sth", cur)
    
get_connection(select_sth)
"""

# https://coolshell.cn/articles/4758.html
# https://docs.python.org/3/library/unittest.html
# http://dacatay.com/data-science/part-3-time-series-stationarity-python/
