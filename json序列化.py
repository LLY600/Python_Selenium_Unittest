import json

def test():
    print('hello word')

info = {
    'name': 'lly',
    'age': 18,
    'func': test
}

with open('test.text', 'w') as f:
    print(json.dumps(info))
    f.write(json.dumps(info))
