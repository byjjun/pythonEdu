#-*- coding: utf-8 -*-

'''
Created on 2017. 12. 12.

@author: 073860
'''
import win32com.client
 
 
objCpCybos = win32com.client.Dispatch("CpUtil.CpCybos")
bConnect = objCpCybos.IsConnect
if (bConnect == 0):
    print("PLUS")
    exit()
 
objCpCodeMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")
codeList = objCpCodeMgr.GetStockListByMarket(1)
codeList2 = objCpCodeMgr.GetStockListByMarket(2) 
 
 
print('코스피', len(codeList))
for i, code in enumerate(codeList):
    secondCode = objCpCodeMgr.GetStockSectionKind(code)
    name = objCpCodeMgr.CodeToName(code)
    stdPrice = objCpCodeMgr.GetStockStdPrice(code)
    print(i, code, secondCode, stdPrice, str(name.encode('utf-8')))
 
print("코스닥", len(codeList2))
for i, code in enumerate(codeList2):
    secondCode = objCpCodeMgr.GetStockSectionKind(code)
    name = objCpCodeMgr.CodeToName(code)
    stdPrice = objCpCodeMgr.GetStockStdPrice(code)
   # print(i, code, secondCode, stdPrice, name)
 
#print("전체종목",len(codeList) + len(codeList2))