# -*- coding: utf-8 -*-

'''
Created on 2018. 1. 30.

@author: 073860
'''


import requests

apikey = 'c00ce82f75408d5a4d3bbe6c8db89dd2'

def get_current_saving_json():
    request_url = 'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth='+apikey+'&topFinGrpNo=020000&pageNo=1'
    print request_url
    data = requests.post(request_url).content
    print data
    #return data
    
get_current_saving_json()