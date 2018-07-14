# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'change_supplier.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(610, 470)
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
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.name_lineEdit = QtWidgets.QLineEdit(Form)
        self.name_lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.name_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.contact_lineEdit = QtWidgets.QLineEdit(Form)
        self.contact_lineEdit.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.contact_lineEdit)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
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
        self.label.setText(_translate("Form", "当前供应商名称"))
        self.label_2.setText(_translate("Form", "修改后供应商名称"))
        self.label_3.setText(_translate("Form", "修改后联系电话"))
        self.pushButton.setText(_translate("Form", "修改"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "序号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "供应商名称"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "联系电话"))


class ChangeSupplier():
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
        self.ui.pushButton.clicked.connect(lambda: self.change_user())
        self.ui.tableWidget.itemDoubleClicked.connect(lambda: self.quick_choose())

    def refresh(self):
        self.load_data()

    def load_data(self):
        try:
            statue, suppliers = self.admin.get_all_suppliers()
            if (statue == True):
                data_num = len(suppliers)
                self.ui.tableWidget.setRowCount(data_num)
                self.ui.comboBox.clear()
                for i, supplier in enumerate(suppliers):
                    self.ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(i + 1)))
                    self.ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(supplier['name'])))
                    self.ui.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(supplier['contact'])))
                    self.ui.comboBox.addItem(str(supplier['name']))
                self.ui.comboBox.setCurrentIndex(-1)
        except Exception as e:
            print(e)

    def change_user(self):
        try:
            # 用户是否管理员确认
            origin_supplier_name = self.ui.comboBox.currentText()
            dest_supplier_name = self.ui.name_lineEdit.text()
            dest_supplier_contact = self.ui.contact_lineEdit.text()

            # 字符串是否为空验证
            if (len(dest_supplier_name) < 1 or len(dest_supplier_contact) < 1):
                QtWidgets.QMessageBox.information(None, '提示', '请输入大于长度1的字符串', QtWidgets.QMessageBox.Ok)
                return False

            # 获取返回状态
            statue, data = self.admin.change_supplier(origin_supplier_name=origin_supplier_name,
                                                      dest_supplier_name=dest_supplier_name,
                                                      dest_supplier_contact=dest_supplier_contact)
            if (statue == True):
                self.load_data()
                QtWidgets.QMessageBox.information(None, '提示', '修改成功', QtWidgets.QMessageBox.Yes)
            elif (statue == False):
                QtWidgets.QMessageBox.information(None, '提示', '修改失败', QtWidgets.QMessageBox.Yes)
                print(data)
            elif (statue == 'network_error'):
                QtWidgets.QMessageBox.warning(None, '提示', '连接服务器超时！', QtWidgets.QMessageBox.Yes)

            # 重置输入，方便下一次进行修改
            self.ui.comboBox.setCurrentIndex(-1)
            self.ui.name_lineEdit.setText('')
            self.ui.contact_lineEdit.setText('')

        except Exception as e:
            print(e)

    def quick_choose(self):
        selected = self.ui.tableWidget.selectedItems()
        self.ui.comboBox.setCurrentText(selected[1].text())
        self.ui.name_lineEdit.setText(selected[1].text())
        self.ui.contact_lineEdit.setText(selected[2].text())
