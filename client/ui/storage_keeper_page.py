# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'storage_keeper_page.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from client.ui.storage_keeper_children import *
from client.ui.welcome_page import WelcomPage


class Ui_storage_keeper_main_page(object):
    def setupUi(self, storage_keeper_main_page):
        storage_keeper_main_page.setObjectName("storage_keeper_main_page")
        storage_keeper_main_page.resize(689, 469)
        self.horizontalLayout = QtWidgets.QHBoxLayout(storage_keeper_main_page)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.treeWidget = QtWidgets.QTreeWidget(storage_keeper_main_page)
        self.treeWidget.setMinimumSize(QtCore.QSize(150, 0))
        self.treeWidget.setMaximumSize(QtCore.QSize(150, 16777215))
        self.treeWidget.setObjectName("treeWidget")

        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        self.horizontalLayout.addWidget(self.treeWidget)
        self.stackedWidget = QtWidgets.QStackedWidget(storage_keeper_main_page)
        self.stackedWidget.setObjectName("stackedWidget")
        # self.page = QtWidgets.QWidget()
        # self.page.setObjectName("page")
        # self.stackedWidget.addWidget(self.page)
        # self.page_2 = QtWidgets.QWidget()
        # self.page_2.setObjectName("page_2")
        # self.stackedWidget.addWidget(self.page_2)
        self.horizontalLayout.addWidget(self.stackedWidget)

        self.retranslateUi(storage_keeper_main_page)
        QtCore.QMetaObject.connectSlotsByName(storage_keeper_main_page)

    def retranslateUi(self, storage_keeper_main_page):
        _translate = QtCore.QCoreApplication.translate
        storage_keeper_main_page.setWindowTitle(_translate("storage_keeper_main_page", "仓库管理员 - 主页"))
        self.treeWidget.headerItem().setText(0, _translate("storage_keeper_main_page", "仓储管理菜单"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)

        self.treeWidget.topLevelItem(0).setText(0, _translate("storage_keeper_main_page", "入库管理"))
        self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("storage_keeper_main_page", "添加入库单"))
        self.treeWidget.topLevelItem(0).child(1).setText(0, _translate("storage_keeper_main_page", "查看入库记录"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("storage_keeper_main_page", "出库管理"))
        self.treeWidget.topLevelItem(1).child(0).setText(0, _translate("storage_keeper_main_page", "添加出库单"))
        self.treeWidget.topLevelItem(1).child(1).setText(0, _translate("storage_keeper_main_page", "查看出库记录"))
        self.treeWidget.topLevelItem(2).setText(0, _translate("storage_keeper_main_page", "查看库存"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)




class StorageKeeperPage():
    def __init__(self, storage_keeper):
        self.storage_keeper = storage_keeper

        self.win = QtWidgets.QWidget()
        self.ui = Ui_storage_keeper_main_page()
        self.ui.setupUi(self.win)

        self.adjust_ui()
        self.bind()

    def adjust_ui(self):
        # 移除mac下蓝色边框
        self.ui.treeWidget.setAttribute(QtCore.Qt.WA_MacShowFocusRect, False)
        # 获取各个widget
        self.stackedWidget_child = {
            '欢迎界面': WelcomPage(),
            '添加入库单': AddInStorageSheet(self.storage_keeper),
            '查看入库记录': CheckInStorageSheets(self.storage_keeper),
            '添加出库单': AddExStorageSheet(self.storage_keeper),
            '查看出库记录': CheckExStorageSheets(self.storage_keeper),
            '查看库存': CheckStorage(self.storage_keeper),
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
            print('error:',e)


if __name__ == '__main__':
    import sys
    from client.model.storage_keeper import StorageKeeper

    app = QtWidgets.QApplication(sys.argv)
    storager_keeper = StorageKeeper('http://127.0.0.1:5000', '3', '3', '仓库管理员')
    if (storager_keeper.login()):
        page = StorageKeeperPage(storager_keeper)
        page.win.show()

    sys.exit(app.exec_())
