import json

with open('test.text', 'r') as f:
    print(json.loads(f.read())['name'])