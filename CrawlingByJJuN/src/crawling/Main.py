#-*- coding: utf-8 -*-

'''
Created on 2017. 12. 22.

@author: 073860
'''

import XmlParser4ELS
import MakeELSHtml

elsdiclist = XmlParser4ELS.elsparser()
rate_sorted = sorted(elsdiclist, key=lambda k: k['elsrate'], reverse=True)

#XmlParser4ELS.debug_els_dic(rate_sorted)
MakeELSHtml.makeelshtml(rate_sorted)

