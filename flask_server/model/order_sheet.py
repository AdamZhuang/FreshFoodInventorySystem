from sqlalchemy.orm import sessionmaker
from flask_server.orm.basic_model import _OrderSheet, _WareHouse, _OrderSheetDetail, _Commodity, _User, _NoticeSheet
from flask_server.public.error_code import *


class OrderSheet(object):
    def __init__(self, engine):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def create_order_sheet(self, code, notice_sheet_code, warehouse_name, order_man_name, delivery_date, order_date,
                           statue, handler_name):
        try:
            # 查询采购单是否存在
            order_sheet = self.session.query(_OrderSheet).filter(_OrderSheet.code == code).first()
            if (order_sheet != None):
                print("order_sheet exist")
                return EXIST_ERROR
            # 查询采购单是否存在
            notice_sheet = self.session.query(_NoticeSheet).filter(_NoticeSheet.code == notice_sheet_code).first()
            if (notice_sheet == None):
                print("notice_sheet is not exist")
                return NOT_EXIST_ERROR
            # 查询仓库是否存在
            warehouse = self.session.query(_WareHouse).filter(_WareHouse.name == warehouse_name).first()
            if (warehouse == None):
                print("warehouse is not exist")
                return NOT_EXIST_ERROR
            # 查询采购员是否存在
            order_man = self.session.query(_User).filter(_User.name == order_man_name).first()
            if (order_man == None):
                print("order_man is not exist")
                return NOT_EXIST_ERROR
            # 查询经手人是否存在
            handler = self.session.query(_User).filter(_User.name == handler_name).first()
            if (handler == None):
                print("handler is not exist")
                return NOT_EXIST_ERROR

            # 新建_OrderSheet对象
            new_order_sheet = _OrderSheet(code=code, notice_sheet_id=notice_sheet.id,
                                          warehouse_id=warehouse.id, order_man_id=order_man.id,
                                          delivery_date=delivery_date, order_date=order_date, statue=statue,
                                          handler_id=handler.id)
            notice_sheet.statue = '采购中'
            # 添加到session:
            self.session.add(new_order_sheet)
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

    def get_order_sheets(self, order_man_name):
        try:
            ret_dic = {'sheets': []}
            order_sheets = self.session.query(_OrderSheet).all()
            for order_sheet in order_sheets:
                order_man = self.session.query(_User).filter(_User.id == order_sheet.order_man_id).first()
                if (order_man.name != order_man_name):
                    continue
                warehouse = self.session.query(_WareHouse).filter(_WareHouse.id == order_sheet.warehouse_id).first()
                handler = self.session.query(_User).filter(_User.id == order_sheet.handler_id).first()
                notice_sheet = self.session.query(_NoticeSheet).filter(
                    _NoticeSheet.id == order_sheet.notice_sheet_id).first()
                ret_dic['sheets'].append({
                    'code': order_sheet.code,
                    'notice_sheet_code': notice_sheet.code,
                    'warehouse_name': warehouse.name,
                    'order_man_name': order_man.name,
                    'delivery_date': str(order_sheet.delivery_date),
                    'order_date': str(order_sheet.order_date),
                    'statue': order_sheet.statue,
                    'handler_name': handler.name,
                })

            return ret_dic
        except Exception as e:
            print(e)
            return UNKNOWN_ERROR

    def get_order_sheets_by_warehouse_name(self, warehouse_name):
        try:
            ret_dic = {'sheets': []}
            order_sheets = self.session.query(_OrderSheet).all()
            warehouse = self.session.query(_WareHouse).filter(_WareHouse.name == warehouse_name).first()
            for order_sheet in order_sheets:
                if (order_sheet.warehouse_id != warehouse.id):
                    continue
                handler = self.session.query(_User).filter(_User.id == order_sheet.handler_id).first()
                ret_dic['sheets'].append({
                    'code': order_sheet.code,
                    'warehouse_name': warehouse.name,
                    'delivery_date': str(order_sheet.delivery_date),
                    'order_date': str(order_sheet.order_date),
                    'statue': order_sheet.statue,
                    'handler_name': handler.name,
                })

            return ret_dic
        except Exception as e:
            print(e)
            return UNKNOWN_ERROR


    def change_order_sheet_statue(self, order_sheet_code, statue):
        try:
            # 查询采购单是否存在
            order_sheet = self.session.query(_OrderSheet).filter(_OrderSheet.code == order_sheet_code).first()
            if (order_sheet == None):
                print("order_sheet is not exist")
                return NOT_EXIST_ERROR
            # 修改
            order_sheet.statue = statue
            # 查询通知单
            notice_sheet = self.session.query(_NoticeSheet).filter(_NoticeSheet.id == order_sheet.notice_sheet_id).first()
            if (notice_sheet == None):
                print("notice_sheet is not exist")
                return NOT_EXIST_ERROR
            notice_sheet.statue = statue
            # commit
            self.session.commit()
            return SUCCESS
        except Exception as e:
            e = str(e.args[0])
            if ('a foreign key constraint fails' in e):
                return FOREIGNKEY_ERROR
            else:
                return UNKNOWN_ERROR

    def close(self):
        try:
            self.session.close()
            return SUCCESS
        except Exception as e:
            print(e)
            return SESSION_CLOSE_ERROR
