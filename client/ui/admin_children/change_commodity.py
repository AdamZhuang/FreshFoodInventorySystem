# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'change_commodity.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_change_commodity(object):
    def setupUi(self, change_commodity):
        change_commodity.setObjectName("add_commodity")
        change_commodity.resize(717, 510)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(change_commodity)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label = QtWidgets.QLabel(change_commodity)
        self.label.setObjectName("label")
        self.horizontalLayout_7.addWidget(self.label)
        self.origin_code_lineEdit = QtWidgets.QLineEdit(change_commodity)
        self.origin_code_lineEdit.setObjectName("origin_code_lineEdit")
        self.horizontalLayout_7.addWidget(self.origin_code_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_3 = QtWidgets.QLabel(change_commodity)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        self.dest_name_lineEdit = QtWidgets.QLineEdit(change_commodity)
        self.dest_name_lineEdit.setObjectName("dest_name_lineEdit")
        self.horizontalLayout_6.addWidget(self.dest_name_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(change_commodity)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.dest_unit_lineEdit = QtWidgets.QLineEdit(change_commodity)
        self.dest_unit_lineEdit.setObjectName("dest_unit_lineEdit")
        self.horizontalLayout_5.addWidget(self.dest_unit_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_8.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(change_commodity)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.dest_code_lineEdit = QtWidgets.QLineEdit(change_commodity)
        self.dest_code_lineEdit.setObjectName("dest_code_lineEdit")
        self.horizontalLayout.addWidget(self.dest_code_lineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(change_commodity)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.dest_type_comboBox = QtWidgets.QComboBox(change_commodity)
        self.dest_type_comboBox.setObjectName("dest_type_comboBox")
        self.dest_type_comboBox.addItem("")
        self.dest_type_comboBox.addItem("")
        self.dest_type_comboBox.addItem("")
        self.dest_type_comboBox.addItem("")
        self.dest_type_comboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.dest_type_comboBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_6 = QtWidgets.QLabel(change_commodity)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.dest_specification_lineEdit = QtWidgets.QLineEdit(change_commodity)
        self.dest_specification_lineEdit.setObjectName("dest_specification_lineEdit")
        self.horizontalLayout_3.addWidget(self.dest_specification_lineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_8.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_7 = QtWidgets.QLabel(change_commodity)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.dest_supplier_comboBox = QtWidgets.QComboBox(change_commodity)
        self.dest_supplier_comboBox.setMinimumSize(QtCore.QSize(140, 0))
        self.dest_supplier_comboBox.setObjectName("dest_supplier_comboBox")
        self.horizontalLayout_4.addWidget(self.dest_supplier_comboBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.tableWidget = QtWidgets.QTableWidget(change_commodity)
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
        self.verticalLayout_4.addWidget(self.tableWidget)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem1)
        self.change_Button = QtWidgets.QPushButton(change_commodity)
        self.change_Button.setObjectName("change_Button")
        self.horizontalLayout_9.addWidget(self.change_Button)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)

        self.retranslateUi(change_commodity)
        QtCore.QMetaObject.connectSlotsByName(change_commodity)

    def retranslateUi(self, change_commodity):
        _translate = QtCore.QCoreApplication.translate
        change_commodity.setWindowTitle(_translate("change_commodity", "Form"))
        self.label.setText(_translate("change_commodity", "修改前商品编号"))
        self.label_3.setText(_translate("change_commodity", "修改后商品名称"))
        self.label_5.setText(_translate("change_commodity", "修改后计量单位"))
        self.label_2.setText(_translate("change_commodity", "修改后商品编号"))
        self.label_4.setText(_translate("change_commodity", "修改后商品类型"))
        self.dest_type_comboBox.setItemText(0, _translate("change_commodity", "水果"))
        self.dest_type_comboBox.setItemText(1, _translate("change_commodity", "蔬菜"))
        self.dest_type_comboBox.setItemText(2, _translate("change_commodity", "肉品"))
        self.dest_type_comboBox.setItemText(3, _translate("change_commodity", "水产"))
        self.dest_type_comboBox.setItemText(4, _translate("change_commodity", "干货"))
        self.label_6.setText(_translate("change_commodity", "修改后规格"))
        self.label_7.setText(_translate("change_commodity", "修改后供应商名"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("change_commodity", "序号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("change_commodity", "商品编号"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("change_commodity", "商品名称"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("change_commodity", "商品类型"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("change_commodity", "计量单位"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("change_commodity", "规格"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("change_commodity", "供应商"))
        self.change_Button.setText(_translate("change_commodity", "修改"))


class ChangeCommodity():
    def __init__(self, admin):
        self.admin = admin
        self.win = QtWidgets.QWidget()
        self.ui = Ui_change_commodity()
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
        self.ui.change_Button.clicked.connect(lambda: self.change_commodity())
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

            statue, suppliers = self.admin.get_all_suppliers()
            self.ui.dest_supplier_comboBox.clear()
            for supplier in suppliers:
                self.ui.dest_supplier_comboBox.addItem(supplier['name'])
        except Exception as e:
            print(e)

    def change_commodity(self):
        try:
            origin_commodity_code = self.ui.origin_code_lineEdit.text()
            dest_commodity_code = self.ui.dest_code_lineEdit.text()
            dest_commodity_name = self.ui.dest_name_lineEdit.text()
            dest_commodity_type = self.ui.dest_type_comboBox.currentText()
            dest_commodity_unit = self.ui.dest_unit_lineEdit.text()
            dest_commodity_specification = self.ui.dest_specification_lineEdit.text()
            dest_commodity_supplier_name = self.ui.dest_supplier_comboBox.currentText()

            if (origin_commodity_code == '' or dest_commodity_code == ''
                or dest_commodity_name == '' or dest_commodity_type == ''
                or dest_commodity_unit == '' or dest_commodity_specification == ''
                or dest_commodity_supplier_name == ''):
                QtWidgets.QMessageBox.information(None, '提示', '请输入长度大于1的字符！', QtWidgets.QMessageBox.Yes)
                return False

            statue, data = self.admin.change_commodity(origin_commodity_code=origin_commodity_code,
                                                       dest_commodity_code=dest_commodity_code,
                                                       dest_commodity_name=dest_commodity_name,
                                                       dest_commodity_type=dest_commodity_type,
                                                       dest_commodity_unit=dest_commodity_unit,
                                                       dest_commodity_specification=dest_commodity_specification,
                                                       dest_commodity_supplier_name=dest_commodity_supplier_name)
            if (statue == True):
                self.load_data()
                QtWidgets.QMessageBox.information(None, '提示', '修改成功', QtWidgets.QMessageBox.Yes)
                self.ui.origin_code_lineEdit.setText('')
                self.ui.dest_code_lineEdit.setText('')
                self.ui.dest_name_lineEdit.setText('')
                self.ui.dest_type_comboBox.setCurrentIndex(-1)
                self.ui.dest_unit_lineEdit.setText('')
                self.ui.dest_specification_lineEdit.setText('')
                self.ui.dest_supplier_comboBox.setCurrentIndex(-1)
            elif (statue == False):
                QtWidgets.QMessageBox.information(None, '提示', '修改失败', QtWidgets.QMessageBox.Yes)
        except Exception as e:
            print(e)

    def quick_choose(self):
        selected = self.ui.tableWidget.selectedItems()
        self.ui.origin_code_lineEdit.setText(selected[1].text())
        self.ui.dest_code_lineEdit.setText(selected[1].text())
        self.ui.dest_name_lineEdit.setText(selected[2].text())
        self.ui.dest_type_comboBox.setCurrentText(selected[3].text())
        self.ui.dest_unit_lineEdit.setText(selected[4].text())
        self.ui.dest_specification_lineEdit.setText(selected[5].text())
        self.ui.dest_supplier_comboBox.setCurrentText(selected[6].text())
