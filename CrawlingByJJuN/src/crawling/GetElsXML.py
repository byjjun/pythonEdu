'''
Created on 2017. 12. 22.

@author: 073860
'''

import requests

def get_current_els_xml():
    request_url = 'http://dis.kofia.or.kr/proframeWeb/XMLSERVICES/'
    request_xml = """<?xml version='1.0' encoding='utf-8'?>
    <message>
      <proframeHeader>
        <pfmAppName>FS-DIS2</pfmAppName>
        <pfmSvcName>DISDlsOfferSO</pfmSvcName>
        <pfmFnName>selectSubscribing</pfmFnName>
      </proframeHeader>
      <systemHeader></systemHeader>
        <DISDlsDTO>
        <val1></val1>
        <val2></val2>
        <val3></val3>
        <val4></val4>
        <val5></val5>
        <val6>0</val6>
    </DISDlsDTO>
    </message>"""
    
    
    headers = {'Content-Type': 'text/xml'} # set what your server accepts
    #data = requests.post(request_url, data=request_xml, headers=headers).text
    data = requests.post(request_url, data=request_xml, headers=headers).content
    return data
