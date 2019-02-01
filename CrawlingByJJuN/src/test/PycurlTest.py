#-*- coding: utf-8 -*-

'''
Created on 2019. 1. 25.

@author: 073860
'''

import requests
import json
import base64


user = 'byjjun'
pythonapp = 'POCKTAN1'
url = 'http://fundingchoice.co.kr/wp-json/wp/v2'
#url = 'http://fundingchoice.co.kr/index.php/wp-json/wp/v2'
#url = 'http://fundingchoice.co.kr/index.php/wp/v2'

data_string = user + ':' + pythonapp

token = base64.b64encode(data_string.encode())

headers = {'Authorization': 'Basic ' + token.decode('utf-8')}

post = {'date': '2019-01-25T12:47:35',
        'title': 'First REST API post',
        'slug': 'stock',
        'status': 'publish',
        'content': '<br>this is the content <br>post',
        'format': 'standard'
        }
'''
post = {'title': 'TEST',
        'slug': 'stock',
        'status': 'publish',
        'content': '<br>this is the content <br>post',
        'author': 'byjjun@gmail.com',
        'format': 'standard'
        }
'''


r = requests.post(url + '/posts', headers=headers, json=post)

print r

temp = {}
tmp= json.loads(r.content)
print tmp['message']
#print temp[message]
#print('Your post is published on ' + json.loads(r.content.decode('utf-8'))['link'])


