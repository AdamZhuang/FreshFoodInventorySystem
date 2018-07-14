# -*- coding: utf-8 -*-

# Form implementation generated from reading client file 'signin.client'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtWidgets
from client.model.admin import Admin
from client.model.storage_keeper import StorageKeeper
from client.model.manager import Manager
from client.model.order_man import OrderMan
from client.ui import *
import re


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(402, 307)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(47, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_username = QtWidgets.QLabel(Form)
        self.label_username.setObjectName("label_username")
        self.verticalLayout_2.addWidget(self.label_username)
        self.label_password = QtWidgets.QLabel(Form)
        self.label_password.setObjectName("label_password")
        self.verticalLayout_2.addWidget(self.label_password)
        self.label_type = QtWidgets.QLabel(Form)
        self.label_type.setObjectName("label_type")
        self.verticalLayout_2.addWidget(self.label_type)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_username = QtWidgets.QLineEdit(Form)
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.verticalLayout.addWidget(self.lineEdit_username)
        self.lineEdit_password = QtWidgets.QLineEdit(Form)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.verticalLayout.addWidget(self.lineEdit_password)
        self.comboBox_type = QtWidgets.QComboBox(Form)
        self.comboBox_type.setObjectName("comboBox_type")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.verticalLayout.addWidget(self.comboBox_type)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.button_login = QtWidgets.QPushButton(Form)
        self.button_login.setObjectName("button_login")
        self.verticalLayout_3.addWidget(self.button_login)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.change_server_address_lineEdit = QtWidgets.QLineEdit(Form)
        self.change_server_address_lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.change_server_address_lineEdit)
        self.change_server_address_Button = QtWidgets.QPushButton(Form)
        self.change_server_address_Button.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.change_server_address_Button)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        spacerItem2 = QtWidgets.QSpacerItem(46, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "登陆"))
        self.label_username.setText(_translate("Form", "用户名:"))
        self.label_password.setText(_translate("Form", "密    码:"))
        self.label_type.setText(_translate("Form", "类    型："))
        self.comboBox_type.setItemText(0, _translate("Form", "系统管理员"))
        self.comboBox_type.setItemText(1, _translate("Form", "经理"))
        self.comboBox_type.setItemText(2, _translate("Form", "采购员"))
        self.comboBox_type.setItemText(3, _translate("Form", "仓库管理员"))
        self.button_login.setText(_translate("Form", "登陆"))
        self.label.setText(_translate("Form", "当前服务器地址：127.0.0.1:5000"))
        self.change_server_address_Button.setText(_translate("Form", "更改服务器IP"))


class SignIn(object):
    def __init__(self, server_address='http://127.0.0.1:5000'):
        self.win = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.win)
        self.server_address = server_address

        self.adjust_ui()
        self.bind()

    def bind(self):
        self.ui.button_login.clicked.connect(lambda: self.login())
        self.ui.change_server_address_Button.clicked.connect(lambda: self.reset_server_address())

    def show(self):
        self.win.show()

    def adjust_ui(self):
        self.ui.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ui.change_server_address_lineEdit.setPlaceholderText('格式：x.x.x.x:port')

    def reset_server_address(self):
        new_address = self.ui.change_server_address_lineEdit.text()
        if (re.match(
                r'^([1-9]?\d|1\d\d|2[0-4]\d|25[0-5])\.([1-9]?\d|1\d\d|2[0-4]\d|25[0-5])\.([1-9]?\d|1\d\d|2[0-4]\d|25[0-5])\.([1-9]?\d|1\d\d|2[0-4]\d|25[0-5]):\d+',
                new_address)):
            self.server_address = 'http://' + new_address
            self.ui.label.setText('当前服务器地址：' + self.server_address)
        else:
            QtWidgets.QMessageBox.information(None, '提示', '请输入合法的ip地址', QtWidgets.QMessageBox.Ok)
            return False

    def login(self):
        username = self.ui.lineEdit_username.text()
        password = self.ui.lineEdit_password.text()
        department = self.ui.comboBox_type.currentText()
        switch = {
            '系统管理员': lambda: self.admin_login(username, password, department),
            '经理': lambda: self.manager_login(username, password, department),
            '采购员': lambda: self.order_man_login(username, password, department),
            '仓库管理员': lambda: self.storage_keeper_login(username, password, department),

        }
        switch[department]()

    def admin_login(self, username, password, department):
        admin = Admin(self.server_address, username, password, department)
        statue = admin.login()
        if (statue == True):
            self.win.hide()
            admin_page = AdminPage(admin)
            admin_page.win.show()
        elif (statue == False):
            QtWidgets.QMessageBox.information(self.win, '提示', '登陆失败，请检查用户名、密码或者部门是否输入正确',
                                              QtWidgets.QMessageBox.Yes)
        elif (statue == 'network_error'):
            QtWidgets.QMessageBox.warning(self.win, '提示', '连接服务器超时！',
                                          QtWidgets.QMessageBox.Yes)

    def manager_login(self, username, password, department):
        manager = Manager(self.server_address, username, password, department)
        statue = manager.login()
        if (statue == True):
            self.win.hide()
            manager_page = ManagerPage(manager)
            manager_page.win.show()
        elif (statue == False):
            QtWidgets.QMessageBox.information(self.win, '提示', '登陆失败，请检查用户名、密码或者部门是否输入正确',
                                              QtWidgets.QMessageBox.Yes)
        elif (statue == 'network_error'):
            QtWidgets.QMessageBox.warning(self.win, '提示', '连接服务器超时！',
                                          QtWidgets.QMessageBox.Yes)

    def storage_keeper_login(self, username, password, department):
        storage_keeper = StorageKeeper(self.server_address, username, password, department)
        statue = storage_keeper.login()
        if (statue == True):
            self.win.hide()
            storage_keeper_page = StorageKeeperPage(storage_keeper)
            storage_keeper_page.win.show()
        elif (statue == False):
            QtWidgets.QMessageBox.information(self.win, '提示', '登陆失败，请检查用户名、密码或者部门是否输入正确',
                                              QtWidgets.QMessageBox.Yes)
        elif (statue == 'network_error'):
            QtWidgets.QMessageBox.warning(self.win, '提示', '连接服务器超时！',
                                          QtWidgets.QMessageBox.Yes)

    def order_man_login(self, username, password, department):
        order_man = OrderMan(self.server_address, username, password, department)
        statue = order_man.login()
        if (statue == True):
            self.win.hide()
            storage_keeper_page = OrderManPage(order_man)
            storage_keeper_page.win.show()
        elif (statue == False):
            QtWidgets.QMessageBox.information(self.win, '提示', '登陆失败，请检查用户名、密码或者部门是否输入正确',
                                              QtWidgets.QMessageBox.Yes)
        elif (statue == 'network_error'):
            QtWidgets.QMessageBox.warning(self.win, '提示', '连接服务器超时！',
                                          QtWidgets.QMessageBox.Yes)
