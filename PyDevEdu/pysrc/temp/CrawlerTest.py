'''
Created on 2017. 12. 7.

@author: 073860
'''

import requests as rq

req = rq.get("http://dis.kofia.or.kr/websquare/index.jsp?w2xPath=/wq/etcann/DISDLSSubscribing.xml&divisionId=MDIS04007001000000&serviceId=SDIS04007001000#!")

print(req.text)
print(req)