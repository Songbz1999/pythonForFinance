# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 18:12:52 2018

@author: Thinkpad
"""

import psycopg2
import pandas as pd
import numpy as np
import statsmodels.api as sm 
    
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


def select_data(cursor):
    cursor.execute("""SELECT pricing_date, close, stock_symbol from sz_stocks WHERE pricing_date < '2018-01-01'  and pricing_date > '2007-12-31'""")
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

def adf_test(price_panal):
    n = 0
    min_p = ['', '', 1]
    pair_count = 0
    test_count = 0
    total = (len(price_panal.columns) * len(price_panal.columns) - len(price_panal.columns))/2
    pair = []
    for i in price_panal.columns[:]:
        n += 1
        for j in price_panal.columns[n:]:
            test_count += 1
            stock1 = price_panal[i]
            stock2 = price_panal[j]
            result = sm.tsa.stattools.coint(stock1, stock2)
            if min_p[2] > result[1]:
                min_p = [i[1], j[1], result[1]]
                print("min P value is updated!, now it's: " + str(result[1]))
            if result[1] < 0.05 :
                pair_count += 1
                pair.append([i[1], j[1], result[1]])
                print('Total ' + str(pair_count) + ' pairs has been found!')
            print(i,j,result)
            stock1 = []
            stock2 = []
            result = []
        speed = round(test_count / total, 3)
        print('total ' + str(test_count) + ' tests have been done! ' + str(100*speed) + '% has been done! min P value is :' + str(min_p[2]) )
    print('ADF test finished!')
    if len(pair) == 0:
        print('no pair is found, return the min P value one')
        return min_p
    else:
        return pair

def into_float(df):
    ans = float(df['close0'])
    return ans

def into_str(df):
    ans = str(df['name0'])
    return ans
    
def test_adffunc():
    i = price_panal.columns[2]
    j = price_panal.columns[3]
    stock1 = np.array(price_panal[i])
    stock2 = np.array(price_panal[j])
    result = sm.tsa.stattools.coint(stock1, stock2)
    print(result, i, j, stock1, stock2)

folder_path = 'C:/Users/Thinkpad/Desktop/2018-7 Goldman Programme/sz_stcok'
database(select_table_name)
price = database(select_data)
price_df = pd.DataFrame(price)
price_df.columns = ['date', 'close0', 'name0']
price_df['close'] = price_df.apply(lambda r: into_float(r), axis = 1)
price_df['name'] = price_df.apply(lambda r: into_str(r), axis = 1)
price_panal = pd.pivot_table(price_df, index = [u'date'], columns = [u'name'], values = [u'close'])
pair = adf_test(price_panal)

test_adffunc()
