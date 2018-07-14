from flask import Blueprint, request
from sqlalchemy import create_engine
from flask_server.model import *
from flask_server.public.public_fun import successful, failed, validate, validate_not_pass, exception
from flask_server.public.error_code import *

# 蓝图模块
storage_keeper = Blueprint('storage_keeper', __name__)
# 数据库连接引擎
engine = create_engine("mysql+pymysql://root:Zxw11071205@127.0.0.1:3306/stock_control",
                       encoding='utf8', echo=False, max_overflow=100)


# 登陆验证模块
def storage_keeper_validate(engine, username, password, department_name):
    # if(username != 'admin' or department_name != '系统管理员'):
    #     return False
    # else:
    return validate(engine, username, password, department_name)


@storage_keeper.route('/', methods=['POST'])
def storage_keeper_index():
    return 'storage_keeper index'


###############################
# 采购单模块
###############################
@storage_keeper.route('/get_order_sheets_by_warehouse_name', methods=['POST'])
def get_order_sheets_by_warehouse_name():
    try:
        # 从客户端获取数据
        username = request.form.get('username')
        password = request.form.get('password')
        department = request.form.get('department')
        warehouse_name = request.form.get('warehouse_name')
        # 用户验证
        if (storage_keeper_validate(engine, username, password, department)):
            # 获取模型
            data_model = order_sheet.OrderSheet(engine)
            result = data_model.get_order_sheets_by_warehouse_name(warehouse_name)
            if (result != UNKNOWN_ERROR):
                return successful(data_model, result)
            else:
                return failed(data_model, data={'code': result})
        else:
            return validate_not_pass()
    except Exception as e:
        print(e)
        return exception()


@storage_keeper.route('/get_order_sheet_details', methods=['POST'])
def get_order_sheet_details():
    try:
        # 从客户端获取数据
        username = request.form.get('username')
        password = request.form.get('password')
        department_name = request.form.get('department_name')
        order_sheet_code = request.form.get('order_sheet_code')
        # 用户验证
        if (storage_keeper_validate(engine, username, password, department_name)):
            # 获取模型
            data_model = order_sheet_details.OrderSheetDetail(engine)
            result = data_model.get_order_sheet_by_order_sheet_code(order_sheet_code)
            if (result != UNKNOWN_ERROR):
                return successful(data_model, result)
            else:
                return failed(data_model, data={'code': result})
        else:
            return validate_not_pass()
    except Exception as e:
        print(e)
        return exception()


###############################
# 入库模块
###############################
@storage_keeper.route('/add_in_storage_sheet', methods=['POST'])
def add_in_storage_sheet():
    try:
        # 从客户端获取数据
        username = request.form.get('username')
        password = request.form.get('password')
        department = request.form.get('department')
        code = request.form.get('code')
        order_sheet_code = request.form.get('order_sheet_code')
        warehouse_name = request.form.get('warehouse_name')
        in_storage_date = request.form.get('in_storage_date')
        handler_name = request.form.get('handler_name')

        # 用户验证
        if (storage_keeper_validate(engine, username, password, department)):
            # 获取模型
            data_model = in_storage_sheet.InStorageSheet(engine)
            statue = data_model.create_in_storage_sheet(code=code, order_sheet_code=order_sheet_code,
                                                        warehouse_name=warehouse_name, in_storage_date=in_storage_date,
                                                        handler_name=handler_name)
            if (statue == SUCCESS):
                return successful(data_model, {'code': statue})
            else:
                return failed(data_model, data={'code': statue})
        else:
            return validate_not_pass()
    except Exception as e:
        print(e)
        return exception()


@storage_keeper.route('/get_in_storage_sheets_by_warehouse_name', methods=['POST'])
def get_in_storage_sheets_by_warehouse_name():
    try:
        # 从客户端获取数据
        username = request.form.get('username')
        password = request.form.get('password')
        department = request.form.get('department')
        warehouse_name = request.form.get('warehouse_name')
        # 用户验证
        if (storage_keeper_validate(engine, username, password, department)):
            # 获取模型
            data_model = in_storage_sheet.InStorageSheet(engine)
            result = data_model.get_in_storage_sheets_by_warehouse_name(warehouse_name)
            if (result != UNKNOWN_ERROR):
                return successful(data_model, result)
            else:
                return failed(data_model, data={'code': result})
        else:
            return validate_not_pass()
    except Exception as e:
        print(e)
        return exception()


###############################
# 入库详单模块
###############################
@storage_keeper.route('/add_in_storage_sheet_detail', methods=['POST'])
def add_in_storage_sheet_detail():
    try:
        # 从客户端获取数据
        username = request.form.get('username')
        password = request.form.get('password')
        department = request.form.get('department')
        in_storage_sheet_code = request.form.get('in_storage_sheet_code')
        commodity_code = request.form.get('commodity_code')
        number = request.form.get('number')
        # 用户验证
        if (storage_keeper_validate(engine, username, password, department)):
            # 获取模型
            data_model = in_storage_sheet_details.InStorageSheetDetail(engine)
            statue = data_model.create_in_storage_sheet_detail(in_storage_sheet_code=in_storage_sheet_code,
                                                               commodity_code=commodity_code, number=number)
            if (statue == SUCCESS):
                return successful(data_model, {'code': statue})
            else:
                return failed(data_model, data={'code': statue})
        else:
            return validate_not_pass()
    except Exception as e:
        print(e)
        return exception()


@storage_keeper.route('/get_in_storage_sheet_details', methods=['POST'])
def get_in_storage_sheet_details():
    try:
        # 从客户端获取数据
        username = request.form.get('username')
        password = request.form.get('password')
        department = request.form.get('department')
        in_storage_sheet_code = request.form.get('in_storage_sheet_code')
        # 用户验证
        if (storage_keeper_validate(engine, username, password, department)):
            # 获取模型
            data_model = in_storage_sheet_details.InStorageSheetDetail(engine)
            result = data_model.get_in_storage_sheet_details(in_storage_sheet_code)
            if (result != UNKNOWN_ERROR):
                return successful(data_model, result)
            else:
                return failed(data_model, data={'code': result})
        else:
            return validate_not_pass()
    except Exception as e:
        print(e)
        return exception()
###############################
# 出库模块
###############################

@storage_keeper.route('/add_ex_storage_sheet', methods=['POST'])
def add_ex_storage_sheet():
    try:
        # 从客户端获取数据
        username = request.form.get('username')
        password = request.form.get('password')
        department = request.form.get('department')
        code = request.form.get('code')
        warehouse_name = request.form.get('warehouse_name')
        date = request.form.get('date')
        handler_name = request.form.get('handler_name')
        # 用户验证
        if (storage_keeper_validate(engine, username, password, department)):
            # 获取模型
            data_model = ex_storage_sheet.ExStorageSheet(engine)
            statue = data_model.create_ex_storage_sheet(code, warehouse_name, date, handler_name)
            if (statue == SUCCESS):
                return successful(data_model, {'code': statue})
            else:
                return failed(data_model, data={'code': statue})
        else:
            return validate_not_pass()
    except Exception as e:
        print(e)
        return exception()


# @storage_keeper.route('/delete_ex_storage_sheet', methods=['POST'])
# def delete_ex_storage_sheet():
#     try:
#         # 从客户端获取数据
#         username = request.form.get('username')
#         password = request.form.get('password')
#         department_name = request.form.get('department_name')
#         ex_storage_sheet_id = request.form.get('ex_storage_sheet_id')
#         # 用户验证
#         if (storage_keeper_validate(engine, username, password, department_name)):
#             # 获取模型
#             data_model = ex_storage_sheet.ExStorageSheet(engine)
#             statue = data_model.delete_ex_storage_sheet(ex_storage_sheet_id=ex_storage_sheet_id)
#             if (statue == SUCCESS):
#                 return successful(data_model, {'code': statue})
#             else:
#                 return failed(data_model, data={'code': statue})
#         else:
#             return validate_not_pass()
#     except Exception as e:
#         print(e)
#         return exception()
#
#
# @storage_keeper.route('/change_ex_storage_sheet', methods=['POST'])
# def change_ex_storage_sheet():
#     pass
#
#
@storage_keeper.route('/get_all_ex_storage_sheets', methods=['POST'])
def get_all_ex_storage_sheets():
    try:
        # 从客户端获取数据
        username = request.form.get('username')
        password = request.form.get('password')
        department = request.form.get('department')
        warehouse_name = request.form.get('warehouse_name')
        # 用户验证
        if (storage_keeper_validate(engine, username, password, department)):
            # 获取模型
            data_model = ex_storage_sheet.ExStorageSheet(engine)
            result = data_model.get_all_ex_storage_sheets_by_warehouse(warehouse_name)
            if (result != UNKNOWN_ERROR):
                return successful(data_model, result)
            else:
                return failed(data_model, data={'code': result})
        else:
            return validate_not_pass()
    except Exception as e:
        print(e)
        return exception()
#
#
# ###############################
# # 出库详单模块
# ###############################

@storage_keeper.route('/add_ex_storage_sheet_detail', methods=['POST'])
def add_ex_storage_sheet_detail():
    try:
        # 从客户端获取数据
        username = request.form.get('username')
        password = request.form.get('password')
        department = request.form.get('department')
        ex_storage_sheet_code = request.form.get('ex_storage_sheet_code')
        commodity_code = request.form.get('commodity_code')
        number = request.form.get('number')
        # 用户验证
        if (storage_keeper_validate(engine, username, password, department)):
            # 获取模型
            data_model = ex_storage_sheet_details.ExStorageSheetDetails(engine)
            statue = data_model.create_ex_storage_sheet_detail(ex_storage_sheet_code, commodity_code, number)
            if (statue == SUCCESS):
                return successful(data_model, {'code': statue})
            else:
                return failed(data_model, data={'code': statue})
        else:
            return validate_not_pass()
    except Exception as e:
        print(e)
        return exception()
#
#
# @storage_keeper.route('/delete_ex_storage_sheet_detail', methods=['POST'])
# def delete_ex_storage_sheet_detail():
#     try:
#         # 从客户端获取数据
#         username = request.form.get('username')
#         password = request.form.get('password')
#         department_name = request.form.get('department_name')
#         id = request.form.get('id')
#         # 用户验证
#         if (storage_keeper_validate(engine, username, password, department_name)):
#             # 获取模型
#             data_model = ex_storage_sheet_details.ExStorageSheetDetails(engine)
#             statue = data_model.delete_ex_storage_sheet_detail(id=id)
#             if (statue == SUCCESS):
#                 return successful(data_model, {'code': statue})
#             else:
#                 return failed(data_model, data={'code': statue})
#         else:
#             return validate_not_pass()
#     except Exception as e:
#         print(e)
#         return exception()
#
#
# @storage_keeper.route('/change_ex_storage_sheet_detail', methods=['POST'])
# def change_ex_storage_sheet_detail():
#     try:
#         # 从客户端获取数据
#         username = request.form.get('username')
#         password = request.form.get('password')
#         department_name = request.form.get('department_name')
#         origin_id = request.form.get('origin_id')
#         dest_id = request.form.get('dest_id')
#         dest_ex_storage_sheet_id = request.form.get('dest_ex_storage_sheet_id')
#         dest_commodity_name = request.form.get('dest_commodity_name')
#         dest_number = request.form.get('dest_number')
#         # 用户验证
#         if (storage_keeper_validate(engine, username, password, department_name)):
#             # 获取模型
#             data_model = ex_storage_sheet_details.ExStorageSheetDetails(engine)
#             statue = data_model.change_ex_storage_sheet_detail(origin_id=origin_id, dest_id=dest_id,
#                                                                dest_ex_storage_sheet_id=dest_ex_storage_sheet_id,
#                                                                dest_commodity_name=dest_commodity_name,
#                                                                dest_number=dest_number)
#             if (statue == SUCCESS):
#                 return successful(data_model, {'code': statue})
#             else:
#                 return failed(data_model, data={'code': statue})
#         else:
#             return validate_not_pass()
#     except Exception as e:
#         print(e)
#         return exception()
#
#
# @storage_keeper.route('/get_ex_storage_sheet_details', methods=['POST'])
# def get_all_ex_storage_sheet_details():
#     try:
#         # 从客户端获取数据
#         username = request.form.get('username')
#         password = request.form.get('password')
#         department_name = request.form.get('department_name')
#         # 用户验证
#         if (storage_keeper_validate(engine, username, password, department_name)):
#             # 获取模型
#             data_model = ex_storage_sheet_details.ExStorageSheetDetails(engine)
#             result = data_model.get_all_ex_storage_sheet_details()
#             if (result != UNKNOWN_ERROR):
#                 return successful(data_model, result)
#             else:
#                 return failed(data_model, data={'code': result})
#         else:
#             return validate_not_pass()
#     except Exception as e:
#         print(e)
#         return exception()
#

################################
#  其他查询模块
###############################
@storage_keeper.route('/get_all_commodities', methods=['POST'])
def get_all_commodities():
    try:
        # 从客户端获取数据
        username = request.form.get('username')
        password = request.form.get('password')
        department = request.form.get('department')
        # 用户验证
        if (storage_keeper_validate(engine, username, password, department)):
            # 获取模型
            data_model = commodity.Commodity(engine)
            result = data_model.get_all_commodities()
            if (result != UNKNOWN_ERROR):
                return successful(data_model, result)
            else:
                return failed(data_model, data={'code': result})
        else:
            return validate_not_pass()
    except Exception as e:
        print(e)
        return exception()


@storage_keeper.route('/get_warehouse_by_manager_name', methods=['POST'])
def get_warehouse_by_manager_name():
    try:
        # 从客户端获取数据
        username = request.form.get('username')
        password = request.form.get('password')
        department = request.form.get('department')
        # 用户验证
        if (storage_keeper_validate(engine, username, password, department)):
            # 获取模型
            data_model = warehouse.Warehouse(engine)
            result = data_model.get_warehouse_by_manager_name(username)
            if (result != UNKNOWN_ERROR):
                return successful(data_model, result)
            else:
                return failed(data_model, data={'code': result})
        else:
            return validate_not_pass()
    except Exception as e:
        print(e)
        return exception()


@storage_keeper.route('/get_stock_details', methods=['POST'])
def get_stock_details():
    try:
        # 从客户端获取数据
        username = request.form.get('username')
        password = request.form.get('password')
        department = request.form.get('department')
        warehouse_name = request.form.get('warehouse_name')
        # 用户验证
        if (storage_keeper_validate(engine, username, password, department)):
            # 获取模型
            data_model = commodity_static.CommodityStatic(engine)
            result = data_model.get_stock_details(warehouse_name)
            if (result != UNKNOWN_ERROR):
                return successful(data_model, result)
            else:
                return failed(data_model, data={'code': result})
        else:
            return validate_not_pass()
    except Exception as e:
        print(e)
        return exception()
