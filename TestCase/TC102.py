# -*- coding: utf-8 -*-
# author:liucong

import inspect
import unittest
from tools.log import logger
from airtest.core.api import *

# 获取工程路径
pro_path = os.path.dirname(inspect.getfile(inspect.currentframe())) + os.path.sep + ".."
# 获取case的图片路径
img_path = os.path.join(pro_path, 'TestCaseImage')
# 获取对应项目的case图片路径
case_img = os.path.join(img_path, 'project1')


def run_case():
    logger.debug("进入unittest")

    class TC102(unittest.TestCase):
        """用例描述"""

        @classmethod
        def setUpClass(cls):
            """ 这里放需要在所有用例执行前执行的部分"""
            pass

        def setUp(self):
            logger.info('测试测试用例')
            """这里放需要在每条用例前执行的部分"""
            pass

        def test_demo(self):
            """点击微信登录"""
            pass

        def tearDown(self):
            """这里放需要在每条用例后执行的部分"""
            sleep(5)

        @classmethod
        def tearDownClass(cls):
            u"""这里放需要在所有用例后执行的部分"""
            pass

    # 调试测试类下所有方法
    srcSuite = unittest.TestLoader().loadTestsFromTestCase(TC102)
    # 调试测试类下某个方法
    # srcSuite = TC101("test_login")
    return srcSuite
