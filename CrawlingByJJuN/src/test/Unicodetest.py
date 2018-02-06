# -*- coding: utf8 -*-

'''
Created on 2018. 2. 2.

@author: 073860
'''
 
hoo = unicode('한글', 'utf-8')
print str(hoo.encode('utf-8'))

bar = '한글'.decode('utf-8')
print bar.encode('utf-8')

foo = u'한글'
print str(foo.encode('utf-8'))