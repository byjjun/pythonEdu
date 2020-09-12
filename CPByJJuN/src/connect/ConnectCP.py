#-*- coding: utf-8 -*-
'''
Created on 2020. 9. 12.

@author: JJ
'''

import win32com.client

def checkConnect():
    # 연결 여부 체크
    objCpCybos = win32com.client.Dispatch("CpUtil.CpCybos")
    bConnect = objCpCybos.IsConnect
    if (bConnect == 0):
        print("PLUS가 정상적으로 연결되지 않음. ")
        exit()
    
    
