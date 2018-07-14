# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'delete_commodity.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_delete_commodity(object):
    def setupUi(self, delete_commodity):
        delete_commodity.setObjectName("add_commodity")
        delete_commodity.resize(717, 510)
        self.verticalLayout = QtWidgets.QVBoxLayout(delete_commodity)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(delete_commodity)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.delete_Button = QtWidgets.QPushButton(delete_commodity)
        self.delete_Button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.delete_Button.setObjectName("delete_Button")
        self.horizontalLayout.addWidget(self.delete_Button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableWidget = QtWidgets.QTableWidget(delete_commodity)
        self.tableWidget.setEditTriggers(
            QtWidgets.QAbstractItemView.DoubleClicked | QtWidgets.QAbstractItemView.SelectedClicked)
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

        self.retranslateUi(delete_commodity)
        QtCore.QMetaObject.connectSlotsByName(delete_commodity)

    def retranslateUi(self, delete_commodity):
        _translate = QtCore.QCoreApplication.translate
        delete_commodity.setWindowTitle(_translate("delete_commodity", "Form"))
        self.label.setText(_translate("delete_commodity", "选中下方一行再点击删除按钮进行删除："))
        self.delete_Button.setText(_translate("delete_commodity", "删除"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("delete_commodity", "序号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("delete_commodity", "商品编号"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("delete_commodity", "商品名称"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("delete_commodity", "商品类型"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("delete_commodity", "计量单位"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("delete_commodity", "规格"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("delete_commodity", "供应商"))


class DeleteCommodity():
    def __init__(self, admin):
        self.admin = admin
        self.win = QtWidgets.QWidget()
        self.ui = Ui_delete_commodity()
        self.ui.setupUi(self.win)
        self.customize()

    def customize(self):
        self.adjust_ui()
        self.load_data()
        self.bind()

    def adjust_ui(self):
        # 调整表格
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.ui.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.ui.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.ui.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

    def bind(self):
        self.ui.delete_Button.clicked.connect(lambda: self.delete_commodity())
        self.ui.tableWidget.itemDoubleClicked.connect(lambda: self.quick_choose())

    def refresh(self):
        self.load_data()

    def load_data(self):
        try:
            statue, commodities = self.admin.get_all_commodities()
            data_num = len(commodities)
            self.ui.tableWidget.setRowCount(data_num)
            for i, commodity in enumerate(commodities):
                self.ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(i + 1)))
                self.ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(commodity['code'])))
                self.ui.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(commodity['name'])))
                self.ui.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str(commodity['type'])))
                self.ui.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(str(commodity['unit'])))
                self.ui.tableWidget.setItem(i, 5, QtWidgets.QTableWidgetItem(str(commodity['specification'])))
                self.ui.tableWidget.setItem(i, 6, QtWidgets.QTableWidgetItem(str(commodity['supplier_name'])))
        except Exception as e:
            print(e)

    def delete_commodity(self):
        try:
            delete_commodity_code = self.ui.tableWidget.selectedItems()[1].text()
            statue, data = self.admin.delete_commodity(delete_commodity_code=delete_commodity_code)
            if (statue == True):
                self.load_data()
                QtWidgets.QMessageBox.information(None, '提示', '删除成功', QtWidgets.QMessageBox.Yes)
            elif (statue == False):
                QtWidgets.QMessageBox.information(None, '提示', '删除失败', QtWidgets.QMessageBox.Yes)
                print(data)
            elif (statue == 'network_error'):
                QtWidgets.QMessageBox.warning(None, '提示', '连接服务器超时！', QtWidgets.QMessageBox.Yes)
        except Exception as e:
            print(e)
