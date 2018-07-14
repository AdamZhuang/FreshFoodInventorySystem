import hashlib
from sqlalchemy.orm import sessionmaker
from flask_server.orm.basic_model import _User
from flask_server.public.error_code import *


class User(object):
    def __init__(self, engine):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    #########################
    # 身份认证部分
    #########################
    def validate_by_encryption_password(self, name, password, department):
        try:
            user = self.session.query(_User).filter(_User.name == name).first()
            if (user != None):
                if (user.password == password and user.department == department):
                    return SUCCESS
            return PWD_WORONG
        except Exception as e:
            print(e)
            return UNKNOWN_ERROR

    def validate_by_origin_password(self, name, password, department_name):
        statue = self.validate_by_encryption_password(name, self.encryption(password), department_name)
        if (statue == SUCCESS):
            return True
        else:
            return False

    def encryption(self, password):
        hash = hashlib.md5()
        hash.update(bytes(password, encoding='utf-8'))
        return hash.hexdigest()

    ########################
    # 增删改查部分
    ########################
    def create_user(self, name, password, contact, department):
        try:
            # 判断用户名是否存在
            user = self.session.query(_User).filter(_User.name == name).first()
            if (user != None):
                print('user exist')
                return EXIST_ERROR
            # 密码加密处理
            password = self.encryption(password)
            # 新建一个用户
            new_user = _User(name=name, password=password, contact=contact, department=department)
            self.session.flush()
            self.session.add(new_user)
            self.session.commit()
            return SUCCESS
        except:
            return UNKNOWN_ERROR

    def delete_user(self, name):
        try:
            # 判断用户名是否存在
            user = self.session.query(_User).filter(_User.name == name).first()
            if (user == None):
                print('user do not exist')
                return NOT_EXIST_ERROR

            self.session.delete(user)
            self.session.commit()
            return SUCCESS
        except:
            return UNKNOWN_ERROR

    def change_user(self, origin_name, dest_name, dest_password, dest_contact, dest_department):
        try:
            origin_user = self.session.query(_User).filter(_User.name == origin_name).first()
            if (origin_user == None):
                print("origin_user does not exist")
                return NOT_EXIST_ERROR

            dest_user = self.session.query(_User).filter(_User.name == dest_name).first()
            if (dest_user != None and dest_user.name != origin_name):
                print("dest_user exist")
                return EXIST_ERROR

            # 修改
            origin_user.name = dest_name
            # 不等于None, 则修改密码
            if (dest_password != None):
                origin_user.password = self.encryption(dest_password)
            origin_user.contact = dest_contact
            origin_user.department = dest_department
            self.session.commit()
            return SUCCESS
        except:
            return UNKNOWN_ERROR

    def get_user(self, name):
        try:
            user = self.session.query(_User).filter(_User.name == name).first()
            if (user == None):
                return NOT_EXIST_ERROR
            return {'user': {'name': user.name, 'password': user.password,
                             'contact': user.contact, 'department': user.department}}
        except Exception as e:
            print(e)
            return UNKNOWN_ERROR

    def get_all_users(self):
        try:
            users = self.session.query(_User).all()
            ret_dict = {'users': []}
            for user in users:
                ret_dict['users'].append({'name': user.name, 'password': user.password,
                                          'contact': user.contact, 'department': user.department})
            return ret_dict
        except Exception as e:
            print(e)
            return UNKNOWN_ERROR

    def get_all_user_in_department(self, department):
        try:
            ret_dict = {'users': []}
            result = self.get_all_users()
            if(result == UNKNOWN_ERROR):
                return UNKNOWN_ERROR

            for user in result['users']:
                if(user['department'] == department):
                    ret_dict['users'].append({'name': user['name'], 'password': user['password'],
                                              'contact': user['contact'], 'department': user['department']})
            return ret_dict
        except Exception as e:
            print(e)
            return UNKNOWN_ERROR


    # def get_all_order_man_names(self):
    #     try:
    #         users = self.session.query(_User).all()
    #         ret_dict = {'order_man_names': []}
    #         for user in users:
    #             if (department.name == '采购部'):
    #                 ret_dict['order_man_names'].append({'name': user.name})
    #         return ret_dict
    #     except Exception as e:
    #         print(e)
    #         return UNKNOWN_ERROR

    def get_password(self, name):
        try:
            user = self.session.query(_User).filter(_User.name == name).first()
            if (user != None):
                ret_dict = {}
                ret_dict['password'] = user.password
                return ret_dict
            else:
                return NOT_EXIST_ERROR
        except Exception as e:
            print(e)
            return UNKNOWN_ERROR

    def commit(self):
        try:
            self.session.flush()
            self.session.commit()
            return SUCCESS
        except Exception as e:
            print(e)
            return UNKNOWN_ERROR

    def close(self):
        try:
            self.session.close()
            return SUCCESS
        except Exception as e:
            print(e)
            return UNKNOWN_ERROR


if __name__ == '__main__':
    from sqlalchemy import create_engine

    engine = create_engine("mysql+pymysql://root:Zxw11071205@127.0.0.1:3306/stock_control",
                           encoding='utf8', echo=False, max_overflow=100)
    data_model = User(engine)

    users = [{'name': '张三', 'password': '123456', 'contact': '654321', 'department_name': '经理'},
             {'name': '李四', 'password': '123456', 'contact': '654321', 'department_name': '仓储部'},
             {'name': '王五', 'password': '123456', 'contact': '654321', 'department_name': '采购部'}]

    for user in users:
        name = user['name']
        password = user['password']
        contact = user['contact']
        department_name = user['department_name']
        data_model.create_user(name=name, password=password, contact=contact, department_name=department_name)

    # data_model.delete_user('张嘟嘟')
    # data_model.change_user('张三', '张嘟嘟', '123455','12344ty67','采购部')

    print(data_model.get_all_users())
    # print(data_model.get_user('李四'))
    # data_model.commit()
    # data_model.close()
