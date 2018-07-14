from sqlalchemy.orm import sessionmaker
from flask_server.orm.basic_model import _InStorageSheet, _InStorageSheetDetail, _Commodity, _CommodityStatic, \
    _Supplier, _WareHouse
from flask_server.public.error_code import *


class InStorageSheetDetail(object):
    def __init__(self, engine):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def create_in_storage_sheet_detail(self, in_storage_sheet_code, commodity_code, number):
        try:
            # 查询入库总单是否存在
            in_storage_sheet = self.session.query(_InStorageSheet).filter(
                _InStorageSheet.code == in_storage_sheet_code).first()
            if (in_storage_sheet == None):
                print("in_storage_sheet does not exist")
                return NOT_EXIST_ERROR
            # 查询商品是否存在
            commodity = self.session.query(_Commodity).filter(_Commodity.code == commodity_code).first()
            if (commodity == None):
                print("commodity does not exist")
                return NOT_EXIST_ERROR

            # 查询库存单，更新库存
            storage_sheet = self.session.query(_CommodityStatic).filter(
                _CommodityStatic.id == commodity.id and _WareHouse.id == in_storage_sheet.warehouse_id).first()
            if (storage_sheet == None):
                new_storage_sheet = _CommodityStatic(warehouse_id=in_storage_sheet.warehouse_id,
                                                     commodity_id=commodity.id, number=number)
                self.session.add(new_storage_sheet)
            else:
                storage_sheet.number = storage_sheet.number + int(number)

            # 满足以上情况，新建_InStorageSheet对象
            new_in_storage_sheet_details = _InStorageSheetDetail(in_storage_sheet_id=in_storage_sheet.id,
                                                                 commodity_id=commodity.id, number=number)
            # 添加到session:
            self.session.add(new_in_storage_sheet_details)
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

    def get_in_storage_sheet_details(self, in_storage_sheet_code):
        try:
            ret_data = {}
            ret_data['details'] = []
            in_storage_sheet = self.session.query(_InStorageSheet).filter(
                _InStorageSheet.code == in_storage_sheet_code).first()
            in_storage_sheet_details = self.session.query(_InStorageSheetDetail).filter(
                _InStorageSheetDetail.in_storage_sheet_id == in_storage_sheet.id).all()
            for in_storage_sheet_detail in in_storage_sheet_details:
                commodity = self.session.query(_Commodity).filter(
                    _Commodity.id == in_storage_sheet_detail.commodity_id).first()
                supplier = self.session.query(_Supplier).filter(_Supplier.id == commodity.supplier_id).first()
                ret_data['details'].append(
                    {'in_storage_sheet_code': in_storage_sheet_code,
                     'commodity_code': commodity.code,
                     'commodity_name': commodity.name,
                     'commodity_type': commodity.type,
                     'commodity_unit': commodity.unit,
                     'commodity_specification': commodity.specification,
                     'commodity_supplier': supplier.name,
                     'number': in_storage_sheet_detail.number})
            return ret_data
        except Exception as e:
            print(e)
            return UNKNOWN_ERROR

    def close(self):
        try:
            self.session.close()
        except Exception as e:
            print(e)
