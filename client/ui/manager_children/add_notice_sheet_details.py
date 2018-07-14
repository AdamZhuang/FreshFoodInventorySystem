# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_notice_sheet_details.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(733, 538)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.commodity_code_comboBox = QtWidgets.QComboBox(Form)
        self.commodity_code_comboBox.setObjectName("commodity_code_comboBox")
        self.verticalLayout.addWidget(self.commodity_code_comboBox)
        self.number_lineEdit = QtWidgets.QLineEdit(Form)
        self.number_lineEdit.setObjectName("number_lineEdit")
        self.verticalLayout.addWidget(self.number_lineEdit)
        self.price_lineEdit = QtWidgets.QLineEdit(Form)
        self.price_lineEdit.setObjectName("price_lineEdit")
        self.verticalLayout.addWidget(self.price_lineEdit)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cancel_Button = QtWidgets.QPushButton(Form)
        self.cancel_Button.setObjectName("cancel_Button")
        self.horizontalLayout.addWidget(self.cancel_Button)
        self.confirm_Button = QtWidgets.QPushButton(Form)
        self.confirm_Button.setObjectName("confirm_Button")
        self.horizontalLayout.addWidget(self.confirm_Button)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setMinimumSize(QtCore.QSize(300, 0))
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
        self.verticalLayout_3.addWidget(self.tableWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.query_lineEdit = QtWidgets.QLineEdit(Form)
        self.query_lineEdit.setObjectName("query_lineEdit")
        self.horizontalLayout_2.addWidget(self.query_lineEdit)
        self.query_Button = QtWidgets.QPushButton(Form)
        self.query_Button.setObjectName("query_Button")
        self.horizontalLayout_2.addWidget(self.query_Button)
        self.check_all_Button = QtWidgets.QPushButton(Form)
        self.check_all_Button.setObjectName("check_all_Button")
        self.horizontalLayout_2.addWidget(self.check_all_Button)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "添加订货通知详单"))
        self.label.setText(_translate("Form", "选择商品编号："))
        self.label_2.setText(_translate("Form", "数量："))
        self.label_4.setText(_translate("Form", "购买经费（单位：元）："))
        self.cancel_Button.setText(_translate("Form", "取消"))
        self.confirm_Button.setText(_translate("Form", "确认"))
        self.label_3.setText(_translate("Form", "双击快速选择商品："))
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
        self.query_Button.setText(_translate("Form", "查询"))
        self.check_all_Button.setText(_translate("Form", "查看所有"))


class AddNoticeSheetDetails():
    def __init__(self, manager):
        self.manager = manager
        self.ret_data = {}

        self.win = QtWidgets.QDialog()
        self.ui = Ui_Form()
        self.ui.setupUi(self.win)

        self.adjust_ui()
        self.load_data()
        self.bind()

    def adjust_ui(self):
        pass

    def load_data(self):
        statue, data = self.manager.get_all_commodities()
        if (statue == True):
            self.commodities = data['commodities']
            self.ui.commodity_code_comboBox.clear()
            self.ui.tableWidget.setRowCount(len(self.commodities))
            for i, item in enumerate(self.commodities):
                self.ui.commodity_code_comboBox.addItem(str(item['code']))
                self.ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(i + 1)))
                self.ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(item['code'])))
                self.ui.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(item['name'])))
                self.ui.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str(item['type'])))
                self.ui.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(str(item['unit'])))
                self.ui.tableWidget.setItem(i, 5, QtWidgets.QTableWidgetItem(str(item['specification'])))
                self.ui.tableWidget.setItem(i, 6, QtWidgets.QTableWidgetItem(str(item['supplier_name'])))
        else:
            QtWidgets.QMessageBox.information(None, '提示', '载入数据出错！请返回重试', QtWidgets.QMessageBox.Ok)

    def bind(self):
        self.ui.confirm_Button.clicked.connect(lambda: self.confirm())
        self.ui.cancel_Button.clicked.connect(lambda: self.cancel())
        self.ui.tableWidget.clicked.connect(lambda: self.quick_choose())
        self.ui.query_Button.clicked.connect(lambda: self.query())
        self.ui.check_all_Button.clicked.connect(lambda: self.check_all())

    def confirm(self):
        commodity_code = self.ui.commodity_code_comboBox.currentText()
        number = self.ui.number_lineEdit.text()
        price = self.ui.price_lineEdit.text()

        if (commodity_code == '' or number == '' or price == ''):
            QtWidgets.QMessageBox.information(None, '提示', '请填写完整的表单信息！', QtWidgets.QMessageBox.Ok)
            return False

        for commodity in self.commodities:
            if (commodity['code'] == commodity_code):
                self.ret_data = {'code': commodity['code'],
                                 'name': commodity['name'],
                                 'type': commodity['type'],
                                 'unit': commodity['unit'],
                                 'specification': commodity['specification'],
                                 'supplier_name': commodity['supplier_name'],
                                 'number': number,
                                 'price': price,
                                 }

        return self.win.accept()

    def cancel(self):
        return self.win.reject()

    def quick_choose(self):
        selected = self.ui.tableWidget.selectedItems()
        if (selected != None):
            commodity_code = selected[1].text()
            self.ui.commodity_code_comboBox.setCurrentText(commodity_code)

    def query(self):
        query_str = self.ui.query_lineEdit.text()
        temp = []
        for item in self.commodities:
            if (query_str in item['code'] or query_str in item['name'] or query_str in item['type']
                or query_str in item['unit'] or query_str in item['specification'] or query_str in item[
                'supplier_name']):
                temp.append(item)

        self.ui.tableWidget.setRowCount(len(temp))
        for i, item in enumerate(temp):
            self.ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(i + 1)))
            self.ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(item['code'])))
            self.ui.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(item['name'])))
            self.ui.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str(item['type'])))
            self.ui.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(str(item['unit'])))
            self.ui.tableWidget.setItem(i, 5, QtWidgets.QTableWidgetItem(str(item['specification'])))
            self.ui.tableWidget.setItem(i, 6, QtWidgets.QTableWidgetItem(str(item['supplier_name'])))

    def check_all(self):
        self.ui.tableWidget.setRowCount(len(self.commodities))
        for i, item in enumerate(self.commodities):
            self.ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(i + 1)))
            self.ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(item['code'])))
            self.ui.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(item['name'])))
            self.ui.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str(item['type'])))
            self.ui.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(str(item['unit'])))
            self.ui.tableWidget.setItem(i, 5, QtWidgets.QTableWidgetItem(str(item['specification'])))
            self.ui.tableWidget.setItem(i, 6, QtWidgets.QTableWidgetItem(str(item['supplier_name'])))


if __name__ == '__main__':
    import sys
    from client.model.manager import Manager

    manager = Manager('http://127.0.0.1:5000', '王二', '123456', '经理')
    if (manager.login()):
        app = QtWidgets.QApplication(sys.argv)
        page = AddNoticeSheetDetails(manager)
        page.win.show()
        sys.exit(app.exec_())
    else:
        print(False)
