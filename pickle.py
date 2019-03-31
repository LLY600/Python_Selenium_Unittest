import _pickle

def test():
    print('hello word')

info = {
    'name': 'lly',
    'age': 18,
    'func': test
}

with open('test.text', 'wb') as f:
    print(_pickle.dumps(info))
    f.write(_pickle.dumps(info))

