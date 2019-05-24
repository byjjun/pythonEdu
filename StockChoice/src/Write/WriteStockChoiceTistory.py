#-*- coding: utf-8 -*-
'''
Created on 2019. 1. 17.

@author: 073860
'''

import requests
from time import time, sleep
import requests as RR

def writeTstoryPost(category,title,tag,contents):
    '''
    $$$$카테고리 $$$$
        괴리율 742010

    '''
    url = 'https://www.tistory.com/apis/post/write'
    print url
    
    parameter = {'access_token' : 'cb08c8f727865836f77fd2fed9f4aef8_f76acdd266a3ec3bda480f948f4a3915',
                 'blogName': 'stockchoice',
                 'title' : 'title'
                 }
    
    post_data = {'content' : '<br>contents</br>으아아아',
                 'tag' : '',
                 'visibility' : '3', 
                 'category' : '742010' }
    
    
    parameter['title']=title
    post_data['tag']=tag
    post_data['content']=contents
    post_data['category']=category

    #print title
    #print post_data['title']
    #print post_data['tag']
    #print post_data['content']
    #print post_data['category']
    
    sleep(10)
    
    #r = RR.post(url, params = parameter, data=json.dumps(post_data), verify=False)
    r = RR.post(url, params = parameter, data=post_data, verify=False)
       
    print(r.text)
    print(r.status_code)




    

