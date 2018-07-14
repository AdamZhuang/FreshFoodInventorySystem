# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_notice_sheet_review.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(726, 417)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.id_lineEdit = QtWidgets.QLineEdit(Form)
        self.id_lineEdit.setEnabled(False)
        self.id_lineEdit.setObjectName("id_lineEdit")
        self.horizontalLayout.addWidget(self.id_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.warehouse_lineEdit = QtWidgets.QLineEdit(Form)
        self.warehouse_lineEdit.setEnabled(False)
        self.warehouse_lineEdit.setObjectName("warehouse_lineEdit")
        self.horizontalLayout_3.addWidget(self.warehouse_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.man_lineEdit = QtWidgets.QLineEdit(Form)
        self.man_lineEdit.setEnabled(False)
        self.man_lineEdit.setObjectName("man_lineEdit")
        self.horizontalLayout_4.addWidget(self.man_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
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
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_2.addWidget(self.checkBox)
        self.back_Button = QtWidgets.QPushButton(Form)
        self.back_Button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.back_Button.setObjectName("back_Button")
        self.horizontalLayout_2.addWidget(self.back_Button)
        self.commit_Button = QtWidgets.QPushButton(Form)
        self.commit_Button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.commit_Button.setObjectName("commit_Button")
        self.horizontalLayout_2.addWidget(self.commit_Button)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "订货通知单审核"))
        self.label.setText(_translate("Form", "订货通知单单号："))
        self.label_2.setText(_translate("Form", "仓库："))
        self.label_3.setText(_translate("Form", "采购员："))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "序号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "商品名称"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "数量"))
        self.checkBox.setText(_translate("Form", "审核"))
        self.back_Button.setText(_translate("Form", "返回修改"))
        self.commit_Button.setText(_translate("Form", "提交"))


class AddNoticeSheetReview():
    def __init__(self, manager, form_data):
        self.manager = manager
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
        warehouse_name = self.form_data['sheet']['warehouse_name']
        order_man_name = self.form_data['sheet']['order_man_name']
        self.ui.id_lineEdit.setText(id)
        self.ui.warehouse_lineEdit.setText(warehouse_name)
        self.ui.man_lineEdit.setText(order_man_name)

        self.ui.tableWidget.setRowCount(len(self.form_data['details']))
        for i, item in enumerate(self.form_data['details']):
            self.ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(i + 1)))
            self.ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(item['commodity_name']))
            self.ui.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(item['number']))

    def commit(self):
        statue = self.ui.checkBox.checkState()
        # 检查是否审核
        if (statue == 0):
            QtWidgets.QMessageBox.information(None, '提示', '请审核后保证内容正确，点击审核，然后再提交！', QtWidgets.QMessageBox.Ok)
            return False
        else:
            # 提交采购单总单
            id = self.form_data['sheet']['id']
            warehouse_name = self.form_data['sheet']['warehouse_name']
            order_man_name = self.form_data['sheet']['order_man_name']
            date = str(self.form_data['sheet']['date'])
            statue = self.form_data['sheet']['statue']
            handler_name = self.form_data['sheet']['handler_name']

            statue, data = self.manager.add_notice_sheet(id=id, warehouse_name=warehouse_name,
                                                         order_man_name=order_man_name, date=date,
                                                         statue=statue, handler_name=handler_name)
            if (statue == False):
                QtWidgets.QMessageBox.information(None, '提示', '提交出现错误，请重试！', QtWidgets.QMessageBox.Ok)
                return False

            for i, item in enumerate(self.form_data['details']):
                notice_sheet_details_id = id + str(i + 1).zfill(3)
                notice_sheet_id = id
                commodity_name = item['commodity_name']
                number = item['number']

                statue, data = self.manager.add_notice_sheet_details(id=notice_sheet_details_id, notice_sheet_id=notice_sheet_id,
                                                                    commodity_name=commodity_name, number=number)
                if (statue == False):
                    # 回滚，即删除刚提交的订单
                    pass
                    return False
                else:
                    pass

            return self.win.accept()

    def cancel(self):
        return self.win.reject()
