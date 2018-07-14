from flask import Flask



def create_app():
    app = Flask(__name__)

    # 未登陆操作模块
    from flask_server.app.unsigned_related import unsigned_related
    app.register_blueprint(unsigned_related, url_prefix='/unsigned_related')
    # 账户模块（登陆）
    from flask_server.app.account_validate import account_validate
    app.register_blueprint(account_validate, url_prefix='/account_validate')
    # # 用户模块
    from flask_server.app.admin import admin
    app.register_blueprint(admin, url_prefix='/admin')
    # 经理模块
    from flask_server.app.manager import manager
    app.register_blueprint(manager, url_prefix='/manager')
    # 采购员模块
    from flask_server.app.order_man import order_man
    app.register_blueprint(order_man, url_prefix='/order_man')
    # 仓库管理员模块
    from flask_server.app.storage_keeper import storage_keeper
    app.register_blueprint(storage_keeper, url_prefix='/storage_keeper')




    return app



if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, )