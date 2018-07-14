from sqlalchemy.orm import sessionmaker
from flask_server.orm.basic_model import _NoticeSheet, _NoticeSheetDetail, _Commodity, _Supplier
from flask_server.public.error_code import *


class NoticeSheetDetails(object):
    def __init__(self, engine):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def create_notice_sheet_detail(self, notice_sheet_code, commodity_code, number, price):
        try:
            notice_sheet = self.session.query(_NoticeSheet).filter(
                _NoticeSheet.code == notice_sheet_code).first()
            if (notice_sheet == None):
                print("notice_sheet does not exist")
                return NOT_EXIST_ERROR

            commodity = self.session.query(_Commodity).filter(_Commodity.code == commodity_code).first()
            if (commodity == None):
                print("commodity does not exist")
                return NOT_EXIST_ERROR

            new_notice_sheet_detail = _NoticeSheetDetail(notice_sheet_id=notice_sheet.id, commodity_id=commodity.id,
                                                         number=number, price=price)
            # 添加到session:
            self.session.add(new_notice_sheet_detail)
            # commit
            self.session.commit()
            # 返回成功标志
            return SUCCESS
        except Exception as e:
            e = str(e.args[0])
            print(e)
            return UNKNOWN_ERROR

            #     def delete_order_sheet_detail(self, id):
            #         try:
            #             # 查询采购详单是否存在
            #             order_sheet_detail = self.session.query(_OrderSheetDetail).filter(
            #                 _OrderSheetDetail.id == id).first()
            #             if (order_sheet_detail == None):
            #                 print("order_sheet_detail does not exist")
            #                 return NOT_EXIST_ERROR
            #             # 添加到session:
            #             self.session.delete(order_sheet_detail)
            #             # 返回commit情况（True or False）
            #             self.session.commit()
            #             # 返回成功标志
            #             return SUCCESS
            #         except Exception as e:
            #             e = str(e.args[0])
            #             if ('a foreign key constraint fails' in e):
            #                 return FOREIGNKEY_ERROR
            #             else:
            #                 return UNKNOWN_ERROR
            #
            #     def get_order_sheet_by_order_sheet_id(self, order_sheet_id):
            #         try:
            #             ret_dic = {'details': []}
            #             order_sheet_details = self.session.query(_OrderSheetDetail).filter(
            #                 _OrderSheetDetail.order_sheet_id == order_sheet_id).all()
            #             for order_sheet_detail in order_sheet_details:
            #                 commodity = self.session.query(_Commodity).filter(
            #                     _Commodity.id == order_sheet_detail.commodity_id).first()
            #                 ret_dic['details'].append({
            #                     'id': order_sheet_detail.id,
            #                     'order_sheet_id': order_sheet_detail.order_sheet_id,
            #                     'commodity_name': commodity.name,
            #                     'number': order_sheet_detail.number,
            #                     'allow_price': order_sheet_detail.allow_price,
            #                     'actual_price': order_sheet_detail.actual_price,
            #                 })
            #             return ret_dic
            #         except Exception as e:
            #             print(e)
            #             return UNKNOWN_ERROR
            #
            #     def change_order_sheet_details(self, order_sheet_detail_id, actual_price):
            #         try:
            #             # 查询采购详单是否存在
            #             order_sheet_detail = self.session.query(_OrderSheetDetail).filter(
            #                 _OrderSheetDetail.id == order_sheet_detail_id).first()
            #             if (order_sheet_detail == None):
            #                 print("order_sheet_detail does not exist")
            #                 return NOT_EXIST_ERROR
            #             # 修改
            #             order_sheet_detail.actual_price = actual_price
            #             # commit
            #             self.session.commit()
            #             # 返回成功标志
            #             return SUCCESS
            #         except Exception as e:
            #             e = str(e.args[0])
            #             if ('a foreign key constraint fails' in e):
            #                 return FOREIGNKEY_ERROR
            #             else:
            #                 return UNKNOWN_ERROR
            #

    def get_notice_sheet_details(self, notice_sheet_code):
        try:
            ret_dic = {'details': []}
            notice_sheet = self.session.query(_NoticeSheet).filter(_NoticeSheet.code == notice_sheet_code).first()
            notice_sheet_details = self.session.query(_NoticeSheetDetail).filter(
                _NoticeSheetDetail.notice_sheet_id == notice_sheet.id).all()
            for notice_sheet_detail in notice_sheet_details:
                commmodity = self.session.query(_Commodity).filter(
                    _Commodity.id == notice_sheet_detail.commodity_id).first()
                supplier = self.session.query(_Supplier).filter(_Supplier.id == commmodity.supplier_id).first()
                ret_dic['details'].append({
                    'commodity_code': commmodity.code,
                    'commodity_name': commmodity.name,
                    'commodity_type': commmodity.type,
                    'commodity_unit': commmodity.unit,
                    'commodity_specification': commmodity.specification,
                    'commodity_supplier': supplier.name,
                    'number': notice_sheet_detail.number,
                    'price': notice_sheet_detail.price,
                })
            return ret_dic
        except Exception as e:
            print(e)
            return UNKNOWN_ERROR
            #

    def close(self):
        try:
            self.session.close()
            return SUCCESS
        except Exception as e:
            print(e)
            return SESSION_CLOSE_ERROR

#
#
# if __name__ == '__main__':
#     from sqlalchemy import create_engine
#     import datetime
#
#     engine = create_engine("mysql+pymysql://root:Zxw11071205@127.0.0.1:3306/stock_control",
#                            encoding='utf8', echo=False, max_overflow=100)
#     # data_model = ExStorageSheetDetails(engine)
#
#     # data_model.create_ex_storage_sheet_details('002', '20152119201111', '苹果', 2)
#     # data_model.delete_ex_storage_sheet_details('002')
#     # data_model.change_ex_storage_sheet_details('002', '002','20152119201111','苹果', 3)
#     # sheets = data_model.get_all_ex_storage_sheet_details()
#     # print(sheets[0])
#
#     # data_model.commit()
#     # data_model.close()
