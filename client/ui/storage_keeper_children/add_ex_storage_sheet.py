# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_in_storage_sheet.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
import random
import uuid
import hashlib
from client.ui.storage_keeper_children.add_ex_storage_sheet_details import AddExStorageSheetDetails
from client.ui.storage_keeper_children.ex_storage_sheet_review import ExStorageSheetReview


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(782, 525)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.gen_code_Button = QtWidgets.QPushButton(Form)
        self.gen_code_Button.setObjectName("gen_code_Button")
        self.horizontalLayout_3.addWidget(self.gen_code_Button)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.add_Button = QtWidgets.QPushButton(Form)
        self.add_Button.setObjectName("add_Button")
        self.horizontalLayout_2.addWidget(self.add_Button)
        self.delete_Button = QtWidgets.QPushButton(Form)
        self.delete_Button.setObjectName("delete_Button")
        self.horizontalLayout_2.addWidget(self.delete_Button)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
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
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.commit_Button = QtWidgets.QPushButton(Form)
        self.commit_Button.setObjectName("commit_Button")
        self.horizontalLayout.addWidget(self.commit_Button)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "出库单填写"))
        self.label.setText(_translate("Form", "出库单编号："))
        self.gen_code_Button.setText(_translate("Form", "生成出库单单号"))
        self.label_3.setText(_translate("Form", "出库详单："))
        self.add_Button.setText(_translate("Form", "添加一行"))
        self.delete_Button.setText(_translate("Form", "删除一行"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "商品编号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "商品名称"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "商品类型"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "计量单位"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "规格"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "供应商"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "出库数量"))
        self.commit_Button.setText(_translate("Form", "提交出库单"))


class AddExStorageSheet():
    def __init__(self, storager_keeper):
        self.storager_keeper = storager_keeper
        self.details = []

        self.win = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.win)

        self.bind()
        self.adjust_ui()

    def bind(self):
        self.ui.gen_code_Button.clicked.connect(lambda: self.gen_code())
        self.ui.add_Button.clicked.connect(lambda: self.add_one())
        self.ui.delete_Button.clicked.connect(lambda: self.delete_one())
        self.ui.commit_Button.clicked.connect(lambda: self.commit())

    def adjust_ui(self):
        self.ui.lineEdit.setEnabled(False)
        self.ui.lineEdit.setPlaceholderText('点击右边按钮生成单号')
        self.ui.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.ui.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

    def load_data(self):
        pass

    def refresh(self):
        self.load_data()

    def gen_code(self):
        # 生成id
        cur_time = datetime.datetime.now()
        t = cur_time.strftime("%Y%m%d%H%M%S")
        username = self.storager_keeper.name
        u = hashlib.md5(username.encode("utf8")).hexdigest()[:10]
        r = str(random.randint(0, 9))
        id = t + u + r
        self.ui.lineEdit.setText(id)

    def add_one(self):
        dialog = AddExStorageSheetDetails(self.storager_keeper)
        statue = dialog.win.exec_()
        if (statue == 1):
            data = dialog.ret_data
            dialog.win.destroy()

            self.details.append(data)
            self.update_table()
        else:
            pass

    def delete_one(self):
        try:
            cur_row = self.ui.tableWidget.currentRow()
            # print(cur_row)
            # print(self.details[cur_row])
            self.details.pop(cur_row)
            self.update_table()
        except:
            QtWidgets.QMessageBox.information(None, '提示', '出现错误，请重试！', QtWidgets.QMessageBox.Ok)

    def update_table(self):
        self.ui.tableWidget.setRowCount(len(self.details))
        for i, detail in enumerate(self.details):
            self.ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(detail['commodity_code'])))
            self.ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(detail['commodity_name'])))
            self.ui.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(detail['commodity_type'])))
            self.ui.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str(detail['commodity_unit'])))
            self.ui.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(str(detail['commodity_specification'])))
            self.ui.tableWidget.setItem(i, 5, QtWidgets.QTableWidgetItem(str(detail['commodity_supplier'])))
            self.ui.tableWidget.setItem(i, 6, QtWidgets.QTableWidgetItem(str(detail['number'])))

    def commit(self):
        code = self.ui.lineEdit.text()
        warehouse_name = self.storager_keeper.warehouse_name
        date = str(datetime.datetime.now())
        handler_name = self.storager_keeper.name
        statue, data = self.storager_keeper.add_ex_storage_sheet(code, warehouse_name, date, handler_name)
        if (statue == True):
            for detail in self.details:
                ex_storage_sheet_code = code
                commodity_code = detail['commodity_code']
                number = detail['number']
                statue, data = self.storager_keeper.add_ex_storage_sheet_details(ex_storage_sheet_code, commodity_code,
                                                                                 number)
            QtWidgets.QMessageBox.information(None, '提示', '提交成功！', QtWidgets.QMessageBox.Ok)
            self.details.clear()
            self.update_table()
            self.ui.lineEdit.setText('')
        else:
            QtWidgets.QMessageBox.information(None, '提示', '提交出库总单失败', QtWidgets.QMessageBox.Ok)


if __name__ == '__main__':
    import sys
    from client.model.storage_keeper import StorageKeeper

    app = QtWidgets.QApplication(sys.argv)
    storager_keeper = StorageKeeper('http://127.0.0.1:5000', '3', '3', '仓库管理员')
    if (storager_keeper.login()):
        page = AddExStorageSheet(storager_keeper)
        page.win.show()

    sys.exit(app.exec_())
