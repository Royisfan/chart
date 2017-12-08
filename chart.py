import sys
import math

import Global_list
from Openfile import read_file

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # 选择文件btn控件
        self.btn_open_file = QtWidgets.QPushButton('打开文件')
        self.btn_open_file.clicked.connect(self.select_file)

        # 显示原始数据btn控件
        self.btn_show_origin_data = QtWidgets.QPushButton('显示原始数据')
        self.btn_show_origin_data.clicked.connect(self.show_origin_data)

        # 两个显示数据的通道
        self.figure = plt.figure()

        # 原始数据通道
        self.axes_origin = self.figure.add_subplot(211)  # 2*1，占据第一个块
        self.axes_origin.set_xlim(0, 100)                # 设置X轴
        self.axes_origin.set_ylim(0, 65535)              # 设置Y轴

        self.axes_change = self.figure.add_subplot(212)  # 2*1，占据第二个块
        self.axes_change.set_xlim(0, 100)                # 设置X轴
        self.axes_change.set_ylim(-1, 1)                  # 设置Y轴

        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)

        # 功能btn控件
        self.btn_sin = QtWidgets.QPushButton('正弦')
        self.btn_sin.clicked.connect(self.sin)

        self.btn_cos = QtWidgets.QPushButton('余弦')
        self.btn_cos.clicked.connect(self.cos)

        # set the layout
        layout = QtWidgets.QVBoxLayout()

        # 显示控件
        btnlayout_operation = QtWidgets.QHBoxLayout()
        btnlayout_operation.addWidget(self.btn_open_file)
        btnlayout_operation.addWidget(self.btn_show_origin_data)
        qw_operation = QtWidgets.QWidget(self)
        qw_operation.setLayout(btnlayout_operation)
        layout.addWidget(qw_operation)

        # 显示两个通道
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)

        # 显示控件
        btnlayout_function = QtWidgets.QHBoxLayout()
        btnlayout_function.addWidget(self.btn_sin)
        btnlayout_function.addWidget(self.btn_cos)
        qw_function = QtWidgets.QWidget(self)
        qw_function.setLayout(btnlayout_function)
        layout.addWidget(qw_function)

        self.setLayout(layout)

    # 选择文件，保存文件路径

    def select_file(self):
        file_path, filetype = QFileDialog.getOpenFileName(self,
                                                          "All Files (*);;Text Files (*.txt)")  # 设置文件扩展名过滤
        Global_list.FILE_PATH = file_path  # 使用全局变量存储打开的文件路径

    # 在原始画布上显示数据

    def show_origin_data(self):
        file_path = Global_list.FILE_PATH  # 获取路径名
        if not file_path:
            print("未打开文件")
        else:
            data = read_file(file_path)  # 获取文件数据
            for i in range(len(data)):
                Global_list.DATA.append(int(data[i], 2))  # 将二进制数转化成十进制， 从0到65535
        self.axes_origin.plot(Global_list.DATA)
        self.canvas.draw()

    # 对原始数据进行的cos函数操作

    def sin(self):
        data = Global_list.DATA
        changed_data = []
        for i in range(len(data)):
            changed_data.append(math.sin(data[i]))
        if changed_data:
            self.clean()
            self.axes_change.plot(changed_data)
            self.canvas.draw()

    # 对原始数据进行的cos函数操作

    def cos(self):
        data = Global_list.DATA
        changed_data = []
        for i in range(len(data)):
            changed_data.append(math.cos(data[i]))
        if changed_data:
            self.clean()
            self.axes_change.plot(changed_data)
            self.canvas.draw()

    # 在每次进行对原始数据的处理显示前，将画布上的数据全部清除

    def clean(self):
        line_length = len(self.axes_change.lines)
        if line_length != 0:
            for i in range(line_length):
                self.axes_change.lines.remove(self.axes_change.lines[i])


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    main = Window()
    main.setWindowTitle('软件构造项目')
    main.show()

    sys.exit(app.exec_())
