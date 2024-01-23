
# add, subtract, multiply, divide


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


# 메서드 오버라이드
class Number:
    def __init__(self, number: int):
        self.num = number
        self.d = {'a': 55, 'b': 100}

    def __add__(self, other):
        self.num += other.num
        return self

    def __sub__(self, other):
        self.num -= other.num
        return self

    def __mul__(self, other):
        self.num *= other.num
        return self

    def __divmod__(self, other):
        self.num /= other.num
        return self

    def __delitem__(self, key):
        print(f'remove item: {key}')
        del self.d[key]


res = Number(5) + Number(7) + Number(12)
res = res - Number(4)
print(res.num)
print(res.d)

del res['a']
print(res.d)

# ###############
'''
json parser

d = {
}
'''

tmp = {
    'level1': {
        'level2': {
            'level3': {

            }
        }
    }
}

file_data = {
    'project': {
        'name': 'mermaid',
        'datetime': '2024-02-01',
        'shot': {
            'EP0001': {
                'EP0001_0010': {
                    'fps': 24,
                    'frange': [1001, 1100],
                    'author': ['anon', 'aa'],
                    'filepath': {
                        'hipfile': '/home/rapa/down',
                        'nkfile': '/home/rapa/nk',
                    }
                }
            },
            'EP0002': {
                'EP002_0010': {
                    'fps': 24,
                    'frange': [1001, 1050],
                    'author': 'anon',
                }
            },
        }
    }
}

key_data = {'project': {'shot': {'EP0001': {'EP0001_0010': {'frange': None}}}}}

# insert, delete, modify, get
json_modify(json_file, ['project', 'shot', 'EP0001', 'EP0001_0010', 'frange'], [1001, 1100])
json_modify(json_file, key_data, [1001, 1100])

insert_key_data = {'project': {'shot': {'EP0005': {'EP0005_0050': {'frange': [1001, 1200]}}}}}

json_insert(json_file, insert_key_data)

delete_key_data = {'project': {'shot': {'EP0005': None}}}
json_delete(json_file, delete_key_data)