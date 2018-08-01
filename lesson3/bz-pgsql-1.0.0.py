# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 13:41:30 2018

@author: BZ
"""
import psycopg2
import pandas as pd
import io
import os
    
def database(db_command_func,*data):
    try:
        conn = psycopg2.connect(dbname='study', user='quant', host='35.240.207.140', password='quant')
        print("connection success")
    except:
        print("I am unable to connect to the database")
        
    ret = 0
    if not data:    
        ret = db_command_func(conn.cursor())
    else:
        ret = db_command_func(conn.cursor(),*data)
        
    conn.commit()
    conn.close()
    
    return ret


def create_table_if_not_exist(cursor):
    cursor.execute("""
                CREATE TABLE IF NOT EXISTS sz_stocks (
                        pricing_date TIMESTAMP NOT NULL, 
                        open  DECIMAL NOT NULL, 
                        high  DECIMAL NOT NULL, 
                        low  DECIMAL NOT NULL,
                        close  DECIMAL NOT NULL,
                        volume  DECIMAL NOT NULL,
                        stock_symbol VARCHAR(255) NOT NULL)""")
    #CURRENT_TIMESTAMP
    print ("Table create successful!")
    
def insert_value(cursor, df):
    output = io.StringIO();
# ignore the index
    df.to_csv(output, sep='\t',index = False, header = False);
    output.getvalue();
# jump to start of stream
    output.seek(0);
    cursor.copy_from(output, 'sz_stocks', null='')
    print ("Data insert successful!")
# df.to_sql('db_table2', engine, if_exists='replace')

def select_data(cursor):
    cursor.execute("""SELECT * from sz_stocks""")
    rows = cursor.fetchall()
    cursor.execute("""SELECT COUNT(*) from sz_stocks""")
    count = cursor.fetchall()
    print ("\nShow me the data:\n")
#    count = 0
    # inserted line sum 5000 * 500, head(0) 
#    for row in rows:
#        print ("   ", row)
#        count += 1
#    print ('total '+ str(count) + 'row data are selected')
    print('Total' + str(count) + ' data are selected')
    return rows

        
def select_table_name(cursor):
    cursor.execute("""SELECT table_schema, table_name FROM information_schema.tables
                       WHERE table_schema = 'public'""")
    rows = cursor.fetchall()
    print ("\nShow me the data:\n")

    # inserted line sum 5000 * 500, head(0) 
    for row in rows:
        print ("   ", row)


def read_csv(folder_path):
    try:
        file_list = os.listdir(folder_path)
    except:
        print('cannot find the folder path')
    # file_list line sum -> 5000 * 500, head(0) random sample 
    count = 0
    print('total '+ str(len(file_list)) + ' files')
    for name in file_list:
        file_path = folder_path + '/' + name
        df0 = pd.read_csv(file_path, sep = ',' ,names = ['date','open','high','low','close','volume','name'],index_col=False,header=None)
        df = df0.drop(df0.index[0])
        df['name'] = name[0:8]
        database(insert_value,df)
        count += 1
        speed = round(count / len(file_list), 3)
        print('file No. ' + str(count) + '; progress bar: '+ str(speed))
    print ("All data insert successful")
    
def check_insert(cursor,folder_path):
    cursor.execute("""SELECT * from sz_stocks WHERE TO_CHAR(pricing_date,'YYYY/MM/DD') = '2017/12/01'""")
    rows = cursor.fetchall()
    test_id = 'SZ000861'
    test_1 = 0
    test_2 = 0
    for row in rows:
        if row[-2] == test_id:
            test_1 += 1
            sql_close = row[-4]
    try:
        file_list = os.listdir(folder_path)
    except:
        print('cannot find the folder path')
    # file_list line sum -> 5000 * 500, head(0) random sample 
    for name in file_list:
        if name == test_id:
            file_path = folder_path + '/' + name
            df0 = pd.read_csv(file_path, sep = ',' ,names = ['date','open','high','low','close','volume','name'],index_col=False,header=None)
            df = df0.drop(df0.index[0])
            
            for _, row in df.iterrows():
                if row.date == '2017/12/1 0:00':
                    test_2 += 1
                    csv_close = row.close
    print ('sql ' + str(test_1) + '; csv ' + str(test_2) + str(test_2))
    print ('sql_close: ' + str(sql_close) + '; csv_close: ' + str(csv_close))
    if sql_close == csv_close:
        print ('Test PASS !!!!!!!!!!!!!')           
    
    
folder_path = 'C:/Users/Thinkpad/Desktop/2018-7 Goldman Programme/sz_stcok'
database(create_table_if_not_exist)
read_csv(folder_path)
database(select_table_name)
a = database(select_data)
database(check_insert,folder_path)

