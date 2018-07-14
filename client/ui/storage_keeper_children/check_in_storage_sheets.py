# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'check_in_storage_sheets.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from client.ui.storage_keeper_children.check_in_storage_sheet_details import CheckInStorageSheetDetails


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(701, 519)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tableWidget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "入库单查看"))
        self.label.setText(_translate("Form", "双击可查看详单："))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "入库单编号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "仓库"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "入库时间"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "入库人员"))


class CheckInStorageSheets():
    def __init__(self, storager_keeper):
        self.storager_keeper = storager_keeper

        self.win = QtWidgets.QDialog()
        self.ui = Ui_Form()
        self.ui.setupUi(self.win)

        self.adjust_ui()
        self.load_data()
        self.bind()

    def adjust_ui(self):
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)

    def load_data(self):
        statue, data = self.storager_keeper.get_in_storage_sheets_by_warehouse_name()
        if (statue == True):
            length = len(data['sheets'])
            self.ui.tableWidget.setRowCount(length)
            for i, item in enumerate(data['sheets']):
                n = length - i - 1
                self.ui.tableWidget.setItem(n, 0, QtWidgets.QTableWidgetItem(item['code']))
                self.ui.tableWidget.setItem(n, 1, QtWidgets.QTableWidgetItem(item['warehouse_name']))
                self.ui.tableWidget.setItem(n, 2, QtWidgets.QTableWidgetItem(item['in_storage_date']))
                self.ui.tableWidget.setItem(n, 3, QtWidgets.QTableWidgetItem(item['handler_name']))
        else:
            QtWidgets.QMessageBox.information(None, '提示', '载入数据出错！请返回重试', QtWidgets.QMessageBox.Ok)

    def bind(self):
        self.ui.tableWidget.itemDoubleClicked.connect(lambda: self.check_details())

    def check_details(self):
        in_storage_sheet_code = self.ui.tableWidget.selectedItems()[0].text()
        warehouse_name = self.ui.tableWidget.selectedItems()[1].text()
        in_storage_date = self.ui.tableWidget.selectedItems()[2].text()
        handler_name = self.ui.tableWidget.selectedItems()[3].text()
        dialog = CheckInStorageSheetDetails(self.storager_keeper, in_storage_sheet_code, warehouse_name, in_storage_date, handler_name)
        dialog.win.exec_()

    def refresh(self):
        self.load_data()
