from sqlalchemy.orm import sessionmaker
from flask_server.orm.basic_model import _InStorageSheet, _WareHouse, _InStorageSheetDetail, _OrderSheet, _User, \
    _NoticeSheet
from flask_server.public.error_code import *


class InStorageSheet(object):
    def __init__(self, engine):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def create_in_storage_sheet(self, code, order_sheet_code, warehouse_name, in_storage_date, handler_name):
        try:
            in_storage_sheet = self.session.query(_InStorageSheet).filter(_InStorageSheet.code == code).first()
            if (in_storage_sheet != None):
                print("exist")
                return EXIST_ERROR
            order_sheet = self.session.query(_OrderSheet).filter(_OrderSheet.code == order_sheet_code).first()
            if (order_sheet == None):
                print("order_sheet does not exist")
                return NOT_EXIST_ERROR
            warehouse = self.session.query(_WareHouse).filter(_WareHouse.name == warehouse_name).first()
            if (warehouse == None):
                print("warehouse does not exist")
                return NOT_EXIST_ERROR
            handler = self.session.query(_User).filter(_User.name == handler_name).first()
            if (handler == None):
                print("handler does not exist")
                return NOT_EXIST_ERROR

            # 更改通知单和采购单状态为已入库
            order_sheet.statue = '已入库'
            notice_sheet = self.session.query(_NoticeSheet).filter(
                _NoticeSheet.id == order_sheet.notice_sheet_id).first()
            notice_sheet.statue = '已入库'

            new_in_storage_sheet = _InStorageSheet(code=code, order_sheet_id=order_sheet.id, warehouse_id=warehouse.id,
                                                   in_storage_date=in_storage_date, handler_id=handler.id)
            # 添加到session:
            self.session.add(new_in_storage_sheet)
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

    def delete_in_storage_sheet(self, id):
        try:
            # 查询入库单是否存在
            in_storage_sheet = self.session.query(_InStorageSheet).filter(_InStorageSheet.id == id).first()
            if (in_storage_sheet == None):
                print("no exist")
                return NOT_EXIST_ERROR

            # 查询是否有入库详单，如果有则删除
            in_storage_sheet_details = self.session.query(_InStorageSheetDetail).filter(
                _InStorageSheetDetail.in_storage_sheet_id == id).all()
            for item in in_storage_sheet_details:
                self.session.delete(item)
            # 删除入库总单
            self.session.delete(in_storage_sheet)
            # 提交
            self.session.commit()
            # 返回成功标志
            return SUCCESS
        except Exception as e:
            e = str(e.args[0])
            if ('a foreign key constraint fails' in e):
                return FOREIGNKEY_ERROR
            else:
                return UNKNOWN_ERROR

    def change_in_storage_sheet(self, origin_id, dest_id, dest_warehouse_name, dest_date):
        try:
            # 查询入库单是否存在
            in_storage_sheet = self.session.query(_InStorageSheet).filter(_InStorageSheet.id == origin_id).first()
            if (in_storage_sheet == None):
                print("no exist")
                return False
            # 查询仓库是否存在
            warehouse = self.session.query(_WareHouse).filter(_WareHouse.name == dest_warehouse_name).first()
            if (warehouse == None):
                print("no exist")
                return False
            # 修改
            in_storage_sheet.id = dest_id
            in_storage_sheet.warehouse_id = warehouse.id
            in_storage_sheet.date = dest_date
            # commit
            self.session.commit()
            return SUCCESS
        except Exception as e:
            e = str(e.args[0])
            if ('a foreign key constraint fails' in e):
                return FOREIGNKEY_ERROR
            else:
                return UNKNOWN_ERROR

    # def get_in_storage_sheets(self, warehouse_name):
    #     try:
    #         ret_data = {}
    #         warehouse = self.session.query(_WareHouse).filter(_WareHouse.name == warehouse_name).first()
    #         if (warehouse == None):
    #             return NOT_EXIST_ERROR
    #         in_storage_sheets = self.session.query(_InStorageSheet).filter(
    #             _InStorageSheet.warehouse_id == warehouse.id).all()
    #         ret_data['sheets'] = []
    #         for in_storage_sheet in in_storage_sheets:
    #             warehouse = self.session.query(_WareHouse).filter(
    #                 _WareHouse.id == in_storage_sheet.warehouse_id).first()
    #             handler = self.session.query(_User).filter(_User.id == in_storage_sheet.handler_id).first()
    #             ret_data['sheets'].append({'code': in_storage_sheet.code, 'warehouse_name': warehouse.name,
    #                                        'in_storage_date': str(in_storage_sheet.in_storage_date),
    #                                        'handler_name': handler.name})
    #         return ret_data
    #     except Exception as e:
    #         print(e)
    #         return UNKNOWN_ERROR

    def get_in_storage_sheets_by_warehouse_name(self, warehouse_name):
        try:
            ret_data = {}
            warehouse = self.session.query(_WareHouse).filter(_WareHouse.name == warehouse_name).first()
            if (warehouse == None):
                return NOT_EXIST_ERROR
            in_storage_sheets = self.session.query(_InStorageSheet).filter(
                _InStorageSheet.warehouse_id == warehouse.id).all()
            ret_data['sheets'] = []
            for in_storage_sheet in in_storage_sheets:
                warehouse = self.session.query(_WareHouse).filter(
                    _WareHouse.id == in_storage_sheet.warehouse_id).first()
                handler = self.session.query(_User).filter(_User.id == in_storage_sheet.handler_id).first()
                ret_data['sheets'].append({'code': in_storage_sheet.code, 'warehouse_name': warehouse.name,
                                           'in_storage_date': str(in_storage_sheet.in_storage_date),
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
