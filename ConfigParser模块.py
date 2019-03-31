#_*_coding:utf-8_*_
#@Author:LLY

import configparser

config = configparser.ConfigParser()
# config['DEFAULT'] = {
#     'key1': 'value1',
#     'key2': 'value2',
#     'key3': 'value3'
# }
# config['DEFAULT1'] = {
#     'key1': 'value1',
#     'key2': 'value2',
#     'key3': 'value3'
# }
#
# with open('config.ini', 'w') as f:
#     config.write(f)

config.read('config.ini')
# print(config.sections()) # ['DEFAULT1'] 默认的不获取
# print(config.default_section)
# print(config.defaults())
# config.remove_section('DEFAULT1')
# for key in config:
#     print(key)

config.remove_section('DEFAULT1')
config.set('DEFAULT', 'name', 'lly')
config.remove_option('DEFAULT', 'name')
with open('config.ini', 'w') as f:
    config.write(f)


print(config.has_section('DEFAULT1'))


