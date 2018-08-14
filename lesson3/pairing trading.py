# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 18:12:52 2018

@author: Thinkpad
"""

import psycopg2
import pandas as pd
import numpy as np
import statsmodels.api as sm 
import matplotlib.pyplot as plt    
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
            stock1 = price_panal[i].sort_index()
            stock2 = price_panal[j].sort_index()
            result = sm.tsa.stattools.coint(stock1[::-1][:500][::-1], stock2[::-1][:500][::-1])
#            plt.plot(stock1)
#            plt.plot(stock2)
#            plt.show()
            if min_p[2] > result[1]:
                min_p = [i[1], j[1], result[1]]
                print("min P value is updated!, now it's: " + str(result[1]))
                plt.plot(stock1)
                plt.plot(stock2)
                plt.show()
            if result[1] < 0.05 :
                if stock1[-1] < 500 and stock2[2] < 500 and i[1][2:5] in ('000','002','300') and j[1][2:5] in ('000','002','300'):
                    pair_count += 1
                    pair.append([i[1], j[1], result[1]])
                    print('Total ' + str(pair_count) + ' pairs has been found!')
#               print(i,j,result)
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
    i = price_panal.columns[22]
    j = price_panal.columns[22]
    stock1 = price_panal[i]
    stock2 = price_panal[j]
    x1 = stock1.dropna()
    result = sm.tsa.stattools.coint(x1, x1)
    print(result, i, j, stock1, stock2)

def pair_plot(pair):
    for i in pair:
        plt.plot(price_panal[('close',i[0])].sort_index())
        plt.plot(price_panal[('close',i[1])].sort_index())
        plt.show()
        print(i[0],i[1])

folder_path = 'C:/Users/Thinkpad/Desktop/2018-7 Goldman Programme/sz_stcok'
#database(select_table_name)
price = database(select_data)
price_df = pd.DataFrame(price)
price_df.columns = ['date', 'close0', 'name0']
price_df['close'] = price_df.apply(lambda r: into_float(r), axis = 1)
price_df['name'] = price_df.apply(lambda r: into_str(r), axis = 1)
price_panal = pd.pivot_table(price_df, index = [u'date'], columns = [u'name'], values = [u'close'])
pair = adf_test(price_panal)
pair_plot(pair)
#
#test_adffunc()
#x = pd.DataFrame({'a':[1.0,3.0,5.0,7,4,5,6,4,7,8,9]})
#x = np.array([1, 2, 3, 4, 5, 6, 7])
#result = x['a']
#p1= sm.tsa.stattools.coint(result, result)
#p2 = sm.tsa.stattools.adfuller(x,1)
#print(p2)
#
##coint(x, x)
#print (p)
plt.plot(price_panal[('close','SZ002511')][::-1][:500][::-1])
plt.plot(price_panal[('close','SZ162411')][::-1][:500][::-1])
plt.show()
plt.plot(price_panal[('close','SZ000011')].sort_index())
plt.plot(price_panal[('close','SZ000921')].sort_index())
plt.show()