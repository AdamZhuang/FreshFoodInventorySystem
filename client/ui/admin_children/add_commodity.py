# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_commodity.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_add_commodity(object):
    def setupUi(self, add_commodity):
        add_commodity.setObjectName("add_commodity")
        add_commodity.resize(717, 510)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(add_commodity)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(add_commodity)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.commodity_code_lineEdit = QtWidgets.QLineEdit(add_commodity)
        self.commodity_code_lineEdit.setObjectName("commodity_code_lineEdit")
        self.horizontalLayout_4.addWidget(self.commodity_code_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(add_commodity)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.type_comboBox = QtWidgets.QComboBox(add_commodity)
        self.type_comboBox.setObjectName("type_comboBox")
        self.type_comboBox.addItem("")
        self.type_comboBox.addItem("")
        self.type_comboBox.addItem("")
        self.type_comboBox.addItem("")
        self.type_comboBox.addItem("")
        self.horizontalLayout_5.addWidget(self.type_comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_3 = QtWidgets.QLabel(add_commodity)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        self.commodity_specification_lineEdit = QtWidgets.QLineEdit(add_commodity)
        self.commodity_specification_lineEdit.setObjectName("commodity_specification_lineEdit")
        self.horizontalLayout_6.addWidget(self.commodity_specification_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_8.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(add_commodity)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.commodity_name_lineEdit = QtWidgets.QLineEdit(add_commodity)
        self.commodity_name_lineEdit.setObjectName("commodity_name_lineEdit")
        self.horizontalLayout.addWidget(self.commodity_name_lineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(add_commodity)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.unit_lineEdit = QtWidgets.QLineEdit(add_commodity)
        self.unit_lineEdit.setObjectName("unit_lineEdit")
        self.horizontalLayout_2.addWidget(self.unit_lineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_6 = QtWidgets.QLabel(add_commodity)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.supplier_comboBox = QtWidgets.QComboBox(add_commodity)
        self.supplier_comboBox.setObjectName("supplier_comboBox")
        self.horizontalLayout_3.addWidget(self.supplier_comboBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_8.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.tableWidget = QtWidgets.QTableWidget(add_commodity)
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
        self.verticalLayout_3.addWidget(self.tableWidget)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.add_Button = QtWidgets.QPushButton(add_commodity)
        self.add_Button.setObjectName("add_Button")
        self.horizontalLayout_7.addWidget(self.add_Button)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.retranslateUi(add_commodity)
        QtCore.QMetaObject.connectSlotsByName(add_commodity)

    def retranslateUi(self, add_commodity):
        _translate = QtCore.QCoreApplication.translate
        add_commodity.setWindowTitle(_translate("add_commodity", "Form"))
        self.label.setText(_translate("add_commodity", "商品编号"))
        self.label_5.setText(_translate("add_commodity", "商品类型"))
        self.type_comboBox.setItemText(0, _translate("add_commodity", "水果"))
        self.type_comboBox.setItemText(1, _translate("add_commodity", "蔬菜"))
        self.type_comboBox.setItemText(2, _translate("add_commodity", "肉品"))
        self.type_comboBox.setItemText(3, _translate("add_commodity", "水产"))
        self.type_comboBox.setItemText(4, _translate("add_commodity", "干货"))
        self.label_3.setText(_translate("add_commodity", "规   格"))
        self.label_2.setText(_translate("add_commodity", "商品名称"))
        self.label_4.setText(_translate("add_commodity", "计量单位"))
        self.label_6.setText(_translate("add_commodity", "供应商"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("add_commodity", "序号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("add_commodity", "商品编号"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("add_commodity", "商品名称"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("add_commodity", "商品类型"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("add_commodity", "计量单位"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("add_commodity", "规格"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("add_commodity", "供应商"))
        self.add_Button.setText(_translate("add_commodity", "添加"))


class AddCommodity():
    def __init__(self, admin):
        self.admin = admin
        self.win = QtWidgets.QWidget()
        self.ui = Ui_add_commodity()
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
        self.ui.add_Button.clicked.connect(lambda: self.add_commodity())

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
            self.ui.supplier_comboBox.clear()
            for supplier in suppliers:
                self.ui.supplier_comboBox.addItem(supplier['name'])

        except Exception as e:
            print(e)

    def add_commodity(self):
        try:
            commodity_code = self.ui.commodity_code_lineEdit.text()
            commodity_name = self.ui.commodity_name_lineEdit.text()
            commodity_type = self.ui.type_comboBox.currentText()
            commodity_unit = self.ui.unit_lineEdit.text()
            commodity_specification = self.ui.commodity_specification_lineEdit.text()
            commodity_supplier = self.ui.supplier_comboBox.currentText()
            if (commodity_code == '' or commodity_name == '' or commodity_unit == '' or commodity_specification == ''):
                QtWidgets.QMessageBox.information(None, '提示', '请输入大于1个字的内容', QtWidgets.QMessageBox.Yes)
                return False
            statue, data = self.admin.add_commodity(commodity_code=commodity_code,
                                                    commodity_name=commodity_name,
                                                    commodity_type=commodity_type,
                                                    commodity_unit=commodity_unit,
                                                    commodity_specification=commodity_specification,
                                                    commodity_supplier_name=commodity_supplier)
            if (statue == True):
                self.load_data()
                QtWidgets.QMessageBox.information(None, '提示', '添加成功', QtWidgets.QMessageBox.Yes)
                self.ui.commodity_code_lineEdit.setText('')
                self.ui.commodity_name_lineEdit.setText('')
                self.ui.type_comboBox.setCurrentIndex(-1)
                self.ui.unit_lineEdit.setText('')
                self.ui.commodity_specification_lineEdit.setText('')
                self.ui.supplier_comboBox.setCurrentIndex(-1)
            elif (statue == False):
                QtWidgets.QMessageBox.information(None, '提示', '添加失败', QtWidgets.QMessageBox.Yes)
        except Exception as e:
            print(e)
