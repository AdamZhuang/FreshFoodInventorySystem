# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'check_notice_sheet_details.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(832, 513)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
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
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.change_Button = QtWidgets.QPushButton(Form)
        self.change_Button.setObjectName("change_Button")
        self.horizontalLayout_2.addWidget(self.change_Button)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "采购详单"))
        self.label.setText(_translate("Form", "采购单号："))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "序号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "采购详单号"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "仓库名称"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "商品名称"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "数量"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "批准经费"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "实际支出"))
        self.change_Button.setText(_translate("Form", "修改此订单状态为已完成"))


class CheckOrderSheetDetail():
    def __init__(self, storage_keeper, order_sheet_id, warehouse_name):
        self.storage_keeper = storage_keeper
        self.order_sheet_id = order_sheet_id
        self.warehouse_name = warehouse_name

        self.win = QtWidgets.QDialog()
        self.ui = Ui_Form()
        self.ui.setupUi(self.win)

        self.bind()
        self.load_data()
        self.adjust_ui()

    def bind(self):
        self.ui.change_Button.clicked.connect(lambda: self.change_statue())

    def load_data(self):
        self.ui.lineEdit.setText(self.order_sheet_id)

        statue, data = self.storage_keeper.get_order_sheet_details(order_sheet_id=self.order_sheet_id)
        if (statue == True):
            self.ui.tableWidget.setRowCount(len(data['details']))
            for i, item in enumerate(data['details']):
                n = len(data['details']) - i -1
                self.ui.tableWidget.setItem(n, 0, QtWidgets.QTableWidgetItem(str(n + 1)))
                self.ui.tableWidget.setItem(n, 1, QtWidgets.QTableWidgetItem(str(item['id'])))
                self.ui.tableWidget.setItem(n, 2, QtWidgets.QTableWidgetItem(str(self.warehouse_name)))
                self.ui.tableWidget.setItem(n, 3, QtWidgets.QTableWidgetItem(str(item['commodity_name'])))
                self.ui.tableWidget.setItem(n, 4, QtWidgets.QTableWidgetItem(str(item['number'])))
                self.ui.tableWidget.setItem(n, 5, QtWidgets.QTableWidgetItem(str(item['allow_price'])))
                self.ui.tableWidget.setItem(n, 6, QtWidgets.QTableWidgetItem(str(item['actual_price'])))
        else:
            QtWidgets.QMessageBox.information(None, '提示', '载入数据失败！', QtWidgets.QMessageBox.Ok)

    def adjust_ui(self):
        self.ui.lineEdit.setEnabled(False)

    def refresh(self):
        self.load_data()

    def change_statue(self):
        order_sheet_id = self.ui.lineEdit.text()
        statue, data = self.storage_keeper.change_order_sheet_statue(order_sheet_id, '已入库')
        if(statue == True):
            QtWidgets.QMessageBox.information(None, '提示', '已经修改订单状态为已完成！', QtWidgets.QMessageBox.Ok)
            return self.win.accept()
        else:
            QtWidgets.QMessageBox.information(None, '提示', '修改出现错误！！', QtWidgets.QMessageBox.Ok)
            return self.win.reject()
