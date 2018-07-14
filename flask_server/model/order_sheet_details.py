from sqlalchemy.orm import sessionmaker
from flask_server.orm.basic_model import _OrderSheet, _OrderSheetDetail, _Commodity, _Supplier
from flask_server.public.error_code import *


class OrderSheetDetail(object):
    def __init__(self, engine):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def create_order_sheet_detail(self, order_sheet_code, commodity_code, number, price):
        try:
            # 查询采购总单是否存在
            order_sheet = self.session.query(_OrderSheet).filter(
                _OrderSheet.code == order_sheet_code).first()
            if (order_sheet == None):
                print("order_sheet does not exist")
                return NOT_EXIST_ERROR
            # 查询商品是否存在
            commodity = self.session.query(_Commodity).filter(_Commodity.code == commodity_code).first()
            if (commodity == None):
                print("commodity does not exist")
                return NOT_EXIST_ERROR

            # 满足以上情况，新建_ExStorageSheet对象
            new_order_sheet_detail = _OrderSheetDetail(order_sheet_id=order_sheet.id, commodity_id=commodity.id,
                                                       number=number, price=price)
            # 添加到session:
            self.session.add(new_order_sheet_detail)
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

    def delete_order_sheet_detail(self, id):
        try:
            # 查询采购详单是否存在
            order_sheet_detail = self.session.query(_OrderSheetDetail).filter(
                _OrderSheetDetail.id == id).first()
            if (order_sheet_detail == None):
                print("order_sheet_detail does not exist")
                return NOT_EXIST_ERROR
            # 添加到session:
            self.session.delete(order_sheet_detail)
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

    def get_order_sheet_by_order_sheet_code(self, order_sheet_code):
        try:
            ret_dic = {'details': []}
            order_sheet = self.session.query(_OrderSheet).filter(_OrderSheet.code == order_sheet_code).first()
            order_sheet_details = self.session.query(_OrderSheetDetail).filter(
                _OrderSheetDetail.order_sheet_id == order_sheet.id).all()
            for order_sheet_detail in order_sheet_details:
                commodity = self.session.query(_Commodity).filter(
                    _Commodity.id == order_sheet_detail.commodity_id).first()
                supplier = self.session.query(_Supplier).filter(_Supplier.id == commodity.supplier_id).first()
                ret_dic['details'].append({
                    'order_sheet_code': order_sheet_code,
                    'commodity_code': commodity.code,
                    'commodity_name': commodity.name,
                    'commodity_type': commodity.type,
                    'commodity_unit': commodity.unit,
                    'commodity_specification': commodity.specification,
                    'commodity_supplier': supplier.name,
                    'number': order_sheet_detail.number,
                    'price': order_sheet_detail.price,
                })
            return ret_dic
        except Exception as e:
            print(e)
            return UNKNOWN_ERROR

    # def change_order_sheet_details(self, order_sheet_detail_id, actual_price):
    #     try:
    #         # 查询采购详单是否存在
    #         order_sheet_detail = self.session.query(_OrderSheetDetail).filter(
    #             _OrderSheetDetail.id == order_sheet_detail_id).first()
    #         if (order_sheet_detail == None):
    #             print("order_sheet_detail does not exist")
    #             return NOT_EXIST_ERROR
    #         # 修改
    #         order_sheet_detail.actual_price = actual_price
    #         # commit
    #         self.session.commit()
    #         # 返回成功标志
    #         return SUCCESS
    #     except Exception as e:
    #         e = str(e.args[0])
    #         if ('a foreign key constraint fails' in e):
    #             return FOREIGNKEY_ERROR
    #         else:
    #             return UNKNOWN_ERROR

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
    # data_model = ExStorageSheetDetails(engine)

    # data_model.create_ex_storage_sheet_details('002', '20152119201111', '苹果', 2)
    # data_model.delete_ex_storage_sheet_details('002')
    # data_model.change_ex_storage_sheet_details('002', '002','20152119201111','苹果', 3)
    # sheets = data_model.get_all_ex_storage_sheet_details()
    # print(sheets[0])

    # data_model.commit()
    # data_model.close()
