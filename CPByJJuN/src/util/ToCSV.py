#-*- coding: utf-8 -*-
'''
Created on 2020. 9. 12.

@author: JJ
'''
from conf import ConfigConsts


def clearCsvFile(stockcode):
    filepath = ConfigConsts.getdatafiledir()+stockcode+".csv"
    file=open(filepath, 'w')
    return file

def openCsvFile(stockcode):
    filepath = ConfigConsts.getdatafiledir()+stockcode+".csv"
    file=open(filepath, 'a')
    return file

def writeFile(file, data):
    file.write(data)
    print(data)
    
def closeCsvFile(file):
    file.close()    
