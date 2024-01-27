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
insert_key_data = {'EP0005': {'EP0005_0050': {'frange': [1001, 1200]}}}

delete_key_data = {'project': {'shot': {'EP0005': None}}}

def json_insert(data: dict, in_data: dict):
    for k, v in data.items():
        if k != 'shot':
            if isinstance(v, dict):
                json_insert(v, in_data)
        else:
            data[k].update(in_data)
    return data


import pprint

pprint.pprint(json_data)
print('-'*50)
pprint.pprint(json_insert(json_data, insert_key_data))
