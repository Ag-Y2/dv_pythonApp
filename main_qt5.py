import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import numpy as np
from db_connect import *
from matplotlib import font_manager, rc

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

    self.lineEdit = QLineEdit()
    self.pushButton0 = QPushButton("search")
    self.pushButton0.clicked.connect(self.pushButtonClicked_searchId)
    self.pushButton = QPushButton("차트그리기")
    self.pushButton.clicked.connect(self.pushButtonClicked)
    self.pushButton1 = QPushButton("차트그리기1")
    self.pushButton1.clicked.connect(self.pushButtonClicked1)

    self.fig = plt.Figure()
    self.canvas = FigureCanvas(self.fig)

    leftLayout = QVBoxLayout()
    leftLayout.addWidget(self.canvas)
    leftLayout.addWidget(NavigationToolbar(self.canvas, self))

    # Right Layout
    rightLayout = QVBoxLayout()
    rightLayout.addWidget(self.lineEdit)
    rightLayout.addWidget(self.pushButton0)
    rightLayout.addWidget(self.pushButton)
    rightLayout.addWidget(self.pushButton1)
    rightLayout.addStretch(1)

    layout = QHBoxLayout()
    layout.addLayout(leftLayout)
    layout.addLayout(rightLayout)
    layout.setStretchFactor(leftLayout, 1)
    layout.setStretchFactor(rightLayout, 0)

    self.setLayout(layout)

  def pushButtonClicked(self):
    print(self.lineEdit.text())
    self.fig.clear()
    #self.addToolBar(NavigationToolbar(self.canvas, self))
    ax = self.fig.subplots()
    ax.plot([0, 1, 2], [1, 5, 3], '-')

    self.canvas.draw()

  def pushButtonClicked_searchId(self):
    print('pushButtonClicked_searchId')
    print(self.lineEdit.text())





  def pushButtonClicked1(self):
    print('btn1')
    #clear canvas
    self.fig.clear()
    print(self.lineEdit.text())
    db_con_stat()

    #query
    product_no = self.lineEdit.text()
    date = '2021-01-09'
    sql = f"""
      SELECT mall, COUNT(mall) AS mallCount, product_no, CAST(sum(qty) as SIGNED) AS quantity , datetime
      FROM `out` 
      WHERE product_no = {product_no} and DATE(datetime) > DATE('{date}') 
      GROUP BY mall, product_no
      """
    #db result
    list = db_connect(sql)

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

        print(f'quantity{qty}, name of mall: {mallName}')

    #draw bar chart
    
    x = np.arange(len(mall_nameList))
    width = 0.5

    fig, ax = plt.subplots()
    dataset1 = ax.bar(x - width/2, mall_qtyList, width, label='qty')

    ax.set_ylabel('quantity')
    ax.set_title('TEST bar chart')
    ax.set_xticks(x)
    ax.set_xticklabels(mall_nameList)
    ax.legend()

    ax.bar_label(dataset1, padding=3)

    fig.tight_layout()

    plt.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()



#https://wikidocs.net/5251