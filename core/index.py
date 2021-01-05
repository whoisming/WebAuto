# -*- coding: utf-8 -*-
# author:liucong
import os
import time
import traceback
from airtest_selenium.exceptions import *
from core.AutoWeb import AutoWeb
from core.RunTestCase import RunTestCase
from tools.Email import Email
from tools.log import logger
import warnings


def main():
    # 忽略输出中的warning
    warnings.filterwarnings('ignore')
    # 读取相关配置
    # 判断url是否填写
    url = AutoWeb.get_url()
    if url == "":
        logger.error('配置文件url字段为空')
        raise
    # 读取是否跳过发送邮件
    skip_email_flag = AutoWeb.get_skip_email()
    skip_email = True if skip_email_flag == '1' else False
    report_path = os.path.join(os.getcwd(), "Report")
    # 没有Report目录时自动创建
    if not os.path.exists(report_path):
        os.mkdir(report_path)
        if os.path.exists(report_path):
            logger.info('{}创建成功'.format(report_path))
        else:
            logger.error('{}创建失败'.format(report_path))
    else:
        logger.info('{}已存在，跳过创建'.format(report_path))
    logger.info("测试开始")
    try:
        start = time.localtime()
        web = AutoWeb()
        # 进入功能进程模块
        RunTestCase(web, start)
        logger.info("测试结束")
    except AirtestSeleniumException:
        logger.error("AirtestSelenium发生错误\n" + traceback.format_exc())
    except Exception:
        logger.error("发生未知错误\n" + traceback.format_exc())
    # 判断是否发送邮件
    if not skip_email:
        try:
            Email().send_email()
        except Exception:
            logger.error(traceback.format_exc())
    else:
        logger.info('跳过发送邮件')
