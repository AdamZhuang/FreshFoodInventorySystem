# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'delete_user.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_delete_user(object):
    def setupUi(self, delete_user):
        delete_user.setObjectName("delete_user")
        delete_user.resize(645, 468)
        self.verticalLayout = QtWidgets.QVBoxLayout(delete_user)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(delete_user)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(delete_user)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        self.delete_button = QtWidgets.QPushButton(delete_user)
        self.delete_button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.delete_button.setObjectName("delete_button")
        self.horizontalLayout.addWidget(self.delete_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableWidget = QtWidgets.QTableWidget(delete_user)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tableWidget)

        self.retranslateUi(delete_user)
        QtCore.QMetaObject.connectSlotsByName(delete_user)

    def retranslateUi(self, delete_user):
        _translate = QtCore.QCoreApplication.translate
        delete_user.setWindowTitle(_translate("delete_user", "Form"))
        self.label.setText(_translate("delete_user", "用户名（可双击下方进行表格进行快速选择）"))
        self.delete_button.setText(_translate("delete_user", "删除"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("delete_user", "序号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("delete_user", "用户名"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("delete_user", "密码（加密后）"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("delete_user", "部门"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("delete_user", "联系方式"))


class DeleteUser():
    def __init__(self, admin):
        self.admin = admin
        self.win = QtWidgets.QWidget()
        self.ui = Ui_delete_user()
        self.ui.setupUi(self.win)
        self.customize()

    def customize(self):
        self.adjust_ui()
        self.load_data()
        self.bind()

    def adjust_ui(self):
        # 调整表格
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.ui.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.ui.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.ui.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

    def bind(self):
        self.ui.delete_button.clicked.connect(lambda: self.delete_user())
        self.ui.tableWidget.itemDoubleClicked.connect(lambda: self.quick_choose())

    def refresh(self):
        self.load_data()

    def load_data(self):
        try:
            statue, users = self.admin.get_all_users()
            if (statue == True):
                data_num = len(users)
                self.ui.tableWidget.setRowCount(data_num)
                self.ui.comboBox.clear()
                for i, user in enumerate(users):
                    self.ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(i + 1)))
                    self.ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(user['name'])))
                    self.ui.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(user['password'])))
                    self.ui.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str(user['department'])))
                    self.ui.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(str(user['contact'])))
                    self.ui.comboBox.addItem(str(user['name']))
            else:
                print('something wrong')
        except Exception as e:
            print(e)

    def delete_user(self):
        try:
            username = self.ui.comboBox.currentText()
            if (username == 'admin'):
                reply = QtWidgets.QMessageBox.information(None, '提示', '无法删除管理员用户',
                                                          QtWidgets.QMessageBox.Yes)
                return False
            if (username == ''):
                reply = QtWidgets.QMessageBox.information(None, '提示', '请选择要删除的用户的用户名',
                                                          QtWidgets.QMessageBox.Yes)
                return False
            statue, data = self.admin.delete_user(delete_username=username)
            if (statue == True):
                self.load_data()
                reply = QtWidgets.QMessageBox.information(None, '提示', '删除成功',
                                                          QtWidgets.QMessageBox.Yes)
                self.ui.comboBox.setCurrentIndex(-1)
            elif (statue == False):
                reply = QtWidgets.QMessageBox.information(None, '提示', '删除失败',
                                                          QtWidgets.QMessageBox.Yes)
            elif (statue == 'network_error'):
                reply = QtWidgets.QMessageBox.warning(None, '提示', '连接服务器超时！',
                                                      QtWidgets.QMessageBox.Yes)
        except Exception as e:
            print(e)

    def quick_choose(self):
        selected = self.ui.tableWidget.selectedItems()[1].text()
        self.ui.comboBox.setCurrentText(selected)
