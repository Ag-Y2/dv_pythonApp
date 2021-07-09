#-*- coding: utf-8 -*-
import pymysql
from _gui import *

data_array = ""

def db_connect(sql):
    print('db connect init')
    conn = None
    cur = None
    global data_array

    _host = "db.marketb.kr"
    _user = "marketb"
    _password = "akzptql1!"
    _db = "marketb"#"wms"
    _charset = "utf8"

    conn = pymysql.connect(host=_host,user=_user,password=_password,db=_db, charset=_charset)
    curs = conn.cursor()

    #sql_desc_100 = "select * from orders_out order by created desc limit 100"
    
    #sql_count_by_mall = "select mall,COUNT(mall), product_name from orders_out group by mall, product_name limit 30"
    
    #sql = sql_count_by_mall

    curs.execute(sql)
    row = curs.fetchall()
    list_row = list(row)

    #set as json formate
    columns = [column[0] for column in curs.description]
    results = []
    for line in row:
        results.append(dict(zip(columns, line)))


    #print(results)
    
    print('connection close')
    conn.close()
    return results #list_row
    '''
    if len(list_row) > 1:
        print('list_row is > 1')
        data_array = list_row
    else:
        print("in else ")
    '''
     

    #add_to_list(list_row)
    #for i in list_row:
    #   print(i)



