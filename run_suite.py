
import os
import unittest
import HTMLTestRunner_PY3
import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
test_path =BASE_DIR + "/script"
suite = unittest.TestSuite()
suite.addTest(unittest.TestLoader().discover(test_path, pattern='test*.py'))

file_name = BASE_DIR + "/report/report_{}.html".format(time.strftime("%Y%m%d%H%M%S"))
with open(file_name, mode='wb') as f:
    runner = HTMLTestRunner_PY3.HTMLTestRunner(f, verbosity=1, title="IHRM登录", description='报告')
    runner.run(suite)
