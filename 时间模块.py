#_*_coding:utf-8_*_
#@Author:LLY

import time


# print(help(time))

# print(time.time())  # 时间戳
#1554001965.0774999

# print(time.clock())

# print(time.gmtime())
#time.struct_time(tm_year=2019, tm_mon=3, tm_mday=31, tm_hour=3, tm_min=12, tm_sec=45, tm_wday=6, tm_yday=90, tm_isdst=0)

#print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
#2019-03-31 11:22:22

#print(time.strptime('2019-10-28 10:35:20', '%Y-%m-%d %H:%M:%S'))
#time.struct_time(tm_year=2019, tm_mon=10, tm_mday=28, tm_hour=10, tm_min=35, tm_sec=20, tm_wday=0, tm_yday=301, tm_isdst=-1)
# a = time.strptime('2019-3-28 10:35:20', '%Y-%m-%d %H:%M:%S')
# print(a.tm_year)
# print(a.tm_mday)
# print(a.tm_wday)
# 2019
# 28
# 3


# print(time.ctime())
# print(time.ctime(time.time()-24*60*60))
# Sun Mar 31 11:32:00 2019
# Sat Mar 30 11:32:00 2019


# print(time.mktime(time.localtime()))
# 1554003120.0

import datetime
print(datetime.datetime.now())
