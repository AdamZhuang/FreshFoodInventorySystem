from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_server.public.error_code import *

from flask_server.orm.basic_model import _Supplier


class Supplier(object):
    def __init__(self, engine):
        self.engine = engine
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def create_supplier(self, name, contact):
        try:
            supplier = self.session.query(_Supplier).filter(_Supplier.name == name).first()
            if (supplier != None):
                print("commodity exist")
                return EXIST_ERROR

            new_supplier = _Supplier(name=name, contact=contact)
            # 添加到session:
            self.session.add(new_supplier)
            self.session.commit()
            # 返回成功标志
            return SUCCESS
        except Exception as e:
            print(e)
            return UNKNOWN_ERROR

    def delete_supplier(self, delete_supplier_name):
        try:
            supplier = self.session.query(_Supplier).filter(_Supplier.name == delete_supplier_name).first()
            if (supplier == None):
                print("do not exist")
                return NOT_EXIST_ERROR
            self.session.delete(supplier)
            self.session.commit()
            return SUCCESS
        except Exception as e:
            print(e)
            return UNKNOWN_ERROR

    def change_supplier(self, origin_supplier_name, dest_supplier_name, dest_supplier_contact):
        try:
            supplier = self.session.query(_Supplier).filter(_Supplier.name == origin_supplier_name).first()
            if (supplier == None):
                print("supplier does not exist")
                return NOT_EXIST_ERROR

            supplier.name = dest_supplier_name
            supplier.contact = dest_supplier_contact
            self.session.commit()
            return SUCCESS
        except Exception as e:
            print(e)
            return UNKNOWN_ERROR

    def get_all_suppliers(self):
        try:
            suppliers = self.session.query(_Supplier).all()
            ret_dic = {'suppliers': []}
            for supplier in suppliers:
                ret_dic['suppliers'].append({'name': supplier.name, 'contact': supplier.contact})
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
