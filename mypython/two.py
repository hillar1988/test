# import tkinter
# top = tkinter.Tk()
# # 进入消息循环
# top.mainloop()

# from tkinter import *           # 导入 tkinter 库
# root = Tk()                     # 创建窗口对象的背景色
#                                 # 创建两个列表
# li     = ['C','python','php','html','SQL','java']
# movie  = ['CSS','jQuery','Bootstrap']
# listb  = Listbox(root)          #  创建两个列表组件
# listb2 = Listbox(root)
# button = Button(root,width = 10)
# for item in li:                 # 第一个小部件插入数据
#     listb.insert(0,item)
#
# for item in movie:              # 第二个小部件插入数据
#     listb2.insert(0,item)
#
# listb.pack()                    # 将小部件放置到主窗口中
# listb2.pack()
# button.pack()
# root.mainloop()                 # 进入消息循环

import sys
import PyQt5.QtWidgets as py

import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from PyQt5.QtCore import QCoreApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Quit button')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
