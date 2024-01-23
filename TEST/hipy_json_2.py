json_data = {
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
# json_modify(json_file, ['project', 'shot', 'EP0001', 'EP0001_0010', 'frange'], [1001, 1100])
# json_modify(json_file, key_data, [1001, 1100])

insert_key_data = {'project': {'shot': {'EP0005': {'EP0005_0050': {'frange': [1001, 1200]}}}}}

# json_insert(json_file, insert_key_data)

delete_key_data = {'project': {'shot': {'EP0005': None}}}
# json_delete(json_file, delete_key_data)


# def json_insert(data: dict):
#     for k, v in data.items():
#         if isinstance(v, dict):
#             for i in range(len(v)):
#                 print(k)
#             # EP0005를 만든 후, key를 발견하면 탈출?
#             if k == 'EP0005':
#                 return
#

def json_insert(data: dict):
    insert_dict = data
    pprint.pprint(insert_dict)
    for k, v in data.items():
        if k != 'shot':
            if isinstance(v, dict):
                print('shot 아니니 넘어가')
                json_insert(v)
        # print(data)
        else:
            print('shot이다')
            print('k번:', insert_dict[k])
            insert_dict[k].add = 'EP0005'  #{'EP0005_0050': {'frange': [1001, 1200]}}
            print('결과일까')
            pprint.pprint(insert_dict)
            return
    return insert_dict


import pprint

# pprint.pprint(json_insert(json_data))
json_insert(json_data)