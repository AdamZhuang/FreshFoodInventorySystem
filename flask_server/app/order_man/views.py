from flask import Blueprint, request
from sqlalchemy import create_engine
from flask_server.model import *
from flask_server.public.public_fun import successful, failed, validate, validate_not_pass, exception
from flask_server.public.error_code import *

# 蓝图模块
order_man = Blueprint('order_man', __name__)
# 数据库连接引擎
engine = create_engine("mysql+pymysql://root:Zxw11071205@127.0.0.1:3306/stock_control",
                       encoding='utf8', echo=False, max_overflow=100)


# 登陆验证模块
def storage_keeper_validate(engine, username, password, department_name):
    # if(username != 'admin' or department_name != '系统管理员'):
    #     return False
    # else:
    return validate(engine, username, password, department_name)


@order_man.route('/', methods=['POST'])
def manager_index():
    return 'manager index'


@order_man.route('/get_notice_sheets_by_order_man_name', methods=['POST'])
def get_notice_sheets_by_order_man_name():
    try:
        # 从客户端获取数据
        username = request.form.get('username')
        password = request.form.get('password')
        department = request.form.get('department')
        order_man_name = request.form.get('order_man_name')
        # 用户验证
        if (storage_keeper_validate(engine, username, password, department)):
            # 获取模型
            data_model = notice_sheet.NoticeSheet(engine)
            result = data_model.get_notice_sheets_by_order_man_name(order_man_name)
            if (result != UNKNOWN_ERROR):
                return successful(data_model, result)
            else:
                return failed(data_model, data={'code': result})
        else:
            return validate_not_pass()
    except Exception as e:
        print(e)
        return exception()


@order_man.route('/get_notice_sheet_details', methods=['POST'])
def get_notice_sheet_details():
    try:
        # 从客户端获取数据
        username = request.form.get('username')
        password = request.form.get('password')
        department = request.form.get('department')
        notice_sheet_code = request.form.get('notice_sheet_code')
        # 用户验证
        if (storage_keeper_validate(engine, username, password, department)):
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


@order_man.route('/add_order_sheet', methods=['POST'])
def add_order_sheet():
    try:
        # 从客户端获取数据
        username = request.form.get('username')
        password = request.form.get('password')
        department_name = request.form.get('department_name')
        code = request.form.get('code')
        notice_sheet_code = request.form.get('notice_sheet_code')
        warehouse_name = request.form.get('warehouse_name')
        order_man_name = request.form.get('order_man_name')
        delivery_date = request.form.get('delivery_date')
        order_date = request.form.get('order_date')
        statue = request.form.get('statue')
        handler_name = request.form.get('handler_name')

        # 用户验证
        if (storage_keeper_validate(engine, username, password, department_name)):
            # 获取模型
            data_model = order_sheet.OrderSheet(engine)
            result = data_model.create_order_sheet(code=code, notice_sheet_code=notice_sheet_code,
                                                   warehouse_name=warehouse_name, order_man_name=order_man_name,
                                                   delivery_date=delivery_date, order_date=order_date, statue=statue,
                                                   handler_name=handler_name)
            if (result != UNKNOWN_ERROR):
                return successful(data_model, result)
            else:
                return failed(data_model, data={'code': result})
        else:
            return validate_not_pass()
    except Exception as e:
        print(e)
        return exception()


@order_man.route('/add_order_sheet_detail', methods=['POST'])
def add_order_sheet_detail():
    try:
        # 从客户端获取数据
        username = request.form.get('username')
        password = request.form.get('password')
        department = request.form.get('department')
        order_sheet_code = request.form.get('order_sheet_code')
        commodity_code = request.form.get('commodity_code')
        number = request.form.get('number')
        price = request.form.get('price')
        # 用户验证
        if (storage_keeper_validate(engine, username, password, department)):
            # 获取模型
            data_model = order_sheet_details.OrderSheetDetail(engine)
            result = data_model.create_order_sheet_detail(order_sheet_code=order_sheet_code,
                                                          commodity_code=commodity_code, number=number, price=price)
            if (result != UNKNOWN_ERROR):
                return successful(data_model, result)
            else:
                return failed(data_model, data={'code': result})
        else:
            return validate_not_pass()
    except Exception as e:
        print(e)
        return exception()


@order_man.route('/get_order_sheets', methods=['POST'])
def get_order_sheets():
    try:
        # 从客户端获取数据
        username = request.form.get('username')
        password = request.form.get('password')
        department = request.form.get('department')
        order_man_name = request.form.get('order_man_name')
        # 用户验证
        if (storage_keeper_validate(engine, username, password, department)):
            # 获取模型
            data_model = order_sheet.OrderSheet(engine)
            result = data_model.get_order_sheets(order_man_name)
            if (result != UNKNOWN_ERROR):
                return successful(data_model, result)
            else:
                return failed(data_model, data={'code': result})
        else:
            return validate_not_pass()
    except Exception as e:
        print(e)


@order_man.route('/get_order_sheet_details', methods=['POST'])
def get_order_sheet_details():
    try:
        # 从客户端获取数据
        username = request.form.get('username')
        password = request.form.get('password')
        department = request.form.get('department')
        order_sheet_code = request.form.get('order_sheet_code')
        # 用户验证
        if (storage_keeper_validate(engine, username, password, department)):
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


@order_man.route('/change_order_sheet_statue', methods=['POST'])
def change_order_sheet_statue():
    try:
        # 从客户端获取数据
        username = request.form.get('username')
        password = request.form.get('password')
        department = request.form.get('department')
        order_sheet_code = request.form.get('order_sheet_code')
        statue = request.form.get('statue')
        # 用户验证
        if (storage_keeper_validate(engine, username, password, department)):
            # 获取模型
            data_model = order_sheet.OrderSheet(engine)
            result = data_model.change_order_sheet_statue(order_sheet_code, statue)
            if (result != UNKNOWN_ERROR):
                return successful(data_model, result)
            else:
                return failed(data_model, data={'code': result})
        else:
            return validate_not_pass()
    except Exception as e:
        print(e)
        return exception()
