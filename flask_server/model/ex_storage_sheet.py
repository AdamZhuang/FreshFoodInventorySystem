from sqlalchemy.orm import sessionmaker
from flask_server.orm.basic_model import _ExStorageSheet, _WareHouse, _ExStorageSheetDetail, _User
from flask_server.public.error_code import *


class ExStorageSheet(object):
    def __init__(self, engine):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def create_ex_storage_sheet(self, code, warehouse_name, date, handler_name):
        try:
            # 查询出库单是否存在
            ex_storage_sheet = self.session.query(_ExStorageSheet).filter(_ExStorageSheet.code == code).first()
            if (ex_storage_sheet != None):
                print("exist")
                return EXIST_ERROR
            # 查询仓库是否存在
            warehouse = self.session.query(_WareHouse).filter(_WareHouse.name == warehouse_name).first()
            if (warehouse == None):
                print("no exist")
                return NOT_EXIST_ERROR
            handler = self.session.query(_User).filter(_User.name == handler_name).first()
            if (handler == None):
                print("no exist")
                return NOT_EXIST_ERROR

            # 新建_ExStorageSheet对象
            new_ex_storage_sheet = _ExStorageSheet(code=code, warehouse_id=warehouse.id, date=date,
                                                   handler_id=handler.id)
            # 添加到session:
            self.session.add(new_ex_storage_sheet)
            # 返回commit情况（True or False）
            self.session.commit()
            # 返回成功标志
            return SUCCESS
        except Exception as e:
            e = str(e.args[0])
            if ('a foreign key constraint fails' in e):
                return FOREIGNKEY_ERROR
            else:
                return UNKNOWN_ERROR

    # def delete_ex_storage_sheet(self, ex_storage_sheet_id):
    #     try:
    #         # 查询出库单是否存在
    #         ex_storage_sheet = self.session.query(_ExStorageSheet).filter(
    #             _ExStorageSheet.id == ex_storage_sheet_id).first()
    #         if (ex_storage_sheet == None):
    #             print("no exist")
    #             return False
    #
    #         # 先删除相关入库详单
    #         ex_storage_sheet_details = self.session.query(_ExStorageSheetDetail).filter(
    #             _ExStorageSheetDetail.id == ex_storage_sheet_id).all
    #         for item in ex_storage_sheet_details:
    #             self.session.delete(item)
    #         # 删除总单:
    #         self.session.delete(ex_storage_sheet)
    #         # 提交
    #         self.session.commit()
    #         # 返回成功标志
    #         return SUCCESS
    #     except Exception as e:
    #         e = str(e.args[0])
    #         if ('a foreign key constraint fails' in e):
    #             return FOREIGNKEY_ERROR
    #         else:
    #             return UNKNOWN_ERROR
    #
    # def change_ex_storage_sheet(self, origin_id, dest_id, dest_warehouse_name, dest_date):
    #     try:
    #         # 查询出库单是否存在
    #         ex_storage_sheet = self.session.query(_ExStorageSheet).filter(_ExStorageSheet.id == origin_id).first()
    #         if (ex_storage_sheet == None):
    #             print("no exist")
    #             return False
    #         # 查询仓库是否存在
    #         warehouse = self.session.query(_WareHouse).filter(_WareHouse.name == dest_warehouse_name).first()
    #         if (warehouse == None):
    #             print("no exist")
    #             return False
    #         # 修改
    #         ex_storage_sheet.id = dest_id
    #         ex_storage_sheet.warehouse_id = warehouse.id
    #         ex_storage_sheet.date = dest_date
    #         # commit
    #         self.session.commit()
    #         return SUCCESS
    #     except Exception as e:
    #         e = str(e.args[0])
    #         if ('a foreign key constraint fails' in e):
    #             return FOREIGNKEY_ERROR
    #         else:
    #             return UNKNOWN_ERROR

    def get_all_ex_storage_sheets_by_warehouse(self, warehouse_name):
        try:
            ret_data = {}
            ex_storage_sheets = self.session.query(_ExStorageSheet).all()
            ret_data['sheets'] = []
            for item in ex_storage_sheets:
                warehouse = self.session.query(_WareHouse).filter(_WareHouse.id == item.warehouse_id).first()
                handler = self.session.query(_User).filter(_User.id == item.handler_id).first()
                ret_data['sheets'].append({'code': item.code, 'warehouse_name': warehouse.name, 'date': str(item.date),
                                           'handler_name': handler.name})
            return ret_data
        except Exception as e:
            print(e)
            return UNKNOWN_ERROR

    def close(self):
        try:
            self.session.close()
            return SUCCESS
        except Exception as e:
            print(e)
            return SESSION_CLOSE_ERROR


if __name__ == '__main__':
    from sqlalchemy import create_engine
    import datetime

    engine = create_engine("mysql+pymysql://root:Zxw11071205@127.0.0.1:3306/stock_control",
                           encoding='utf8', echo=False, max_overflow=100)
    data_model = ExStorageSheet(engine)

    # data_model.create_ex_storage_sheet('2015211921', '1', datetime.datetime.now())
    # statue = data_model.delete_ex_storage_sheet('20152119201111')
    # print(statue)
    # data_model.change_ex_storage_sheet('20152119201', '20152119201111','1',datetime.datetime.now())
    # sheets = data_model.get_all_ex_storage_sheet()
    # print(sheet for sheet in data_model.get_all_ex_storage_sheet())


    # data_model.commit()
    data_model.close()
