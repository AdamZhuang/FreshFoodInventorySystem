# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_notice_sheet.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
import hashlib
import random
from client.ui.manager_children.add_notice_sheet_details import AddNoticeSheetDetails
from client.ui.manager_children.add_notice_sheet_review import AddNoticeSheetReview


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(728, 483)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.code_lineEdit = QtWidgets.QLineEdit(Form)
        self.code_lineEdit.setObjectName("code_lineEdit")
        self.horizontalLayout_3.addWidget(self.code_lineEdit)
        self.gen_code_Button = QtWidgets.QPushButton(Form)
        self.gen_code_Button.setObjectName("gen_id_Button")
        self.horizontalLayout_3.addWidget(self.gen_code_Button)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.warehouse_comboBox = QtWidgets.QComboBox(Form)
        self.warehouse_comboBox.setObjectName("warehouse_comboBox")
        self.horizontalLayout_2.addWidget(self.warehouse_comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.order_man_comboBox = QtWidgets.QComboBox(Form)
        self.order_man_comboBox.setObjectName("order_man_comboBox")
        self.horizontalLayout_4.addWidget(self.order_man_comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(Form)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.horizontalLayout_5.addWidget(self.dateTimeEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.add_Button = QtWidgets.QPushButton(Form)
        self.add_Button.setObjectName("add_Button")
        self.horizontalLayout.addWidget(self.add_Button)
        self.delete_Button = QtWidgets.QPushButton(Form)
        self.delete_Button.setObjectName("delete_Button")
        self.horizontalLayout.addWidget(self.delete_Button)
        self.commit_Button = QtWidgets.QPushButton(Form)
        self.commit_Button.setObjectName("commit_Button")
        self.horizontalLayout.addWidget(self.commit_Button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(9)
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tableWidget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "填写订货通知单"))
        self.label_2.setText(_translate("Form", "订货通知单编号："))
        self.gen_code_Button.setText(_translate("Form", "生成单号"))
        self.label_3.setText(_translate("Form", "选择仓库："))
        self.label_4.setText(_translate("Form", "选择采购人员："))
        self.label_5.setText(_translate("Form", "到货时间："))
        self.label.setText(_translate("Form", "详单操作："))
        self.add_Button.setText(_translate("Form", "添加一行"))
        self.delete_Button.setText(_translate("Form", "删除选中行"))
        self.commit_Button.setText(_translate("Form", "提交"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "序号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "商品编号"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "商品名"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "商品类型"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "计量单位"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "商品规格"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "供应商名称"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Form", "购买数量"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("Form", "购买经费（单位：元）"))


class AddNoticeSheet(object):
    def __init__(self, manager):
        self.manager = manager

        self.win = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.win)

        self.adjust_ui()
        self.bind()
        self.load_data()

        self.notice_details = []

    def adjust_ui(self):
        self.ui.code_lineEdit.setEnabled(False)
        self.ui.dateTimeEdit.setDisplayFormat("yyyy-MM-dd")
        # self.ui.dateTimeEdit.setTime()
        self.ui.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.ui.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

    def bind(self):
        self.ui.gen_code_Button.clicked.connect(lambda: self.gen_code())
        self.ui.add_Button.clicked.connect(lambda: self.add_details())
        self.ui.delete_Button.clicked.connect(lambda: self.delete_details())
        self.ui.commit_Button.clicked.connect(lambda: self.commit())

    def load_data(self):
        statue, data = self.manager.get_all_warehouses()
        if (statue == True):
            self.ui.warehouse_comboBox.clear()
            for item in data['warehouses']:
                self.ui.warehouse_comboBox.addItem(str(item['name']))
        statue, data = self.manager.get_all_order_man()
        if (statue == True):
            self.ui.order_man_comboBox.clear()
            for item in data['users']:
                self.ui.order_man_comboBox.addItem(str(item['name']))
        else:
            QtWidgets.QMessageBox.information(None, '提示', '载入数据失败', QtWidgets.QMessageBox.Ok)

    def refresh(self):
        self.load_data()

    def gen_code(self):
        # 生成id
        cur_time = datetime.datetime.now()
        t = cur_time.strftime("%Y%m%d%H%M%S")
        username = self.manager.name
        u = hashlib.md5(username.encode("utf8")).hexdigest()[:10]
        r = str(random.randint(0, 9))
        code = t + u + r

        self.ui.code_lineEdit.setText(code)

    def add_details(self):
        dialog = AddNoticeSheetDetails(self.manager)
        statue = dialog.win.exec_()
        if (statue == 1):
            data = dialog.ret_data
            dialog.win.destroy()
            self.notice_details.append(data)
            self.update_table()
        else:
            pass

    def delete_details(self):
        try:
            items = self.ui.tableWidget.selectedItems()
            if (items == []):
                QtWidgets.QMessageBox.information(None, '提示', '请选择要删除的行！', QtWidgets.QMessageBox.Ok)
                return False

            index = items[0].text()
            for i, item in enumerate(self.notice_details):
                if (index == str(i + 1)):
                    self.notice_details.pop(i)

            self.update_table()
        except:
            QtWidgets.QMessageBox.information(None, '提示', '出现错误，请重试！', QtWidgets.QMessageBox.Ok)

    def commit(self):
        if (self.ui.code_lineEdit.text() == ''):
            QtWidgets.QMessageBox.information(None, '提示', '请点击按钮生成订货通知单号再提交！', QtWidgets.QMessageBox.Ok)
            return False

        if (self.notice_details == []):
            QtWidgets.QMessageBox.information(None, '提示', '请检查详单是否填完整再提交！', QtWidgets.QMessageBox.Ok)
            return False

        notice_sheet_code = self.ui.code_lineEdit.text()
        warehouse_name = self.ui.warehouse_comboBox.currentText()
        order_man_name = self.ui.order_man_comboBox.currentText()
        delivery_date = str(self.ui.dateTimeEdit.text())
        notice_date = str(datetime.datetime.now())
        statue = '未处理'
        handler_name = self.manager.name

        statue, data = self.manager.add_notice_sheet(code=notice_sheet_code, warehouse_name=warehouse_name,
                                                     order_man_name=order_man_name, delivery_date=delivery_date,
                                                     notice_date=notice_date, statue=statue, handler_name=handler_name)
        if (statue == True):
            for notice_sheet_detail in self.notice_details:
                statue, data = self.manager.add_notice_sheet_details(notice_sheet_code=notice_sheet_code,
                                                                     commodity_code=notice_sheet_detail['code'],
                                                                     number=notice_sheet_detail['number'],
                                                                     price=notice_sheet_detail['price'])
                if(statue == False):
                    QtWidgets.QMessageBox.information(None, '提示', '创建订货详单失败！', QtWidgets.QMessageBox.Ok)
                    return False

            QtWidgets.QMessageBox.information(None, '提示', '提交成功！', QtWidgets.QMessageBox.Ok)
            self.ui.code_lineEdit.setText('')
            self.notice_details.clear()
            self.update_table()
        else:
            QtWidgets.QMessageBox.information(None, '提示', '创建订货通知单失败！', QtWidgets.QMessageBox.Ok)
            return False



    def update_table(self):
        self.ui.tableWidget.setRowCount(len(self.notice_details))
        for i, item in enumerate(self.notice_details):
            self.ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(i + 1)))
            self.ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(item['code'])))
            self.ui.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(item['name'])))
            self.ui.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str(item['type'])))
            self.ui.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(str(item['unit'])))
            self.ui.tableWidget.setItem(i, 5, QtWidgets.QTableWidgetItem(str(item['specification'])))
            self.ui.tableWidget.setItem(i, 6, QtWidgets.QTableWidgetItem(str(item['supplier_name'])))
            self.ui.tableWidget.setItem(i, 7, QtWidgets.QTableWidgetItem(str(item['number'])))
            self.ui.tableWidget.setItem(i, 8, QtWidgets.QTableWidgetItem(str(item['price'])))


if __name__ == '__main__':
    import sys
    from client.model.manager import Manager

    manager = Manager('http://127.0.0.1:5000', '1', '1', '经理')
    if (manager.login()):
        app = QtWidgets.QApplication(sys.argv)
        page = AddNoticeSheet(manager)
        page.win.show()
        sys.exit(app.exec_())
    else:
        print(False)
