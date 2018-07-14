import requests

from client.public.public_func import *


class Admin(object):
    def __init__(self, server_address, name, password, department):
        self.server_address = server_address
        self.name = name
        self.origin_password = password
        self.encryption_password = ''
        self.department = department

    # @timeout(2, 'network_error')
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

    #########################
    # 用户管理模块
    #########################
    # @timeout(3, 'network_error')
    def add_user(self, add_username, add_user_password, add_user_contact, add_user_department):
        try:
            data = {'username': self.name,
                    'password': self.encryption_password,
                    'department': self.department,
                    'add_username': add_username,
                    'add_user_password': add_user_password,
                    'add_user_contact': add_user_contact,
                    'add_user_department': add_user_department
                    }
            url = '{server_address}/admin/add_user'
            url = url.format(server_address=self.server_address)
            result = requests.post(url=url, data=data)
            result_dict = json_str_to_dict(result.text)
            if (result_dict['statue'] == 'successful'):
                return True, result_dict['data']
            else:
                return False, result_dict['data']
        except Exception as e:
            # raise TimeoutError('e')
            return False, str(e)

    # @timeout(3, 'network_error')
    def delete_user(self, delete_username):
        try:
            data = {'username': self.name,
                    'password': self.encryption_password,
                    'department': self.department,
                    'delete_username': delete_username}
            url = '{server_address}/admin/delete_user'
            url = url.format(server_address=self.server_address)
            result = requests.post(url=url, data=data)
            result_dict = json_str_to_dict(result.text)
            if (result_dict['statue'] == 'successful'):
                return True, result_dict['data']
            else:
                return False, result_dict['data']
        except Exception as e:
            return False, str(e)

    # @timeout(3, 'network_error')
    def change_user(self, origin_name, dest_name, dest_password, dest_contact, dest_department):
        try:
            data = {'username': self.name,
                    'password': self.encryption_password,
                    'department': self.department,
                    'origin_name': origin_name,
                    'dest_name': dest_name,
                    'dest_password': dest_password,
                    'dest_contact': dest_contact,
                    'dest_department': dest_department}
            url = '{server_address}/admin/change_user'
            url = url.format(server_address=self.server_address)
            result = requests.post(url=url, data=data)
            result_dict = json_str_to_dict(result.text)
            if (result_dict['statue'] == 'successful'):
                return True, result_dict['data']
            else:
                return False, result_dict['data']
        except Exception as e:
            return False, str(e)

    # @timeout(3, 'network_error')
    def get_all_users(self):
        try:
            data = {'username': self.name,
                    'password': self.encryption_password,
                    'department': self.department,
                    }
            url = '{server_address}/admin/get_all_users'
            url = url.format(server_address=self.server_address)
            result = requests.post(url=url, data=data)
            result_dict = json_str_to_dict(result.text)
            if (result_dict['statue'] == 'successful'):
                return True, result_dict['data']['users']
            else:
                return False, result_dict['data']
        except Exception as e:
            return False, str(e)

    # @timeout(3, 'network_error')
    def get_all_user_in_department(self, query_department):
        try:
            data = {'username': self.name,
                    'password': self.encryption_password,
                    'department': self.department,
                    'query_department': query_department}
            url = '{server_address}/admin/get_all_user_in_department'
            url = url.format(server_address=self.server_address)
            result = requests.post(url=url, data=data)
            result_dict = json_str_to_dict(result.text)
            if (result_dict['statue'] == 'successful'):
                return result_dict['data']['users']
            else:
                return False, result_dict['data']
        except Exception as e:
            return False, str(e)

    ########################
    # 仓库管理模块
    #######################@
    # @timeout(3, 'network_error')
    def add_warehouse(self, warehouse_name, warehouse_location, warehouse_manager_name):
        try:
            data = {'username': self.name,
                    'password': self.encryption_password,
                    'department': self.department,
                    'warehouse_name': warehouse_name,
                    'warehouse_location': warehouse_location,
                    'warehouse_manager_name': warehouse_manager_name
                    }
            url = '{server_address}/admin/add_warehouse'
            url = url.format(server_address=self.server_address)
            result = requests.post(url=url, data=data)
            result_dict = json_str_to_dict(result.text)
            if (result_dict['statue'] == 'successful'):
                return True, result_dict['data']
            else:
                return False, result_dict['data']
        except Exception as e:
            return False, str(e)

    # @timeout(3, 'network_error')
    def delete_warehouse(self, delete_warehouse_name):
        try:
            data = {'username': self.name,
                    'password': self.encryption_password,
                    'department': self.department,
                    'delete_warehouse_name': delete_warehouse_name}
            url = '{server_address}/admin/delete_warehouse'
            url = url.format(server_address=self.server_address)
            result = requests.post(url=url, data=data)
            result_dict = json_str_to_dict(result.text)
            if (result_dict['statue'] == 'successful'):
                return True, result_dict['data']
            else:
                return False, result_dict['data']
        except Exception as e:
            return False, str(e)

    # @timeout(3, 'network_error')
    def change_warehouse(self, origin_warehouse_name, dest_warehouse_name, dest_warehouse_location,
                         dest_warehouse_manager_name):
        try:
            data = {'username': self.name,
                    'password': self.encryption_password,
                    'department': self.department,
                    'origin_warehouse_name': origin_warehouse_name,
                    'dest_warehouse_name': dest_warehouse_name,
                    'dest_warehouse_location': dest_warehouse_location,
                    'dest_warehouse_manager_name': dest_warehouse_manager_name, }
            url = '{server_address}/admin/change_warehouse'
            url = url.format(server_address=self.server_address)
            result = requests.post(url=url, data=data)
            result_dict = json_str_to_dict(result.text)
            if (result_dict['statue'] == 'successful'):
                return True, result_dict['data']
            else:
                return False, result_dict['data']
        except Exception as e:
            return False, str(e)

    # @timeout(3, 'network_error')
    def get_all_warehouses(self):
        try:
            data = {'username': self.name,
                    'password': self.encryption_password,
                    'department': self.department,
                    }
            url = '{server_address}/admin/get_all_warehouses'
            url = url.format(server_address=self.server_address)
            result = requests.post(url=url, data=data)
            result_dict = json_str_to_dict(result.text)
            if (result_dict['statue'] == 'successful'):
                return True, result_dict['data']['warehouses']
            else:
                return False, result_dict['data']
        except Exception as e:
            return False, str(e)

    ######################
    # 供应商管理模块
    ######################
    def add_supplier(self, supplier_name, supplier_contact):
        try:
            data = {'username': self.name,
                    'password': self.encryption_password,
                    'department': self.department,
                    'supplier_name': supplier_name,
                    'supplier_contact': supplier_contact,
                    }
            url = '{server_address}/admin/add_supplier'
            url = url.format(server_address=self.server_address)
            result = requests.post(url=url, data=data)
            result_dict = json_str_to_dict(result.text)
            if (result_dict['statue'] == 'successful'):
                return True, result_dict['data']
            else:
                return False, result_dict['data']
        except Exception as e:
            return False, str(e)

    def delete_supplier(self, delete_supplier_name):
        try:
            data = {'username': self.name,
                    'password': self.encryption_password,
                    'department': self.department,
                    'delete_supplier_name': delete_supplier_name,
                    }
            url = '{server_address}/admin/delete_supplier'
            url = url.format(server_address=self.server_address)
            result = requests.post(url=url, data=data)
            result_dict = json_str_to_dict(result.text)
            if (result_dict['statue'] == 'successful'):
                return True, result_dict['data']
            else:
                return False, result_dict['data']
        except Exception as e:
            return False, str(e)

    def change_supplier(self, origin_supplier_name, dest_supplier_name, dest_supplier_contact):
        try:
            data = {'username': self.name,
                    'password': self.encryption_password,
                    'department': self.department,
                    'origin_supplier_name': origin_supplier_name,
                    'dest_supplier_name': dest_supplier_name,
                    'dest_supplier_contact': dest_supplier_contact, }
            url = '{server_address}/admin/change_supplier'
            url = url.format(server_address=self.server_address)
            result = requests.post(url=url, data=data)
            result_dict = json_str_to_dict(result.text)
            if (result_dict['statue'] == 'successful'):
                return True, result_dict['data']
            else:
                return False, result_dict['data']
        except Exception as e:
            return False, str(e)

    def get_all_suppliers(self):
        try:
            data = {'username': self.name,
                    'password': self.encryption_password,
                    'department': self.department,
                    }
            url = '{server_address}/admin/get_all_suppliers'
            url = url.format(server_address=self.server_address)
            result = requests.post(url=url, data=data)
            result_dict = json_str_to_dict(result.text)
            if (result_dict['statue'] == 'successful'):
                return True, result_dict['data']['suppliers']
            else:
                return False, result_dict['data']
        except Exception as e:
            return False, str(e)

    ######################
    # 商品管理模块
    ######################
    # @timeout(3, 'network_error')
    def add_commodity(self, commodity_code, commodity_name, commodity_type, commodity_unit, commodity_specification,
                      commodity_supplier_name):
        try:
            data = {'username': self.name,
                    'password': self.encryption_password,
                    'department_name': self.department,
                    'commodity_code': commodity_code,
                    'commodity_name': commodity_name,
                    'commodity_type': commodity_type,
                    'commodity_unit': commodity_unit,
                    'commodity_specification': commodity_specification,
                    'commodity_supplier_name': commodity_supplier_name,
                    }
            url = '{server_address}/admin/add_commodity'
            url = url.format(server_address=self.server_address)
            result = requests.post(url=url, data=data)
            result_dict = json_str_to_dict(result.text)
            if (result_dict['statue'] == 'successful'):
                return True, result_dict['data']
            else:
                return False, result_dict['data']
        except Exception as e:
            return False, str(e)

    # @timeout(3, 'network_error')
    def delete_commodity(self, delete_commodity_code):
        try:
            data = {'username': self.name,
                    'password': self.encryption_password,
                    'department_name': self.department,
                    'delete_commodity_code': delete_commodity_code}
            url = '{server_address}/admin/delete_commodity'
            url = url.format(server_address=self.server_address)
            result = requests.post(url=url, data=data)
            result_dict = json_str_to_dict(result.text)
            if (result_dict['statue'] == 'successful'):
                return True, result_dict['data']
            else:
                return False, result_dict['data']
        except Exception as e:
            return False, str(e)

    # @timeout(3, 'network_error')
    def change_commodity(self, origin_commodity_code, dest_commodity_code, dest_commodity_name,
                         dest_commodity_type, dest_commodity_unit, dest_commodity_specification,
                         dest_commodity_supplier_name):
        try:
            data = {'username': self.name,
                    'password': self.encryption_password,
                    'department_name': self.department,
                    'origin_commodity_code': origin_commodity_code,
                    'dest_commodity_code': dest_commodity_code,
                    'dest_commodity_name': dest_commodity_name,
                    'dest_commodity_type': dest_commodity_type,
                    'dest_commodity_unit': dest_commodity_unit,
                    'dest_commodity_specification': dest_commodity_specification,
                    'dest_commodity_supplier_name': dest_commodity_supplier_name,
                    }
            url = '{server_address}/admin/change_commodity'
            url = url.format(server_address=self.server_address)
            result = requests.post(url=url, data=data)
            result_dict = json_str_to_dict(result.text)
            if (result_dict['statue'] == 'successful'):
                return True, result_dict['data']
            else:
                return False, result_dict['data']
        except Exception as e:
            return False, str(e)

    # @timeout(3, 'network_error')
    def get_all_commodities(self):
        try:
            data = {'username': self.name,
                    'password': self.encryption_password,
                    'department_name': self.department,
                    }
            url = '{server_address}/admin/get_all_commodities'
            url = url.format(server_address=self.server_address)
            result = requests.post(url=url, data=data)
            result_dict = json_str_to_dict(result.text)
            if (result_dict['statue'] == 'successful'):
                return True, result_dict['data']['commodities']
            else:
                return False, result_dict['data']
        except Exception as e:
            return False, str(e)


if __name__ == '__main__':
    try:
        admin = Admin('http://127.0.0.1:5000', 'admin', 'admin', '系统管理员')
        statue = admin.login()
        # admin.add_user(add_username='5', add_user_password='5', add_user_contact='5', add_user_department='5')
        # print(admin.get_all_user_in_department('阿斯顿'))
        # print(admin.add_warehouse(warehouse_name='111', warehouse_location='111', warehouse_manager_name='3'))
        # print(admin.get_all_warehouses())
        # print(admin.add_supplier('供应商2','2'))
        # print(admin.delete_supplier('供应商2'))
        # print(admin.change_supplier('供应商1','供应商2','2'))
        # print(admin.get_all_suppliers())
        # print(admin.add_commodity('赣南脐橙2', '水果', '个', '20-100g/个', '供应商1'))
        # print(admin.delete_commodity('赣南脐橙2'))
        print(admin.get_all_commodities())
    except Exception as e:
        print(e)
