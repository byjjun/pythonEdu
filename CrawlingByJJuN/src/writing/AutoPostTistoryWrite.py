#-*- coding: utf-8 -*-
'''
Created on 2019. 1. 17.

@author: 073860
'''

import requests


'''
ELS 771976
예금적금 771977
주식 771978
대출받기 771980
'''

def writeTstoryPost(category,tag,title,contents):
#def writeTstoryPost():
    url = 'https://www.tistory.com/apis/post/write'
    
    post_data = {'access_token' : 'cb08c8f727865836f77fd2fed9f4aef8_f76acdd266a3ec3bda480f948f4a3915',
                 'blogName': 'fundingchoice',
                 'title' : 'title',
                 'content' : 'contents',
                 'tag' : '',
                 'visibility' : '3', 
                 'category' : '771976' }
    
    
    post_data['title']='TITLE TEST'
    post_data['tag']='TAG TEST'
    post_data['content']='<br>aaa</br><br>aaa</br><br>aaa</br>'
    post_data['category']='771976'

    r = requests.post(url, params=post_data, verify=False)
   
    print(r.text)
    print(r.status_code)


writeTstoryPost()


    

