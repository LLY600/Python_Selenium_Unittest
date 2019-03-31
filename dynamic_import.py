import importlib


test = importlib.import_module('dir1.dir2.test')

print(test.Test('lly').test1())