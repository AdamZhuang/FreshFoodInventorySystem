from flask import Blueprint, request
from sqlalchemy import create_engine

from flask_server.model import *
from flask_server.public.public_fun import successful, failed, validate, validate_not_pass, exception
from flask_server.public.error_code import *

# 蓝图模块
admin = Blueprint('admin', __name__)
# 数据库连接引擎
engine = create_engine("mysql+pymysql://root:Zxw11071205@127.0.0.1:3306/stock_control",
                       encoding='utf8', echo=False, max_overflow=100)


def admin_validate(engine, username, password, department_name):
    # if(username != 'admin' or department_name != '系统管理员'):
    #     return False
    # else:
    return validate(engine, username, password, department_name)


@admin.route('/', methods=['POST'])
def admin_index():
    print('admin index')


######################
# 用户管理模块
######################
@admin.route('/add_user', methods=['POST'])
def add_user():
    try:
        # 从客户端获取数据
        username = request.form.get('username')
        password = request.form.get('password')
        department = request.form.get('department')
        add_username = request.form.get('add_username')
        add_user_password = request.form.get('add_user_password')
        add_user_contact = request.form.get('add_user_contact')
        add_user_department = request.form.get('add_user_department')
        if (admin_validate(engine, username, password, department)):
            data_model = user.User(engine)
            statue = data_model.create_user(name=add_username, password=add_user_password, contact=add_user_contact,
                                            department=add_user_department)
            if (statue == SUCCESS):
                return successful(data_model, {'code': statue})
            else:
                return failed(data_model, {'code': statue})
        else:
            return validate_not_pass()
    except Exception as e:
        print(e)
        return exception()


@admin.route('/delete_user', methods=['POST'])
def delete_user():
    try:
        # 从客户端获取数据
        username = request.form.get('username')
        password = request.form.get('password')
        department = request.form.get('department')
        delete_username = request.form.get('delete_username')
        if (admin_validate(engine, username, password, department)):
            data_model = user.User(engine)
            statue = data_model.delete_user(name=delete_username)
            if (statue == SUCCESS):
                return successful(data_model, {'code': statue})
            else:
                return failed(data_model, {'code': statue})
        else:
            return validate_not_pass()
    except Exception as e:
        print(e)
        return exception()


@admin.route('/change_user', methods=['POST'])
def change_user():
    try:
        # 认证信息
        username = request.form.get('username')
        password = request.form.get('password')
        department = request.form.get('department')
        # 修改信息
        origin_name = request.form.get('origin_name')
        dest_name = request.form.get('dest_name')
        dest_password = request.form.get('dest_password')
        dest_contact = request.form.get('dest_contact')
        dest_department = request.form.get('dest_department')
        if (admin_validate(engine, username, password, department)):
            data_model = user.User(engine)
            statue = data_model.change_user(origin_name=origin_name, dest_name=dest_name, dest_password=dest_password,
                                          dest_contact=dest_contact, dest_department=dest_department)
            if (statue == statue):
                return successful(data_model, {'code': statue})
            else:
                return failed(data_model, {'code': statue})
        else:
            return validate_not_pass()
    except Exception as e:
        print(e)
        return exception()



@admin.route('/get_all_users', methods=['POST'])
def get_all_users():
    try:
        # 认证信息
        username = request.form.get('username')
        password = request.form.get('password')
        department = request.form.get('department')
        # 获取模型
        if (admin_validate(engine, username, password, department)):
            data_model = user.User(engine)
            result = data_model.get_all_users()
            if (result != UNKNOWN_ERROR):
                return successful(data_model, result)
            else:
                return failed(data_model, {'code': result})
        else:
            return validate_not_pass()
    except Exception as e:
        print(e)
        return exception()


@admin.route('/get_all_user_in_department', methods=['POST'])
def get_all_user_in_department():
    try:
        # 认证信息
        username = request.form.get('username')
        password = request.form.get('password')
        department = request.form.get('department')
        query_department = request.form.get('query_department')
        # 获取模型
        if (admin_validate(engine, username, password, department)):
            data_model = user.User(engine)
            result = data_model.get_all_user_in_department(query_department)
            if (result != UNKNOWN_ERROR):
                return successful(data_model, result)
            else:
                return failed(data_model, {'code': result})
        else:
            return validate_not_pass()
    except Exception as e:
        print(e)
        return exception()


#####################
# 仓库管理模块
#####################
@admin.route('/add_warehouse', methods=["POST"])
def add_warehouse():
    try:
        # 认证信息
        username = request.form.get('username')
        password = request.form.get('password')
        department = request.form.get('department')
        warehouse_name = request.form.get('warehouse_name')
        warehouse_location = request.form.get('warehouse_location')
        warehouse_manager_name = request.form.get('warehouse_manager_name')

        if (admin_validate(engine, username, password, department)):
            data_model = warehouse.Warehouse(engine)
            code = data_model.create_warehouse(name=warehouse_name, location=warehouse_location,
                                               warehouse_manager_name=warehouse_manager_name)
            if (code == SUCCESS):
                return successful(data_model, {'code': code})
            else:
                return failed(data_model, {'code': code})
        else:
            return validate_not_pass()
    except Exception as e:
        print(e)
        return exception()


@admin.route('/delete_warehouse', methods=["POST"])
def delete_warehouse():
    try:
        username = request.form.get('username')
        password = request.form.get('password')
        department = request.form.get('department')
        delete_warehouse_name = request.form.get('delete_warehouse_name')
        if (admin_validate(engine, username, password, department)):
            data_model = warehouse.Warehouse(engine)
            statue = data_model.delete_warehouse(name=delete_warehouse_name)
            if (statue == SUCCESS):
                return successful(data_model, {'code': statue})
            else:
                return failed(data_model, {'code': statue})
        else:
            return validate_not_pass()
    except Exception as e:
        print(e)
        return exception()


@admin.route('/change_warehouse', methods=["POST"])
def change_warehouse():
    try:
        # 认证信息
        username = request.form.get('username')
        password = request.form.get('password')
        department = request.form.get('department')
        # 修改信息
        origin_warehouse_name = request.form.get('origin_warehouse_name')
        dest_warehouse_name = request.form.get('dest_warehouse_name')
        dest_warehouse_location = request.form.get('dest_warehouse_location')
        dest_warehouse_manager_name = request.form.get('dest_warehouse_manager_name')
        if (admin_validate(engine, username, password, department)):
            data_model = warehouse.Warehouse(engine)
            statue = data_model.change_warehouse(origin_name=origin_warehouse_name, dest_name=dest_warehouse_name,
                                                 dest_location=dest_warehouse_location,
                                                 dest_warehouse_manager_name=dest_warehouse_manager_name)
            if (statue == SUCCESS):
                return successful(data_model, {'code': statue})
            else:
                return failed(data_model, {'code': statue})
        else:
            return validate_not_pass()
    except Exception as e:
        print(e)
        return exception()


@admin.route('/get_all_warehouses', methods=["POST"])
def get_all_warehouses():
    try:
        # 认证信息
        username = request.form.get('username')
        password = request.form.get('password')
        department = request.form.get('department')
        if (admin_validate(engine, username, password, department)):
            data_model = warehouse.Warehouse(engine)
            result = data_model.get_all_warehouses()
            if (result != UNKNOWN_ERROR):
                return successful(data_model, result)
            else:
                return failed(data_model, {'code': result})
        else:
            return validate_not_pass()
    except Exception as e:
        print(e)
        return exception()


#####################
# 供应商管理模块
#####################
@admin.route('/add_supplier', methods=["POST"])
def add_supplier():
    try:
        username = request.form.get('username')
        password = request.form.get('password')
        department = request.form.get('department')
        supplier_name = request.form.get('supplier_name')
        supplier_contact = request.form.get('supplier_contact')

        if (admin_validate(engine, username, password, department)):
            data_model = supplier.Supplier(engine)
            code = data_model.create_supplier(name=supplier_name, contact=supplier_contact)
            if (code == SUCCESS):
                return successful(data_model, {'code': code})
            else:
                return failed(data_model, {'code': code})
        else:
            return validate_not_pass()
    except Exception as e:
        print(e)
        return exception()


@admin.route('/delete_supplier', methods=["POST"])
def delete_supplier():
    try:
        username = request.form.get('username')
        password = request.form.get('password')
        department = request.form.get('department')
        delete_supplier_name = request.form.get('delete_supplier_name')
        if (admin_validate(engine, username, password, department)):
            data_model = supplier.Supplier(engine)
            statue = data_model.delete_supplier(delete_supplier_name=delete_supplier_name)
            if (statue == SUCCESS):
                return successful(data_model, {'code': statue})
                return successful(data_model, {'code': statue})
            else:
                return failed(data_model, {'code': statue})
        else:
            return validate_not_pass()
    except Exception as e:
        print(e)
        return exception()


@admin.route('/change_supplier', methods=["POST"])
def change_supplier():
    try:
        username = request.form.get('username')
        password = request.form.get('password')
        department = request.form.get('department')
        origin_supplier_name = request.form.get('origin_supplier_name')
        dest_supplier_name = request.form.get('dest_supplier_name')
        dest_supplier_contact = request.form.get('dest_supplier_contact')

        if (admin_validate(engine, username, password, department)):
            data_model = supplier.Supplier(engine)
            statue = data_model.change_supplier(origin_supplier_name, dest_supplier_name, dest_supplier_contact)
            if (statue == SUCCESS):
                return successful(data_model, {'code': statue})
            else:
                return failed(data_model, {'code': statue})
        else:
            return validate_not_pass()
    except Exception as e:
        print(e)
        return exception()


@admin.route('/get_all_suppliers', methods=["POST"])
def get_all_suppliers():
    try:
        # 认证信息
        username = request.form.get('username')
        password = request.form.get('password')
        department = request.form.get('department')
        if (admin_validate(engine, username, password, department)):
            data_model = supplier.Supplier(engine)
            result = data_model.get_all_suppliers()
            if (result != UNKNOWN_ERROR):
                return successful(data_model, result)
            else:
                return failed(data_model, {'code': result})
        else:
            return validate_not_pass()
    except Exception as e:
        print(e)
        return exception()


######################
# 商品管理模块
######################
@admin.route('/add_commodity', methods=["POST"])
def add_commodity():
    try:
        # 认证信息
        username = request.form.get('username')
        password = request.form.get('password')
        department_name = request.form.get('department_name')
        # 添加商品信息
        commodity_code = request.form.get('commodity_code')
        commodity_name = request.form.get('commodity_name')
        commodity_type = request.form.get('commodity_type')
        commodity_unit = request.form.get('commodity_unit')
        commodity_specification = request.form.get('commodity_specification')
        commodity_supplier_name = request.form.get('commodity_supplier_name')

        if (admin_validate(engine, username, password, department_name)):
            data_model = commodity.Commodity(engine)
            code = data_model.create_commodity(code=commodity_code, name=commodity_name, type=commodity_type, unit=commodity_unit,
                                               specification=commodity_specification,
                                               supplier_name=commodity_supplier_name)
            if (code == SUCCESS):
                return successful(data_model, {'code': code})
            else:
                return failed(data_model, {'code': code})
        else:
            return validate_not_pass()
    except Exception as e:
        print(e)
        return exception()


@admin.route('/delete_commodity', methods=["POST"])
def delete_commodity():
    try:
        # 认证信息
        username = request.form.get('username')
        password = request.form.get('password')
        department_name = request.form.get('department_name')
        # 删除信息
        delete_commodity_code = request.form.get('delete_commodity_code')
        if (admin_validate(engine, username, password, department_name)):
            data_model = commodity.Commodity(engine)
            code = data_model.delete_commodity(code=delete_commodity_code)
            if (code == SUCCESS):
                return successful(data_model, {'code': code})
            else:
                return failed(data_model, {'code': code})
        else:
            return validate_not_pass()
    except Exception as e:
        print(e)
        return exception()


@admin.route('/change_commodity', methods=["POST"])
def change_commodity():
    try:
        # 认证信息
        username = request.form.get('username')
        password = request.form.get('password')
        department_name = request.form.get('department_name')
        # 修改信息
        origin_commodity_code = request.form.get('origin_commodity_code')
        dest_commodity_code = request.form.get('dest_commodity_code')
        dest_commodity_name = request.form.get('dest_commodity_name')
        dest_commodity_type = request.form.get('dest_commodity_type')
        dest_commodity_unit = request.form.get('dest_commodity_unit')
        dest_commodity_specification = request.form.get('dest_commodity_specification')
        dest_commodity_supplier_name = request.form.get('dest_commodity_supplier_name')

        if (admin_validate(engine, username, password, department_name)):
            data_model = commodity.Commodity(engine)
            code = data_model.change_commodity(origin_commodity_code=origin_commodity_code,
                                               dest_commodity_code=dest_commodity_code,
                                               dest_commodity_name=dest_commodity_name,
                                               dest_commodity_type=dest_commodity_type,
                                               dest_commodity_unit=dest_commodity_unit,
                                               dest_commodity_specification=dest_commodity_specification,
                                               dest_commodity_supplier_name=dest_commodity_supplier_name)
            if (code == SUCCESS):
                return successful(data_model, {'code': code})
            else:
                return failed(data_model, {'code': code})
        else:
            return validate_not_pass()
    except Exception as e:
        print(e)
        return exception()


@admin.route('/get_all_commodities', methods=["POST"])
def get_all_commodities():
    try:
        # 认证信息
        username = request.form.get('username')
        password = request.form.get('password')
        department_name = request.form.get('department_name')
        if (admin_validate(engine, username, password, department_name)):
            data_model = commodity.Commodity(engine)
            result = data_model.get_all_commodities()
            if (result != UNKNOWN_ERROR):
                return successful(data_model, result)
            else:
                return failed(data_model, {'code': result})
        else:
            return validate_not_pass()
    except Exception as e:
        print(e)
        return exception()


@admin.route('/get_commodity_name', methods=["POST"])
def get_commodity_name():
    try:
        # 认证信息
        username = request.form.get('username')
        password = request.form.get('password')
        department_name = request.form.get('department_name')
        get_commodity_name = request.form.get('get_commodity_name')
        if (admin_validate(engine, username, password, department_name)):
            data_model = commodity.Commodity(engine)
            result = data_model.get_commodity(name=get_commodity_name)
            if (result != UNKNOWN_ERROR):
                return successful(data_model, result)
            else:
                return failed(data_model, {'code': result})
        else:
            return validate_not_pass()
    except Exception as e:
        print(e)
        return exception()
