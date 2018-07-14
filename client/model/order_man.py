import requests
from client.public.public_func import *


class OrderMan(object):
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

    def get_notice_sheets_by_order_man_name(self, order_man_name):
        try:
            data = {'username': self.name,
                    'password': self.encryption_password,
                    'department': self.department,
                    'order_man_name': order_man_name,
                    }
            url = '{server_address}/order_man/get_notice_sheets_by_order_man_name'
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
                    'notice_sheet_code': notice_sheet_code,
                    }
            url = '{server_address}/order_man/get_notice_sheet_details'
            url = url.format(server_address=self.server_address)
            result = requests.post(url=url, data=data)
            result_dict = json_str_to_dict(result.text)
            if (result_dict['statue'] == 'successful'):
                return True, result_dict['data']
            else:
                return False, result_dict['data']
        except Exception as e:
            return False, str(e)

    def add_order_sheet(self, code, notice_sheet_code, warehouse_name, order_man_name, delivery_date, order_date,
                        statue, handler_name):
        try:
            data = {'username': self.name,
                    'password': self.encryption_password,
                    'department_name': self.department,
                    'code': code,
                    'notice_sheet_code': notice_sheet_code,
                    'warehouse_name': warehouse_name,
                    'order_man_name': order_man_name,
                    'delivery_date': delivery_date,
                    'order_date': order_date,
                    'statue': statue,
                    'handler_name': handler_name,
                    }
            url = '{server_address}/order_man/add_order_sheet'
            url = url.format(server_address=self.server_address)
            result = requests.post(url=url, data=data)
            result_dict = json_str_to_dict(result.text)
            if (result_dict['statue'] == 'successful'):
                return True, result_dict['data']
            else:
                return False, result_dict['data']
        except Exception as e:
            return False, str(e)

    def add_order_sheet_details(self, order_sheet_code, commodity_code, number, price):
        try:
            data = {'username': self.name,
                    'password': self.encryption_password,
                    'department': self.department,
                    'order_sheet_code': order_sheet_code,
                    'commodity_code': commodity_code,
                    'number': number,
                    'price': price,
                    }
            url = '{server_address}/order_man/add_order_sheet_detail'
            url = url.format(server_address=self.server_address)
            result = requests.post(url=url, data=data)
            result_dict = json_str_to_dict(result.text)
            if (result_dict['statue'] == 'successful'):
                return True, result_dict['data']
            else:
                return False, result_dict['data']
        except Exception as e:
            return False, str(e)

    def get_order_sheets(self, order_man_name):
        try:
            data = {'username': self.name,
                    'password': self.encryption_password,
                    'department': self.department,
                    'order_man_name': order_man_name,
                    }
            url = '{server_address}/order_man/get_order_sheets'
            url = url.format(server_address=self.server_address)
            result = requests.post(url=url, data=data)
            result_dict = json_str_to_dict(result.text)
            if (result_dict['statue'] == 'successful'):
                return True, result_dict['data']
            else:
                return False, result_dict['data']
        except Exception as e:
            return False, str(e)

    def get_order_sheet_details(self, order_sheet_code):
        try:
            data = {'username': self.name,
                    'password': self.encryption_password,
                    'department': self.department,
                    'order_sheet_code': order_sheet_code,
                    }
            url = '{server_address}/order_man/get_order_sheet_details'
            url = url.format(server_address=self.server_address)
            result = requests.post(url=url, data=data)
            result_dict = json_str_to_dict(result.text)
            if (result_dict['statue'] == 'successful'):
                return True, result_dict['data']
            else:
                return False, result_dict['data']
        except Exception as e:
            return False, str(e)

    def change_order_sheet_statue(self, order_sheet_code, statue):
        try:
            data = {'username': self.name,
                    'password': self.encryption_password,
                    'department': self.department,
                    'order_sheet_code': order_sheet_code,
                    'statue': statue,
                    }
            url = '{server_address}/order_man/change_order_sheet_statue'
            url = url.format(server_address=self.server_address)
            result = requests.post(url=url, data=data)
            result_dict = json_str_to_dict(result.text)
            if (result_dict['statue'] == 'successful'):
                return True, result_dict['data']
            else:
                return False, result_dict['data']
        except Exception as e:
            return False, str(e)
            #
            # def get_warehouse_name(self):
            #     try:
            #         data = {'username': self.name,
            #                 'password': self.encryption_password,
            #                 'department_name': self.department,
            #                 }
            #         url = '{server_address}/order_man/get_warehouse_name'
            #         url = url.format(server_address=self.server_address)
            #         result = requests.post(url=url, data=data)
            #         result_dict = json_str_to_dict(result.text)
            #         if (result_dict['statue'] == 'successful'):
            #             return True, result_dict['data']
            #         else:
            #             return False, result_dict['data']
            #     except Exception as e:
            #         return False, str(e)


if __name__ == '__main__':
    import datetime

    try:
        order_man = OrderMan('http://127.0.0.1:5000', '2', '2', '采购员')
        order_man.login()
        # print(order_man.get_notice_sheets_by_order_man_name(order_man.name))
        # print(order_man.get_notice_sheet_details('2018'))
        print(order_man.add_order_sheet('001', '2018', '北邮', '2', str(datetime.datetime.now()),
                                        str(datetime.datetime.now()), '未处理', '2'))
        print(order_man.add_order_sheet_details('001', '10001', 10, 100))
        print(order_man.add_order_sheet_details('001', '10002', 20, 200))
        # print(order_man.get_order_sheets('2'))
        # print(order_man.get_order_sheet_details('001'))
        # print(order_man.change_order_sheet_statue('001', '已购买'))
    except Exception as e:
        print(e)
