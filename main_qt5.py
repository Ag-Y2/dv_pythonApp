import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import numpy as np
from db_connect import *
from matplotlib import font_manager, rc
from datetime import date, datetime

font_path = "C:/Windows/Fonts/gulim.ttc"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)


class MyWindow(QWidget):
  def __init__(self):
    super().__init__()
    self.setupUI()

  def setupUI(self):
    self.setGeometry(600, 200, 1200, 600)
    self.setWindowTitle("PyChart Viewer v0.1")
    self.setWindowIcon(QIcon('icon.png'))

    self.lineEdit_startdate = QLineEdit()
    self.lineEdit_startdate.setPlaceholderText('type start date')
    self.lineEdit_enddate = QLineEdit()
    self.lineEdit_enddate.setPlaceholderText('type end date')

    self.lineEdit = QLineEdit()
    self.lineEdit.setPlaceholderText('type id *req*')

    self.pushButton0 = QPushButton("search")
    self.pushButton0.clicked.connect(self.pushButtonClicked_searchId)
    self.pushButton = QPushButton("차트그리기 in canvas")
    self.pushButton.clicked.connect(self.pushButtonClicked)
    self.pushButton1 = QPushButton("상품 매장별 비교 date")
    self.pushButton1.clicked.connect(self.pushButtonClicked1)
    self.pushButton1.clicked.connect(self.pbc1_draw_oncanve)
    self.pushButton_settext = QPushButton("set text")
    self.pushButton_settext.clicked.connect(self.pushButton_pushButton_settext_click)
  

    


    self.fig = plt.Figure()
    self.canvas = FigureCanvas(self.fig)

    #left layout
    self.tableWidget = QTableWidget()
    #self.tableWidget.setGeometry(100, 200, 1400, 1400)
    self.tableWidget.setRowCount(1)
    self.tableWidget.setColumnCount(5)
    self.tableWidget.setItem(0,0, QTableWidgetItem('c1'))
    self.tableWidget.setItem(0,1, QTableWidgetItem('c2'))
    self.tableWidget.setItem(0,2, QTableWidgetItem('c3'))
    self.tableWidget.setItem(0,3, QTableWidgetItem('c4'))
    self.tableWidget.setItem(0,4, QTableWidgetItem('c5'))
    self.tableWidget.doubleClicked.connect(self.tableW_doub_click)

    leftLayout = QVBoxLayout()
    leftLayout.addWidget(self.tableWidget)
    leftLayout.addWidget(self.canvas)
    leftLayout.addWidget(NavigationToolbar(self.canvas, self))

    # Right Layout
    rightLayout = QVBoxLayout()
    rightLayout.addWidget(self.lineEdit_startdate)
    rightLayout.addWidget(self.lineEdit_enddate)
    rightLayout.addWidget(self.lineEdit)
    rightLayout.addWidget(self.pushButton0)
    rightLayout.addWidget(self.pushButton)
    rightLayout.addWidget(self.pushButton1)
    rightLayout.addWidget(self.pushButton_settext)
    rightLayout.addStretch(1)

    layout = QHBoxLayout()
    layout.addLayout(leftLayout)
    layout.addLayout(rightLayout)
    layout.setStretchFactor(leftLayout, 1)
    layout.setStretchFactor(rightLayout, 0)

    self.setLayout(layout)
  ###########setupUI###########

  def tableW_doub_click(self):
    row = self.tableWidget.currentIndex().row()
    column = self.tableWidget.currentIndex().column()
    cell = self.tableWidget.item(row, column)

    if cell is not None:
      self.lineEdit.setText(cell.text())
      print(cell.text())
    else:
      print('cell is null')

  def pushButtonClicked(self):
    print(self.lineEdit.text())
    self.fig.clear()
    #self.addToolBar(NavigationToolbar(self.canvas, self))
    ax = self.fig.subplots()
    ax.plot([0, 1, 2], [1, 5, 3], '-')

    self.canvas.draw()
  ################pushButtonClicked################

  def pushButtonClicked_searchId(self):
    print('pushButtonClicked_searchId')
    print(self.lineEdit.text())
    sql = f"""
    SELECT ID, productName , middleoption, lastOption, productCode
    FROM products
    WHERE productCode LIKE '%{self.lineEdit.text()}%'
    """

    print(sql)

    list = db_connect(sql)

    if list == "error":
      print('error')
      return 

    if (len(list) > 0):
      coutrow = self.tableWidget.rowCount()
      for x in range (0 , coutrow):
        self.tableWidget.removeRow(x)

      #self.tableWidget.clear()
      for i in list:
        rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)

        id = i.get('ID')
        pid = str(id)
        print(id)
        product_name = i.get('productName')
        middle_option = i.get('middleoption')
        last_option = i.get('lastOption')
        product_code = i.get('productCode')

        self.tableWidget.setItem(rowPosition,0, QTableWidgetItem(pid))
        self.tableWidget.setItem(rowPosition,1, QTableWidgetItem(product_name))
        self.tableWidget.setItem(rowPosition,2, QTableWidgetItem(middle_option))
        self.tableWidget.setItem(rowPosition,3, QTableWidgetItem(last_option))
        self.tableWidget.setItem(rowPosition,4, QTableWidgetItem(product_code))

    self.fig.clear()
    self.canvas.draw()

    


  ############## /pushButtonClicked_searchId ############

  def pushButtonClicked1(self):
    print('btn1')
    #clear canvas
    self.fig.clear()
    print(self.lineEdit.text())
    db_con_stat()

    #query
    start_date = self.lineEdit_startdate.text()
    end_date = self.lineEdit_enddate.text()
    product_no = self.lineEdit.text()

    today = date.today()

    if not end_date:
      print('stirng is empty')
      
      today_date = today.strftime("%Y-%m-%d")
      enddate = today_date
      print(today_date)
    else:
      print('string is not empty')
      enddate = end_date
    
    if not start_date:
      today_date = today.strftime("%Y-%m-%d")
      if today.month < 10:
        mon = f'0{today.month}'

      start_date = f'{today.year - 1}-{mon}-{today.day}'
      start_date = start_date



    #enddate = '2021-01-09'
    #sql = f"""
    #  SELECT mall, COUNT(mall) AS mallCount, product_no, CAST(sum(qty) as SIGNED) AS quantity , datetime
    #  FROM `out` 
    #  WHERE product_no = {product_no} and DATE(datetime) <= DATE('{enddate}') 
    #  GROUP BY mall, product_no
    #  """

    sql = f"""
      SELECT mall, COUNT(mall) AS mallCount, product_no, CAST(sum(qty) as SIGNED) AS quantity , datetime
      FROM `out` 
      WHERE product_no = {product_no} and DATE(datetime) BETWEEN '{start_date}'  and '{enddate}'
      GROUP BY mall, product_no
      """

    print(sql)
    #db result   39709198
    list = db_connect(sql)

    if list == "error":
      print('error')
      return 
    #allocat data
    mall_nameList = []
    mall_qtyList = []

    if (len(list) > 1):
      print('listing data')
      for i in list:
        qty = i.get('quantity')
        mallName = i.get('mall')
        mall_nameList.append(mallName)
        mall_qtyList.append(qty)

        #print(f'quantity{qty}, name of mall: {mallName}')

    #draw bar chart
    
    x = np.arange(len(mall_nameList))
    width = 0.5

    fig, ax = plt.subplots()
    dataset1 = ax.bar(x - width/2, mall_qtyList, width, label='qty')

    ax.set_ylabel('quantity')
    ax.set_title(f'TEST bar chart {product_no} / {enddate}')
    ax.set_xticks(x)
    ax.set_xticklabels(mall_nameList)
    ax.legend()

    ax.bar_label(dataset1, padding=3)

    fig.tight_layout()

    plt.show()



  ############## /pushButtonClicked1 ############

  def pbc1_draw_oncanve(self):
    print('will try to draw')
    print(self.lineEdit.text())
    start_date = self.lineEdit_startdate.text()
    end_date = self.lineEdit_enddate.text()
    product_no = self.lineEdit.text()

    today = date.today()

    if not end_date:
      print('stirng is empty')
      
      today_date = today.strftime("%Y-%m-%d")
      enddate = today_date
      print(today_date)
    else:
      print('string is not empty')
      enddate = end_date
    
    if not start_date:
      today_date = today.strftime("%Y-%m-%d")
      if today.month < 10:
        mon = f'0{today.month}'

      start_date = f'{today.year - 1}-{mon}-{today.day}'
      start_date = start_date

    sql = f"""
      select DATE_FORMAT(DATE(datetime), '%Y-%m') AS month, CAST(sum(qty) as SIGNED) AS quantity
      FROM `out`
      WHERE product_no = {product_no} and DATE(datetime) BETWEEN '{start_date}'  and '{enddate}'
      group by month

      """

    list = db_connect(sql)

    if list == "error":
      print('error')
      return 

    month_List = []
    qty_List = []

    if (len(list) > 0):
      print('listing data')
      for i in list:
        month = i.get('month')
        qty = i.get('quantity')
        month_List.append(month)
        qty_List.append(qty)

    self.fig.clear()
    #self.addToolBar(NavigationToolbar(self.canvas, self))
    ax = self.fig.subplots()
    #ax.plot([0, 1, 2], [1, 5, 3], '-')  , color='blue'
    
    ax.plot(month_List, qty_List, marker='o', linestyle='solid')
    #ax.xlabel('month')
    #ax.ylabel('qty')

    self.canvas.draw()


  
  def pushButton_pushButton_settext_click(self):
    print('pushButton_pushButton_settext_click')
    rowPosition = self.tableWidget.rowCount()
    self.tableWidget.insertRow(rowPosition)
    self.tableWidget.setItem(rowPosition,4, QTableWidgetItem('c5'))

  ############## /pushButton_pushButton_settext_click ############

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()



#https://wikidocs.net/5251