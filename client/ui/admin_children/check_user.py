# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'check_user.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(558, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
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

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "所有用户如下表："))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "新建列"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "序号"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "用户名"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "密码（加密后）"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "联系方式"))


class CheckUser():
    def __init__(self, admin):
        self.admin = admin
        self.win = QtWidgets.QWidget()
        self.ui = Ui_Form()
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
        pass


    def refresh(self):
        self.load_data()


    def load_data(self):
        try:
            statue, users = self.admin.get_all_users()
            if(statue == True):
                data_num = len(users)
                self.ui.tableWidget.setRowCount(data_num)
                for  i, user in enumerate(users):
                    self.ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(i+1)))
                    self.ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(user['name'])))
                    self.ui.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(user['password'])))
                    self.ui.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str(user['department'])))
                    self.ui.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(str(user['contact'])))
        except Exception as e:
            print(e)