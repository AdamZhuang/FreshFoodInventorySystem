# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'change_user.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_change_user(object):
    def setupUi(self, change_user):
        change_user.setObjectName("change_user")
        change_user.resize(603, 467)
        self.verticalLayout = QtWidgets.QVBoxLayout(change_user)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(change_user)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.origin_username_comboBox = QtWidgets.QComboBox(change_user)
        self.origin_username_comboBox.setMinimumSize(QtCore.QSize(240, 0))
        self.origin_username_comboBox.setObjectName("origin_username_comboBox")
        self.horizontalLayout.addWidget(self.origin_username_comboBox)
        self.label_2 = QtWidgets.QLabel(change_user)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.dest_username_lineEdit = QtWidgets.QLineEdit(change_user)
        self.dest_username_lineEdit.setObjectName("dest_username_lineEdit")
        self.horizontalLayout.addWidget(self.dest_username_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(change_user)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.dest_passwordlineEdit = QtWidgets.QLineEdit(change_user)
        self.dest_passwordlineEdit.setObjectName("dest_passwordlineEdit")
        self.horizontalLayout_2.addWidget(self.dest_passwordlineEdit)
        self.checkBox = QtWidgets.QCheckBox(change_user)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_2.addWidget(self.checkBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(change_user)
        self.label_4.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.department_comboBox = QtWidgets.QComboBox(change_user)
        self.department_comboBox.setMinimumSize(QtCore.QSize(230, 0))
        self.department_comboBox.setObjectName("department_comboBox")
        self.department_comboBox.addItem("")
        self.department_comboBox.addItem("")
        self.department_comboBox.addItem("")
        self.horizontalLayout_3.addWidget(self.department_comboBox)
        self.label_5 = QtWidgets.QLabel(change_user)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.dest_contact_lineEdit = QtWidgets.QLineEdit(change_user)
        self.dest_contact_lineEdit.setObjectName("dest_contact_lineEdit")
        self.horizontalLayout_3.addWidget(self.dest_contact_lineEdit)
        self.change_button = QtWidgets.QPushButton(change_user)
        self.change_button.setObjectName("change_button")
        self.horizontalLayout_3.addWidget(self.change_button)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.label_6 = QtWidgets.QLabel(change_user)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.tableWidget = QtWidgets.QTableWidget(change_user)
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

        self.retranslateUi(change_user)
        QtCore.QMetaObject.connectSlotsByName(change_user)

    def retranslateUi(self, change_user):
        _translate = QtCore.QCoreApplication.translate
        change_user.setWindowTitle(_translate("change_user", "Form"))
        self.label.setText(_translate("change_user", "旧用户名"))
        self.label_2.setText(_translate("change_user", "新用户名"))
        self.label_3.setText(_translate("change_user", "新密码"))
        self.checkBox.setText(_translate("change_user", "重置密码请勾选，否则将不会修改密码"))
        self.label_4.setText(_translate("change_user", "新部门"))
        self.department_comboBox.setItemText(0, _translate("change_user", "经理"))
        self.department_comboBox.setItemText(1, _translate("change_user", "采购员"))
        self.department_comboBox.setItemText(2, _translate("change_user", "仓库管理员"))
        self.label_5.setText(_translate("change_user", "新联系方式"))
        self.change_button.setText(_translate("change_user", "修改"))
        self.label_6.setText(_translate("change_user", "双击下方可进行快速选择："))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("change_user", "序号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("change_user", "用户名"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("change_user", "密码（加密后）"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("change_user", "部门"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("change_user", "联系方式"))



class ChangeUser():
    def __init__(self, admin):
        self.admin = admin
        self.win = QtWidgets.QWidget()
        self.ui = Ui_change_user()
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
        self.ui.change_button.clicked.connect(lambda :self.change_user())
        self.ui.tableWidget.itemDoubleClicked.connect(lambda :self.quick_choose())


    def refresh(self):
        self.load_data()


    def load_data(self):
        try:
            statue, users = self.admin.get_all_users()
            if (statue == True):
                data_num = len(users)
                self.ui.tableWidget.setRowCount(data_num)
                self.ui.origin_username_comboBox.clear()
                for  i, user in enumerate(users):
                    self.ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(i+1)))
                    self.ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(user['name'])))
                    self.ui.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(user['password'])))
                    self.ui.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str(user['department'])))
                    self.ui.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(str(user['contact'])))
                    self.ui.origin_username_comboBox.addItem(str(user['name']))
                self.ui.origin_username_comboBox.setCurrentIndex(-1)
        except Exception as e:
            print(e)


    def change_user(self):
        try:
            # 用户是否管理员确认
            origin_username = self.ui.origin_username_comboBox.currentText()
            if(origin_username == 'admin'):
                QtWidgets.QMessageBox.warning(None, '提示', '无法修改管理员用户',
                                                  QtWidgets.QMessageBox.Ok)
                return False

            # 密码是否修改确认
            if (self.ui.checkBox.checkState() == 2):
                dest_password = self.ui.dest_passwordlineEdit.text()
                if (len(dest_password) < 1):
                    QtWidgets.QMessageBox.information(None, '提示', '请输入大于长度1的字符串',
                                                      QtWidgets.QMessageBox.Ok)
                    return False
            else:
                dest_password = None
            dest_username = self.ui.dest_username_lineEdit.text()
            dest_contact = self.ui.dest_contact_lineEdit.text()
            dest_department = self.ui.department_comboBox.currentText()

            # 字符串是否为空验证
            if(len(dest_username)<1 or len(dest_contact)<1):
                QtWidgets.QMessageBox.information(None,'提示', '请输入大于长度1的字符串',
                                                  QtWidgets.QMessageBox.Ok)
                return False

            # 获取返回状态
            statue, data = self.admin.change_user(origin_name=origin_username, dest_name=dest_username, dest_password=dest_password, dest_contact=dest_contact, dest_department=dest_department)
            if (statue == True):
                # if(data['code']==0):
                self.load_data()
                reply = QtWidgets.QMessageBox.information(None, '提示', '修改成功',
                                                          QtWidgets.QMessageBox.Yes)
            elif (statue == False):
                reply = QtWidgets.QMessageBox.information(None, '提示', '修改失败',
                                                          QtWidgets.QMessageBox.Yes)
                print(data)
            elif (statue == 'network_error'):
                reply = QtWidgets.QMessageBox.warning(None, '提示', '连接服务器超时！',
                                                      QtWidgets.QMessageBox.Yes)

            # 重置输入，方便下一次进行修改
            self.ui.origin_username_comboBox.setCurrentIndex(-1)
            self.ui.dest_username_lineEdit.setText('')
            self.ui.dest_passwordlineEdit.setText('')
            self.ui.dest_contact_lineEdit.setText('')
            # self.ui.checkBox.setCheckState(QtWidgets.QCheckBox.)

        except Exception as e:
            print(e)


    def quick_choose(self):
        selected = self.ui.tableWidget.selectedItems()
        self.ui.origin_username_comboBox.setCurrentText(selected[1].text())
        self.ui.dest_username_lineEdit.setText(selected[1].text())
        # self.ui.dest_password_lineEdit.setText(selected[2].text())
        self.ui.department_comboBox.setCurrentText(selected[3].text())
        self.ui.dest_contact_lineEdit.setText(selected[4].text())
