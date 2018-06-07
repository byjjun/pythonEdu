#-*- coding: utf-8 -*-

'''
Created on 2018. 6. 7.

@author: 073860
'''
from LOAN import CreditLoanGetJSON
from LOAN import CreditLOANJSONParser


from datetime import datetime

def make_creditloan_hello():
    str_hello = ''
    str_hello += \
    str(datetime.today().strftime('%Y년 %m월 %d일 '))+'신용대출 및 마이너스통장 최저금리 리스트 입니다.' \
    "<br>자세한 목록은 아래를 참조해 주세요." \
    "<br/>"\
    "<br><br>FundingChoice에서는 매일 최신의 자료로 업데이트 됩니다"\
    "<br><font size=5><a href=\"http://fundingchoice.co.kr/?cat=5\">여기</a></font>에서 최신 비교자료를 확인하세요"\
    "<br/>"\
    "&nbsp;"
    return str_hello

def mkhtml_creditloan():
    
    loanlist = CreditLOANJSONParser.loanparser('은행','개인신용대출',5)
    creditloan_htmlstr = ''
    for _bankloaninfo in loanlist:
        creditloan_htmlstr += \
        "<table>"\
        "<tr>"\
        "<th colspan=\"2\"><strong>"+_bankloaninfo['fin_compy_name'].encode('UTF-8')+"</th>"\
        "<th colspan=\"2\"><strong>"+_bankloaninfo['loan_name'].encode('UTF-8')+"</th>"\
        "</tr>"\
        "<tr>"\
        "<td colspan=\"2\"><strong>평균대출금리</td>"\
        "<td colspan=\"2\"><strong>"+str(_bankloaninfo['crdt_grad_avg']).encode('UTF-8')+"%</td>"\
        "</tr>"\
        "<tr>"\
        "<td>1~2등급</td>"\
        "<td>"+str(_bankloaninfo['crdt_grad_1']).encode('UTF-8')+"%</td>"\
        "<td>3~4등급</td>"\
        "<td>"+str(_bankloaninfo['crdt_grad_4']).encode('UTF-8')+"%</td>"\
        "</tr>"\
        "<tr>"\
        "<td>5~6등급</td>"\
        "<td>"+str(_bankloaninfo['crdt_grad_5']).encode('UTF-8')+"%</td>"\
        "<td>7~8등급</td>"\
        "<td>"+str(_bankloaninfo['crdt_grad_6']).encode('UTF-8')+"%</td>"\
        "</tr>"\
        "</table>"\
        "<hr/>"\
    
    return creditloan_htmlstr

print make_creditloan_hello()
print mkhtml_creditloan()