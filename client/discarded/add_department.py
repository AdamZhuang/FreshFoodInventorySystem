# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_department.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from client.model import admin

class Ui_add_department(object):
    def setupUi(self, add_department):
        add_department.setObjectName("add_department")
        add_department.resize(1062, 573)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(add_department)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add_department_label = QtWidgets.QLabel(add_department)
        self.add_department_label.setObjectName("add_department_label")
        self.horizontalLayout.addWidget(self.add_department_label)
        self.add_department_lineedit = QtWidgets.QLineEdit(add_department)
        self.add_department_lineedit.setObjectName("add_department_lineedit")
        self.horizontalLayout.addWidget(self.add_department_lineedit)
        self.add_department_button = QtWidgets.QPushButton(add_department)
        self.add_department_button.setObjectName("add_department_button")
        self.horizontalLayout.addWidget(self.add_department_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.all_department_label = QtWidgets.QLabel(add_department)
        self.all_department_label.setObjectName("all_department_label")
        self.verticalLayout.addWidget(self.all_department_label)
        self.tableWidget = QtWidgets.QTableWidget(add_department)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(True)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.verticalLayout.addWidget(self.tableWidget)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(add_department)
        QtCore.QMetaObject.connectSlotsByName(add_department)

    def retranslateUi(self, add_department):
        _translate = QtCore.QCoreApplication.translate
        add_department.setWindowTitle(_translate("add_department", "Form"))
        self.add_department_label.setText(_translate("add_department", "请输入要添加部门的名称："))
        self.add_department_button.setText(_translate("add_department", "添加"))
        self.all_department_label.setText(_translate("add_department", "当前所有部门:"))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("add_department", "序号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("add_department", "部门名称"))



class AddDepartment():
    def __init__(self, admin):
        self.admin = admin
        self.win = QtWidgets.QWidget()
        self.ui = Ui_add_department()
        self.ui.setupUi(self.win)
        self.customize()


    def customize(self):
        self.adjust_ui()
        self.load_data()
        self.bind()


    def adjust_ui(self):
        # 调整表格
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(1,QtWidgets.QHeaderView.Stretch)
        self.ui.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.ui.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)


    def bind(self):
        self.ui.add_department_button.clicked.connect(lambda :self.add_department())
        pass


    def refresh(self):
        self.load_data()


    def load_data(self):
        try:
            departments = self.admin.get_all_departments()
            data_num = len(departments)
            self.ui.tableWidget.setRowCount(data_num)
            for  i, department in enumerate(departments):
                self.ui.tableWidget.setItem(i,0, QtWidgets.QTableWidgetItem(str(i+1)))
                self.ui.tableWidget.setItem(i,1, QtWidgets.QTableWidgetItem(str(department)))

            # self.ui.tableWidget.set
        except Exception as e:
            print(e)


    def add_department(self):
        try:
            add_department_name = self.ui.add_department_lineedit.text()
            if(self.admin.add_department(add_department_name)):
                self.load_data()
                # print('添加成功')
                reply = QtWidgets.QMessageBox.information(None, '提示', '添加成功',
                                                          QtWidgets.QMessageBox.Yes)
            else:
                self.load_data()
                reply = QtWidgets.QMessageBox.information(None, '提示', '添加失败',
                                                          QtWidgets.QMessageBox.Yes)
        except Exception as e:
            print(e)




