#-*- coding: utf-8 -*-
'''
Created on 2020. 9. 12.

@author: JJ
'''
from conf import ConfigConsts


def clearCsvFile(stockcode):
    filepath = ConfigConsts.getdatafiledir()+stockcode+"tmp.csv"
    file=open(filepath, 'w')
    return file

def openCsvFile(stockcode):
    filepath = ConfigConsts.getdatafiledir()+stockcode+"tmp.csv"
    file=open(filepath, 'a')
    return file

def writeFile(file, data):
    file.write(data)
    print(data)
    
def closeCsvFile(file):
    file.close()    

def __clearReverseCsvFile(stockcode):
    filepath = ConfigConsts.getdatafiledir()+stockcode+".csv"
    file=open(filepath, 'w')
    return file

def __openReverseCsvFile(stockcode):
    filepath = ConfigConsts.getdatafiledir()+stockcode+".csv"
    file=open(filepath, 'a')
    return file

def makeReversedCsvFile(stockcode):
    print("MAKE REVERSE")
    filepath = ConfigConsts.getdatafiledir()+stockcode+"tmp.csv"
    ofile=open(filepath,"r")
    k=ofile.readlines()
    t=reversed(k)
    
    __clearReverseCsvFile(stockcode)
    newfile=__openReverseCsvFile(stockcode)
    
    for i in t:
        writeFile(newfile,i)
        
    closeCsvFile(newfile)
    print("MAKE REVERSE COMPLETE")
        
        
        