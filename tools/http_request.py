#作者:HP
#日期:2020-03-17 22:35
#文件:http_request
import requests
from tools.my_log import MyLog
my_logger=MyLog()
class HttpRequest:     #创建一个http请求

    @staticmethod
    def http_request(url,data,http_method,cookie=None):
        try:
            if http_method.upper()=='GET':
                res=requests.get(url,data,cookies=cookie)

            elif http_method.upper()=='POST':
                res=requests.post(url,json=data,cookies=cookie)
            else:
                my_logger.info("输入的请求方法不对")
        except Exception as e:
            my_logger.error("请求报错：{0}".format(e))
            raise e
        return res   #返回结果
# if __name__ =='__main__':
#     #登录
#     login_url='http://210.56.195.158:7006/auth/api/nameLogin'
#     login_data={"name":"tom","password":"123qwe"}
#
#     #创建文件夹
#     creart_url='http://210.56.195.158:7006/file/api/mkdirByPath'
#     creart_data={"path":"self:261993005056/12"}
#
#     login_res=HttpRequest().http_request(login_url,login_data,'get')
#     creart_res=HttpRequest().http_request(creart_url,creart_data,'post',login_res.cookies)
#
#     print("创建文件夹：{0}".format(creart_res.json()))








