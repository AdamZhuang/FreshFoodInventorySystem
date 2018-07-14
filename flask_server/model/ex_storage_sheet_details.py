from sqlalchemy.orm import sessionmaker
from flask_server.orm.basic_model import _ExStorageSheet, _ExStorageSheetDetail, _Commodity, _CommodityStatic, \
    _WareHouse
from flask_server.public.error_code import *


class ExStorageSheetDetails(object):
    def __init__(self, engine):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def create_ex_storage_sheet_detail(self, ex_storage_sheet_code, commodity_code, number):
        try:
            # 查询出库总单是否存在
            ex_storage_sheet = self.session.query(_ExStorageSheet).filter(
                _ExStorageSheet.code == ex_storage_sheet_code).first()
            if (ex_storage_sheet == None):
                print("ex_storage_sheet does not exist")
                return NOT_EXIST_ERROR
            # 查询商品是否存在
            commodity = self.session.query(_Commodity).filter(_Commodity.code == commodity_code).first()
            if (commodity == None):
                print("commodity does not exist")
                return NOT_EXIST_ERROR
            # 查询库存表
            storage_sheet = self.session.query(_CommodityStatic).filter(
                _CommodityStatic.commodity_id == commodity.id and _WareHouse.id == ex_storage_sheet.warehouse_id).first()
            # 判断是否存在
            if (storage_sheet == None):
                return NOT_EXIST_ERROR
            else:
                if (storage_sheet.number - int(number) < 0):
                    return NOT_ENOUGH_NUMBER
                else:
                    # 更新库存表
                    storage_sheet.number = storage_sheet.number - int(number)

            # 满足以上情况，新建_ExStorageSheetDetails对象
            new_ex_storage_sheet_details = _ExStorageSheetDetail(ex_storage_sheet_id=ex_storage_sheet.warehouse_id,
                                                                 commodity_id=commodity.id, number=number)
            # 添加到session:
            self.session.add(new_ex_storage_sheet_details)
            # commit
            self.session.commit()
            # 返回成功标志
            return SUCCESS
        except Exception as e:
            e = str(e.args[0])
            print(e)
            if ('a foreign key constraint fails' in e):
                return FOREIGNKEY_ERROR
            else:
                return UNKNOWN_ERROR

    def delete_ex_storage_sheet_detail(self, id):
        try:
            # 查询出库详单是否存在
            ex_storage_sheet_details = self.session.query(_ExStorageSheetDetail).filter(
                _ExStorageSheetDetail.id == id).first()
            if (ex_storage_sheet_details == None):
                print("ex_storage_sheet_details does not exist")
                return NOT_EXIST_ERROR
            # 添加到session:
            self.session.delete(ex_storage_sheet_details)
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

    def change_ex_storage_sheet_detail(self, origin_id, dest_id, dest_ex_storage_sheet_id, dest_commodity_name,
                                       dest_number):
        try:
            # 查询出库详单是否存在
            ex_storage_sheet_details = self.session.query(_ExStorageSheetDetail).filter(
                _ExStorageSheetDetail.id == origin_id).first()
            if (ex_storage_sheet_details == None):
                print("ex_storage_sheet_details is not exist")
                return NOT_EXIST_ERROR
            # 查询商品是否存在
            commodity = self.session.query(_Commodity).filter(
                _Commodity.name == dest_commodity_name).first()
            if (commodity == None):
                print("commodity does not exist")
                return NOT_EXIST_ERROR
            # 修改
            ex_storage_sheet_details.id = dest_id
            ex_storage_sheet_details.ex_storage_sheet_id = dest_ex_storage_sheet_id
            ex_storage_sheet_details.commodity_id = commodity.id
            ex_storage_sheet_details.number = dest_number
            # commit
            self.session.commit()
            # 返回成功标志
            return SUCCESS
        except Exception as e:
            e = str(e.args[0])
            if ('a foreign key constraint fails' in e):
                return FOREIGNKEY_ERROR
            else:
                return UNKNOWN_ERROR

    def get_all_ex_storage_sheet_details(self):
        try:
            ret_data = {}
            ret_data['details'] = []
            ex_storage_sheets_details = self.session.query(_ExStorageSheetDetail).all()
            for item in ex_storage_sheets_details:
                id = item.id
                ex_storage_sheet_id = item.ex_storage_sheet_id
                commodity_name = self.session.query(_Commodity).filter(_Commodity.id == item.commodity_id).first().name
                number = item.number
                ret_data['details'].append({'id': id, 'ex_storage_sheet_id': ex_storage_sheet_id,
                                            'commodity_name': commodity_name, 'number': number})
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
    data_model = ExStorageSheetDetails(engine)

    # data_model.create_ex_storage_sheet_details('002', '20152119201111', '苹果', 2)
    # data_model.delete_ex_storage_sheet_details('002')
    # data_model.change_ex_storage_sheet_details('002', '002','20152119201111','苹果', 3)
    sheets = data_model.get_all_ex_storage_sheet_details()
    print(sheets[0])

    # data_model.commit()
    data_model.close()
