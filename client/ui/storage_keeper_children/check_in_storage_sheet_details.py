# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'check_in_storage_sheet_details.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(900, 563)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.in_storage_sheet_code_lineEdit = QtWidgets.QLineEdit(Form)
        self.in_storage_sheet_code_lineEdit.setObjectName("in_storage_sheet_lineEdit")
        self.horizontalLayout.addWidget(self.in_storage_sheet_code_lineEdit)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.warehouse_lineEdit = QtWidgets.QLineEdit(Form)
        self.warehouse_lineEdit.setObjectName("in_storage_sheet_lineEdit_2")
        self.horizontalLayout.addWidget(self.warehouse_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.in_storage_time_lineEdit = QtWidgets.QLineEdit(Form)
        self.in_storage_time_lineEdit.setObjectName("in_storage_sheet_lineEdit_3")
        self.horizontalLayout_2.addWidget(self.in_storage_time_lineEdit)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.in_storage_man_lineEdit = QtWidgets.QLineEdit(Form)
        self.in_storage_man_lineEdit.setObjectName("in_storage_sheet_lineEdit_4")
        self.horizontalLayout_2.addWidget(self.in_storage_man_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
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
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tableWidget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "查看入库详单"))
        self.label_2.setText(_translate("Form", "入库单编号："))
        self.label_3.setText(_translate("Form", "仓库名称："))
        self.label_4.setText(_translate("Form", "入库时间    ："))
        self.label_5.setText(_translate("Form", "入库人员："))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "序号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "商品编号"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "商品名称"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "商品类别"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "计量单位"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "规格"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "供应商"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Form", "数量"))


class CheckInStorageSheetDetails():
    def __init__(self, storage_keeper, in_storage_sheet_code, warehouse_name, in_storage_date, handler_name):
        self.storage_keeper = storage_keeper
        self.in_storage_sheet_code = in_storage_sheet_code
        self.warehouse_name = warehouse_name
        self.in_storage_date = in_storage_date
        self.handler_name = handler_name

        self.win = QtWidgets.QDialog()
        self.ui = Ui_Form()
        self.ui.setupUi(self.win)

        self.adjust_ui()
        self.load_data()

    def adjust_ui(self):
        self.ui.in_storage_sheet_code_lineEdit.setEnabled(False)
        self.ui.warehouse_lineEdit.setEnabled(False)
        self.ui.in_storage_time_lineEdit.setEnabled(False)
        self.ui.in_storage_man_lineEdit.setEnabled(False)


    def load_data(self):
        self.ui.in_storage_sheet_code_lineEdit.setText(self.in_storage_sheet_code)
        self.ui.warehouse_lineEdit.setText(self.warehouse_name)
        self.ui.in_storage_time_lineEdit.setText(self.in_storage_date)
        self.ui.in_storage_man_lineEdit.setText(self.handler_name)


        # 加载详单
        statue, data = self.storage_keeper.get_in_storage_sheet_details(self.in_storage_sheet_code)
        if (statue == True):
            self.ui.tableWidget.setRowCount(len(data['details']))
            for i, item in enumerate(data['details']):
                self.ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(i + 1)))
                self.ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(item['commodity_code'])))
                self.ui.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(item['commodity_name'])))
                self.ui.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str(item['commodity_type'])))
                self.ui.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(str(item['commodity_unit'])))
                self.ui.tableWidget.setItem(i, 5, QtWidgets.QTableWidgetItem(str(item['commodity_specification'])))
                self.ui.tableWidget.setItem(i, 6, QtWidgets.QTableWidgetItem(str(item['commodity_supplier'])))
                self.ui.tableWidget.setItem(i, 7, QtWidgets.QTableWidgetItem(str(item['number'])))
        else:
            QtWidgets.QMessageBox.information(None, '提示', '载入数据出错！请返回重试', QtWidgets.QMessageBox.Ok)

    def refresh(self):
        self.load_data()
