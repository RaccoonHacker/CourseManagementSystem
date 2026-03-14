import pymysql

# 增加这一行，手动指定一个足够高的版本号来骗过 Django 的检查
pymysql.version_info = (2, 2, 1, "final", 0)

pymysql.install_as_MySQLdb()