#作者:HP
#日期:2020-03-24 22:04
#文件:my_log
import logging
class MyLog:
    def my_log(self,msg,level):
        # 定义一个日志收集器my_logger
        my_logger = logging.getLogger('python11')

        # 设定级别
        my_logger.setLevel('DEBUG')

        # 设置日志输出格式
        formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息：%(message)s')

        # 创建一个输出渠道
        ch = logging.StreamHandler()
        ch.setLevel('ERROR')
        ch.setFormatter(formatter)

        fh = logging.FileHandler('py11.txt', encoding='utf-8')
        fh.setLevel('DEBUG')
        fh.setFormatter(formatter)

        # 两则对接
        my_logger.addHandler(ch)
        my_logger.addHandler(fh)

        # 收集日志
        if level=='DEBUG':
            my_logger.debug(msg)
        elif level=='INFO':
            my_logger.info(msg)
        elif level == 'WARNING':
            my_logger.warning(msg)
        elif level=='ERROR':
            my_logger.error(msg)
        elif level=='CRITICAL':
            my_logger.critical(msg)

        #关闭日志收集器
        my_logger.removeHandler(ch)
        my_logger.removeHandler(fh)
    def debug(self,msg):
        self.my_log(msg,'DEBUG')

    def info(self,msg):
        self.my_log(msg,'INFO')

    def error(self,msg):
        self.my_log(msg,'ERROR')

# if __name__=='__main__':

