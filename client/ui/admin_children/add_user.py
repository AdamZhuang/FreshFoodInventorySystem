# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_user.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_add_user(object):
    def setupUi(self, add_user):
        add_user.setObjectName("add_user")
        add_user.resize(685, 449)
        self.verticalLayout = QtWidgets.QVBoxLayout(add_user)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(add_user)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.username_lineEdit = QtWidgets.QLineEdit(add_user)
        self.username_lineEdit.setObjectName("username_lineEdit")
        self.horizontalLayout.addWidget(self.username_lineEdit)
        self.label_2 = QtWidgets.QLabel(add_user)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.password_lineEdit = QtWidgets.QLineEdit(add_user)
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.horizontalLayout.addWidget(self.password_lineEdit)
        self.label_3 = QtWidgets.QLabel(add_user)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.comboBox = QtWidgets.QComboBox(add_user)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.label_4 = QtWidgets.QLabel(add_user)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.contact_lineEdit = QtWidgets.QLineEdit(add_user)
        self.contact_lineEdit.setObjectName("contact_lineEdit")
        self.horizontalLayout.addWidget(self.contact_lineEdit)
        self.add_button = QtWidgets.QPushButton(add_user)
        self.add_button.setObjectName("add_button")
        self.horizontalLayout.addWidget(self.add_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableWidget = QtWidgets.QTableWidget(add_user)
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
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tableWidget)

        self.retranslateUi(add_user)
        QtCore.QMetaObject.connectSlotsByName(add_user)

    def retranslateUi(self, add_user):
        _translate = QtCore.QCoreApplication.translate
        add_user.setWindowTitle(_translate("add_user", "Form"))
        self.label.setText(_translate("add_user", "用户名"))
        self.label_2.setText(_translate("add_user", "密码"))
        self.label_3.setText(_translate("add_user", "部门"))
        self.comboBox.setItemText(0, _translate("add_user", "经理"))
        self.comboBox.setItemText(1, _translate("add_user", "采购员"))
        self.comboBox.setItemText(2, _translate("add_user", "仓库管理员"))
        self.label_4.setText(_translate("add_user", "联系电话"))
        self.add_button.setText(_translate("add_user", "添加"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("add_user", "序号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("add_user", "用户名"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("add_user", "密码（加密后）"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("add_user", "部门"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("add_user", "联系电话"))


class AddUser():
    def __init__(self, admin):
        self.admin = admin
        self.win = QtWidgets.QWidget()
        self.ui = Ui_add_user()
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
        self.ui.add_button.clicked.connect(lambda :self.add_user())


    def refresh(self):
        self.load_data()
        pass


    def load_data(self):
        try:
            statue, users = self.admin.get_all_users()
            if(statue==True):
                data_num = len(users)
                self.ui.tableWidget.setRowCount(data_num)
                for  i, user in enumerate(users):
                    self.ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(i+1)))
                    self.ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(user['name'])))
                    self.ui.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(user['password'])))
                    self.ui.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str(user['department'])))
                    self.ui.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(str(user['contact'])))
            else:
                print('something wrong')
        except Exception as e:
            print(e)


    def add_user(self):
        try:
            username = self.ui.username_lineEdit.text()
            password = self.ui.password_lineEdit.text()
            contact = self.ui.contact_lineEdit.text()
            department = self.ui.comboBox.currentText()
            if(username=='' or password=='' or contact==''):
                QtWidgets.QMessageBox.information(None, '提示', '请输入大于1个字的内容',
                                                          QtWidgets.QMessageBox.Yes)
                return False
            statue, data = self.admin.add_user(add_username=username, add_user_password=password,
                                              add_user_contact=contact, add_user_department=department)
            if(statue == True):
                self.load_data()
                QtWidgets.QMessageBox.information(None, '提示', '添加成功',
                                                          QtWidgets.QMessageBox.Yes)
                self.ui.username_lineEdit.setText('')
                self.ui.password_lineEdit.setText('')
                self.ui.contact_lineEdit.setText('')
                self.ui.comboBox.setCurrentIndex(-1)
            elif(statue == False):
                QtWidgets.QMessageBox.information(None, '提示', '添加失败',
                                                          QtWidgets.QMessageBox.Yes)
            elif(statue == 'network_error'):
                QtWidgets.QMessageBox.warning(None, '提示', '连接服务器超时！',
                                                          QtWidgets.QMessageBox.Yes)
        except Exception as e:
            print(e)

