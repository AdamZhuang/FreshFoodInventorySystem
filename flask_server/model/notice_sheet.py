from sqlalchemy.orm import sessionmaker
from flask_server.orm.basic_model import _NoticeSheet, _WareHouse, _NoticeSheetDetail, _Commodity, _User
from flask_server.public.error_code import *


class NoticeSheet(object):
    def __init__(self, engine):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def create_notice_sheet(self, code, warehouse_name, order_man_name, delivery_date, notice_date, statue,
                            handler_name):
        try:
            # 查询采购单是否存在
            notice_sheet = self.session.query(_NoticeSheet).filter(_NoticeSheet.code == code).first()
            if (notice_sheet != None):
                print("notice_sheet exist")
                return EXIST_ERROR
            # 查询仓库是否存在
            warehouse = self.session.query(_WareHouse).filter(_WareHouse.name == warehouse_name).first()
            if (warehouse == None):
                print("warehouse is not exist")
                return NOT_EXIST_ERROR
            # 查询用户是否存在
            order_man = self.session.query(_User).filter(_User.name == order_man_name).first()
            if (order_man == None):
                print("user is not exist")
                return NOT_EXIST_ERROR
            # 查询用户是否存在
            handler = self.session.query(_User).filter(_User.name == handler_name).first()
            if (handler == None):
                print("user is not exist")
                return NOT_EXIST_ERROR

            # 新建_OrderSheet对象
            new_notice_sheet = _NoticeSheet(code=code, warehouse_id=warehouse.id, order_man_id=order_man.id,
                                            delivery_date=delivery_date, notice_date=notice_date, statue=statue,
                                            handler_id=handler.id)
            # 添加到session:
            self.session.add(new_notice_sheet)
            # 返回commit情况（True or False）
            self.session.commit()
            # 返回成功标志
            return SUCCESS
        except Exception as e:
            e = str(e.args[0])
            print(e)
            return UNKNOWN_ERROR

    def get_all_notice_sheets(self):
        try:
            ret_dic = {'sheets': []}
            notice_sheets = self.session.query(_NoticeSheet).all()
            for notice_sheet in notice_sheets:
                warehouse = self.session.query(_WareHouse).filter(_WareHouse.id == notice_sheet.warehouse_id).first()
                order_man = self.session.query(_User).filter(_User.id == notice_sheet.order_man_id).first()
                handler = self.session.query(_User).filter(_User.id == notice_sheet.handler_id).first()
                ret_dic['sheets'].append({
                    'code': notice_sheet.code,
                    'warehouse_name': warehouse.name,
                    'order_man_name': order_man.name,
                    'delivery_date': str(notice_sheet.delivery_date),
                    'notice_date': str(notice_sheet.notice_date),
                    'statue': notice_sheet.statue,
                    'handler_name': handler.name,
                })
            return ret_dic
        except Exception as e:
            print(e)
            return UNKNOWN_ERROR

    def get_notice_sheets_by_order_man_name(self, order_man_name):
        try:
            ret_dic = {'sheets': []}
            temp = self.get_all_notice_sheets()
            for item in temp['sheets']:
                if (item['order_man_name'] == order_man_name):
                    ret_dic['sheets'].append(item)
            return ret_dic
        except Exception as e:
            print(e)
            return UNKNOWN_ERROR

    def close(self):
        self.session.close()
