from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_server.public.error_code import *

from flask_server.orm.basic_model import _Commodity, _Supplier


class Commodity(object):
    def __init__(self, engine):
        self.engine = engine
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def create_commodity(self, code, name, type, unit, specification, supplier_name):
        try:
            commodity = self.session.query(_Commodity).filter(_Commodity.code == code).first()
            if (commodity != None):
                print("commodity exist")
                return EXIST_ERROR
            supplier = self.session.query(_Supplier).filter(_Supplier.name == supplier_name).first()
            if (supplier == None):
                print("supplier does exist")
                return NOT_EXIST_ERROR

            new_commodity = _Commodity(code=code, name=name, type=type, unit=unit, specification=specification,
                                       supplier_id=supplier.id)
            # 添加到session:
            self.session.add(new_commodity)
            self.session.commit()
            # 返回成功标志
            return SUCCESS
        except Exception as e:
            print(e)
            return UNKNOWN_ERROR

    def delete_commodity(self, code):
        try:
            # 查询名称是否已存在
            commodity = self.session.query(_Commodity).filter(_Commodity.code == code).first()
            if (commodity == None):
                print("do not exist")
                return NOT_EXIST_ERROR
            self.session.delete(commodity)
            self.session.commit()
            return SUCCESS
        except Exception as e:
            print(e)
            return UNKNOWN_ERROR

    def change_commodity(self, origin_commodity_code, dest_commodity_code, dest_commodity_name,
                         dest_commodity_type, dest_commodity_unit, dest_commodity_specification,
                         dest_commodity_supplier_name):
        try:
            origin_commodity = self.session.query(_Commodity).filter(_Commodity.code == origin_commodity_code).first()
            dest_commodity = self.session.query(_Commodity).filter(_Commodity.code == dest_commodity_code).first()
            supplier = self.session.query(_Supplier).filter(_Supplier.name == dest_commodity_supplier_name).first()

            # 修改后商品编号为已存在商品编号，并且不是自身当前编号情况
            if (dest_commodity != None and dest_commodity.code != origin_commodity.code):
                return EXIST_ERROR

            origin_commodity.code = dest_commodity_code
            origin_commodity.name = dest_commodity_name
            origin_commodity.type = dest_commodity_type
            origin_commodity.unit = dest_commodity_unit
            origin_commodity.specification = dest_commodity_specification
            origin_commodity.supplier_id = supplier.id

            self.session.commit()
            return SUCCESS
        except Exception as e:
            print(e)
            return UNKNOWN_ERROR

    def get_all_commodities(self):
        try:
            commodities = self.session.query(_Commodity).all()
            ret_dic = {'commodities': []}
            for commodity in commodities:
                supplier = self.session.query(_Supplier).filter(_Supplier.id == commodity.supplier_id).first()
                ret_dic['commodities'].append({'code': commodity.code, 'name': commodity.name, 'type': commodity.type,
                                               'unit': commodity.unit, 'specification': commodity.specification,
                                               'supplier_name': supplier.name})
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


if __name__ == '__main__':
    commodities = [{'name': '苹果', 'type': '水果', 'reference_price': '10元每斤'},
                   {'name': '香蕉', 'type': '水果', 'reference_price': '15元每斤'},
                   {'name': '梨子', 'type': '水果', 'reference_price': '20元每斤'}]

    engine = create_engine("mysql+pymysql://root:Zxw11071205@127.0.0.1:3306/stock_control",
                           encoding='utf8', echo=False, max_overflow=5)
    commodity_model = Commodity(engine)

    # 增
    for commodity in commodities:
        name = commodity['name']
        type = commodity['type']
        reference_price = commodity['reference_price']

        commodity_model.create_commodity(name=name, type=type, reference_price=reference_price)
    # 删
    commodity_model.delete_commodity('香蕉')
    # 改
    commodity_model.change_commodity('苹果', '苹果1', '水果', '20元每斤')
    # 查
    print(commodity_model.get_all_commodities())
    print(commodity_model.get_commodity('梨子'))
    # 提交
    commodity_model.close()
