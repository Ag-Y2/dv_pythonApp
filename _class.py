# -*- coding: utf-8 -*-
class Cup:
    def __init__(self, t):
        self.count = t

    def getcount(self):
        return self.count

    def setcount(self, n):
        self.count = n

mall_nameList = []
mall_qtyList = []
class Mall:
    def __init__(self):
        self.mallname = "mallName"
        self.mallcount = "mallCount"
        self.mallqty = "mallQty"
        self.productno = "productNumber"
        self.mallnameList = []
        self.mallqtyList = []

    def set_mallname(self, name):
        self.mallname = name
    
    def set_mallcount(self, count):
        self.mallcount = count

    def set_mallqty(self, qty):
        self.mallqty = qty
    
    def print_mall(self):
        txt = 'mall'

    def set_mallname_list(self, name):
        print(name)
        self.mallnameList.append(name)

    def set_mallqty_list(self, qty):
        print(qty)
        self.mallqtyList.append(qty)

    def get_mallname_list(self):
        print('getting name')
        return self.mallnameList

    def get_mallqty_list(self):
        print('getting qty')
        return self.mallqtyList