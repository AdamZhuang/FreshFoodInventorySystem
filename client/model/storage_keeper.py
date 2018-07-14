import requests
from client.public.public_func import *


class StorageKeeper(object):
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
                statue, data = self.get_warehouse_by_manager_name()
                if (statue == True):
                    self.warehouse_name = data['name']
                    return True
                else:
                    return False
            else:
                return False
        except Exception as e:
            return str(e)

    ##########################
    # 采购单操作
    ##########################
    def get_order_sheets_by_warehouse_name(self):
        try:
            data = {'username': self.name,
                    'password': self.encryption_password,
                    'department': self.department,
                    'warehouse_name': self.warehouse_name,
                    }
            url = '{server_address}/storage_keeper/get_order_sheets_by_warehouse_name'
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
                    'department_name': self.department,
                    'order_sheet_code': order_sheet_code
                    }
            url = '{server_address}/storage_keeper/get_order_sheet_details'
            url = url.format(server_address=self.server_address)
            result = requests.post(url=url, data=data)
            result_dict = json_str_to_dict(result.text)
            if (result_dict['statue'] == 'successful'):
                return True, result_dict['data']
            else:
                return False, result_dict['data']
        except Exception as e:
            return False, str(e)

    ##########################
    # 入库单操作
    ##########################
    def add_in_storage_sheet(self, code, order_sheet_code, warehouse_name, in_storage_date, handler_name):
        try:
            data = {'username': self.name,
                    'password': self.encryption_password,
                    'department': self.department,
                    'code': code,
                    'order_sheet_code': order_sheet_code,
                    'warehouse_name': warehouse_name,
                    'in_storage_date': in_storage_date,
                    'handler_name': handler_name,
                    }
            url = '{server_address}/storage_keeper/add_in_storage_sheet'
            url = url.format(server_address=self.server_address)
            result = requests.post(url=url, data=data)
            result_dict = json_str_to_dict(result.text)
            if (result_dict['statue'] == 'successful'):
                return True, result_dict['data']
            else:
                return False, result_dict['data']
        except Exception as e:
            return False, str(e)

    def add_in_storage_sheet_details(self, in_storage_sheet_code, commodity_code, number):
        try:
            data = {'username': self.name,
                    'password': self.encryption_password,
                    'department': self.department,
                    'in_storage_sheet_code': in_storage_sheet_code,
                    'commodity_code': commodity_code,
                    'number': number,
                    }
            url = '{server_address}/storage_keeper/add_in_storage_sheet_detail'
            url = url.format(server_address=self.server_address)
            result = requests.post(url=url, data=data)
            result_dict = json_str_to_dict(result.text)
            if (result_dict['statue'] == 'successful'):
                return True, result_dict['data']
            else:
                return False, result_dict['data']
        except Exception as e:
            return False, str(e)

    def get_in_storage_sheets_by_warehouse_name(self):
        try:
            data = {'username': self.name,
                    'password': self.encryption_password,
                    'department': self.department,
                    'warehouse_name': self.warehouse_name,
                    }
            url = '{server_address}/storage_keeper/get_in_storage_sheets_by_warehouse_name'
            url = url.format(server_address=self.server_address)
            result = requests.post(url=url, data=data)
            result_dict = json_str_to_dict(result.text)
            if (result_dict['statue'] == 'successful'):
                return True, result_dict['data']
            else:
                return False, result_dict['data']
        except Exception as e:
            return False, str(e)

    def get_in_storage_sheet_details(self, in_storage_sheet_code):
        try:
            data = {'username': self.name,
                    'password': self.encryption_password,
                    'department': self.department,
                    'in_storage_sheet_code': in_storage_sheet_code
                    }
            url = '{server_address}/storage_keeper/get_in_storage_sheet_details'
            url = url.format(server_address=self.server_address)
            result = requests.post(url=url, data=data)
            result_dict = json_str_to_dict(result.text)
            if (result_dict['statue'] == 'successful'):
                return True, result_dict['data']
            else:
                return False, result_dict['data']
        except Exception as e:
            return False, str(e)

    ##########################
    # 出库单操作
    ##########################
    def add_ex_storage_sheet(self, code, warehouse_name, date, handler_name):
        try:
            data = {'username': self.name,
                    'password': self.encryption_password,
                    'department': self.department,
                    'code': code,
                    'warehouse_name': warehouse_name,
                    'date': date,
                    'handler_name': handler_name
                    }
            url = '{server_address}/storage_keeper/add_ex_storage_sheet'
            url = url.format(server_address=self.server_address)
            result = requests.post(url=url, data=data)
            result_dict = json_str_to_dict(result.text)
            if (result_dict['statue'] == 'successful'):
                return True, result_dict['data']
            else:
                return False, result_dict['data']
        except Exception as e:
            return False, str(e)

    def add_ex_storage_sheet_details(self, ex_storage_sheet_code, commodity_code, number):
        try:
            data = {'username': self.name,
                    'password': self.encryption_password,
                    'department': self.department,
                    'ex_storage_sheet_code': ex_storage_sheet_code,
                    'commodity_code': commodity_code,
                    'number': number,
                    }
            url = '{server_address}/storage_keeper/add_ex_storage_sheet_detail'
            url = url.format(server_address=self.server_address)
            result = requests.post(url=url, data=data)
            result_dict = json_str_to_dict(result.text)
            if (result_dict['statue'] == 'successful'):
                return True, result_dict['data']
            else:
                return False, result_dict['data']
        except Exception as e:
            return False, str(e)

    def get_all_ex_storage_sheets(self):
        try:
            data = {'username': self.name,
                    'password': self.encryption_password,
                    'department': self.department,
                    'warehouse_name': self.warehouse_name,
                    }
            url = '{server_address}/storage_keeper/get_all_ex_storage_sheets'
            url = url.format(server_address=self.server_address)
            result = requests.post(url=url, data=data)
            result_dict = json_str_to_dict(result.text)
            if (result_dict['statue'] == 'successful'):
                return True, result_dict['data']
            else:
                return False, result_dict['data']
        except Exception as e:
            return False, str(e)

    def get_ex_storage_sheet_details(self, ex_storage_sheet_id):
        try:
            data = {'username': self.name,
                    'password': self.encryption_password,
                    'department_name': self.department,
                    'warehouse_name': self.warehouse_name,
                    'ex_storage_sheet_id': ex_storage_sheet_id
                    }
            url = '{server_address}/storage_keeper/get_ex_storage_sheet_details'
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
    def get_commodities(self):
        try:
            data = {'username': self.name,
                    'password': self.encryption_password,
                    'department_name': self.department,
                    }
            url = '{server_address}/storage_keeper/get_all_commodities'
            url = url.format(server_address=self.server_address)
            result = requests.post(url=url, data=data)
            result_dict = json_str_to_dict(result.text)
            if (result_dict['statue'] == 'successful'):
                return True, result_dict['data']
            else:
                return False, result_dict['data']
        except Exception as e:
            return False, str(e)

    def get_warehouse_by_manager_name(self):
        try:
            data = {'username': self.name,
                    'password': self.encryption_password,
                    'department': self.department,
                    }
            url = '{server_address}/storage_keeper/get_warehouse_by_manager_name'
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
                    'warehouse_name': self.warehouse_name,
                    }
            url = '{server_address}/storage_keeper/get_stock_details'
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
        storage_keeper = StorageKeeper('http://127.0.0.1:5000', '3', '3', '仓库管理员')
        storage_keeper.login()
        # print(storage_keeper.get_order_sheets())
        # print(storage_keeper.get_order_sheet_details('001'))
        # print(storage_keeper.get_warehouse_by_manager_name())
        # print(storage_keeper.add_in_storage_sheet('00001', '001', '北邮', str(datetime.datetime.now()), '3'))
        # print(storage_keeper.add_in_storage_sheet_details('00001','赣南脐橙',3))
        # print(storage_keeper.get_in_storage_sheets_by_warehouse_name())
        print(storage_keeper.get_in_storage_sheet_details('00001'))
    except Exception as e:
        print(e)
