# -*- coding: utf-8 -*-
# author:liucong

import configparser
import inspect
import os

con = configparser.ConfigParser()
# 获取当前项目的根路径
pro_path = os.path.dirname(inspect.getfile(inspect.currentframe())) + os.path.sep + ".."
# 获取配置文件路径
config_path = os.path.join(pro_path, 'config.ini')


# 解析project配置，获取项目名称
def get_pro_info(key):
    con.read(config_path)
    result = con.get("project", key)
    return result


# 解析对应工程的config文件并将其结果转成一个list，对单个的value，可以用[0]取值
def get_pro_config(pro, key):
    con.read(config_path)
    result = con.get("{}_config".format(pro), key)
    config = result.split(",")
    return config


# 解析base_config配置
def get_basic_config(key):
    con.read(config_path)
    result = con.get("basic_config", key)
    return result


# 解析email配置
def get_email_config(key):
    con.read(config_path)
    result = con.get("Email", key)
    return result
