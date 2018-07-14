# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'order_man_page.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from client.ui.order_man_children import *
from client.ui.welcome_page import WelcomPage


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(647, 457)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.treeWidget = QtWidgets.QTreeWidget(Form)
        self.treeWidget.setMinimumSize(QtCore.QSize(150, 0))
        self.treeWidget.setMaximumSize(QtCore.QSize(150, 16777215))
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        self.horizontalLayout.addWidget(self.treeWidget)
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setObjectName("stackedWidget")
        # self.page = QtWidgets.QWidget()
        # self.page.setObjectName("page")
        # self.stackedWidget.addWidget(self.page)
        # self.page_2 = QtWidgets.QWidget()
        # self.page_2.setObjectName("page_2")
        # self.stackedWidget.addWidget(self.page_2)
        self.horizontalLayout.addWidget(self.stackedWidget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "采购员 - 主页"))
        self.treeWidget.headerItem().setText(0, _translate("Form", "功能列表"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("Form", "添加采购单"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("Form", "查看采购单"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)


class OrderManPage():
    def __init__(self, order_man):
        self.order_man = order_man

        self.win = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.win)

        self.adjust_ui()
        self.bind()

    def adjust_ui(self):
        # 移除mac下蓝色边框
        self.ui.treeWidget.setAttribute(QtCore.Qt.WA_MacShowFocusRect, False)
        # 获取各个widget
        self.stackedWidget_child = {
            '欢迎界面': WelcomPage(),
            '添加采购单': AddOrderSheet(self.order_man),
            '查看采购单': CheckOrderSheet(self.order_man),
        }

        for str in self.stackedWidget_child:
            self.ui.stackedWidget.addWidget(self.stackedWidget_child[str].win)

    def bind(self):
        self.ui.treeWidget.itemDoubleClicked.connect(lambda: self.open_child())

    def show(self):
        self.win.show()

    def open_child(self):
        try:
            clicked_str = self.ui.treeWidget.currentItem().text(0)
            self.ui.stackedWidget.setCurrentWidget(self.stackedWidget_child[clicked_str].win)
            # 刷新页面
            self.stackedWidget_child[clicked_str].refresh()
        except Exception as e:
            print('error:', e)


if __name__ == '__main__':
    import sys
    from client.model.order_man import OrderMan

    app = QtWidgets.QApplication(sys.argv)
    order_man = OrderMan('http://127.0.0.1:5000', '2', '2', '采购员')
    if (order_man.login()):
        page = OrderManPage(order_man)
        page.win.show()
    else:
        print('error')

    sys.exit(app.exec_())
