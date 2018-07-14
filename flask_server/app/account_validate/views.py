from flask import Blueprint, request
from sqlalchemy import create_engine

from flask_server.model import *
from flask_server.public.public_fun import successful, failed, exception

# 蓝图模块
account_validate = Blueprint('account_validate', __name__)
# 数据库连接引擎
engine = create_engine("mysql+pymysql://root:Zxw11071205@127.0.0.1:3306/stock_control",
                                    encoding='utf8', echo=False, max_overflow=100)


@account_validate.route('/validate', methods=['POST'])
def validate():
    try:
        # 从客户端获取数据
        username = request.form.get('username')
        password = request.form.get('password')
        department = request.form.get('department')
        # 获取模型
        data_model = user.User(engine)
        if(data_model.validate_by_origin_password(name=username, password=password, department_name=department)):
            data = data_model.get_password(username)
            return successful(data_model, data)
        else:
            return failed(data_model,{})
    except Exception as e:
        print(e)
        return exception()