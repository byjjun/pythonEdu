#-*- coding: utf-8 -*-
'''
Created on 2020. 9. 15.

@author: JJ
'''

makefile = True
datafiledir = "D:\\cpbyjjun\\data\\"
stockcode = ''


def getmakeFile():
    global makefile
    return makefile

def setmakeFile(setting):
    global makefile
    makefile = setting
    
def getdatafiledir():
    global datafiledir
    return datafiledir


def setStockCode(code):
    global stockcode
    stockcode = code

def getStockCode():
    global stockcode
    return stockcode
    


        
def logger(logstr):
    print(logstr)
    


    
    
    
    
    
