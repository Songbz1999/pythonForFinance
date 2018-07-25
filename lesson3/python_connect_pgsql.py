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
    
def database(db_command_func,*data):
    try:
        conn = psycopg2.connect(dbname='study', user='quant', host='35.240.207.140', password='quant')
    except:
        print("I am unable to connect to the database")
        
    if not data:    
        db_command_func(conn.cursor())
    else:
        db_command_func(conn.cursor(),*data)
        
    conn.commit()
    conn.close()


def create_table_if_not_exist(cursor):
    cursor.execute("""
                CREATE TABLE IF NOT EXISTS sz_stocks (
                        id SERIAL PRIMARY KEY,
                        stock_symbol VARCHAR(255) NOT NULL,
                        pricing_date TIMESTAMP NOT NULL, 
                        open  DECIMAL NOT NULL, 
                        high  DECIMAL NOT NULL, 
                        low  DECIMAL NOT NULL,
                        close  DECIMAL NOT NULL,
                        volume  DECIMAL NOT NULL,
                        created_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
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

def select_data(cursor,table_name):
    cursor.execute("""SELECT COUNT(*) from table_name WHERE DATE(created_at) = TODAY()""")
    rows = cursor.fetchall()
    return rows

        
def select_table_name(cursor):
    cursor.execute("""SELECT table_schema, table_name FROM information_schema.tables
                       WHERE table_schema = 'public'""")
    rows = cursor.fetchall()
    return rows

def read_csv(folder_path):
    file_list = os.listdir(folder_path)
    # file_list line sum -> 5000 * 500, head(0) random sample 
    for name in file_list:
        file_path = folder_path + '/' + name
        df = pd.read_csv(file_path, sep = ',' )
        df["stock_symbol"] = name
        database(insert_value,df)
    print ("All data insert successful")
    
def print_data(rows):
    print ("\nShow me the data:\n")
    # inserted line sum 5000 * 500, head(0) 
    for row in rows:
        print ("   ", row)

folder_path = 'C:/Users/Thinkpad/Desktop/2018-7 Goldman Programme/sz_stock'
database(create_table_if_not_exist)
read_csv(folder_path)
data = database(select_table_name)
print_data(data())
database(select_data,'sz_stocks')


#cur.execute("""COPY Stock FROM 'C:/Users/Thinkpad/Desktop/SZ000021.txt'""")

"""
def get_connection(execute_sql,*data):
    cur = 15
    if not data:
        execute_sql(cur)
    else:
        execute_sql(cur,*data)

    print("in foo: ", cur)
    
def select_sth_1(cur1,cur2):
    print("select_sth_1", cur1, cur2)
 
def select_sth_2(cur1):
    print("select_sth_2", cur1)

get_connection(select_sth_1,10)
get_connection(select_sth_2)
"""
"""
def add(exe,num):
    lis=[1,2]
    exe(lis,num)
    return lis
#add(lis.append(),3)

def appen(lis,num):
    lis.append(num)
add(appen,3)
"""
# https://coolshell.cn/articles/4758.html
# https://docs.python.org/3/library/unittest.html
# http://dacatay.com/data-science/part-3-time-series-stationarity-python/
