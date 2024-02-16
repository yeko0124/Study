#!/usr/bin/env python
# encoding=utf-8

# author        : yeeun ko
# create date   : 2024.02.16
# modified date : 2024.02.16
# description   :

import requests

tasks = [
    {
        'id': 1,
        'title': 'Task 1',
        'done': False
    },
    {
        'id': 2,
        'title': 'Task 2',
        'done': True
    }
]

url = 'http://127.0.0.1:5000'

r = requests.get(url+'/tasks')
r.json()
print('get', r.json())

r = requests.get(url+'/tasks/1')
print('get', r.json())


data = {'user': 'yeeun', 'dept': 'td', 'title': 'lalala'}
r = requests.post(url+'/tasks', json=data)
print('post', r.json())

r = requests.put(url+'/tasks/2', json=data)
print('put', r.json())

r = requests.delete(url+'/tasks/1,2', json=data)
print(r.status_code)
print(r.text)

###############################################

r = requests.get(url+'/tasks')
print(r.json())

