# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'change_warehouse.ui'
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
        self.old_warehouse_name_comboBox = QtWidgets.QComboBox(Form)
        self.old_warehouse_name_comboBox.setMinimumSize(QtCore.QSize(200, 0))
        self.old_warehouse_name_comboBox.setObjectName("old_warehouse_name_comboBox")
        self.horizontalLayout.addWidget(self.old_warehouse_name_comboBox)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.new_warehouse_name_lineEdit = QtWidgets.QLineEdit(Form)
        self.new_warehouse_name_lineEdit.setObjectName("new_warehouse_name_lineEdit")
        self.horizontalLayout.addWidget(self.new_warehouse_name_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.new_warehouse_location_lineEdit = QtWidgets.QLineEdit(Form)
        self.new_warehouse_location_lineEdit.setObjectName("new_warehouse_location_lineEdit")
        self.horizontalLayout_2.addWidget(self.new_warehouse_location_lineEdit)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.new_manager_comboBox = QtWidgets.QComboBox(Form)
        self.new_manager_comboBox.setMinimumSize(QtCore.QSize(200, 0))
        self.new_manager_comboBox.setObjectName("new_manager_comboBox")
        self.horizontalLayout_2.addWidget(self.new_manager_comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
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
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.change_Button = QtWidgets.QPushButton(Form)
        self.change_Button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.change_Button.setObjectName("change_Button")
        self.horizontalLayout_3.addWidget(self.change_Button)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "旧仓库名"))
        self.label_2.setText(_translate("Form", "新仓库名"))
        self.label_3.setText(_translate("Form", "新仓库地址"))
        self.label_4.setText(_translate("Form", "新仓库管理员"))
        self.label_5.setText(_translate("Form", "当前所有仓库："))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "序号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "仓库名称"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "仓库地址"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "仓库管理员"))
        self.change_Button.setText(_translate("Form", "修改"))


class ChangeWarehouse():
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
        self.ui.change_Button.clicked.connect(lambda: self.change_warehouse())
        self.ui.tableWidget.itemDoubleClicked.connect(lambda: self.quick_choose())

    def refresh(self):
        self.load_data()

    def load_data(self):
        try:
            statue1, warehouses = self.admin.get_all_warehouses()
            statue2, users = self.admin.get_all_users()
            if (statue1 == True and statue2 == True):
                # 保存数据
                self.warehouses = warehouses
                self.users = users

                data_num = len(warehouses)
                # 加载表格数据
                self.ui.tableWidget.setRowCount(data_num)
                self.ui.old_warehouse_name_comboBox.clear()
                for i, warehouse in enumerate(warehouses):
                    self.ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(i + 1)))
                    self.ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(warehouse['name'])))
                    self.ui.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(warehouse['location'])))
                    self.ui.tableWidget.setItem(i, 3,
                                                QtWidgets.QTableWidgetItem(str(warehouse['warehouse_manager_name'])))
                    self.ui.old_warehouse_name_comboBox.addItem(str(warehouse['name']))

                self.ui.new_manager_comboBox.clear()

                for user in users:
                    if (user['department'] == '仓库管理员'):
                        self.ui.new_manager_comboBox.addItem(user['name'])
            else:
                print('error')
        except Exception as e:
            print(e)

    def change_warehouse(self):
        try:
            origin_warehouse_name = self.ui.old_warehouse_name_comboBox.currentText()
            dest_warehouse_name = self.ui.new_warehouse_name_lineEdit.text()
            dest_warehouse_location = self.ui.new_warehouse_location_lineEdit.text()
            dest_warehouse_manager_name = self.ui.new_manager_comboBox.currentText()

            for warehouse in self.warehouses:
                # 修改后的人员已经绑定另外一个仓库的情况，弹窗报错中断执行！
                if (dest_warehouse_manager_name == warehouse['warehouse_manager_name'] and warehouse[
                    'name'] != origin_warehouse_name):
                    QtWidgets.QMessageBox.information(None, '提示', '无法修改！因为该仓储管理员已经绑定另外一个仓库！', QtWidgets.QMessageBox.Ok)
                    return False

            statue, data = self.admin.change_warehouse(origin_warehouse_name=origin_warehouse_name,
                                                       dest_warehouse_name=dest_warehouse_name,
                                                       dest_warehouse_location=dest_warehouse_location,
                                                       dest_warehouse_manager_name=dest_warehouse_manager_name)
            if (statue == True):
                self.load_data()
                QtWidgets.QMessageBox.information(None, '提示', '修改成功',
                                                  QtWidgets.QMessageBox.Yes)
                self.ui.old_warehouse_name_comboBox.setCurrentIndex(-1)
                self.ui.new_warehouse_name_lineEdit.setText('')
                self.ui.new_warehouse_location_lineEdit.setText('')
                self.ui.new_manager_comboBox.setCurrentIndex(-1)
            elif (statue == False):
                QtWidgets.QMessageBox.information(None, '提示', '修改失败', QtWidgets.QMessageBox.Yes)
            elif (statue == 'network_error'):
                QtWidgets.QMessageBox.warning(None, '提示', '连接服务器超时！', QtWidgets.QMessageBox.Yes)

        except Exception as e:
            print(e)

    def quick_choose(self):
        selected = self.ui.tableWidget.selectedItems()
        self.ui.old_warehouse_name_comboBox.setCurrentText(selected[1].text())
        self.ui.new_warehouse_name_lineEdit.setText(selected[1].text())
        self.ui.new_warehouse_location_lineEdit.setText(selected[2].text())
        self.ui.new_manager_comboBox.setCurrentText(selected[3].text())
