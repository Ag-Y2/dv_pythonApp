# -*- coding: utf-8 -*-
from matplotlib.figure import Figure
from pymysql import cursors
from _class import *
#from _gui import *
from tkinter import *
from db_connect import *
from db_matplot import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import json

'''
http://www.gisdeveloper.co.kr/?p=8343

qt5 over tkinter 
'''

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
            #mallName = unicode(mallName, "utf-8")
            mall_nameList.append(mallName)
            mall_qtyList.append(qty)


    else:
        print("in else ")

def init_run():
    print('dfdf')
    init_gui()
    
    
if __name__ == "__main__":
    init_run()
    #barchart()
    #db_connect()
    #init_gui()
    #db_connect()




count = 0
window = Tk()
root = window
frame = Frame(window)

sb_xyis = Scrollbar(window, orient="horizontal")
sb_xyis.pack(side = BOTTOM, fill = X)

window.title("gui interface")
window.geometry("640x400+300+50")
window.resizable(False, False)


label=Label(window, text="hi, there")
label.pack()


label_count= Label(window, text=0)
label_count.pack()

def countUp():
    global count
    count += 1
    label_count.config(text=str(count))
    #add_to_list()


button = Button(window, overrelief="solid", width=15, command=sql_mall, repeatdelay=1000, repeatinterval=100)
button.pack()

frame.pack()
window.mainloop()

