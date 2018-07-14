# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_in_storage_sheet_details.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(843, 525)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.cancel_Button = QtWidgets.QPushButton(Form)
        self.cancel_Button.setObjectName("cancel_Button")
        self.horizontalLayout_4.addWidget(self.cancel_Button)
        self.confirm_Button = QtWidgets.QPushButton(Form)
        self.confirm_Button.setObjectName("confirm_Button")
        self.horizontalLayout_4.addWidget(self.confirm_Button)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
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
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.query_lineEdit = QtWidgets.QLineEdit(Form)
        self.query_lineEdit.setObjectName("query_lineEdit")
        self.horizontalLayout_3.addWidget(self.query_lineEdit)
        self.query_Button = QtWidgets.QPushButton(Form)
        self.query_Button.setObjectName("query_Button")
        self.horizontalLayout_3.addWidget(self.query_Button)
        self.check_all_Button = QtWidgets.QPushButton(Form)
        self.check_all_Button.setObjectName("check_all_Button")
        self.horizontalLayout_3.addWidget(self.check_all_Button)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "选择商品编号："))
        self.label_2.setText(_translate("Form", "输入出库数量："))
        self.cancel_Button.setText(_translate("Form", "取消"))
        self.confirm_Button.setText(_translate("Form", "确定"))
        self.label_3.setText(_translate("Form", "双击快速选择商品："))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "商品编号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "商品名称"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "商品类型"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "计量单位"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "规格"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "供应商"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "库存数量"))
        self.query_Button.setText(_translate("Form", "查询"))
        self.check_all_Button.setText(_translate("Form", "查看所有"))


class AddExStorageSheetDetails():
    def __init__(self, storage_keeper):
        self.storager_keeper = storage_keeper
        self.ret_data = {}

        self.win = QtWidgets.QDialog()
        self.ui = Ui_Form()
        self.ui.setupUi(self.win)

        self.bind()
        self.adjust_ui()
        self.load_data()

    def bind(self):
        self.ui.confirm_Button.clicked.connect(lambda: self.confirm())
        self.ui.cancel_Button.clicked.connect(lambda: self.cancel())
        self.ui.tableWidget.clicked.connect(lambda: self.quick_choose())
        self.ui.query_Button.clicked.connect(lambda: self.query())
        self.ui.check_all_Button.clicked.connect(lambda: self.check_all())

    def confirm(self):
        commodity_code = self.ui.comboBox.currentText()
        number = self.ui.lineEdit.text()
        if (commodity_code == '' or number == ''):
            QtWidgets.QMessageBox.information(None, '提示', '请填写完整的表单信息！', QtWidgets.QMessageBox.Ok)
            return False

        for item in self.stock_details:
            if (item['commodity_code'] == commodity_code):
                if (int(item['number']) < int(number)):
                    QtWidgets.QMessageBox.information(None, '提示', '库存不足，请修改出库数量！！', QtWidgets.QMessageBox.Ok)
                    return False

        for i, item in enumerate(self.stock_details):
            if (item['commodity_code'] == commodity_code):
                self.ret_data = {'commodity_code': self.ui.tableWidget.item(i, 0).text(),
                                 'commodity_name': self.ui.tableWidget.item(i, 1).text(),
                                 'commodity_type': self.ui.tableWidget.item(i, 2).text(),
                                 'commodity_unit': self.ui.tableWidget.item(i, 3).text(),
                                 'commodity_specification': self.ui.tableWidget.item(i, 4).text(),
                                 'commodity_supplier': self.ui.tableWidget.item(i, 5).text(),
                                 'number': self.ui.lineEdit.text(),
                                 }

            return self.win.accept()

    def cancel(self):
        return self.win.reject()

    def adjust_ui(self):
        pass

    def load_data(self):
        statue, data = self.storager_keeper.get_stock_details()
        if (statue == True):
            self.stock_details = data['stock_details']
            self.ui.comboBox.clear()
            self.ui.tableWidget.setRowCount(len(data['stock_details']))
            for i, item in enumerate(data['stock_details']):
                self.ui.comboBox.addItem(item['commodity_code'])
                self.ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(item['commodity_code'])))
                self.ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(item['commodity_name'])))
                self.ui.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(item['commodity_type'])))
                self.ui.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str(item['commodity_unit'])))
                self.ui.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(str(item['commodity_specification'])))
                self.ui.tableWidget.setItem(i, 5, QtWidgets.QTableWidgetItem(str(item['commodity_supplier'])))
                self.ui.tableWidget.setItem(i, 6, QtWidgets.QTableWidgetItem(str(item['number'])))
        else:
            QtWidgets.QMessageBox.information(None, '提示', '载入数据出错！请返回重试', QtWidgets.QMessageBox.Ok)

    def quick_choose(self):
        selected = self.ui.tableWidget.selectedItems()
        if (selected != None):
            commodity_name = selected[1].text()
            self.ui.comboBox.setCurrentText(commodity_name)

    def query(self):
        query_str = self.ui.query_lineEdit.text()
        temp = []
        for item in self.stock_details:
            if (query_str in item['commodity_name']):
                temp.append(item)

        self.ui.tableWidget.setRowCount(len(temp))
        for i, item in enumerate(temp):
            self.ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(i + 1)))
            self.ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(item['commodity_name'])))
            self.ui.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(item['number'])))

    def check_all(self):
        self.ui.tableWidget.setRowCount(len(self.stock_details))
        for i, item in enumerate(self.stock_details):
            self.ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(i + 1)))
            self.ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(item['commodity_name'])))
            self.ui.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(item['number'])))


if __name__ == '__main__':
    import sys
    from client.model.storage_keeper import StorageKeeper

    app = QtWidgets.QApplication(sys.argv)
    storager_keeper = StorageKeeper('http://127.0.0.1:5000', '3', '3', '仓库管理员')
    if (storager_keeper.login()):
        page = AddExStorageSheetDetails(storager_keeper)
        page.win.show()

    sys.exit(app.exec_())
