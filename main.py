#-*- coding: utf-8 -*-
from pymysql import cursors
from _class import *
from _gui import *
from db_connect import *
from db_matplot import *
import json



get_cup = Cup(555)
print('=======data array len=======')
print(len(data_array))
print('==============')
#for i in data_array:
#    print(i)

print('--------')
print(get_cup.count)
print('--------')

def sql_mall():
    product_no = 11923
    date = '2021-01-09'
    #sql = f'SELECT mall, COUNT(mall), product_no, CAST(sum(qty) as SIGNED), datetime FROM `out` WHERE product_no = {product_no} and DATE(datetime) > DATE({date}) GROUP BY mall, product_no'
    sql = f"""
        SELECT mall, COUNT(mall) AS mallCount, product_no, CAST(sum(qty) as SIGNED) AS quantity , datetime
        FROM `out` 
        WHERE product_no = {product_no} and DATE(datetime) > DATE('{date}') 
        GROUP BY mall, product_no
    """
    print(sql)
    #cursors.execute(sql, product_no , date )
    
    #"select mall,COUNT(mall), product_no, CAST(sum(qty) as SIGNED), datetime from `out` where product_no = 11923 and DATE(datetime) > DATE('2021-01-09')  group by mall, product_no "
    list = db_connect(sql)

    mall = Mall()


    if len(list) > 1:
        print('list_row is > 1')
        for i in list:
            #json parsing
            qty = i.get('quantity')
            #print(qty)
            
            mallName = i.get('mall')
            
            #print(f'{mallName}: {qty} ')
            #mall.set_mallname_list(mallName)
            #mall.set_mallqty_list(qty)
            mall_nameList.append(mallName)
            mall_qtyList.append(qty)


    else:
        print("in else ")

def init_run():
    print('dfdf')
    sql_mall()
    
if __name__ == "__main__":
    init_run()
    barchart()
    #db_connect()
    #init_gui()
    #db_connect()