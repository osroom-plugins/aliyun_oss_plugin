# -*-coding:utf-8-*-
import oss2
from apps.plugins.aliyun_oss_plugin.config import ENDPOINT, BUCKET_NAME, IS_CNAME, TIME_OUT, ACCESS_KEY, SECRET_KEY
from apps.plugins.aliyun_oss_plugin.upfile_cloud import alioss_upload, alioss_file_del, alioss_file_rename, \
    get_file_url

__author__ = "Allen Woo"
auth = oss2.Auth(ACCESS_KEY, SECRET_KEY)
alioss = oss2.Bucket(auth=auth,
                     endpoint=ENDPOINT,
                     bucket_name=BUCKET_NAME,
                     is_cname=IS_CNAME,
                      connect_timeout = TIME_OUT
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

    elif kwargs.get("action") == "delete":
        data = alioss_file_del(alioss, **kwargs)

    elif kwargs.get("action") == "rename":
        data = alioss_file_rename(alioss, **kwargs)
    elif kwargs.get("action") == "get_file_url":
        data = get_file_url(**kwargs)
    else:
        assert False
    return data


