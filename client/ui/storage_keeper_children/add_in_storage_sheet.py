# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_in_storage_sheet.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
import random
import hashlib


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(810, 563)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setMinimumSize(QtCore.QSize(200, 0))
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        self.query_lineEdit = QtWidgets.QLineEdit(Form)
        self.query_lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.query_lineEdit)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.gen_in_storage_sheet_Button = QtWidgets.QPushButton(Form)
        self.gen_in_storage_sheet_Button.setObjectName("gen_in_storage_sheet_Button")
        self.horizontalLayout_4.addWidget(self.gen_in_storage_sheet_Button)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.in_storage_sheet_code_lineEdit = QtWidgets.QLineEdit(Form)
        self.in_storage_sheet_code_lineEdit.setObjectName("in_storage_sheet_lineEdit")
        self.horizontalLayout_2.addWidget(self.in_storage_sheet_code_lineEdit)
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
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.commit_Button = QtWidgets.QPushButton(Form)
        self.commit_Button.setObjectName("commit_Button")
        self.horizontalLayout_3.addWidget(self.commit_Button)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "选择采购单编号（已购买）"))
        self.pushButton.setText(_translate("Form", "查询"))
        self.gen_in_storage_sheet_Button.setText(_translate("Form", "根据采购单生成入库单"))
        self.label_2.setText(_translate("Form", "入库单编号："))
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
        self.commit_Button.setText(_translate("Form", "提交入库单"))


class AddInStorageSheet():
    def __init__(self, storager_keeper):
        self.storager_keeper = storager_keeper

        self.win = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.win)

        self.bind()
        self.adjust_ui()

    def bind(self):
        self.ui.gen_in_storage_sheet_Button.clicked.connect(lambda: self.gen_in_storage_sheet())
        self.ui.commit_Button.clicked.connect(lambda :self.commit())

    def adjust_ui(self):
        self.ui.in_storage_sheet_code_lineEdit.setEnabled(False)
        # self.ui.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        # self.ui.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        # self.ui.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

    def refresh(self):
        self.load_data()

    def gen_in_storage_sheet(self):
        self.in_storage_sheet_code = self.gen_code()
        self.ui.in_storage_sheet_code_lineEdit.setText(str(self.in_storage_sheet_code))

        self.order_sheet_code = self.ui.comboBox.currentText()
        statue, data = self.storager_keeper.get_order_sheet_details(self.order_sheet_code)
        if (statue == True):
            self.ui.tableWidget.setRowCount(len(data['details']))
            for i, detail in enumerate(data['details']):
                self.ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(i + 1)))
                self.ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(detail['commodity_code'])))
                self.ui.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(detail['commodity_name'])))
                self.ui.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str(detail['commodity_type'])))
                self.ui.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(str(detail['commodity_unit'])))
                self.ui.tableWidget.setItem(i, 5, QtWidgets.QTableWidgetItem(str(detail['commodity_specification'])))
                self.ui.tableWidget.setItem(i, 6, QtWidgets.QTableWidgetItem(str(detail['commodity_supplier'])))
                self.ui.tableWidget.setItem(i, 7, QtWidgets.QTableWidgetItem(str(detail['number'])))

                # print(data)
        else:
            QtWidgets.QMessageBox.information(None, '提示', '载入数据失败！', QtWidgets.QMessageBox.Ok)
            return False

    def gen_code(self):
        # 生成code
        cur_time = datetime.datetime.now()
        t = cur_time.strftime("%Y%m%d%H%M%S")
        username = self.storager_keeper.name
        u = hashlib.md5(username.encode("utf8")).hexdigest()[:10]
        r = str(random.randint(0, 9))
        code = t + u + r
        return code

    def load_data(self):
        statue, data = self.storager_keeper.get_order_sheets_by_warehouse_name()
        if (statue == True):
            self.sheets = data['sheets']

            self.ui.comboBox.clear()
            for sheet in self.sheets:
                if(sheet['statue'] == '已购买'):
                    self.ui.comboBox.addItem(sheet['code'])
                # print(sheet['code'])
                # print(sheet['delivery_date'])
                # print(sheet['statue'])
                # print(sheet['warehouse_name'])
                # print(sheet['handler_name'])
                # print(sheet['order_date'])
            print(data)
        else:
            QtWidgets.QMessageBox.information(None, '提示', '载入数据失败！', QtWidgets.QMessageBox.Ok)
            return False

    def commit(self):
        if (self.ui.in_storage_sheet_code_lineEdit == ''):
            QtWidgets.QMessageBox.information(None, '提示', '请点击生成入库单再提交！', QtWidgets.QMessageBox.Ok)
            return False

        code = self.in_storage_sheet_code
        order_sheet_code = self.order_sheet_code
        warehouse_name = self.storager_keeper.warehouse_name
        in_storage_date = str(datetime.datetime.now())
        handler_name = self.storager_keeper.name
        statue, data = self.storager_keeper.add_in_storage_sheet(code, order_sheet_code, warehouse_name,
                                                                 in_storage_date, handler_name)
        if(statue == True):
            for i in range(self.ui.tableWidget.rowCount()):
                in_storage_sheet_code = self.ui.in_storage_sheet_code_lineEdit.text()
                commodity_code = self.ui.tableWidget.item(i,1).text()
                number = self.ui.tableWidget.item(i,7).text()
                statue, data = self.storager_keeper.add_in_storage_sheet_details(in_storage_sheet_code, commodity_code, number)
            QtWidgets.QMessageBox.information(None, '提示', '提交成功！', QtWidgets.QMessageBox.Ok)
            self.load_data()
            self.ui.in_storage_sheet_code_lineEdit.setText('')
            # self.ui.tableWidget.clear()
            self.ui.tableWidget.setRowCount(0)
        else:
            QtWidgets.QMessageBox.information(None, '提示', '提交总单失败！', QtWidgets.QMessageBox.Ok)
            return False


if __name__ == '__main__':
    import sys
    from client.model.storage_keeper import StorageKeeper

    app = QtWidgets.QApplication(sys.argv)
    storager_keeper = StorageKeeper('王五', '123456', '仓储部')
    if (storager_keeper.login()):
        page = AddInStorageSheet(storager_keeper)
        page.win.showMaximized()

    sys.exit(app.exec_())
