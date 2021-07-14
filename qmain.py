import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvas as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure


class MyApp(QMainWindow):
  def __init__(self):
    super().__init__()

    self.main_widget = QWidget()
    self.setCentralWidget(self.main_widget)

    canvas = FigureCanvas(Figure(figsize=(4, 3)))
    vbox = QVBoxLayout(self.main_widget)
    vbox.addWidget(canvas)

    self.addToolBar(NavigationToolbar(canvas, self))

    self.ax = canvas.figure.subplots()
    self.ax.plot([0, 1, 2], [1, 5, 3], '-')

    self.setWindowTitle('Matplotlib in PyQt5')
    self.setGeometry(300, 200, 600, 400)
    self.show()


if __name__ == '__main__':
  app = QApplication(sys.argv)
  ex = MyApp()
  sys.exit(app.exec_())