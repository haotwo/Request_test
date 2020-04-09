#作者:HP
#日期:2020-03-17 21:56
#文件:run

#执行代码入口
import unittest
import HTMLTestReportCN
from tools.project_path import *
from tools.test_http_request import TestHttpRequest

#加载测试用例
suite=unittest.TestSuite()
loader=unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestHttpRequest))

#执行用例
with open(test_report_path,'wb') as file:
    runner=HTMLTestReportCN.HTMLTestRunner( stream=file,
                                            verbosity=2,
                                            title='单元测试报告',
                                            description="单元测试报告",
                                            tester='Lyle')
    runner.run(suite)



