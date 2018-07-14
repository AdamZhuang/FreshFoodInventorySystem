# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_warehouse.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(656, 374)
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
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.warehouse_location_lineEdit = QtWidgets.QLineEdit(Form)
        self.warehouse_location_lineEdit.setObjectName("warehouse_location_lineEdit")
        self.horizontalLayout.addWidget(self.warehouse_location_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setMaximumSize(QtCore.QSize(70, 16777215))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.warehouse_manager_comboBox = QtWidgets.QComboBox(Form)
        self.warehouse_manager_comboBox.setObjectName("warehouse_manager_comboBox")
        self.horizontalLayout_2.addWidget(self.warehouse_manager_comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.add_Button = QtWidgets.QPushButton(Form)
        self.add_Button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.add_Button.setObjectName("add_Button")
        self.horizontalLayout_3.addWidget(self.add_Button)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
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
        self.label.setText(_translate("Form", "仓库名"))
        self.label_3.setText(_translate("Form", "仓库地址"))
        self.label_2.setText(_translate("Form", "仓库管理员"))
        self.label_5.setText(_translate("Form", "当前所有仓库："))
        self.add_Button.setText(_translate("Form", "添加"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "序号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "仓库名称"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "仓库地址"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "仓库管理员"))


class AddWarehouse():
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
        pass

    def bind(self):
        self.ui.add_Button.clicked.connect(lambda: self.add_warehouse())

    def refresh(self):
        self.load_data()
        pass

    def load_data(self):
        try:
            statue1, warehouses = self.admin.get_all_warehouses()
            statue2, users = self.admin.get_all_users()
            if (statue1 == True and statue2 == True):
                data_num = len(warehouses)
                # 加载表格数据
                user_already_arrage = []
                self.ui.tableWidget.setRowCount(data_num)
                for i, warehouse in enumerate(warehouses):
                    self.ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(i + 1)))
                    self.ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(warehouse['name'])))
                    self.ui.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(warehouse['location'])))
                    self.ui.tableWidget.setItem(i, 3,
                                                QtWidgets.QTableWidgetItem(str(warehouse['warehouse_manager_name'])))
                    user_already_arrage.append(warehouse['warehouse_manager_name'])
                # 加载combobox数据
                self.ui.warehouse_manager_comboBox.clear()
                for user in users:
                    if (user['department'] == '仓库管理员' and user['name'] not in user_already_arrage):
                        self.ui.warehouse_manager_comboBox.addItem(user['name'])
        except Exception as e:
            print(e)

    def add_warehouse(self):
        try:
            warehouse_name = self.ui.warehouse_name_lineEdit.text()
            warehouse_location = self.ui.warehouse_location_lineEdit.text()
            warehouse_manager = self.ui.warehouse_manager_comboBox.currentText()
            if (warehouse_name == '' or warehouse_location == '' or warehouse_manager == ''):
                QtWidgets.QMessageBox.information(None, '提示', '请输入大于1个字的内容', QtWidgets.QMessageBox.Yes)
                return False
            statue, data = self.admin.add_warehouse(warehouse_name=warehouse_name,
                                                    warehouse_location=warehouse_location,
                                                    warehouse_manager_name=warehouse_manager)
            if (statue == True):
                self.load_data()
                QtWidgets.QMessageBox.information(None, '提示', '添加成功', QtWidgets.QMessageBox.Yes)
                self.ui.warehouse_name_lineEdit.setText('')
                self.ui.warehouse_location_lineEdit.setText('')
                self.ui.warehouse_manager_comboBox.setCurrentIndex(-1)
            elif (statue == False):
                QtWidgets.QMessageBox.information(None, '提示', '添加失败', QtWidgets.QMessageBox.Yes)
            elif (statue == 'network_error'):
                QtWidgets.QMessageBox.warning(None, '提示', '连接服务器超时！', QtWidgets.QMessageBox.Yes)
        except Exception as e:
            print(e)
