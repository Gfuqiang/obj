"""
TMach系统获取token接口demo。
Python version: 3.6
"""
import requests


# 深圳TMach系统ip地址: 10.61.1.26
url = 'http://10.61.1.26:8000/api/v1/login/'
body = {'username': 'admin', 'password': 'admin'}

rep = requests.post(url, json=body)
token = rep.json().get('token')
print(token)
# b6970f6001b5a6076745d38f25c2022d76009950
print(rep.json())
# {'id': 2, 'username': 'admin', 'last_name': '', 'token': 'b6970f6001b5a6076745d38f25c2022d76009950'}