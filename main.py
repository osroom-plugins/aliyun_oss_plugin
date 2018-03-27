# -*-coding:utf-8-*-
import oss2

from apps.core.plug_in.config_process import import_plugin_config, get_plugin_config
from apps.plugins.aliyun_oss_plugin.config import CONFIG, PLUGIN_NAME
from apps.plugins.aliyun_oss_plugin.upfile_cloud import alioss_upload, alioss_file_del, alioss_file_rename, \
    get_file_url

__author__ = "Allen Woo"
import_plugin_config(PLUGIN_NAME, CONFIG)
auth = oss2.Auth(get_plugin_config(PLUGIN_NAME, "ACCESS_KEY"),
                 get_plugin_config(PLUGIN_NAME, "SECRET_KEY"))
alioss = oss2.Bucket(auth=auth,
                     endpoint=get_plugin_config(PLUGIN_NAME, "ENDPOINT"),
                     bucket_name=get_plugin_config(PLUGIN_NAME, "BUCKET_NAME"),
                     is_cname=get_plugin_config(PLUGIN_NAME, "IS_CNAME"),
                      connect_timeout = get_plugin_config(PLUGIN_NAME, "TIME_OUT")
                     )

def main(**kwargs):

    '''
    主函数
    :param kwargs:
        action: 动作
    :return:
    '''
    if kwargs.get("action") == "upload":
        data = alioss_upload(alioss, **kwargs)
    elif kwargs.get("action") == "copy_file":
        data = alioss_upload(alioss, **kwargs)
    elif kwargs.get("action") == "delete":
        data = alioss_file_del(alioss, **kwargs)
    elif kwargs.get("action") == "rename":
        data = alioss_file_rename(alioss, **kwargs)
    elif kwargs.get("action") == "get_file_url":
        data = get_file_url(**kwargs)
    else:
        assert False
    return data


