# login/init.py
# learn
# ├── __init__.py
# ├── admin.py    后台相关的设置
# ├── apps.py     app相关的设置文件
# ├── migrations  数据库变更相关
# │   └── __init__.py
# ├── models.py   数据库模型相关
# ├── tests.py    单元测试
# └── views.py    视图逻辑
import pymysql

pymysql.install_as_MySQLdb()
