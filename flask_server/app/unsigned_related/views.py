from flask import Blueprint
from sqlalchemy import create_engine

from flask_server.model import *
from flask_server.public.public_fun import successful

# 蓝图模块
unsigned_related = Blueprint('unsigned_related', __name__)
# 数据库连接引擎
engine = create_engine("mysql+pymysql://root:Zxw11071205@127.0.0.1:3306/stock_control",
                                    encoding='utf8', echo=False, max_overflow=100)

@unsigned_related.route('/get_all_departments', methods=['POST'])
def get_all_departments():
    data_model = department.Department()
    data = data_model.get_all_departments()
    return successful(data_model, data)