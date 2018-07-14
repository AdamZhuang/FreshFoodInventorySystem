from sqlalchemy.orm import sessionmaker
from flask_server.orm.basic_model import _WareHouse, _User
from flask_server.public.error_code import *


class Warehouse(object):
    def __init__(self, engine):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def create_warehouse(self, name, location, warehouse_manager_name):
        try:
            # 查询名称是否已存在
            warehouse = self.session.query(_WareHouse).filter(_WareHouse.name == name).first()
            manager = self.session.query(_User).filter(_User.name == warehouse_manager_name).first()
            if (warehouse != None):
                print("warehouse exist")
                return EXIST_ERROR
            if (manager == None):
                print("manager or order_man does not exist")
                return NOT_EXIST_ERROR

            # 新建commodity对象
            new_warehouse = _WareHouse(name=name, location=location, warehouse_manager_id=manager.id)
            # 添加到session:
            self.session.add(new_warehouse)
            self.session.commit()
            # 返回成功标志
            return SUCCESS
        except Exception as e:
            print(e)
            return UNKNOWN_ERROR

    def delete_warehouse(self, name):
        try:
            # 查询名称是否已存在
            warehouse = self.session.query(_WareHouse).filter(_WareHouse.name == name).first()
            if (warehouse == None):
                print("do not exist")
                return NOT_EXIST_ERROR

            self.session.delete(warehouse)
            self.session.commit()
            return SUCCESS
        except Exception as e:
            print(e)
            return UNKNOWN_ERROR

    def change_warehouse(self, origin_name, dest_name, dest_location, dest_warehouse_manager_name):
        try:
            # 查询名称是否已存在
            origin_warehouse = self.session.query(_WareHouse).filter(_WareHouse.name == origin_name).first()
            dest_warehouse = self.session.query(_WareHouse).filter(_WareHouse.name == dest_name).first()
            dest_warehouse_manager = self.session.query(_User).filter(_User.name == dest_warehouse_manager_name).first()
            if (origin_warehouse == None or dest_warehouse_manager == None):
                print('origin_warehouse or dest_manager does not exist')
                return NOT_EXIST_ERROR
            # 两个仓库不是同一个仓库，并且修改后的仓库名称与存在的仓库名称冲突
            if (dest_warehouse != None and dest_warehouse.name != origin_warehouse.name):
                print("dest_warehouse exist")
                return EXIST_ERROR

            origin_warehouse.name = dest_name
            origin_warehouse.location = dest_location
            origin_warehouse.warehouse_manager_id = dest_warehouse_manager.id
            self.session.commit()
            return SUCCESS
        except Exception as e:
            print(e)
            return UNKNOWN_ERROR

    def get_all_warehouses(self):
        try:
            warehouses = self.session.query(_WareHouse).all()
            ret_dict = {'warehouses': []}
            for warehouse in warehouses:
                user = self.session.query(_User).filter(_User.id == warehouse.warehouse_manager_id).first()
                ret_dict['warehouses'].append(
                    {'name': warehouse.name, 'location': warehouse.location, 'warehouse_manager_name': user.name})

            return ret_dict
        except Exception as e:
            print(e)
            return UNKNOWN_ERROR

    def get_warehouse_by_manager_name(self, warehouse_manager_name):
        try:
            warehouses = self.get_all_warehouses()['warehouses']
            for warehouse in warehouses:
                if(warehouse['warehouse_manager_name']== warehouse_manager_name):
                    return  {'name': warehouse['name'], 'location': warehouse['location'], 'warehouse_manager_name': warehouse_manager_name}
            return {}
        except Exception as e:
            print(e)
            return UNKNOWN_ERROR

    def commit(self):
        try:
            self.session.flush()
            self.session.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def close(self):
        try:
            self.session.close()
            return True
        except Exception as e:
            print(e)
            return False
