import sys
import numpy
import random
import Global_list
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from Openfile import read_file
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.btn_open_file = QtWidgets.QPushButton('打开文件')
        self.btn_open_file.clicked.connect(self.msg)

        self.btn_show_origin_data = QtWidgets.QPushButton('显示原始数据')
        self.btn_show_origin_data.clicked.connect(self.show_origin_data)

        self.figure = plt.figure()
        self.axes = self.figure.add_subplot(211)
        self.axes2 = self.figure.add_subplot(212)
        # We want the axes cleared every time plot() is called
        self.axes.set_xlim(0, 100)
        self.axes.set_ylim(0, 65535)
        self.axes2.set_xlim(0, 100)
        self.axes2.set_ylim(0, 65535)
        self.canvas = FigureCanvas(self.figure)
        self.axes.set_title('Chart')


        self.toolbar = NavigationToolbar(self.canvas, self)
        # self.toolbar.hide()

        # Just some button
        self.button1 = QtWidgets.QPushButton('Plot')
        self.button1.clicked.connect(self.plot)

        self.button2 = QtWidgets.QPushButton('Zoom')
        self.button2.clicked.connect(self.zoom)

        self.button3 = QtWidgets.QPushButton('Pan')
        self.button3.clicked.connect(self.pan)

        self.button4 = QtWidgets.QPushButton('Home')
        self.button4.clicked.connect(self.home)

        self.button5 = QtWidgets.QPushButton('Save')
        self.button5.clicked.connect(self.save)

        self.button6 = QtWidgets.QPushButton('Clear')
        self.button6.clicked.connect(self.clear)

        # set the layout
        btnlayout1 = QtWidgets.QHBoxLayout()
        btnlayout1.addWidget(self.btn_open_file)
        btnlayout1.addWidget(self.btn_show_origin_data)
        qw1 = QtWidgets.QWidget(self)
        qw1.setLayout(btnlayout1)


        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(qw1)
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)

        btnlayout = QtWidgets.QHBoxLayout()
        btnlayout.addWidget(self.button1)
        btnlayout.addWidget(self.button2)
        btnlayout.addWidget(self.button3)
        btnlayout.addWidget(self.button4)
        btnlayout.addWidget(self.button5)
        btnlayout.addWidget(self.button6)
        qw = QtWidgets.QWidget(self)
        qw.setLayout(btnlayout)
        layout.addWidget(qw)

        self.setLayout(layout)
    def msg(self):
        file_path, filetype = QFileDialog.getOpenFileName(self,
                                                          "All Files (*);;Text Files (*.txt)")  # 设置文件扩展名过滤
        Global_list.FILE_PATH = file_path  # 使用全局变量存储打开的文件路径

        a = numpy.array([i for i in range(100)])
        print(a)

    def show_origin_data(self):
        file_path = Global_list.FILE_PATH#获取路径名
        if not file_path:
            print("未打开文件")
        else:
            data = read_file(file_path)
            for i in range(len(data)):
                Global_list.DATA.append(int(data[i], 2))  #将二进制数转化成十进制， 从0到65535
        self.axes.plot(Global_list.DATA)
        self.canvas.draw()
    def home(self):
        self.toolbar.home()

    def zoom(self):
        self.toolbar.zoom()

    def pan(self):
        self.toolbar.pan()

    def save(self):
        self.toolbar.save_figure()

    def plot(self):
        self.axes2.plot(Global_list.DATA)
        self.canvas.draw()

    def clear(self):
        self.axes.cla()
        self.axes.set_xlabel('Frequency')
        self.axes.set_ylabel('Amplification')
        self.axes.set_title('test')
        self.canvas.draw()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    main = Window()
    main.setWindowTitle('软件构草项目')
    main.show()

    sys.exit(app.exec_())
