#作者:HP
#日期:2020-03-20 20:48
#文件:test_http_request
import unittest
from tools.http_request import HttpRequest
from tools.get_data import GetCookie
from ddt import ddt,data    #
from tools.do_excel import DoExcel
from tools.project_path import *



test_data=DoExcel.get_data(test_case_path,'login')    #执行登录用例
@ddt
class TestHttpRequest(unittest.TestCase):
    def setUp(self,):
        pass
    @data(*test_data)
    def test_api(self,item):
        res=HttpRequest.http_request(item['url'],eval(item['data']),item['http_method'],getattr(GetCookie,'Cookie'))

        try:
            self.assertEqual(item['expected'],res.json()['stat'])
            TestResult='PASS'
        except Exception as e:
            TestResult = 'Failed'
            print("执行用例出错：{0}".format(e))
            raise e
        finally:
            DoExcel.write_back(test_case_path,'login',item['case_id']+1,str(res.json()),TestResult)
            print("获取到结果是：{0}".format(res.json()))

    def tearDown(self):
        pass


