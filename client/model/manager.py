import requests

from client.public.public_func import *


class Manager(object):
    def __init__(self, server_address, name, password, department):
        self.server_address = server_address
        self.name = name
        self.origin_password = password
        self.encryption_password = ''
        self.department = department

    def login(self):
        try:
            data = {'username': self.name,
                    'password': self.origin_password,
                    'department': self.department}
            url = '{server_address}/account_validate/validate'
            url = url.format(server_address=self.server_address)
            result = requests.post(url=url, data=data)
            result_dict = json_str_to_dict(result.text)
            if (result_dict['statue'] == 'successful'):
                self.encryption_password = result_dict['data']['password']
                return True
            else:
                return False
        except Exception as e:
            return str(e)

    ##########################
    # 订货通知单操作
    ##########################
    def add_notice_sheet(self, code, warehouse_name, order_man_name, delivery_date, notice_date, statue, handler_name):
        try:
            data = {'username': self.name,
                    'password': self.encryption_password,
                    'department': self.department,
                    'code': code,
                    'warehouse_name': warehouse_name,
                    'order_man_name': order_man_name,
                    'delivery_date': delivery_date,
                    'notice_date': notice_date,
                    'statue': statue,
                    'handler_name': handler_name,
                    }
            url = '{server_address}/manager/add_notice_sheet'
            url = url.format(server_address=self.server_address)
            result = requests.post(url=url, data=data)
            result_dict = json_str_to_dict(result.text)
            if (result_dict['statue'] == 'successful'):
                return True, result_dict['data']
            else:
                return False, result_dict['data']
        except Exception as e:
            return False, str(e)

    def add_notice_sheet_details(self, notice_sheet_code, commodity_code, number, price):
        try:
            data = {'username': self.name,
                    'password': self.encryption_password,
                    'department': self.department,
                    'notice_sheet_code': notice_sheet_code,
                    'commodity_code': commodity_code,
                    'number': number,
                    'price': price,
                    }
            url = '{server_address}/manager/add_notice_sheet_detail'
            url = url.format(server_address=self.server_address)
            result = requests.post(url=url, data=data)
            result_dict = json_str_to_dict(result.text)
            if (result_dict['statue'] == 'successful'):
                return True, result_dict['data']
            else:
                return False, result_dict['data']
        except Exception as e:
            return False, str(e)

    def delete_notice_sheet(self, notice_sheet_id):
        try:
            data = {'username': self.name,
                    'password': self.encryption_password,
                    'department_name': self.department,
                    'notice_sheet_id': notice_sheet_id,
                    }
            url = '{server_address}/manager/delete_notice_sheet_id'
            url = url.format(server_address=self.server_address)
            result = requests.post(url=url, data=data)
            result_dict = json_str_to_dict(result.text)
            if (result_dict['statue'] == 'successful'):
                return True, result_dict['data']
            else:
                return False, result_dict['data']
        except Exception as e:
            return False, str(e)

    def get_all_notice_sheets(self):
        try:
            data = {'username': self.name,
                    'password': self.encryption_password,
                    'department': self.department
                    }
            url = '{server_address}/manager/get_all_notice_sheets'
            url = url.format(server_address=self.server_address)
            result = requests.post(url=url, data=data)
            result_dict = json_str_to_dict(result.text)
            if (result_dict['statue'] == 'successful'):
                return True, result_dict['data']
            else:
                return False, result_dict['data']
        except Exception as e:
            return False, str(e)

    def get_notice_sheet_details(self, notice_sheet_code):
        try:
            data = {'username': self.name,
                    'password': self.encryption_password,
                    'department': self.department,
                    'notice_sheet_code': notice_sheet_code
                    }
            url = '{server_address}/manager/get_notice_sheet_details'
            url = url.format(server_address=self.server_address)
            result = requests.post(url=url, data=data)
            result_dict = json_str_to_dict(result.text)
            if (result_dict['statue'] == 'successful'):
                return True, result_dict['data']
            else:
                return False, result_dict['data']
        except Exception as e:
            return False, str(e)

    def change_order_sheet_statue(self, order_sheet_id, statue):
        try:
            data = {'username': self.name,
                    'password': self.encryption_password,
                    'department_name': self.department,
                    'order_sheet_id': order_sheet_id,
                    'statue': statue,
                    }
            url = '{server_address}/manager/change_order_sheet_statue'
            url = url.format(server_address=self.server_address)
            result = requests.post(url=url, data=data)
            result_dict = json_str_to_dict(result.text)
            if (result_dict['statue'] == 'successful'):
                return True, result_dict['data']
            else:
                return False, result_dict['data']
        except Exception as e:
            return False, str(e)

    ###################
    # 其他操作
    ###################
    def get_all_commodities(self):
        try:
            data = {'username': self.name,
                    'password': self.encryption_password,
                    'department_name': self.department,
                    }
            url = '{server_address}/manager/get_all_commodities'
            url = url.format(server_address=self.server_address)
            result = requests.post(url=url, data=data)
            result_dict = json_str_to_dict(result.text)
            if (result_dict['statue'] == 'successful'):
                return True, result_dict['data']
            else:
                return False, result_dict['data']
        except Exception as e:
            return False, str(e)

    def get_all_warehouses(self):
        try:
            data = {'username': self.name,
                    'password': self.encryption_password,
                    'department': self.department,
                    }
            url = '{server_address}/manager/get_all_warehouses'
            url = url.format(server_address=self.server_address)
            result = requests.post(url=url, data=data)
            result_dict = json_str_to_dict(result.text)
            if (result_dict['statue'] == 'successful'):
                return True, result_dict['data']
            else:
                return False, result_dict['data']
        except Exception as e:
            return False, str(e)

    def get_all_order_man(self):
        try:
            data = {'username': self.name,
                    'password': self.encryption_password,
                    'department': self.department,
                    }
            url = '{server_address}/manager/get_all_order_man'
            url = url.format(server_address=self.server_address)
            result = requests.post(url=url, data=data)
            result_dict = json_str_to_dict(result.text)
            if (result_dict['statue'] == 'successful'):
                return True, result_dict['data']
            else:
                return False, result_dict['data']
        except Exception as e:
            return False, str(e)

    def get_stock_details(self):
        try:
            data = {'username': self.name,
                    'password': self.encryption_password,
                    'department': self.department,
                    }
            url = '{server_address}/manager/get_stock_details'
            url = url.format(server_address=self.server_address)
            result = requests.post(url=url, data=data)
            result_dict = json_str_to_dict(result.text)
            if (result_dict['statue'] == 'successful'):
                return True, result_dict['data']
            else:
                return False, result_dict['data']
        except Exception as e:
            return False, str(e)


if __name__ == '__main__':
    import datetime

    try:
        manager = Manager('http://127.0.0.1:5000', '1', '1', '经理')
        manager.login()
        print(manager.add_notice_sheet('2018', '北邮', '2', str(datetime.datetime.now()),
                                       str(datetime.datetime.now()), '未处理', '1'))
        # # print(manager.get_all_notice_sheets())
        print(manager.add_notice_sheet_details('2018', '10001', 10, 100))
        print(manager.add_notice_sheet_details('2018', '10002', 20, 200))
        # print(manager.add_notice_sheet_details
        # print(manager.get_notice_sheet_details('201806170001'))
        # print(manager.get_all_commodities())
        # print(manager.get_all_warehouses())
        # print(manager.get_all_order_man())
        # print()
    except Exception as e:
        print(e)
