import json

file_path = './1.log'
a = {"a":1 ,"b":2}

with open(file_path, 'w') as f:
    f.write(json.dumps(a))


if __name__ == '__main__':

    a = set([1,2,3])
    print(json.dumps(a))
