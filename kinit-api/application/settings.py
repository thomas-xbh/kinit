# -*- coding: utf-8 -*-
# @version        : 1.0
# @Creaet Time    : 2021/10/19 15:47
# @File           : settings.py
# @IDE            : PyCharm
# @desc           : 主配置文件

import os
from fastapi.security import OAuth2PasswordBearer

"""
系统版本
"""
VERSION = "1.4.0"

"""安全警告: 不要在生产中打开调试运行!"""
DEBUG = False

"""是否开启演示功能：取消所有POST,DELETE,PUT操作权限"""
DEMO = True
"""演示功能白名单"""
DEMO_WHITE_LIST_PATH = [
    "/auth/login/",
    "/vadmin/system/dict/types/details/",
    "/vadmin/auth/user/export/query/list/to/excel/"
]

"""
引入数据库配置
"""
if DEBUG:
    from application.config.development import *
else:
    from application.config.production import *

"""项目根目录"""
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

"""
是否开启登录认证
只适用于简单的接口
如果是与认证关联性比较强的接口，则无法使用
"""
OAUTH_ENABLE = True
"""登录认证视图"""
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login/", auto_error=False) if OAUTH_ENABLE else lambda: ""
"""安全的随机密钥，该密钥将用于对 JWT 令牌进行签名"""
SECRET_KEY = 'vgb0tnl9d58+6n-6h-ea&u^1#s0ccp!794=kbvqacjq75vzps$'
"""用于设定 JWT 令牌签名算法"""
ALGORITHM = "HS256"
"""令牌过期时间，9999分钟"""
ACCESS_TOKEN_EXPIRE_MINUTES = 9999

"""
挂载临时文件目录，并添加路由访问，此路由不会在接口文档中显示
TEMP_ENABLE：是否启用临时文件目录访问
TEMP_URL：路由访问
TEMP_DIR：临时文件目录绝对路径
官方文档：https://fastapi.tiangolo.com/tutorial/static-files/
"""
TEMP_ENABLE = True
TEMP_URL = "/temp"
TEMP_DIR = os.path.join(BASE_DIR, "temp")

"""
挂载静态目录，并添加路由访问，此路由不会在接口文档中显示
STATIC_ENABLE：是否启用静态目录访问
STATIC_URL：路由访问
STATIC_ROOT：静态文件目录绝对路径
官方文档：https://fastapi.tiangolo.com/tutorial/static-files/
"""
STATIC_ENABLE = True
STATIC_URL = "/media"
STATIC_ROOT = os.path.join(BASE_DIR, "static")


"""
跨域解决
详细解释：https://cloud.tencent.com/developer/article/1886114
官方文档：https://fastapi.tiangolo.com/tutorial/cors/
"""
# 是否启用跨域
CORS_ORIGIN_ENABLE = True
# 只允许访问的域名列表，* 代表所有
ALLOW_ORIGINS = ["*"]
# 是否支持携带 cookie
ALLOW_CREDENTIALS = True
# 设置允许跨域的http方法，比如 get、post、put等。
ALLOW_METHODS = ["*"]
# 允许携带的headers，可以用来鉴别来源等作用。
ALLOW_HEADERS = ["*"]

"""
全局事件配置
"""
EVENTS = [
    "core.event.register_mongo" if MONGO_DB_ENABLE else None,
    "core.event.register_redis" if REDIS_DB_ENABLE else None,
]

"""
其他项目配置
"""
# 默认密码，"0" 默认为手机号后六位
DEFAULT_PASSWORD = "0"
# 是否开启保存登录日志
LOGIN_LOG_RECORD = True
# 是否开启保存每次请求日志到本地
REQUEST_LOG_RECORD = True
# 是否开启每次操作日志记录到MongoDB数据库
OPERATION_LOG_RECORD = True
# 只记录包括的请求方式操作到MongoDB数据库
OPERATION_RECORD_METHOD = ["POST", "PUT", "DELETE"]
# 忽略的操作接口函数名称，列表中的函数名称不会被记录到操作日志中
IGNORE_OPERATION_FUNCTION = ["post_dicts_details"]

"""
中间件配置
"""
MIDDLEWARES = [
    "core.middleware.register_request_log_middleware" if REQUEST_LOG_RECORD else None,
    "core.middleware.register_operation_record_middleware" if OPERATION_LOG_RECORD and MONGO_DB_ENABLE else None,
    "core.middleware.register_demo_env_middleware" if DEMO else None,
]
