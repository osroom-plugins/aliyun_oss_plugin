# -*-coding:utf-8-*-

__author__ = "Allen Woo"
PLUGIN_NAME = "aliyun_oss_plugin"

CONFIG = {
    "ACCESS_KEY":{
        "info":"ACCESS KEY ID",
        "value_type":"string",
        "value":"<Your AK ID>",
        "reactivate":True
    },
    "SECRET_KEY":{
        "info":"SECRET KEY",
        "value_type":"password",
        "value":"<Your SK>",
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
        "value":"如oss-cn-shenzhen.aliyuncs.com",
        "reactivate":True
    },
    "BUCKET_NAME":{
        "info":"BUCKET 名称",
        "value_type":"string",
        "value":"如osroom-test2",
        "reactivate":True
    },
    "TIME_OUT":{
        "info":"连接超时",
        "value_type":"int",
        "value":60,
        "reactivate":True
    },
    "DOMAIN":{
        "info":"域名(带http://或https://):访问上传的文件的域名",
        "value_type":"string",
        "value":"如https://osroom-test2.oss-cn-shenzhen.aliyuncs.com",
        "reactivate":False
    }

}

