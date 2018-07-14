# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin_page.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from client.ui.admin_children import *
from client.ui.welcome_page import WelcomPage


class Ui_admin_page(object):
    def setupUi(self, admin_page):
        admin_page.setObjectName("admin_page")
        admin_page.resize(884, 651)
        admin_page.setMinimumSize(QtCore.QSize(0, 0))
        admin_page.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.horizontalLayout = QtWidgets.QHBoxLayout(admin_page)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.treeWidget = QtWidgets.QTreeWidget(admin_page)
        self.treeWidget.setMinimumSize(QtCore.QSize(171, 0))
        self.treeWidget.setMaximumSize(QtCore.QSize(171, 16777215))
        self.treeWidget.setStyleSheet("QWidget:focus{outline: none;}")
        self.treeWidget.setIndentation(21)
        self.treeWidget.setRootIsDecorated(True)
        self.treeWidget.setItemsExpandable(True)
        self.treeWidget.setHeaderHidden(False)
        self.treeWidget.setExpandsOnDoubleClick(True)
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.horizontalLayout.addWidget(self.treeWidget)
        self.stackedWidget = QtWidgets.QStackedWidget(admin_page)
        self.stackedWidget.setObjectName("stackedWidget")
        # self.page_1 = QtWidgets.QWidget()
        # self.page_1.setObjectName("page_1")
        # self.stackedWidget.addWidget(self.page_1)
        # self.page_2 = QtWidgets.QWidget()
        # self.page_2.setObjectName("page_2")
        # self.stackedWidget.addWidget(self.page_2)
        self.horizontalLayout.addWidget(self.stackedWidget)

        self.retranslateUi(admin_page)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(admin_page)

    def retranslateUi(self, admin_page):
        _translate = QtCore.QCoreApplication.translate
        admin_page.setWindowTitle(_translate("admin_page", "Form"))
        self.treeWidget.headerItem().setText(0, _translate("admin_page", "功能面板"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("admin_page", "用户管理"))
        self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("admin_page", "添加用户"))
        self.treeWidget.topLevelItem(0).child(1).setText(0, _translate("admin_page", "删除用户"))
        self.treeWidget.topLevelItem(0).child(2).setText(0, _translate("admin_page", "修改用户信息"))
        self.treeWidget.topLevelItem(0).child(3).setText(0, _translate("admin_page", "查看用户信息"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("admin_page", "仓库管理"))
        self.treeWidget.topLevelItem(1).child(0).setText(0, _translate("admin_page", "添加仓库"))
        self.treeWidget.topLevelItem(1).child(1).setText(0, _translate("admin_page", "删除仓库"))
        self.treeWidget.topLevelItem(1).child(2).setText(0, _translate("admin_page", "修改仓库信息"))
        self.treeWidget.topLevelItem(1).child(3).setText(0, _translate("admin_page", "查看仓库信息"))
        self.treeWidget.topLevelItem(2).setText(0, _translate("admin_page", "供应商管理"))
        self.treeWidget.topLevelItem(2).child(0).setText(0, _translate("admin_page", "添加供应商"))
        self.treeWidget.topLevelItem(2).child(1).setText(0, _translate("admin_page", "删除供应商"))
        self.treeWidget.topLevelItem(2).child(2).setText(0, _translate("admin_page", "修改供应商信息"))
        self.treeWidget.topLevelItem(2).child(3).setText(0, _translate("admin_page", "查看供应商信息"))
        self.treeWidget.topLevelItem(3).setText(0, _translate("admin_page", "商品管理"))
        self.treeWidget.topLevelItem(3).child(0).setText(0, _translate("admin_page", "添加商品"))
        self.treeWidget.topLevelItem(3).child(1).setText(0, _translate("admin_page", "删除商品"))
        self.treeWidget.topLevelItem(3).child(2).setText(0, _translate("admin_page", "修改商品信息"))
        self.treeWidget.topLevelItem(3).child(3).setText(0, _translate("admin_page", "查看商品信息"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)



class AdminPage():
    def __init__(self, admin):
        # 保存登陆窗口传来的admin信息
        self.admin = admin
        # 创建新窗口,绘制ui
        self.win = QtWidgets.QWidget()
        self.ui = Ui_admin_page()
        self.ui.setupUi(self.win)

        self.adjust_ui()
        # 绑定事件
        self.bind()

    def bind(self):
        self.ui.treeWidget.itemDoubleClicked.connect(lambda: self.open_child())

    def show(self):
        self.win.show()

    def hide(self):
        self.win.hide()

    def adjust_ui(self):
        # 移除mac下蓝色边框
        self.ui.treeWidget.setAttribute(QtCore.Qt.WA_MacShowFocusRect, False)
        # 获取各个widget
        self.stackedWidget_child = {
            '欢迎界面': WelcomPage(),
            '添加用户': AddUser(self.admin),
            '删除用户': DeleteUser(self.admin),
            '修改用户信息': ChangeUser(self.admin),
            '查看用户信息': CheckUser(self.admin),
            '添加仓库': AddWarehouse(self.admin),
            '删除仓库': DeleteWarehouse(self.admin),
            '修改仓库信息': ChangeWarehouse(self.admin),
            '查看仓库信息': CheckWarehouse(self.admin),
            '添加供应商': AddSupplier(self.admin),
            '删除供应商': DeleteSupplier(self.admin),
            '修改供应商信息': ChangeSupplier(self.admin),
            '查看供应商信息': CheckSupplier(self.admin),
            '添加商品': AddCommodity(self.admin),
            '删除商品': DeleteCommodity(self.admin),
            '修改商品信息': ChangeCommodity(self.admin),
            '查看商品信息': CheckCommodity(self.admin)
        }

        for str in self.stackedWidget_child:
            self.ui.stackedWidget.addWidget(self.stackedWidget_child[str].win)

    def open_child(self):
        try:
            clicked_str = self.ui.treeWidget.currentItem().text(0)
            self.ui.stackedWidget.setCurrentWidget(self.stackedWidget_child[clicked_str].win)
            # 刷新页面
            self.stackedWidget_child[clicked_str].refresh()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    import sys
    from client.model.admin import *

    app = QtWidgets.QApplication(sys.argv)
    admin = Admin('http://127.0.0.1:5000','admin', 'admin', '系统管理员')
    if (admin.login()):
        admin_page = AdminPage(admin)
        admin_page.show()
    else:
        print('error')

    sys.exit(app.exec_())
