# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'check_storage.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(884, 480)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.warehouse_name_lineEdit = QtWidgets.QLineEdit(Form)
        self.warehouse_name_lineEdit.setObjectName("warehouse_name_lineEdit")
        self.horizontalLayout_2.addWidget(self.warehouse_name_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tableWidget = QtWidgets.QTableWidget(Form)
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
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.quert_str_lineEdit = QtWidgets.QLineEdit(Form)
        self.quert_str_lineEdit.setObjectName("quert_str_lineEdit")
        self.horizontalLayout.addWidget(self.quert_str_lineEdit)
        self.query_Button = QtWidgets.QPushButton(Form)
        self.query_Button.setObjectName("query_Button")
        self.horizontalLayout.addWidget(self.query_Button)
        self.check_all_Button = QtWidgets.QPushButton(Form)
        self.check_all_Button.setObjectName("check_all_Button")
        self.horizontalLayout.addWidget(self.check_all_Button)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "查看库存"))
        self.label_2.setText(_translate("Form", "仓库名称："))
        self.label.setText(_translate("Form", "库存详情："))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "商品编号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "商品名称"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "商品类别"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "计量单位"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "规格"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "供应商"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "库存数量"))
        self.query_Button.setText(_translate("Form", "模糊查询"))
        self.check_all_Button.setText(_translate("Form", "查看所有"))


class CheckStorage(object):
    def __init__(self, storage_keeper):
        self.storage_keeper = storage_keeper

        self.win = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.win)

        self.load_data()
        self.adjust_ui()
        self.bind()

    def adjust_ui(self):
        self.ui.warehouse_name_lineEdit.setEnabled(False)
        self.ui.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.ui.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

    def load_data(self):
        self.ui.warehouse_name_lineEdit.setText(self.storage_keeper.warehouse_name)

        statue, data = self.storage_keeper.get_stock_details()
        if (statue == True):
            self.stock_details = data['stock_details']
            self.ui.tableWidget.setRowCount(len(data['stock_details']))
            for i, item in enumerate(data['stock_details']):
                self.ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(item['commodity_code'])))
                self.ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(item['commodity_name'])))
                self.ui.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(item['commodity_type'])))
                self.ui.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str(item['commodity_unit'])))
                self.ui.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(str(item['commodity_specification'])))
                self.ui.tableWidget.setItem(i, 5, QtWidgets.QTableWidgetItem(str(item['commodity_supplier'])))
                self.ui.tableWidget.setItem(i, 6, QtWidgets.QTableWidgetItem(str(item['number'])))
        else:
            QtWidgets.QMessageBox.information(None, '提示', '载入数据出错！请返回重试', QtWidgets.QMessageBox.Ok)

    def refresh(self):
        self.load_data()

    def bind(self):
        self.ui.query_Button.clicked.connect(lambda :self.quick_choose())
        self.ui.check_all_Button.clicked.connect(lambda :self.check_all())

    def quick_choose(self):
        query_str = self.ui.quert_str_lineEdit.text()
        temp = []
        for stock_detail in self.stock_details:
            if (query_str in stock_detail['warehouse_name']
                or query_str in stock_detail['commodity_code']
                or query_str in stock_detail['commodity_name']
                or query_str in stock_detail['commodity_type']
                or query_str in stock_detail['commodity_unit']
                or query_str in stock_detail['commodity_specification']
                or query_str in stock_detail['commodity_supplier']):
                temp.append(stock_detail)

        self.ui.tableWidget.setRowCount(len(temp))
        for i, item in enumerate(temp):
            self.ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(item['commodity_code'])))
            self.ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(item['commodity_name'])))
            self.ui.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(item['commodity_type'])))
            self.ui.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str(item['commodity_unit'])))
            self.ui.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(str(item['commodity_specification'])))
            self.ui.tableWidget.setItem(i, 5, QtWidgets.QTableWidgetItem(str(item['commodity_supplier'])))
            self.ui.tableWidget.setItem(i, 6, QtWidgets.QTableWidgetItem(str(item['number'])))

    def check_all(self):
        self.ui.tableWidget.setRowCount(len(self.stock_details))
        for i, item in enumerate(self.stock_details):
            self.ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(item['commodity_code'])))
            self.ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(item['commodity_name'])))
            self.ui.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(item['commodity_type'])))
            self.ui.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str(item['commodity_unit'])))
            self.ui.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(str(item['commodity_specification'])))
            self.ui.tableWidget.setItem(i, 5, QtWidgets.QTableWidgetItem(str(item['commodity_supplier'])))
            self.ui.tableWidget.setItem(i, 6, QtWidgets.QTableWidgetItem(str(item['number'])))
