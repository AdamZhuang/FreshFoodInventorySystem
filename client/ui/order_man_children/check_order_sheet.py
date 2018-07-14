# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'check_notice_sheet.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from client.ui.order_man_children.check_order_sheet_details import CheckOrderSheetDetails


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(853, 563)
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
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
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
        Form.setWindowTitle(_translate("Form", "采购单查看"))
        self.label.setText(_translate("Form", "提示：双击可查看采购单详单"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "采购单单号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "仓库名称"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "采购员"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "到货时间"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "下单时间"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "订单状态"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "经手人"))
        self.query_Button.setText(_translate("Form", "查询"))
        self.check_all_Button.setText(_translate("Form", "查看所有"))


class CheckOrderSheet(object):
    def __init__(self, order_man):
        self.order_man = order_man

        self.win = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.win)

        self.load_data()
        self.adjust_ui()
        self.bind()

    def load_data(self):
        statue, data = self.order_man.get_order_sheets(self.order_man.name)
        if (statue == True):
            self.sheets = data['sheets']
            self.ui.tableWidget.setRowCount(len(data['sheets']))
            for i, item in enumerate(data['sheets']):
                n = len(data['sheets']) - i - 1
                self.ui.tableWidget.setItem(n, 0, QtWidgets.QTableWidgetItem(str(item['code'])))
                self.ui.tableWidget.setItem(n, 1, QtWidgets.QTableWidgetItem(str(item['warehouse_name'])))
                self.ui.tableWidget.setItem(n, 2, QtWidgets.QTableWidgetItem(str(item['order_man_name'])))
                self.ui.tableWidget.setItem(n, 3, QtWidgets.QTableWidgetItem(str(item['delivery_date'])))
                self.ui.tableWidget.setItem(n, 4, QtWidgets.QTableWidgetItem(str(item['order_date'])))
                self.ui.tableWidget.setItem(n, 5, QtWidgets.QTableWidgetItem(str(item['statue'])))
                self.ui.tableWidget.setItem(n, 6, QtWidgets.QTableWidgetItem(str(item['handler_name'])))

    def adjust_ui(self):
        self.ui.tableWidget.resizeColumnsToContents()

    def bind(self):
        self.ui.tableWidget.itemDoubleClicked.connect(lambda: self.open_change_dialog())
        self.ui.query_Button.clicked.connect(lambda :self.query())
        self.ui.check_all_Button.clicked.connect(lambda :self.check_all())

    def open_change_dialog(self):
        try:
            selected = self.ui.tableWidget.selectedItems()
            order_sheet_code = selected[0].text()
            warehouse_name = selected[1].text()
            order_man_name = selected[2].text()
            delivery_date = selected[3].text()
            order_date = selected[4].text()
            statue = selected[5].text()
            handler_name = selected[6].text()
            dialog = CheckOrderSheetDetails(self.order_man, order_sheet_code, warehouse_name, order_man_name,
                                            delivery_date, order_date, statue,
                                            handler_name)
            dialog.win.exec_()
            dialog.win.destroy()
            self.load_data()
        except Exception as e:
            print(e)
            QtWidgets.QMessageBox.information(None, '提示', '打开窗口错误！', QtWidgets.QMessageBox.Ok)

    def refresh(self):
        self.load_data()

    def query(self):
        query_str = self.ui.lineEdit.text()
        temp = []
        for sheet in self.sheets:
            if(query_str in sheet['code']
               or query_str in sheet['warehouse_name']
               or query_str in sheet['order_man_name']
               or query_str in sheet['delivery_date']
               or query_str in sheet['order_date']
               or query_str in sheet['statue']
               or query_str in sheet['handler_name']):
                temp.append(sheet)

        self.ui.tableWidget.setRowCount(len(temp))
        for i, item in enumerate(temp):
            n = len(temp) - i - 1
            self.ui.tableWidget.setItem(n, 0, QtWidgets.QTableWidgetItem(str(item['code'])))
            self.ui.tableWidget.setItem(n, 1, QtWidgets.QTableWidgetItem(str(item['warehouse_name'])))
            self.ui.tableWidget.setItem(n, 2, QtWidgets.QTableWidgetItem(str(item['order_man_name'])))
            self.ui.tableWidget.setItem(n, 3, QtWidgets.QTableWidgetItem(str(item['delivery_date'])))
            self.ui.tableWidget.setItem(n, 4, QtWidgets.QTableWidgetItem(str(item['order_date'])))
            self.ui.tableWidget.setItem(n, 5, QtWidgets.QTableWidgetItem(str(item['statue'])))
            self.ui.tableWidget.setItem(n, 6, QtWidgets.QTableWidgetItem(str(item['handler_name'])))

    def check_all(self):
        self.ui.tableWidget.setRowCount(len(self.sheets))
        for i, item in enumerate(self.sheets):
            n = len(self.sheets) - i - 1
            self.ui.tableWidget.setItem(n, 0, QtWidgets.QTableWidgetItem(str(item['code'])))
            self.ui.tableWidget.setItem(n, 1, QtWidgets.QTableWidgetItem(str(item['warehouse_name'])))
            self.ui.tableWidget.setItem(n, 2, QtWidgets.QTableWidgetItem(str(item['order_man_name'])))
            self.ui.tableWidget.setItem(n, 3, QtWidgets.QTableWidgetItem(str(item['delivery_date'])))
            self.ui.tableWidget.setItem(n, 4, QtWidgets.QTableWidgetItem(str(item['order_date'])))
            self.ui.tableWidget.setItem(n, 5, QtWidgets.QTableWidgetItem(str(item['statue'])))
            self.ui.tableWidget.setItem(n, 6, QtWidgets.QTableWidgetItem(str(item['handler_name'])))


if __name__ == '__main__':
    import sys
    from client.model.order_man import OrderMan

    app = QtWidgets.QApplication(sys.argv)
    order_man = OrderMan('http://127.0.0.1:5000', '程彬', '1', '采购部')
    if (order_man.login()):
        page = CheckOrderSheet(order_man)
        page.win.show()

    sys.exit(app.exec_())
