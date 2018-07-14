######################
# 错误编码定义
######################

# 状态正常
SUCCESS = True
# 密码错误
PWD_WORONG = -1
# 插入对象已存在
EXIST_ERROR = -2
# 插入对象不存在
NOT_EXIST_ERROR = -3
# 执行出现外键约束，无法继续下去
FOREIGNKEY_ERROR = -4
# 数据库Session关闭错误
SESSION_CLOSE_ERROR = -5
# 出库商品不足
NOT_ENOUGH_NUMBER = -6
# 未知错误
UNKNOWN_ERROR = -1000
