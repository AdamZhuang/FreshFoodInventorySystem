# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'delete_warehouse.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(656, 420)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.warehouse_name_lineEdit = QtWidgets.QLineEdit(Form)
        self.warehouse_name_lineEdit.setObjectName("warehouse_name_lineEdit")
        self.horizontalLayout.addWidget(self.warehouse_name_lineEdit)
        self.delete_Button = QtWidgets.QPushButton(Form)
        self.delete_Button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.delete_Button.setObjectName("delete_Button")
        self.horizontalLayout.addWidget(self.delete_Button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.tableWidget = QtWidgets.QTableWidget(Form)
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
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "删除仓库名称"))
        self.delete_Button.setText(_translate("Form", "删除"))
        self.label_5.setText(_translate("Form", "当前所有仓库："))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "序号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "仓库名称"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "仓库地址"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "仓库管理员"))


class DeleteWarehouse():
    def __init__(self, admin):
        self.admin = admin
        self.win = QtWidgets.QWidget()
        self.ui = Ui_Form()
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
        self.ui.delete_Button.clicked.connect(lambda: self.delete_warehouse())
        self.ui.tableWidget.itemDoubleClicked.connect(lambda: self.quick_choose())

    def refresh(self):
        self.load_data()

    def load_data(self):
        try:
            statue, warehouses = self.admin.get_all_warehouses()
            if (statue == True):
                data_num = len(warehouses)
                # 加载表格数据
                self.ui.tableWidget.setRowCount(data_num)
                for i, warehouse in enumerate(warehouses):
                    self.ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(i + 1)))
                    self.ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(warehouse['name'])))
                    self.ui.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(warehouse['location'])))
                    self.ui.tableWidget.setItem(i, 3,
                                                QtWidgets.QTableWidgetItem(str(warehouse['warehouse_manager_name'])))
            else:
                print('error')
        except Exception as e:
            print(e)

    def delete_warehouse(self):
        try:
            warehouse = self.ui.warehouse_name_lineEdit.text()
            statue, data = self.admin.delete_warehouse(delete_warehouse_name=warehouse)
            if (statue == True):
                self.load_data()
                QtWidgets.QMessageBox.information(None, '提示', '删除成功', QtWidgets.QMessageBox.Yes)
                self.ui.warehouse_name_lineEdit.setText('')
            elif (statue == False):
                QtWidgets.QMessageBox.information(None, '提示', '删除失败', QtWidgets.QMessageBox.Yes)
            elif (statue == 'network_error'):
                QtWidgets.QMessageBox.warning(None, '提示', '连接服务器超时！', QtWidgets.QMessageBox.Yes)

        except Exception as e:
            print(e)

    def quick_choose(self):
        selected = self.ui.tableWidget.selectedItems()[1].text()
        self.ui.warehouse_name_lineEdit.setText(selected)
