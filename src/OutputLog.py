import logging
import os

'''
#单独输出到文件或控制台：
logging.basicConfig:日志的统一处理器，对日志的输出格式和方式做配置
日志级别等级 CRITICAL>ERROR>WARNING>INFO>DEBUG

log_file=os.path.join(os.getcwd(),'wlog.log')#指定
log_format = "%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s:%(message)s"

#logging.basicConfig(level=logging.WARNING,format=log_format)#WARNING必须大写，且前面一定是"logging.";如果参数不含filename,则默认打印到控制台
logging.basicConfig(level=logging.WARNING,format=log_format,filename=log_file,filemode="w")#w必须要小写

logging.warning("warning message")
logging.error("error message")

'''

#既输出到控制台，又输出到文件
'''
思路：
先创建一个父日志对象，其中包含将日志输出到控制台的子对象和将日志输出到文件的子对象
每个日志对象都要设置日志打印级别，保持一致.setLevel
子日志对象需要设置日志的格式。（使用logging.Formatter类将格式转换为格式对象，再调用setFormatter）
两个子日志对象最终都要归父日志对象统一管理
'''
logger=logging.getLogger("mylog")
logger.setLevel(logging.WARNING)#设置日志的格式都是固定的，logging.INFO

fh=logging.FileHandler(filename="C:/Users/flyyujunmh/PycharmProjects/unitest/logs/mylog.log",mode="w")#创建一个对象，将日志输出到文件
fh.setLevel(logging.WARNING)

sh=logging.StreamHandler()#创建一个对象，将日志打印到控制台
sh.setLevel(logging.WARNING)

log_format = "%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s:%(message)s"
formatter=logging.Formatter(log_format)
fh.setFormatter(formatter)
sh.setFormatter(formatter)

logger.addHandler(sh)
logger.addHandler(fh)

logger.error("practice log output error msg")





