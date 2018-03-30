# -*- coding: utf8 -*-

'''
Created on 2018. 2. 2.

@author: 073860
'''
 
s="AAA"\
+"AAA"

print s 
 
hoo = unicode('한글', 'utf-8')
print str(hoo.encode('utf-8'))

bar = '한글'.decode('utf-8')
print bar.encode('utf-8')

foo = u'한글'
print str(foo.encode('utf-8'))

str1 = 'AAA'+'BBB'\
+'BBB'\
+'CCC'
print str1



str_elshtml = \
"<hr />"\
"<table style=\"height: 91px;\" width=\"475\">"\
"<tbody>"\
"<tr style=\"height: 29px;\">"\
"<td style=\"width: 343px; height: 29px; background-color: #d7d6a5;\" colspan=\"3\">"+'elsdic'+"</td>"\
"<td style=\"width: 116px; height: 29px; background-color: #dba67b;\">"+'elsdic'+"% </td>"\
"</tr>"\
"<tr style=\"height: 29px;\">"\
"<td style=\"width: 109px; height: 29px; background-color: #c4e7e7;\">판매종료</td>"\
"<td style=\"width: 114px; height: 29px; background-color: #f2ede4;\">"+'elsdic'+"</td>"\
"<td style=\"width: 108px; height: 29px; background-color: #c4e7e7;\">만기일</td>"\
"<td style=\"width: 116px; height: 29px; background-color: #f2ede4;\">"+'elsdic'+"</td>"\
"</tr>"\
"<tr style=\"height: 30px;\">"\
"<td style=\"width: 109px; height: 30px; background-color: #c4e7e7;\">기초자산</td>"\
"<td style=\"width: 350px; height: 30px; background-color: #f2ede4;\" colspan=\"3\">"+'elsdic'+"</td>"\
"</tr>"\
"<tr style=\"height: 30px;\">"\
"<td style=\"width: 109px; height: 30px; background-color: #c4e7e7;\">ELS구조</td>"\
"<td style=\"width: 350px; height: 30px; background-color: #f2ede4;\" colspan=\"3\">"+'elsdic'+"</td>"\
"</tr>"\
"<tr style=\"height: 30px;\">"\
"<td style=\"width: 109px; height: 30px; background-color: #c4e7e7;\"><a href=\""+'elsdic'+"\" target=\"_blank\" rel=\"noopener\">상세정보(Click)</a></td>"\
"<td style=\"width: 350px; height: 30px; background-color: #f2ede4;\" colspan=\"3\">"+'elsdic'+"</td>"\
"</tr>"\
"</tbody>"\
"</table>"

print str_elshtml