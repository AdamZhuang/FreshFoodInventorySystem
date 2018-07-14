from flask import jsonify
from flask_server.model import *
from flask_server.public.error_code import *


def validate(engine, username, password, department):
    try:
        data_model = user.User(engine)
        result = data_model.validate_by_encryption_password(name=username, password=password, department=department)
        data_model.close()
        if(result == SUCCESS):
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False


def validate_not_pass():
    ret_data = {}
    ret_data['statue'] = 'validate not pass'
    return jsonify(ret_data)


def failed(data_model, data):
    ret_data = {}
    try:
        data_model.close()
        ret_data['data'] = data
        ret_data['statue'] = 'failed'
        return jsonify(ret_data)
    except Exception as e:
        print(e)
        ret_data['statue'] = 'failed'
        return jsonify(ret_data)


def successful(data_model, data):
    ret_data = {}
    try:
        data_model.close()
        ret_data['data'] = data
        ret_data['statue'] = 'successful'
        return jsonify(ret_data)
    except Exception as e:
        print(e)
        ret_data['statue'] = 'failed'
        return jsonify(ret_data)


def exception():
    ret_data = {}
    # ret_data['data'] = data
    ret_data['statue'] = 'exception'
    return jsonify(ret_data)