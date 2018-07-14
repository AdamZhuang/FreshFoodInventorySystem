from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, DATETIME, ForeignKey, UniqueConstraint, Index
from sqlalchemy import create_engine

Base = declarative_base()


class _User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    password = Column(String(32), nullable=False)
    contact = Column(String(20), nullable=False)
    department = Column(String(20), nullable=False)


class _WareHouse(Base):
    __tablename__ = 'warehouse'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    location = Column(String(20), nullable=False)
    warehouse_manager_id = Column(Integer, ForeignKey('user.id'))


class _Supplier(Base):
    __tablename__ = 'supplier'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    contact = Column(String(20), nullable=False)


class _Commodity(Base):
    __tablename__ = 'commodity'
    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String(30), nullable=False)
    name = Column(String(20), nullable=False)
    type = Column(String(20), nullable=False)
    unit = Column(String(20), nullable=False)
    specification = Column(String(20), nullable=False)
    supplier_id = Column(Integer, ForeignKey('supplier.id'))

    __table_args__ = (UniqueConstraint('code', name='code_uc'),)


class _NoticeSheet(Base):
    __tablename__ = 'notice_sheet'
    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String(30), nullable=False)
    warehouse_id = Column(Integer, ForeignKey('warehouse.id'))
    order_man_id = Column(Integer, ForeignKey('user.id'))
    delivery_date = Column(DATETIME, nullable=False)
    notice_date = Column(DATETIME, nullable=False)
    statue = Column(String(30), nullable=False)
    handler_id = Column(Integer, ForeignKey('user.id'))

    __table_args__ = (UniqueConstraint('code', name='code_uc'),)


class _NoticeSheetDetail(Base):
    __tablename__ = 'notice_sheet_detail'
    id = Column(Integer, primary_key=True, autoincrement=True)
    notice_sheet_id = Column(Integer, ForeignKey('notice_sheet.id'))
    commodity_id = Column(Integer, ForeignKey('commodity.id'))
    number = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)


class _OrderSheet(Base):
    __tablename__ = 'order_sheet'
    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String(30), nullable=False)
    notice_sheet_id = Column(Integer, ForeignKey('notice_sheet.id'))
    order_man_id = Column(Integer, ForeignKey('user.id'))
    warehouse_id = Column(Integer, ForeignKey('warehouse.id'))
    order_date = Column(DATETIME, nullable=False)
    delivery_date = Column(DATETIME, nullable=False)
    statue = Column(String(30), nullable=False)
    handler_id = Column(Integer, ForeignKey('user.id'))

    __table_args__ = (UniqueConstraint('code', name='code_uc'),
                      UniqueConstraint('notice_sheet_id', name='notice_sheet_id'))


class _OrderSheetDetail(Base):
    __tablename__ = 'order_sheet_detail'
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_sheet_id = Column(Integer, ForeignKey('order_sheet.id'))
    commodity_id = Column(Integer, ForeignKey('commodity.id'))
    number = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)


class _InStorageSheet(Base):
    __tablename__ = 'in_storage_sheet'
    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String(30), nullable=False)
    order_sheet_id = Column(Integer, ForeignKey('order_sheet.id'))
    warehouse_id = Column(Integer, ForeignKey('warehouse.id'))
    in_storage_date = Column(DATETIME, nullable=False)
    handler_id = Column(Integer, ForeignKey('user.id'))

    __table_args__ = (UniqueConstraint('code', name='code_uc'),
                      UniqueConstraint('order_sheet_id', name='order_sheet_id'))


class _InStorageSheetDetail(Base):
    __tablename__ = 'in_storage_sheet_detail'
    id = Column(Integer, primary_key=True, autoincrement=True)
    in_storage_sheet_id = Column(Integer, ForeignKey('in_storage_sheet.id'))
    commodity_id = Column(Integer, ForeignKey('commodity.id'))
    number = Column(Integer, nullable=False)


class _ExStorageSheet(Base):
    __tablename__ = 'ex_storage_sheet'
    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String(30), nullable=False)
    warehouse_id = Column(Integer, ForeignKey('warehouse.id'))
    date = Column(DATETIME, nullable=False)
    handler_id = Column(Integer, ForeignKey('user.id'))


class _ExStorageSheetDetail(Base):
    __tablename__ = 'ex_storage_sheet_detail'
    id = Column(Integer, primary_key=True, autoincrement=True)
    ex_storage_sheet_id = Column(Integer, ForeignKey('ex_storage_sheet.id'))
    commodity_id = Column(Integer, ForeignKey('commodity.id'))
    number = Column(Integer, nullable=False)


class _CommodityStatic(Base):
    __tablename__ = 'commodity_static'
    id = Column(Integer, primary_key=True)
    warehouse_id = Column(Integer, ForeignKey('warehouse.id'))
    commodity_id = Column(Integer, ForeignKey('commodity.id'))
    number = Column(Integer, nullable=False, server_default='0')


if __name__ == '__main__':
    import hashlib


    def encryption(password):
        hash = hashlib.md5()
        hash.update(bytes(password, encoding='utf-8'))
        return hash.hexdigest()


    # 初始化数据库
    engine = create_engine("mysql+pymysql://root:Zxw11071205@127.0.0.1:3306/stock_control",
                           max_overflow=10, encoding='utf8', echo=False)
    Base.metadata.drop_all(engine)  # 创建表
    Base.metadata.create_all(engine)  # 创建表

    # construct data
    users = [{
        'name': 'admin', 'password': 'admin', 'contact': '15600931071', 'department': '系统管理员'
    }, {
        'name': '经理', 'password': '1', 'contact': '1', 'department': '经理'
    }, {
        'name': '采购员1', 'password': '2', 'contact': '2', 'department': '采购员'
    }, {
        'name': '采购员2', 'password': '2', 'contact': '2', 'department': '采购员'
    }, {
        'name': '仓库管理员1', 'password': '3', 'contact': '3', 'department': '仓库管理员'
    }]
    warehouses = [{
        'name': '北邮', 'location': '北邮', 'warehouse_manager_id': 5,
    }]
    suppliers = [{
        'name': '供应商1', 'contact': '1',
    }, {
        'name': '供应商2', 'contact': '2',
    }]
    commodities = [{
        'name': '富士苹果', 'code': '10001', 'type': '水果', 'unit': '斤', 'specification': '80-100g/个', 'supplier_id': 1
    }, {
        'name': '富士苹果', 'code': '10002', 'type': '水果', 'unit': '斤', 'specification': '50-80g/个', 'supplier_id': 2
    }, {
        'name': '赣南脐橙', 'code': '10003', 'type': '水果', 'unit': '斤', 'specification': '80-100g/个', 'supplier_id': 1
    }, {
        'name': '大白菜', 'code': '10004', 'type': '蔬菜', 'unit': '斤', 'specification': '0.75-1千克/株', 'supplier_id': 2
    }]

    from sqlalchemy.orm import sessionmaker

    Session = sessionmaker(bind=engine)
    sess = Session()

    for user in users:
        new_user = _User(name=user['name'], password=encryption(user['password']), contact=user['contact'],
                         department=user['department'])
        sess.add(new_user)
    sess.commit()

    for warehouse in warehouses:
        new_warehouse = _WareHouse(name=warehouse['name'], location=warehouse['location'],
                                   warehouse_manager_id=warehouse['warehouse_manager_id'])
        sess.add(new_warehouse)
    sess.commit()

    for supplier in suppliers:
        new_supplier = _Supplier(name=supplier['name'], contact=supplier['contact'])
        sess.add(new_supplier)
    sess.commit()

    for commodity in commodities:
        new_commodity = _Commodity(code=commodity['code'], name=commodity['name'], type=commodity['type'],
                                   unit=commodity['unit'], specification=commodity['specification'],
                                   supplier_id=commodity['supplier_id'])
        sess.add(new_commodity)
    sess.commit()

    sess.close()
