#-*- coding: utf-8 -*-
'''
Created on 2021. 3. 6.

@author: JJ
'''

import win32com.client




'''
excel = win32com.client.Dispatch("Excel.Application")
excel.Visible = True

wb = excel.WorkBooks.Add()
ws = wb.Worksheets("Sheet1")
ws.Cells(1,1).Value = "Hello Hello"
'''

instCpStockCode = win32com.client.Dispatch("CpUtil.CpStockCode")
print(instCpStockCode.GetCount())
print(instCpStockCode.CodeToName("A005930"))
print(instCpStockCode.NameToCode("아이큐어"))


cpsysdiblist = win32com.client.Dispatch("CpSysDib.CssStgList")

## 전략을 가져올 Type 세팅(나의전략:ord('1')
cpsysdiblist.SetInputValue(0, ord('1'))  # '0' : 예제전략, '1': 나의전략

##Block모드로 
cpsysdiblist.BlockRequest()

##불러오기
count = cpsysdiblist.GetHeaderValue(0)    #0 : (long) 전략목록수
flag =  cpsysdiblist.GetHeaderValue(1)    #1 : (char) 요청구분

for i in range(count):
    item = {}
    item['전략명'] = cpsysdiblist.GetDataValue(0,i);
    item['전략ID'] = cpsysdiblist.GetDataValue(1,i);
    print("----")
    print(item)


cpsysdibfind = win32com.client.Dispatch("CpSysDib.CssStgFind")

