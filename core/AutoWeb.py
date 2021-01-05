# -*- coding: utf-8 -*-
# author:liucong
import inspect
import logging
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from airtest_selenium.proxy import WebChrome

from tools import Config
from tools.log import get_logger

logger = get_logger('selenium')
root_path = os.path.dirname(inspect.getfile(inspect.currentframe())) + os.path.sep + '..'


class AutoWeb(WebChrome):
    """
    AutoWeb类封装了所有与web有关的方法。
    """

    # 定位元素最大超时时间
    max_time = 10

    # 获取项目名
    _pro_name = Config.get_pro_info('pro_name')
    _pro_desc = Config.get_pro_info('pro_desc')
    # 获取项目配置
    _url = Config.get_pro_config(_pro_name, 'url')[0]
    _jenkins_url = Config.get_pro_config(_pro_name, 'jenkins_url')[0]
    _testcase = Config.get_pro_config(_pro_name, 'testcase')
    _testCasePath = Config.get_pro_config(_pro_name, "testcasepath")[0]
    # 获取基本配置
    _skip_email = Config.get_basic_config("skip_email")
    _skip_generate_report = Config.get_basic_config("skip_generate_report")

    def __init__(self, executable_path="chromedriver", port=0, options=None, service_args=None,
                 desired_capabilities=None, service_log_path=None, chrome_options=None):
        super(AutoWeb, self).__init__(chrome_options=chrome_options, executable_path=executable_path,
                                      port=port, options=options, service_args=service_args,
                                      service_log_path=service_log_path, desired_capabilities=desired_capabilities)

    # 获取项目名称
    @classmethod
    def get_pro_name(cls):
        return cls._pro_name

    @classmethod
    def get_pro_desc(cls):
        return cls._pro_desc

    # 获取测试用例路径
    @classmethod
    def get_testcase_path(cls):
        if cls._testCasePath == '':
            cls._testCasePath = os.path.join(root_path, 'TestCase')
        return cls._testCasePath

    # 获取项目的jenkins地址
    @classmethod
    def get_jenkins_url(cls):
        return cls._jenkins_url

    # 获取测试地址
    @classmethod
    def get_url(cls):
        return cls._url

    # 获取测试用例
    @classmethod
    def get_testcase(cls):
        return cls._testcase

    # 获取是否跳过发送邮件
    @classmethod
    def get_skip_email(cls):
        return cls._skip_email

    # 获取是否跳过生成报告
    @classmethod
    def get_skip_report(cls):
        return cls._skip_generate_report

    def find_element_by_id(self, el):
        try:
            logger.info("---------->正在定位：：{}".format(el))
            element = WebDriverWait(self, self.max_time).until(EC.visibility_of_element_located((By.ID, el)))
        except Exception:
            logger.error("---------->定位失败：{}".format(el))
            raise
        else:
            logger.info("---------->定位成功：{}".format(el))
            return element

    def find_elements_by_id(self, el):
        try:
            logger.info("---------->正在定位：{}".format(el))
            elements = WebDriverWait(self, self.max_time).until(EC.visibility_of_all_elements_located((By.ID, el)))
        except Exception:
            logger.error("---------->定位失败：{}".format(el))
            raise
        else:
            logger.info("---------->定位成功：{}".format(el))
            return elements

    def find_element_by_class_name(self, el):
        try:
            logger.info("---------->正在定位：{}".format(el))
            element = WebDriverWait(self, self.max_time).until(EC.visibility_of_element_located((By.CLASS_NAME, el)))
        except Exception:
            logger.error("---------->定位失败：{}".format(el))
            raise
        else:
            logger.info("---------->定位成功：{}".format(el))
            return element

    def find_elements_by_class_name(self, el):
        try:
            logger.info("---------->正在定位：{}".format(el))
            elements = WebDriverWait(self, self.max_time).until(
                EC.visibility_of_all_elements_located((By.CLASS_NAME, el)))
        except Exception:
            logger.error("---------->定位失败：".format(el))
            raise
        else:
            logger.info("---------->定位成功：{}".format(el))
            return elements

    def find_element_by_xpath(self, el):
        try:
            logger.info("---------->正在定位：{}".format(el))
            element = WebDriverWait(self, self.max_time).until(EC.visibility_of_element_located((By.XPATH, el)))
        except Exception:
            logger.error("---------->定位失败：{}".format(el))
            raise
        else:
            logger.info("---------->定位成功：{}".format(el))
            return element

    def find_elements_by_xpath(self, el):
        try:
            logger.info("---------->正在定位：{}".format(el))
            elements = WebDriverWait(self, self.max_time).until(
                EC.visibility_of_all_elements_located((By.XPATH, el)))
        except Exception:
            logger.error("---------->定位失败：".format(el))
            raise
        else:
            logger.info("---------->定位成功：{}".format(el))
            return elements
