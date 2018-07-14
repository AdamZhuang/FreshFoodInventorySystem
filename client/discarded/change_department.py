# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'change_department.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets


class Ui_change_department(object):
    def setupUi(self, change_department):
        change_department.setObjectName("change_department")
        change_department.resize(770, 566)
        self.verticalLayout = QtWidgets.QVBoxLayout(change_department)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_before = QtWidgets.QLabel(change_department)
        self.label_before.setObjectName("label_before")
        self.horizontalLayout_2.addWidget(self.label_before)
        self.comboBox = QtWidgets.QComboBox(change_department)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_after = QtWidgets.QLabel(change_department)
        self.label_after.setObjectName("label_after")
        self.horizontalLayout.addWidget(self.label_after)
        self.lineEdit = QtWidgets.QLineEdit(change_department)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.change_button = QtWidgets.QPushButton(change_department)
        self.change_button.setObjectName("change_button")
        self.horizontalLayout.addWidget(self.change_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableWidget = QtWidgets.QTableWidget(change_department)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tableWidget)

        self.retranslateUi(change_department)
        QtCore.QMetaObject.connectSlotsByName(change_department)

    def retranslateUi(self, change_department):
        _translate = QtCore.QCoreApplication.translate
        change_department.setWindowTitle(_translate("change_department", "Form"))
        self.label_before.setText(_translate("change_department", "更改前部门名称(双击表格行进行快捷选中)："))
        self.label_after.setText(_translate("change_department", "更改后部门名称："))
        self.change_button.setText(_translate("change_department", "修改"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("change_department", "序号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("change_department", "部门名称"))



class ChangeDepartment():
    def __init__(self, admin):
        self.admin = admin
        self.win = QtWidgets.QWidget()
        self.ui = Ui_change_department()
        self.ui.setupUi(self.win)
        self.customize()

    def customize(self):
        self.adjust_ui()
        self.bind()
        self.load_data()


    def adjust_ui(self):
        # 调整表格自适应
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(1 ,QtWidgets.QHeaderView.Stretch)
        self.ui.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)


    def bind(self):
        self.ui.change_button.clicked.connect(lambda :self.change_department())
        self.ui.tableWidget.itemDoubleClicked.connect(lambda :self.get_double_clicked())

    def refresh(self):
        self.load_data()



    def load_data(self):
        try:
            data = self.admin.get_all_departments()
            if(data == False):
                QtWidgets.QMessageBox.information(None, '提示', '载入数据失败', QtWidgets.QMessageBox.Ok)
            elif(data == 'network_error'):
                QtWidgets.QMessageBox.information(None, '提示', '连接服务器超时', QtWidgets.QMessageBox.Ok)
            else:
                departments = data
                data_num = len(departments)
                self.ui.tableWidget.setRowCount(data_num)
                # 表格数据加载
                for  i, department in enumerate(departments):
                    self.ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(i+1)))
                    self.ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(department)))
                # 清空combobox数据并加载
                self.ui.comboBox.clear()
                for i, department in enumerate(departments):
                    self.ui.comboBox.addItem(str(department))
        except Exception as e:
            print(e)



    def change_department(self):
        try:
            origin_department_name = self.ui.comboBox.currentText()
            dest_department_name = self.ui.lineEdit.text()
            if(len(dest_department_name) < 1):
                QtWidgets.QMessageBox.information(None, '提示', '请不要输入空字符串', QtWidgets.QMessageBox.Ok)
                return False


            statue = self.admin.change_department(origin_department_name=origin_department_name,
                                                  dest_department_name=dest_department_name)
            if(statue == True):
                if (origin_department_name == self.admin.department):
                    self.admin.department = dest_department_name
                self.load_data()
                QtWidgets.QMessageBox.information(None, '提示', '修改成功', QtWidgets.QMessageBox.Ok)
            elif(statue == False):
                QtWidgets.QMessageBox.information(None, '提示', '修改失败', QtWidgets.QMessageBox.Ok)
            elif(statue == 'network_error'):
                QtWidgets.QMessageBox.warning(None,'提示', '连接服务器超时！', QtWidgets.QMessageBox.Ok)
        except Exception as e:
            print(e)

    def get_double_clicked(self):
        selected_str = self.ui.tableWidget.selectedItems()[1].text()
        self.ui.comboBox.setCurrentText(selected_str)