# -*-coding:utf-8-*-
from flask_babel import gettext
from apps.plugins.aliyun_oss_plugin.config import BUCKET_NAME, DOMAIN
from apps.plugins.aliyun_oss_plugin.upfile_local import local_file_del, upload_to_local, fileup_base_64

__author__ = "Allen Woo"


def alioss_upload(alioss, **kwargs):

    """
    文件上传
    :param kwargs:

    file:上传：获取文件对象
    fetch_url:远程文件url
    file_name:文件名, 如果带上"/"则会创建对应的子目录,如post-img/xxxx-xxx-xxx.jpg
    file_format_name: jpg, png,txt, json....
    prefix: 文件名前缀
    is_base_64: 上传的时转码成base64的格式文件

    :return:
    """

    file = kwargs.get("file")
    fetch_url = kwargs.get("fetch_url")
    filename = kwargs.get("file_name")
    file_format_name = kwargs.get("file_format_name")
    prefix = kwargs.get("prefix")
    is_base_64 = kwargs.get("is_base_64")
    
    if is_base_64:
        # localfilepath要上传文件的本地路径, key上传到七牛后保存的文件名
        localfile_path, key = fileup_base_64(file=file, file_name=filename,
                                              file_format=file_format_name,
                                             prefix=prefix)
    else:
        # localfilepath要上传文件的本地路径, key上传到七牛后保存的文件名
        localfile_path, key = upload_to_local(file=file, filename=filename,
                                              file_format=file_format_name,
                                              fetch_url=fetch_url, prefix=prefix)

    # 上传
    with open(localfile_path, 'rb') as fileobj:
        alioss.put_object(key, fileobj)
        
    # 删除本地临时文件
    local_file_del(localfile_path)

    result = {"key": key, "type": "aliyun", "bucket_name": BUCKET_NAME}
    return result


def alioss_save_file(alioss, **kwargs):
    """
    文件上传
    :param kwargs:

    localfile_path:要保存的本地文件路径
    file_name:文件名, 如果带上"/"则会创建对应的子目录,如post-img/xxxx-xxx-xxx.jpg

    :return:
    """


    filename = kwargs.get("file_name")
    localfile_path = kwargs.get("localfile_path")


    # 上传
    with open(localfile_path, 'rb') as fileobj:
        alioss.put_object(filename, fileobj)

    # 删除本地临时文件
    local_file_del(localfile_path)

    result = {"key": filename, "type": "aliyun", "bucket_name": BUCKET_NAME}
    return result


def alioss_file_del(alioss, **kwargs):

    '''
    阿里云OSS上文件删除
    :return:
    '''

    # path_obj:上传文件时返回的那个result格式的字典
    path_obj = kwargs.get("path_obj")
    if isinstance(path_obj, dict) and "key" in path_obj:

        alioss.delete_object(path_obj["key"])

        return True
    else:
        return False


def alioss_file_rename(alioss, **kwargs):

    '''
    文件重命名
    :return:
    '''

    # path_obj:上传文件时返回的那个result格式的字典
    path_obj = kwargs.get("path_obj")
    new_filename = kwargs.get("new_filename")
    if isinstance(path_obj, dict) and "key" in path_obj:

        alioss.copy_object(BUCKET_NAME, path_obj["key"], new_filename)

        return True
    else:
        return False


def get_file_url(**kwargs):

    '''
    阿里云OSS上文件删除
    :return:
    '''

    # path_obj:上传文件时返回的那个result格式的字典
    path_obj = kwargs.get("path_obj")
    if isinstance(path_obj, dict) and "key" in path_obj:
        if not DOMAIN:
            raise Exception(gettext("Please configure the third-party file storage domain name"))

        url = "{}/{}".format(DOMAIN, path_obj["key"])
        return url
    return None