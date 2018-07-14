from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_server.public.error_code import *

from flask_server.orm.basic_model import _CommodityStatic, _Commodity, _WareHouse, _Supplier


class CommodityStatic(object):
    def __init__(self, engine):
        self.engine = engine
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def get_all_stock_details(self):
        ret_dic = {'stock_details': []}
        try:
            static = self.session.query(_CommodityStatic).all()
            for item in static:
                commodity = self.session.query(_Commodity).filter(_Commodity.id == item.id).first()
                supplier = self.session.query(_Supplier).filter(_Supplier.id == commodity.supplier_id).first()
                warehouse = self.session.query(_WareHouse).filter(_WareHouse.id == item.warehouse_id).first()
                ret_dic['stock_details'].append(
                    {'warehouse_name': warehouse.name,
                     'commodity_code': commodity.code,
                     'commodity_name': commodity.name,
                     'commodity_type': commodity.type,
                     'commodity_unit': commodity.unit,
                     'commodity_specification': commodity.specification,
                     'commodity_supplier': supplier.name,
                     'number': item.number})
            return ret_dic
        except Exception as e:
            print(e)
            return UNKNOWN_ERROR

    def get_stock_details(self, warehouse_name):
        ret_dic = {'stock_details': []}
        try:
            static = self.session.query(_CommodityStatic).filter(_WareHouse.name == warehouse_name).all()
            for item in static:
                commodity = self.session.query(_Commodity).filter(_Commodity.id == item.id).first()
                supplier = self.session.query(_Supplier).filter(_Supplier.id == commodity.supplier_id).first()
                ret_dic['stock_details'].append(
                    {'warehouse_name': warehouse_name,
                     'commodity_code': commodity.code,
                     'commodity_name': commodity.name,
                     'commodity_type': commodity.type,
                     'commodity_unit': commodity.unit,
                     'commodity_specification': commodity.specification,
                     'commodity_supplier': supplier.name,
                     'number': item.number})
            return ret_dic
        except Exception as e:
            print(e)
            return UNKNOWN_ERROR

    def close(self):
        try:
            self.session.close()
            return True

        except Exception as e:
            print(e)
            return False
