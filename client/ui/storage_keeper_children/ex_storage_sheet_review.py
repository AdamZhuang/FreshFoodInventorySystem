# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'in_storage_sheet_review.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import datetime


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(610, 414)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout.addWidget(self.checkBox)
        self.back_Button = QtWidgets.QPushButton(Form)
        self.back_Button.setObjectName("back_Button")
        self.horizontalLayout.addWidget(self.back_Button)
        self.commit_Button = QtWidgets.QPushButton(Form)
        self.commit_Button.setObjectName("commit_Button")
        self.horizontalLayout.addWidget(self.commit_Button)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "订单审核"))
        self.label.setText(_translate("Form", "出库单号"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "序号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "商品名称"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "数量"))
        self.checkBox.setText(_translate("Form", "审核"))
        self.back_Button.setText(_translate("Form", "返回修改"))
        self.commit_Button.setText(_translate("Form", "确认提交"))


class ExStorageSheetReview():
    def __init__(self, storager_keeper, form_data):
        self.storager_keeper = storager_keeper
        self.form_data = form_data

        self.win = QtWidgets.QDialog()
        self.ui = Ui_Form()
        self.ui.setupUi(self.win)

        self.bind()
        self.load_data()

    def bind(self):
        self.ui.commit_Button.clicked.connect(lambda: self.commit())
        self.ui.back_Button.clicked.connect(lambda: self.cancel())

    def load_data(self):
        id = self.form_data['sheet']['id']
        # warehouse = self.form_data['sheet']['warehouse']
        # date = self.form_data['sheet']['date']
        details = self.form_data['details']

        self.ui.lineEdit.setText(id)
        self.ui.tableWidget.setRowCount(len(details))
        for i, detail in enumerate(details):
            self.ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(i + 1)))
            self.ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(detail['commodity_name']))
            self.ui.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(detail['number']))

    def commit(self):
        statue = self.ui.checkBox.checkState()
        # 检查是否审核
        if (statue == 0):
            QtWidgets.QMessageBox.information(None, '提示', '请审核后保证内容正确，点击审核，然后再提交！', QtWidgets.QMessageBox.Ok)
            return False
        else:
            # 提交出库总单
            id = self.form_data['sheet']['id']
            warehouse_name = self.form_data['sheet']['warehouse_name']
            date = str(self.form_data['sheet']['date'])
            statue, data = self.storager_keeper.add_ex_storage_sheet(id=id, warehouse_name=warehouse_name, date=date)
            if (statue == False):
                QtWidgets.QMessageBox.information(None, '提示', '提交出库总单出现错误，请重试！', QtWidgets.QMessageBox.Ok)
                return False

            # 提交出库详单
            for i, item in enumerate(self.form_data['details']):
                details_id = id + str(i+1).zfill(3)
                commodity_name = item['commodity_name']
                number = item['number']
                statue, data = self.storager_keeper.add_ex_storage_sheet_details(id=details_id, ex_storage_sheet_id=id,
                                                                                 commodity_name=commodity_name,
                                                                                 number=number)
                if(statue ==False):
                    # 回滚，即删除刚提交的订单
                    pass
                    return False
                else:
                    pass

            return self.win.accept()

    def cancel(self):
        return self.win.reject()
