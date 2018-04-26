#-*- coding: utf-8 -*-
'''
Created on 2018. 2. 6.

@author: 073860
'''
from datetime import datetime
from SAVING import MakeSAVINGHtml
from SAVING import JSONParser4SAVING

if __name__ == '__main__':
    pass

#은행
#정기예금 - 우대포함
print datetime.today().strftime('%Y년 %m월 %d일 '),'기준  예금금리  Top 5 입니다.'
print "<br/>"
print "<hr/>"
print "은행 우대금리 기준 Top 5"
print "<br/>"
topsaving_list=JSONParser4SAVING.savingparser('은행', '예금', 1)
print MakeSAVINGHtml.make_str_produchtml(topsaving_list)

#정기예금 - 우대 비포함
print "<hr/>"
print "은행 단순금리 기준 Top 5"
print "<br/>"
topsaving_list=JSONParser4SAVING.savingparser('은행', '예금', 2)
print MakeSAVINGHtml.makeproduchtml(topsaving_list)

#저축은행
#정기예금 - 우대포함
print "<hr/>"
print "저축은행 우대금리기준 Top 5"
print "<br/>"
JSONParser4SAVING.savingparser('저축은행', '예금', 1)
print MakeSAVINGHtml.makeproduchtml(topsaving_list)
#정기예금 - 우대비포함
print "<hr/>"
print "저축은행 일반금리기준 Top 5"
print "<br/>"
topsaving_list=JSONParser4SAVING.savingparser('저축은행', '예금', 2)
print MakeSAVINGHtml.makeproduchtml(topsaving_list)
