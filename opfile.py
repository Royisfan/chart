from PyQt5.QtWidgets import *


def msg(self):

    filename = QFileDialog.getOpenFileName(self,
                                           "选取文件",
                                           "xuyifan/",
                                           "All Files (*);;Text Files (*.txt)")  # 设置文件扩展名过滤,注意用双分号间隔
    return filename