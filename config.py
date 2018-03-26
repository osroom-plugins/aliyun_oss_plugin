# -*-coding:utf-8-*-

__author__ = "Allen Woo"
PLUGIN_NAME = "aliyun_oss_plugin"

CONFIG = {
    "ACCESS_KEY":{
        "info":"ACCESS KEY ID",
        "value_type":"string",
        "value":"",
        "reactivate":True
    },
    "SECRET_KEY":{
        "info":"SECRET KEY",
        "value_type":"password",
        "value":"",
        "reactivate":True
    },
    "IS_CNAME":{
        "info":"是否绑定了自定义域名(自己的)",
        "value_type":"bool",
        "value":False,
        "reactivate":True
    },
    "ENDPOINT":{
        "info":"EndPoint, 阿里云提供的区域访问EndPoint或者是自己绑定的域名",
        "value_type":"string",
        "value":"oss-cn-shenzhen.aliyuncs.com",
        "reactivate":True
    },
    "BUCKET_NAME":{
        "info":"BUCKET 名称",
        "value_type":"string",
        "value":"osroom-test2",
        "reactivate":True
    },
    "TIME_OUT":{
        "info":"连接超时",
        "value_type":"int",
        "value":60,
        "reactivate":True
    },
    "LOCAL_TEMP_FOLDER":{
        "info":"本地服务器临时保存目录名, 将建立在static目录下(可以不修改此项)",
        "value_type":"string",
        "value":"upload_temp",
        "reactivate":False
    },
    "DOMAIN":{
        "info":"域名(带http://或https://):访问上传的文件的域名",
        "value_type":"string",
        "value":"https://osroom-test2.oss-cn-shenzhen.aliyuncs.com",
        "reactivate":False
    }

}

