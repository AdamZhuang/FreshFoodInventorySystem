from flask import Blueprint, request
from sqlalchemy import create_engine
from flask_server.model import *
from flask_server.public.public_fun import successful, failed, validate, validate_not_pass, exception
from flask_server.public.error_code import *

# 蓝图模块
manager = Blueprint('manager', __name__)
# 数据库连接引擎
engine = create_engine("mysql+pymysql://root:Zxw11071205@127.0.0.1:3306/stock_control",
                       encoding='utf8', echo=False, max_overflow=100)


# 登陆验证模块
def manager_validate(engine, username, password, department_name):
    # if(username != 'admin' or department_name != '系统管理员'):
    #     return False
    # else:
    return validate(engine, username, password, department_name)


@manager.route('/', methods=['POST'])
def manager_index():
    return 'manager index'


###############################
# 订货通知单模块
###############################

@manager.route('/add_notice_sheet', methods=['POST'])
def add_notice_sheet():
    try:
        # 从客户端获取数据
        username = request.form.get('username')
        password = request.form.get('password')
        department = request.form.get('department')
        code = request.form.get('code')
        warehouse_name = request.form.get('warehouse_name')
        order_man_name = request.form.get('order_man_name')
        delivery_date = request.form.get('delivery_date')
        notice_date = request.form.get('notice_date')
        statue = request.form.get('statue')
        handler_name = request.form.get('handler_name')
        # 用户验证
        if (manager_validate(engine, username, password, department)):
            # 获取模型
            data_model = notice_sheet.NoticeSheet(engine)
            statue = data_model.create_notice_sheet(code=code, warehouse_name=warehouse_name,
                                                    order_man_name=order_man_name, delivery_date=delivery_date,
                                                    notice_date=notice_date, statue=statue, handler_name=handler_name)
            if (statue == SUCCESS):
                return successful(data_model, {'code': statue})
            else:
                return failed(data_model, data={'code': statue})
        else:
            return validate_not_pass()
    except Exception as e:
        print(e)
        return exception()


# @manager.route('/delete_notice_sheet', methods=['POST'])
# def delete_notice_sheet():
#     try:
#         # 从客户端获取数据
#         username = request.form.get('username')
#         password = request.form.get('password')
#         department_name = request.form.get('department_name')
#         id = request.form.get('id')
#         # 用户验证
#         if (storage_keeper_validate(engine, username, password, department_name)):
#             # 获取模型
#             data_model = order_sheet.OrderSheet(engine)
#             statue = data_model.delete_order_sheet(id=id)
#             if (statue == SUCCESS):
#                 return successful(data_model, {'code': statue})
#             else:
#                 return failed(data_model, data={'code': statue})
#         else:
#             return validate_not_pass()
#     except Exception as e:
#         print(e)
#         return exception()


@manager.route('/get_all_notice_sheets', methods=['POST'])
def get_all_notice_sheets():
    try:
        # 从客户端获取数据
        username = request.form.get('username')
        password = request.form.get('password')
        department = request.form.get('department')
        # 用户验证
        if (manager_validate(engine, username, password, department)):
            # 获取模型
            data_model = notice_sheet.NoticeSheet(engine)
            result = data_model.get_all_notice_sheets()
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
# 订货通知详单模块
###############################

@manager.route('/add_notice_sheet_detail', methods=['POST'])
def add_notice_sheet_detail():
    try:
        # 从客户端获取数据
        username = request.form.get('username')
        password = request.form.get('password')
        department = request.form.get('department')
        notice_sheet_code = request.form.get('notice_sheet_code')
        commodity_code = request.form.get('commodity_code')
        number = request.form.get('number')
        price = request.form.get('price')

        # 用户验证
        if (manager_validate(engine, username, password, department)):
            # 获取模型
            data_model = notice_sheet_details.NoticeSheetDetails(engine)
            statue = data_model.create_notice_sheet_detail(notice_sheet_code=notice_sheet_code,
                                                           commodity_code=commodity_code, number=number, price=price)
            if (statue == SUCCESS):
                return successful(data_model, {'code': statue})
            else:
                return failed(data_model, data={'code': statue})
        else:
            return validate_not_pass()
    except Exception as e:
        print(e)
        return exception()


@manager.route('/get_notice_sheet_details', methods=['POST'])
def get_notice_sheet_details():
    try:
        # 从客户端获取数据
        username = request.form.get('username')
        password = request.form.get('password')
        department = request.form.get('department')
        notice_sheet_code = request.form.get('notice_sheet_code')
        # 用户验证
        if (manager_validate(engine, username, password, department)):
            # 获取模型
            data_model = notice_sheet_details.NoticeSheetDetails(engine)
            result = data_model.get_notice_sheet_details(notice_sheet_code)
            if (result != UNKNOWN_ERROR):
                return successful(data_model, result)
            else:
                return failed(data_model, data={'code': result})
        else:
            return validate_not_pass()
    except Exception as e:
        print(e)
        return exception()


################################
#  其他查询模块
###############################
@manager.route('/get_all_commodities', methods=["POST"])
def get_all_commodities():
    try:
        # 认证信息
        username = request.form.get('username')
        password = request.form.get('password')
        department_name = request.form.get('department_name')
        if (manager_validate(engine, username, password, department_name)):
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


@manager.route('/get_all_warehouses', methods=["POST"])
def get_all_warehouses():
    try:
        # 认证信息
        username = request.form.get('username')
        password = request.form.get('password')
        department = request.form.get('department')
        if (manager_validate(engine, username, password, department)):
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


@manager.route('/get_all_order_man', methods=['POST'])
def get_all_order_man():
    try:
        # 从客户端获取数据
        username = request.form.get('username')
        password = request.form.get('password')
        department = request.form.get('department')
        # 用户验证
        if (manager_validate(engine, username, password, department)):
            # 获取模型
            data_model = user.User(engine)
            result = data_model.get_all_user_in_department('采购员')
            if (result != UNKNOWN_ERROR):
                return successful(data_model, result)
            else:
                return failed(data_model, data={'code': result})
        else:
            return validate_not_pass()
    except Exception as e:
        print(e)
        return exception()

@manager.route('/get_stock_details', methods=['POST'])
def get_stock_details():
    try:
        # 从客户端获取数据
        username = request.form.get('username')
        password = request.form.get('password')
        department = request.form.get('department')
        # 用户验证
        if (manager_validate(engine, username, password, department)):
            # 获取模型
            data_model = commodity_static.CommodityStatic(engine)
            result = data_model.get_all_stock_details()
            if (result != UNKNOWN_ERROR):
                return successful(data_model, result)
            else:
                return failed(data_model, data={'code': result})
        else:
            return validate_not_pass()
    except Exception as e:
        print(e)
        return exception()
