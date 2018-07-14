# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_order_sheet.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
import hashlib
import random


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(833, 466)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setMinimumSize(QtCore.QSize(200, 0))
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        self.query_lineEdit = QtWidgets.QLineEdit(Form)
        self.query_lineEdit.setObjectName("query_lineEdit")
        self.horizontalLayout.addWidget(self.query_lineEdit)
        self.query_Button = QtWidgets.QPushButton(Form)
        self.query_Button.setObjectName("query_Button")
        self.horizontalLayout.addWidget(self.query_Button)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.add_by_order_shhet_Button = QtWidgets.QPushButton(Form)
        self.add_by_order_shhet_Button.setObjectName("add_by_order_shhet_Button")
        self.horizontalLayout_3.addWidget(self.add_by_order_shhet_Button)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.order_id_lineEdit = QtWidgets.QLineEdit(Form)
        self.order_id_lineEdit.setEnabled(False)
        self.order_id_lineEdit.setObjectName("order_id_lineEdit")
        self.horizontalLayout_4.addWidget(self.order_id_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.delivery_date_lineEdit = QtWidgets.QLineEdit(Form)
        self.delivery_date_lineEdit.setEnabled(False)
        self.delivery_date_lineEdit.setObjectName("delivery_date_lineEdit")
        self.horizontalLayout_5.addWidget(self.delivery_date_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.warehouse_lineEdit = QtWidgets.QLineEdit(Form)
        self.warehouse_lineEdit.setEnabled(False)
        self.warehouse_lineEdit.setObjectName("warehouse_lineEdit")
        self.horizontalLayout_6.addWidget(self.warehouse_lineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_7.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.verticalLayout_3.addWidget(self.tableWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.commit_Button = QtWidgets.QPushButton(Form)
        self.commit_Button.setObjectName("commit_Button")
        self.horizontalLayout_2.addWidget(self.commit_Button)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "添加采购单"))
        self.label.setText(_translate("Form", "选择订货通知单单号（未处理）："))
        self.query_Button.setText(_translate("Form", "查询"))
        self.add_by_order_shhet_Button.setText(_translate("Form", "根据订货通知单填写采购单"))
        self.label_2.setText(_translate("Form", "采购单id："))
        self.label_5.setText(_translate("Form", "交货时间："))
        self.label_4.setText(_translate("Form", "购买至仓库："))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "商品编号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "商品名称"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "商品类型"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "计量单位"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "商品规格"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "供应商"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "采购数量"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Form", "采购金额（单位：元）"))
        self.commit_Button.setText(_translate("Form", "提交采购单"))


class AddOrderSheet(object):
    def __init__(self, order_man):
        self.order_man = order_man

        self.win = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.win)

        self.load_data()
        self.adjust_ui()
        self.bind()

    def load_data(self):
        statue, data = self.order_man.get_notice_sheets_by_order_man_name(self.order_man.name)
        self.sheets = data['sheets']
        if (statue == True):
            self.ui.comboBox.clear()
            for item in data['sheets']:
                if (item['statue'] == '未处理'):
                    self.ui.comboBox.addItem(item['code'])

    def adjust_ui(self):
        self.ui.tableWidget.resizeColumnsToContents()

    def bind(self):
        self.ui.add_by_order_shhet_Button.clicked.connect(lambda: self.gen_order_sheet())
        self.ui.commit_Button.clicked.connect(lambda: self.commit())
        # self.ui.query_Button.clicked.connect(lambda: self.query())

    def gen_order_sheet(self):
        notice_sheet_code = self.ui.comboBox.currentText()

        self.notice_sheet_code = notice_sheet_code

        for sheet in self.sheets:
            if (sheet['code'] == notice_sheet_code):
                self.ui.order_id_lineEdit.setText(self.gen_code())
                self.ui.warehouse_lineEdit.setText(sheet['warehouse_name'])
                self.ui.delivery_date_lineEdit.setText(sheet['delivery_date'])

        statue, data = self.order_man.get_notice_sheet_details(notice_sheet_code)
        if (statue == True):
            self.ui.tableWidget.setRowCount(len(data['details']))
            for i, item in enumerate(data['details']):
                self.ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(item['commodity_code'])))
                self.ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(item['commodity_name'])))
                self.ui.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(item['commodity_type'])))
                self.ui.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str(item['commodity_unit'])))
                self.ui.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(str(item['commodity_specification'])))
                self.ui.tableWidget.setItem(i, 5, QtWidgets.QTableWidgetItem(str(item['commodity_supplier'])))
                self.ui.tableWidget.setItem(i, 6, QtWidgets.QTableWidgetItem(str(item['number'])))
                self.ui.tableWidget.setItem(i, 7, QtWidgets.QTableWidgetItem(str(item['price'])))
        else:
            QtWidgets.QMessageBox.information(None, '提示', '出现错误！', QtWidgets.QMessageBox.Ok)

    def gen_code(self):
        # 生成id
        cur_time = datetime.datetime.now()
        t = cur_time.strftime("%Y%m%d%H%M%S")
        username = self.order_man.name
        u = hashlib.md5(username.encode("utf8")).hexdigest()[:10]
        r = str(random.randint(0, 9))
        code = t + u + r
        return code

    def commit(self):
        try:
            code = self.ui.order_id_lineEdit.text()
            notice_sheet_code = self.notice_sheet_code
            order_man_name = self.order_man.name
            warehouse_name = self.ui.warehouse_lineEdit.text()
            order_date = str(datetime.datetime.now())
            delivery_date = self.ui.delivery_date_lineEdit.text()
            statue = '未处理'
            handler_name = self.order_man.name

            statue, date = self.order_man.add_order_sheet(code=code, notice_sheet_code=notice_sheet_code,
                                                          order_man_name=order_man_name, warehouse_name=warehouse_name,
                                                          delivery_date=delivery_date, order_date=order_date,
                                                          statue=statue, handler_name=handler_name)
            if (statue == True):
                for i in range(self.ui.tableWidget.rowCount()):
                    order_sheet_code = code
                    commodity_code = self.ui.tableWidget.item(i, 0).text()
                    number = self.ui.tableWidget.item(i, 6).text()
                    price = self.ui.tableWidget.item(i, 7).text()

                    statue, data = self.order_man.add_order_sheet_details(order_sheet_code, commodity_code, number, price)
                    if(statue == True):
                        pass
                    else:
                        QtWidgets.QMessageBox.information(None, '提示', '提交详单出现错误！', QtWidgets.QMessageBox.Ok)
                        return False

                QtWidgets.QMessageBox.information(None, '提示', '提交成功！！', QtWidgets.QMessageBox.Ok)
                self.load_data()
                # self.ui.tableWidget.clear()
                self.ui.tableWidget.setRowCount(0)
                self.ui.order_id_lineEdit.setText('')
                self.ui.warehouse_lineEdit.setText('')
                self.ui.warehouse_lineEdit.setText('')
                self.ui.delivery_date_lineEdit.setText('')
            else:
                QtWidgets.QMessageBox.information(None, '提示', '提交总单出现错误！', QtWidgets.QMessageBox.Ok)
                return False
        except Exception as e:
            print(e)

    def query(self):
        pass

    def refresh(self):
        self.load_data()


if __name__ == '__main__':
    import sys
    from client.model.order_man import OrderMan

    app = QtWidgets.QApplication(sys.argv)
    order_man = OrderMan('http://127.0.0.1:5000', '2', '2', '采购部')
    if (order_man.login()):
        page = AddOrderSheet(order_man)
        page.win.show()
    else:
        print('error')

    sys.exit(app.exec_())
