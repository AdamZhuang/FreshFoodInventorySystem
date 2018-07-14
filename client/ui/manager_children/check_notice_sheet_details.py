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
        Form.resize(921, 546)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.notice_sheet_code_lineEdit = QtWidgets.QLineEdit(Form)
        self.notice_sheet_code_lineEdit.setEnabled(False)
        self.notice_sheet_code_lineEdit.setObjectName("notice_sheet_code_lineEdit")
        self.horizontalLayout.addWidget(self.notice_sheet_code_lineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.order_man_lineEdit = QtWidgets.QLineEdit(Form)
        self.order_man_lineEdit.setEnabled(False)
        self.order_man_lineEdit.setObjectName("order_man_lineEdit")
        self.horizontalLayout_5.addWidget(self.order_man_lineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        self.notice_date_lineEdit = QtWidgets.QLineEdit(Form)
        self.notice_date_lineEdit.setEnabled(False)
        self.notice_date_lineEdit.setObjectName("notice_date_lineEdit")
        self.horizontalLayout_7.addWidget(self.notice_date_lineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.handler_lineEdit = QtWidgets.QLineEdit(Form)
        self.handler_lineEdit.setEnabled(False)
        self.handler_lineEdit.setObjectName("handler_lineEdit")
        self.horizontalLayout_2.addWidget(self.handler_lineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_6.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.warehouse_lineEdit = QtWidgets.QLineEdit(Form)
        self.warehouse_lineEdit.setEnabled(False)
        self.warehouse_lineEdit.setObjectName("warehouse_lineEdit")
        self.horizontalLayout_3.addWidget(self.warehouse_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.delivery_date_lineEdit = QtWidgets.QLineEdit(Form)
        self.delivery_date_lineEdit.setEnabled(False)
        self.delivery_date_lineEdit.setObjectName("delivery_date_lineEdit")
        self.horizontalLayout_4.addWidget(self.delivery_date_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_8.addWidget(self.label_7)
        self.statue_lineEdit = QtWidgets.QLineEdit(Form)
        self.statue_lineEdit.setEnabled(False)
        self.statue_lineEdit.setObjectName("statue_lineEdit")
        self.horizontalLayout_8.addWidget(self.statue_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_6.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(9)
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.verticalLayout_3.addWidget(self.tableWidget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "订货通知详单查看"))
        self.label.setText(_translate("Form", "订货通知单单号："))
        self.label_5.setText(_translate("Form", "采购员："))
        self.label_6.setText(_translate("Form", "订货通知日期："))
        self.label_3.setText(_translate("Form", "经手人："))
        self.label_2.setText(_translate("Form", "仓库："))
        self.label_4.setText(_translate("Form", "到货日期："))
        self.label_7.setText(_translate("Form", "订货通知单状态："))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "序号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "商品编号"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "商品类型"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "商品名称"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "计量单位"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "规格"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "供应商名称"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Form", "数量"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("Form", "购买经费（单位：元）"))


class CheckOrderSheetDetail():
    def __init__(self, manager, notice_sheet_code, warehouse_name, order_man_name, delivery_date, notice_date, statue,
                 handler_name):
        self.manager = manager
        self.notice_sheet_code = notice_sheet_code
        self.warehouse_name = warehouse_name
        self.order_man_name = order_man_name
        self.delivery_date = delivery_date
        self.notice_date = notice_date
        self.statue = statue
        self.handler_name = handler_name

        self.win = QtWidgets.QDialog()
        self.ui = Ui_Form()
        self.ui.setupUi(self.win)

        self.load_data()
        self.adjust_ui()

    def load_data(self):
        self.ui.notice_sheet_code_lineEdit.setText(self.notice_sheet_code)
        self.ui.warehouse_lineEdit.setText(self.warehouse_name)
        self.ui.order_man_lineEdit.setText(self.order_man_name)
        self.ui.delivery_date_lineEdit.setText(self.delivery_date)
        self.ui.notice_date_lineEdit.setText(self.notice_date)
        self.ui.statue_lineEdit.setText(self.statue)
        self.ui.handler_lineEdit.setText(self.handler_name)

        statue, data = self.manager.get_notice_sheet_details(notice_sheet_code=self.notice_sheet_code)
        if (statue == True):
            self.ui.tableWidget.setRowCount(len(data['details']))
            for i, item in enumerate(data['details']):
                n = len(data['details']) - i - 1
                self.ui.tableWidget.setItem(n, 0, QtWidgets.QTableWidgetItem(str(n + 1)))
                self.ui.tableWidget.setItem(n, 1, QtWidgets.QTableWidgetItem(str(item['commodity_code'])))
                self.ui.tableWidget.setItem(n, 2, QtWidgets.QTableWidgetItem(str(item['commodity_name'])))
                self.ui.tableWidget.setItem(n, 3, QtWidgets.QTableWidgetItem(str(item['commodity_type'])))
                self.ui.tableWidget.setItem(n, 4, QtWidgets.QTableWidgetItem(str(item['commodity_unit'])))
                self.ui.tableWidget.setItem(n, 5, QtWidgets.QTableWidgetItem(str(item['commodity_specification'])))
                self.ui.tableWidget.setItem(n, 6, QtWidgets.QTableWidgetItem(str(item['commodity_supplier'])))
                self.ui.tableWidget.setItem(n, 7, QtWidgets.QTableWidgetItem(str(item['number'])))
                self.ui.tableWidget.setItem(n, 8, QtWidgets.QTableWidgetItem(str(item['price'])))
        else:
            QtWidgets.QMessageBox.information(None, '提示', '载入数据失败！', QtWidgets.QMessageBox.Ok)

    def adjust_ui(self):
        self.ui.warehouse_lineEdit.setEnabled(False)
        self.ui.warehouse_lineEdit.setEnabled(False)
        self.ui.warehouse_lineEdit.setEnabled(False)
        self.ui.tableWidget.resizeColumnsToContents()

    def refresh(self):
        self.load_data()
