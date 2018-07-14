# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'check_notice_sheet.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from client.ui.storage_keeper_children.check_order_sheet_details import CheckOrderSheetDetail


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(563, 436)
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
        self.tableWidget.setColumnCount(5)
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
        self.label.setText(_translate("Form", "提示：双击可查看采购详单"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "序号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "采购单号"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "仓库名称"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "下单时间"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "状态"))
        self.query_Button.setText(_translate("Form", "查询"))
        self.check_all_Button.setText(_translate("Form", "查看所有"))


class CheckOrderSheet(object):
    def __init__(self, storage_keeper):
        self.storage_keeper = storage_keeper

        self.win = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.win)

        self.load_data()
        self.adjust_ui()
        self.bind()

    def bind(self):
        self.ui.tableWidget.itemDoubleClicked.connect(lambda: self.check_details())
        self.ui.query_Button.clicked.connect(lambda: self.query())
        self.ui.check_all_Button.clicked.connect(lambda: self.check_all())

    def load_data(self):
        statue, data = self.storage_keeper.get_order_sheets(self.storage_keeper.warehouse_name)
        if (statue == True):
            self.sheets = data['sheets']
            self.ui.tableWidget.setRowCount(len(data['sheets']))
            for i, item in enumerate(data['sheets']):
                n = len(data['sheets']) - i - 1
                self.ui.tableWidget.setItem(n, 0, QtWidgets.QTableWidgetItem(str(n + 1)))
                self.ui.tableWidget.setItem(n, 1, QtWidgets.QTableWidgetItem(str(item['order_sheet_id'])))
                self.ui.tableWidget.setItem(n, 2, QtWidgets.QTableWidgetItem(str(item['warehouse_name'])))
                self.ui.tableWidget.setItem(n, 3, QtWidgets.QTableWidgetItem(str(item['date'])))
                self.ui.tableWidget.setItem(n, 4, QtWidgets.QTableWidgetItem(str(item['statue'])))

        else:
            self.sheets = []
            QtWidgets.QMessageBox.information(None, '提示', '载入数据出错！', QtWidgets.QMessageBox.Ok)

    def adjust_ui(self):
        self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.ui.tableWidget.resizeColumnsToContents()

    def check_details(self):
        try:
            order_sheet_id = self.ui.tableWidget.selectedItems()[1].text()
            warehouse_name = self.ui.tableWidget.selectedItems()[2].text()
            statue = self.ui.tableWidget.selectedItems()[4].text()
            if(statue != '已购买'):
                QtWidgets.QMessageBox.information(None, '提示', '只有状态为已购买的采购单才能操作！')
                return False
            dialog = CheckOrderSheetDetail(self.storage_keeper, order_sheet_id, warehouse_name)
            dialog.win.exec_()
            # 刷新界面，重载数据
            self.refresh()
        except Exception as e:
            print(e)
            QtWidgets.QMessageBox.information(None, '提示', '出现错误，窗口打开失败，无法查看详单！', QtWidgets.QMessageBox.Ok)

    def query(self):
        query_str = self.ui.lineEdit.text()
        # 用temp存储满足的列表
        temp = []
        for item in self.sheets:
            if(query_str in item['warehouse_name']):
                temp.append(item)
        # 将temp数据加载到界面
        self.ui.tableWidget.setRowCount(len(temp))
        for i, item in enumerate(temp):
            n = len(temp) - i - 1
            self.ui.tableWidget.setItem(n, 0, QtWidgets.QTableWidgetItem(str(n + 1)))
            self.ui.tableWidget.setItem(n, 1, QtWidgets.QTableWidgetItem(str(item['order_sheet_id'])))
            self.ui.tableWidget.setItem(n, 2, QtWidgets.QTableWidgetItem(str(item['warehouse_name'])))
            self.ui.tableWidget.setItem(n, 3, QtWidgets.QTableWidgetItem(item['date']))

    def check_all(self):
        self.ui.tableWidget.setRowCount(len(self.sheets))
        for i, item in enumerate(self.sheets):
            n = len(self.sheets) - i - 1
            self.ui.tableWidget.setItem(n, 0, QtWidgets.QTableWidgetItem(str(n + 1)))
            self.ui.tableWidget.setItem(n, 1, QtWidgets.QTableWidgetItem(str(item['order_sheet_id'])))
            self.ui.tableWidget.setItem(n, 2, QtWidgets.QTableWidgetItem(str(item['warehouse_name'])))
            self.ui.tableWidget.setItem(n, 3, QtWidgets.QTableWidgetItem(item['date']))


    def refresh(self):
        self.load_data()


if __name__ == '__main__':
    import sys
    from client.model.manager import Manager

    manager = Manager('http://127.0.0.1:5000', 'admin', 'admin', '系统管理员')
    if (manager.login()):
        app = QtWidgets.QApplication(sys.argv)
        page = CheckOrderSheet(manager)
        page.win.show()
        sys.exit(app.exec_())
    else:
        print(False)