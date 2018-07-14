# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'check_commodity.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_check_commodity(object):
    def setupUi(self, check_commodity):
        check_commodity.setObjectName("add_commodity")
        check_commodity.resize(717, 510)
        self.verticalLayout = QtWidgets.QVBoxLayout(check_commodity)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(check_commodity)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tableWidget = QtWidgets.QTableWidget(check_commodity)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.SelectedClicked)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tableWidget)

        self.retranslateUi(check_commodity)
        QtCore.QMetaObject.connectSlotsByName(check_commodity)

    def retranslateUi(self, add_commodity):
        _translate = QtCore.QCoreApplication.translate
        add_commodity.setWindowTitle(_translate("check_commodity", "Form"))
        self.label.setText(_translate("check_commodity", "当前所有商品："))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("check_commodity", "序号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("check_commodity", "商品编号"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("check_commodity", "商品名称"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("check_commodity", "商品类型"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("check_commodity", "计量单位"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("check_commodity", "规格"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("check_commodity", "供应商"))


class CheckCommodity():
    def __init__(self, admin):
        self.admin = admin
        self.win = QtWidgets.QWidget()
        self.ui = Ui_check_commodity()
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
            statue, commodities = self.admin.get_all_commodities()
            data_num = len(commodities)
            self.ui.tableWidget.setRowCount(data_num)
            for i, commodity in enumerate(commodities):
                self.ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(i + 1)))
                self.ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(commodity['code'])))
                self.ui.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(commodity['name'])))
                self.ui.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str(commodity['type'])))
                self.ui.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(str(commodity['unit'])))
                self.ui.tableWidget.setItem(i, 5, QtWidgets.QTableWidgetItem(str(commodity['specification'])))
                self.ui.tableWidget.setItem(i, 6, QtWidgets.QTableWidgetItem(str(commodity['supplier_name'])))
        except Exception as e:
            print(e)