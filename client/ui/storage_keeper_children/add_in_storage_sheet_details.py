# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_in_storage_sheet_details.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(403, 415)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout_2.addWidget(self.comboBox)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cancel_Button = QtWidgets.QPushButton(Form)
        self.cancel_Button.setObjectName("cancel_Button")
        self.horizontalLayout.addWidget(self.cancel_Button)
        self.confirm_Button = QtWidgets.QPushButton(Form)
        self.confirm_Button.setObjectName("confirm_Button")
        self.horizontalLayout.addWidget(self.confirm_Button)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.verticalLayout_3.addWidget(self.tableWidget)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.query_lineEdit = QtWidgets.QLineEdit(Form)
        self.query_lineEdit.setObjectName("query_lineEdit")
        self.horizontalLayout_3.addWidget(self.query_lineEdit)
        self.query_Button = QtWidgets.QPushButton(Form)
        self.query_Button.setObjectName("query_Button")
        self.horizontalLayout_3.addWidget(self.query_Button)
        self.check_all_Button = QtWidgets.QPushButton(Form)
        self.check_all_Button.setObjectName("check_all_Button")
        self.horizontalLayout_3.addWidget(self.check_all_Button)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        spacerItem3 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "详单添加"))
        self.label.setText(_translate("Form", "选择商品："))
        self.label_2.setText(_translate("Form", "输入数量："))
        self.cancel_Button.setText(_translate("Form", "取消"))
        self.confirm_Button.setText(_translate("Form", "确定"))
        self.label_3.setText(_translate("Form", "双击快速选择商品："))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "序号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "商品名称"))
        self.query_Button.setText(_translate("Form", "查询"))
        self.check_all_Button.setText(_translate("Form", "查看所有"))


class AddInStorageSheetDetails():
    def __init__(self, storager_keeper):
        self.storager_keeper = storager_keeper

        self.win = QtWidgets.QDialog()
        self.ui = Ui_Form()
        self.ui.setupUi(self.win)

        self.bind()
        self.adjust_ui()
        self.load_data()

    def bind(self):
        self.ui.confirm_Button.clicked.connect(lambda: self.confirm())
        self.ui.cancel_Button.clicked.connect(lambda: self.cancel())
        self.ui.tableWidget.clicked.connect(lambda: self.quick_choose())
        self.ui.query_Button.clicked.connect(lambda :self.query())
        self.ui.check_all_Button.clicked.connect(lambda :self.check_all())

    def confirm(self):
        commodity_name = self.ui.comboBox.currentText()
        number = self.ui.lineEdit.text()
        if (commodity_name == '' or number == ''):
            QtWidgets.QMessageBox.information(None, '提示', '请填写完整的表单信息！', QtWidgets.QMessageBox.Ok)
            return False
        self.data = {'commodity_name': commodity_name, 'number': number}
        return self.win.accept()

    def cancel(self):
        return self.win.reject()

    def adjust_ui(self):
        pass

    def load_data(self):
        statue, data = self.storager_keeper.get_commodities()
        if (statue == True):
            self.commodities = data['commodities']
            self.ui.comboBox.clear()
            self.ui.tableWidget.setRowCount(len(self.commodities))
            for i, item in enumerate(self.commodities):
                self.ui.comboBox.addItem(item['name'])
                self.ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(i + 1)))
                self.ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(item['name']))
        else:
            QtWidgets.QMessageBox.information(None, '提示', '载入数据出错！请返回重试', QtWidgets.QMessageBox.Ok)

    def quick_choose(self):
        selected = self.ui.tableWidget.selectedItems()
        if (selected != None):
            commodity_name = selected[1].text()
            self.ui.comboBox.setCurrentText(commodity_name)

    def query(self):
        query_str = self.ui.query_lineEdit.text()
        temp = []
        for item in self.commodities:
            if (query_str in item['name']):
                temp.append(item['name'])

        self.ui.tableWidget.setRowCount(len(temp))
        for i, item in enumerate(temp):
            self.ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(i + 1)))
            self.ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(item)))

    def check_all(self):
        self.ui.tableWidget.setRowCount(len(self.commodities))
        for i, item in enumerate(self.commodities):
            self.ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(i + 1)))
            self.ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(item['name']))


if __name__ == '__main__':
    import sys
    from client.model.storage_keeper import StorageKeeper

    app = QtWidgets.QApplication(sys.argv)
    storager_keeper = StorageKeeper('admin', 'admin', '系统管理员')
    if (storager_keeper.login()):
        page = AddInStorageSheetDetails(storager_keeper)
        page.win.show()

    sys.exit(app.exec_())
