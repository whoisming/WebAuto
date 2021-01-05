# -*- coding: utf-8 -*-
# author:liucong

import os
import time
import unittest

from beautifulReport import BeautifulReport
from core.AutoWeb import AutoWeb, logger
from TestCase import *
from tools import File
from tools.Jenkins import jenkins_lastBuild_info

root_path = os.path.abspath(os.path.dirname(__file__) + os.path.sep + '..')


# 运行Testcase的主函数
def RunTestCase(driver: AutoWeb, start):
    logger.info("进入RunTestCase")
    # 读取ini配置文件
    # 获取测试网页的url
    url = driver.get_url()
    logger.info('测试的网页：{}'.format(url))
    # 获取测试网页的描述
    desc = driver.get_pro_desc()
    # 获取是否跳过生成测试报告
    skip_report = driver.get_skip_report()
    report_flag = True if skip_report == "1" else False

    # 获取jenkins部署信息
    jenkins_branch, timestamp = jenkins_lastBuild_info()
    logger.info('jenkins分支：{}'.format(jenkins_branch))
    timeArray = time.localtime(timestamp / 1000)
    jenkins_time = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    logger.info('部署时间：{}'.format(jenkins_time))

    # 获取测试用例路径
    TestCasePath = AutoWeb.get_testcase_path()
    if not os.path.exists(TestCasePath):
        logger.error("测试用例需放到‘TestCase’文件目录下")

    # 获得期望测试的用例列表
    TestList = AutoWeb.get_testcase()
    logger.info("待测用例为：{}".format(TestList))

    # 通过GetPyList方法，取得目录里可测试的用例列表
    scriptList = File.GetPyList(TestCasePath)
    # 初始化测试套件
    suite = unittest.TestSuite()
    for i in range(len(TestList)):
        fileName = "TC_" + TestList[i]
        logger.debug("fileName={}".format(fileName))
        if fileName in scriptList:
            # 在整个命名空间里遍历所有名称为"TC_xx.py"形式的文件，默认这些文件都是unittest测试文件，然后调用其run_case函数。
            result = globals()[fileName].run_case(driver, url)
            # 根据result类型判断调试单个方法or全部方法
            if isinstance(result, unittest.suite.TestSuite):
                suite.addTests(result)
            else:
                suite.addTest(result)
    # 聚合报告到BR
    unittestReport = BeautifulReport(suite)
    nowtime = time.strftime("%Y%m%d%H%M%S", start)
    reportpath = os.path.join(os.getcwd(), "Report")
    unittestReport.report(filename=str(nowtime), description=desc, url=url[8:], report_dir=reportpath,
                          jenkins_branch=jenkins_branch, jenkins_time=jenkins_time, report_flag=report_flag)
    # 测试case中如果使用airtest_touch方法进行定位元素，会产生一个temp.jpg的截图文件，测试完成后删除
    temp_img_path = os.path.join(root_path, 'temp.jpg')
    if os.path.exists(temp_img_path):
        os.remove(temp_img_path)
        logger.info('完成删除临时截图文件')
    else:
        logger.info('不存在临时截图文件：{}'.format(temp_img_path))
