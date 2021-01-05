# -*- coding: utf-8 -*-
# author:liucong

import inspect
import unittest

from core.AutoWeb import AutoWeb
from tools.log import logger
from airtest.core.api import *

# 获取工程路径
pro_path = os.path.dirname(inspect.getfile(inspect.currentframe())) + os.path.sep + ".."
# 获取case的图片路径
img_path = os.path.join(pro_path, 'TestCaseImage')
# 获取对应项目的case图片路径
case_path = os.path.join(img_path, 'BWMOCR')


def run_case(driver: AutoWeb, url):
    logger.debug("进入unittest")

    class TC101(unittest.TestCase):
        """用例描述"""

        @classmethod
        def setUpClass(cls):
            """ 窗口最大化并访问测试网页地址"""
            driver.maximize_window()
            driver.get(url)
            driver.find_element_by_xpath("//*[@type='text']").send_keys('zwq')
            driver.find_element_by_xpath("//*[@type='password']").send_keys('situ1234')
            driver.airtest_touch(Template('{}/login_on.png'.format(case_path)))

        def setUp(self):
            """这里放需要在每条用例前执行的部分"""
            pass

        @classmethod
        def test_login(cls):
            """点击微信登录"""
            logger.info('测试登录')
            pass

        def test_demo2(self):
            """点击手机号登录"""
            pass

        def test_demo3(self):
            """touch使用"""
            pass

        def tearDown(self):
            """这里放需要在每条用例后执行的部分"""
            sleep(1)

        @classmethod
        def tearDownClass(cls):
            """关闭浏览器"""
            time.sleep(1)
            driver.quit()

    # 调试测试类下所有方法
    # srcSuite = unittest.TestLoader().loadTestsFromTestCase(TC101)
    # 调试测试类下某个方法
    srcSuite = TC101("test_login")
    return srcSuite
