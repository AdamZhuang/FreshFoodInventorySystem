# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'manager_page.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from client.ui.manager_children import *


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(850, 442)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.treeWidget = QtWidgets.QTreeWidget(Form)
        self.treeWidget.setMinimumSize(QtCore.QSize(150, 0))
        self.treeWidget.setMaximumSize(QtCore.QSize(150, 16777215))
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.horizontalLayout.addWidget(self.treeWidget)
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.horizontalLayout.addWidget(self.stackedWidget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "经理 - 主页"))
        self.treeWidget.headerItem().setText(0, _translate("Form", "功能列表"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("Form", "订货通知管理"))
        self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("Form", "添加订货通知单"))
        self.treeWidget.topLevelItem(0).child(1).setText(0, _translate("Form", "查看订货通知单"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("Form", "仓储管理"))
        self.treeWidget.topLevelItem(1).child(0).setText(0, _translate("Form", "查看库存"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)


class ManagerPage(object):
    def __init__(self, manager):
        self.manager = manager
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
            '添加订货通知单': AddNoticeSheet(self.manager),
            '查看订货通知单': CheckNoticeSheet(self.manager),
            '查看库存': CheckStorage(self.manager),
        }

        for str in self.stackedWidget_child:
            self.ui.stackedWidget.addWidget(self.stackedWidget_child[str].win)

    def bind(self):
        self.ui.treeWidget.itemDoubleClicked.connect(lambda: self.open_child())

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
    from client.model.manager import Manager

    app = QtWidgets.QApplication(sys.argv)
    manager = Manager('http://127.0.0.1:5000', '1', '1', '经理')
    if (manager.login()):
        page = ManagerPage(manager)
        page.win.show()
    else:
        print('error')

    sys.exit(app.exec_())