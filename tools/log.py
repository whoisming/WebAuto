# -*- coding: utf-8 -*-
# author:liucong

import logging
import time
import os
import inspect

from tools.Config import get_basic_config

proj_path = os.path.dirname(inspect.getfile(inspect.currentframe())) + os.path.sep + '..'
log_path = os.path.join(proj_path, 'log')
log_name = os.path.join(log_path, '{0}.txt'.format(time.strftime('%Y-%m-%d')))


def get_logger(name='Web Automation'):
    init_logger = logging.getLogger(name)
    init_logger.setLevel(logging.DEBUG)
    # 格式化模板
    formatter = logging.Formatter(
        fmt='[%(asctime)s][%(levelname)s]<%(name)s> %(message)s',
        datefmt='%H:%M:%S'
    )
    # 流处理器创建与添加
    handler = logging.StreamHandler()
    detail_flag = get_basic_config('detail_log')
    detail_flag = True if detail_flag == '1' else False
    if detail_flag:
        level = logging.DEBUG
    else:
        level = logging.INFO
    handler.setLevel(level)
    handler.setFormatter(formatter)
    init_logger.addHandler(handler)
    # 日志处理器创建与添加，用于写入日志文件
    # 创建日志目录和日志文件
    os.makedirs(log_path, exist_ok=True)
    if not os.path.exists(log_name):
        log = open(log_name, "a")
        log.close()
    log_handle = logging.FileHandler(log_name, 'a', encoding='utf-8')
    log_handle.setLevel(logging.DEBUG)
    log_handle.setFormatter(formatter)
    init_logger.addHandler(log_handle)
    return init_logger


logger = get_logger()
