## OSROOM开源系统的阿里云Aliyun OSS对象储存插件
### 注意:
- 1.使用前请配置好config.py, 再压缩上传安装(或直接放入osroom项目的apps/plugins目录下)

- 2.安装前请保证插件主目录名称为:aliyun_oss_plugin, aliyun_oss_plugin-master之类的

- 3.此插件需要安装qiniu的python包, 注意安装在osroom系统运行的python环境下. pip安装方法如下
 ```
    pip install oss2
 ```
更多安装方法见:https://help.aliyun.com/document_detail/32026.html?spm=5176.87240.400427.49.yz1BP9
### 配置:

```

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

```

### 类似插件还有

七牛云储存插件: https://github.com/osroom-plugins/qiniu_cloud_plugin
