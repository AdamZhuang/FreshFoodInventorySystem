# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'delete_department.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_delete_department(object):
    def setupUi(self, delete_department):
        delete_department.setObjectName("delete_department")
        delete_department.resize(963, 582)
        self.verticalLayout = QtWidgets.QVBoxLayout(delete_department)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.all_department_label = QtWidgets.QLabel(delete_department)
        self.all_department_label.setObjectName("all_department_label")
        self.horizontalLayout.addWidget(self.all_department_label)
        self.delete_department_button = QtWidgets.QPushButton(delete_department)
        self.delete_department_button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.delete_department_button.setObjectName("delete_department_button")
        self.horizontalLayout.addWidget(self.delete_department_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableWidget = QtWidgets.QTableWidget(delete_department)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.verticalLayout.addWidget(self.tableWidget)

        self.retranslateUi(delete_department)
        QtCore.QMetaObject.connectSlotsByName(delete_department)

    def retranslateUi(self, delete_department):
        _translate = QtCore.QCoreApplication.translate
        delete_department.setWindowTitle(_translate("delete_department", "删除部门"))
        self.all_department_label.setText(_translate("delete_department", "当前所有部门（请选中要删除的部门，点击删除按钮进行删除）:"))
        self.delete_department_button.setText(_translate("delete_department", "删除"))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("delete_department", "序号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("delete_department", "部门名称"))



class DeleteDepartment():
    def __init__(self, admin):
        self.admin = admin
        self.win = QtWidgets.QWidget()
        self.ui = Ui_delete_department()
        self.ui.setupUi(self.win)
        self.customize()

    def customize(self):
        self.adjust_ui()
        self.bind()
        self.load_data()


    def adjust_ui(self):
        # 调整表格自适应
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(1 ,QtWidgets.QHeaderView.Stretch)


    def bind(self):
        self.ui.delete_department_button.clicked.connect(lambda :self.delete_department())


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


    def delete_department(self):
        try:
            selected = self.ui.tableWidget.selectedItems()
            for i, s in enumerate(selected):
                if((i+1)%2 == 0):
                    statue = self.admin.delete_department(s.text())
                    if(statue == False):
                        tips = '删除{delete}成功'.format(delete='s.text()')
                        QtWidgets.QMessageBox.information(None, '提示', tips)

            self.load_data()
            QtWidgets.QMessageBox.information(None, '提示', '删除成功')
        except Exception as e:
            print(e)


