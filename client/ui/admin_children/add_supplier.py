# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_supplier.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(610, 361)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.name_lineEdit = QtWidgets.QLineEdit(Form)
        self.name_lineEdit.setObjectName("name_lineEdit")
        self.horizontalLayout.addWidget(self.name_lineEdit)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.contact_lineEdit = QtWidgets.QLineEdit(Form)
        self.contact_lineEdit.setObjectName("contact_lineEdit")
        self.horizontalLayout.addWidget(self.contact_lineEdit)
        self.add_Button = QtWidgets.QPushButton(Form)
        self.add_Button.setObjectName("add_Button")
        self.horizontalLayout.addWidget(self.add_Button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tableWidget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "供应商名称"))
        self.label_2.setText(_translate("Form", "联系方式"))
        self.add_Button.setText(_translate("Form", "添加供应商"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "序号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "供应商名称"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "联系电话"))


class AddSupplier():
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
        self.ui.tableWidget.setEditTriggers(QtWidgets.QTableWidget.DoubleClicked)

    def bind(self):
        self.ui.add_Button.clicked.connect(lambda: self.add_supplier())

    def load_data(self):
        try:
            statue, suppliers = self.admin.get_all_suppliers()
            if (statue == True):
                data_num = len(suppliers)
                self.ui.tableWidget.setRowCount(data_num)
                for i, user in enumerate(suppliers):
                    self.ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(i + 1)))
                    self.ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(user['name'])))
                    self.ui.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(user['contact'])))
            else:
                print('something wrong')
        except Exception as e:
            print(e)

    def refresh(self):
        self.load_data()

    def add_supplier(self):
        try:
            supplier_name = self.ui.name_lineEdit.text()
            supplier_contact = self.ui.contact_lineEdit.text()
            if (supplier_name == '' or supplier_contact == ''):
                QtWidgets.QMessageBox.information(None, '提示', '请输入大于1个字的内容', QtWidgets.QMessageBox.Yes)
                return False
            statue, data = self.admin.add_supplier(supplier_name=supplier_name, supplier_contact=supplier_contact)
            if (statue == True):
                self.load_data()
                QtWidgets.QMessageBox.information(None, '提示', '添加成功', QtWidgets.QMessageBox.Yes)
                self.ui.name_lineEdit.setText('')
                self.ui.contact_lineEdit.setText('')
            elif (statue == False):
                QtWidgets.QMessageBox.information(None, '提示', '添加失败', QtWidgets.QMessageBox.Yes)
            elif (statue == 'network_error'):
                QtWidgets.QMessageBox.warning(None, '提示', '连接服务器超时！', QtWidgets.QMessageBox.Yes)
        except Exception as e:
            print(e)
