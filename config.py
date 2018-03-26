# -*-coding:utf-8-*-

__author__ = "Allen Woo"
'''
验证
'''
ACCESS_KEY = "<Your AK>"
SECRET_KEY = "<Your SK>"

# 如果你的存储访问绑定的是自己的域名, 则开启, 即IS_CNAME改为True
IS_CNAME = False
# 访问EndPoint, 阿里云提供的区域访问EndPoint　或者　绑定的自己的域名
ENDPOINT = "oss-cn-shenzhen.aliyuncs.com"
BUCKET_NAME = "<Your bucket name>"
TIME_OUT = 60 # 超时连接秒

# 自己服务器的临时存储目录, 可以不修改
LOCAL_TEMP_FOLDER = "upload_temp"

'''
访问
'''

DOMAIN = "https://osroom-test.oss-cn-shenzhen.aliyuncs.com"
