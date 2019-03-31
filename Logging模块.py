
#_*_coding:utf-8_*_
#@Author:LLY


import logging

# logging.debug('debug')
# logging.info('info')
# logging.warning('warning')
# logging.error('error')
# logging.critical('critical')

# 级别不一样，只打印如下
# WARNING:root:warning
# ERROR:root:error
# CRITICAL:root:critical

# 修改配置
# logging.basicConfig(
#     level=logging.DEBUG,
#     format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s',
#     datefmt='%a,%d %b %Y %H:%M:%S',
#     filename='test.log',
#     filemode='w'
# )
# logging.debug('debug')
# logging.info('info')
# logging.warning('warning')
# logging.error('error')
# logging.critical('critical')


logger = logging.getLogger()
#创建一个handler，用于写入日志文件，文件输出流
fh = logging.FileHandler('test.log')
#创建一个handler，用于输入到控制台
sh = logging.StreamHandler()

formtter = logging.Formatter('%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s')


fh.setFormatter(formtter)
sh.setFormatter(formtter)

logger.addHandler(fh)
logger.addHandler(sh)

logger.debug('debug')
logger.info('info')
logger.warning('warning')
logger.error('error')
logger.critical('critical')