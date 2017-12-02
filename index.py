import sys
import Global_list
from Openfile import read_file
from PyQt5.QtWidgets import *


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()
        self.center()

    def initUI(self):

        btn_open_file = QPushButton('读取文件', self)
        btn_open_file.resize(200, 20)
        btn_open_file.move(20, 20)
        btn_open_file.clicked.connect(self.msg)

        btn_show_origin_data = QPushButton('显示原始数据', self)
        btn_show_origin_data.resize(200, 20)
        btn_show_origin_data.move(230, 20)
        btn_show_origin_data.clicked.connect(self.show_origin_data)

        btn_show_changed_data = QPushButton('显示计算后的数据', self)
        btn_show_changed_data.resize(200, 20)
        btn_show_changed_data.move(440, 20)
        btn_show_changed_data.clicked.connect(self.show_changed_data)

        btn_multiply_x = QPushButton('对x轴做扩展', self)
        btn_multiply_x.resize(200, 20)
        btn_multiply_x.move(20, 50)
        btn_multiply_x.clicked.connect(self.multiply_x)

        btn_devide_x = QPushButton('对x轴做压缩', self)
        btn_devide_x.resize(200, 20)
        btn_devide_x.move(20, 80)

        btn_multiply_y = QPushButton('对y轴做扩展', self)
        btn_multiply_y.resize(200, 20)
        btn_multiply_y.move(20, 110)

        btn_devide_y = QPushButton('对y轴做压缩', self)
        btn_devide_y.resize(200, 20)
        btn_devide_y.move(20, 140)

        btn_operation_one = QPushButton('操作一', self)
        btn_operation_one.resize(200, 20)
        btn_operation_one.move(20, 190)

        btn_operation_two = QPushButton('操作二', self)
        btn_operation_two.resize(200, 20)
        btn_operation_two.move(20, 220)

        btn_operation_three = QPushButton('操作三', self)
        btn_operation_three.resize(200, 20)
        btn_operation_three.move(20, 250)

        self.resize(650, 500)
        self.center()
        self.setWindowTitle('Icon')
        self.show()

    def center(self):  #将窗口居中显示
        qr = self.frameGeometry()  #获得主窗口的一个矩形特定几何图形
        cp = QDesktopWidget().availableGeometry().center()  #计算相对于显示器的绝对值，根据绝对值获得屏幕中心点
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def msg(self):
        file_path, filetype = QFileDialog.getOpenFileName(self,
                                                "All Files (*);;Text Files (*.txt)")  # 设置文件扩展名过滤
        Global_list.FILE_PATH = file_path  #使用全局变量存储打开的文件路径

    def show_origin_data(self):
        file_path = Global_list.FILE_PATH  #获取路径名
        data = read_file(file_path)
        for i in range(len(data)):
            Global_list.DATA[i] = int(data[i], 2)  #将二进制数转化成十进制， 从0到65535
            print(Global_list.DATA[i])

    def show_changed_data(self):
        print(Global_list.DATA)
        data = Global_list.DATA
        for i in range(len(data)):
            data[i] += 1000
            print(data[i])

    def multiply_x(self):
        data = Global_list.DATA
        changed_data = {}
        for i in range(len(data)):
            changed_data[2*i] = data[i]
            print(changed_data)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())




