# -*-coding:utf-8-*-
import os
from flask_babel import gettext
from apps.core.plug_in.config_process import get_plugin_config
from apps.plugins.aliyun_oss_plugin.config import PLUGIN_NAME

__author__ = "Allen Woo"

def alioss_upload(alioss, **kwargs):

    """
    文件上传
    :param kwargs:
    localfile_path:要上传的本地服务器文件路径
    filename:文件名, 如果带上"/"则会创建对应的子目录,如post-img/xxxx-xxx-xxx.jpg
    prefix: 文件名前缀
    :return:
    """

    localfile_path = kwargs.get("localfile_path")
    filename = kwargs.get("filename")
    prefix = kwargs.get("prefix")

    if prefix:
        filename = "{}{}".format(prefix, filename).replace("//", "/")
    # 上传
    with open(localfile_path, 'rb') as fileobj:
        alioss.put_object(filename, fileobj)


    result = {"key": filename, "type": "aliyun",
              "bucket_name": get_plugin_config(PLUGIN_NAME, "BUCKET_NAME")}
    return result


def alioss_copy(alioss, **kwargs):
    """
    文件复制
    :param kwargs:
    :return:
    """

    # file_url_obj:上传文件时返回的那个result格式的字典
    file_url_obj = kwargs.get("file_url_obj")
    new_filename = kwargs.get("filename")
    if isinstance(file_url_obj, dict) and "key" in file_url_obj:

        alioss.copy_object(get_plugin_config(PLUGIN_NAME, "BUCKET_NAME"),
                           file_url_obj["key"], new_filename)

        return True
    else:
        return False

def alioss_file_del(alioss, **kwargs):

    '''
    阿里云OSS上文件删除
    :return:
    '''

    # file_url_obj:上传文件时返回的那个result格式的字典
    file_url_obj = kwargs.get("file_url_obj")
    if isinstance(file_url_obj, dict) and "key" in file_url_obj:

        alioss.delete_object(file_url_obj["key"])

        return True
    else:
        return False


def alioss_file_rename(alioss, **kwargs):

    '''
    文件重命名
    :return:
    '''

    # file_url_obj:上传文件时返回的那个result格式的字典
    file_url_obj = kwargs.get("file_url_obj")
    new_filename = kwargs.get("new_filename")
    if isinstance(file_url_obj, dict) and "key" in file_url_obj:

        alioss.copy_object(get_plugin_config(PLUGIN_NAME, "BUCKET_NAME"), file_url_obj["key"], new_filename)

        return True
    else:
        return False


def get_file_url(**kwargs):

    '''
    阿里云OSS上文件删除
    :return:
    '''

    # file_url_obj:上传文件时返回的那个result格式的字典
    file_url_obj = kwargs.get("file_url_obj")
    if isinstance(file_url_obj, dict) and "key" in file_url_obj:
        domain = get_plugin_config(PLUGIN_NAME, "DOMAIN")
        if not domain:
            raise Exception(gettext("Please configure the third-party file storage domain name"))

        url = "{}/{}".format(domain, file_url_obj["key"])
        return url
    return None

