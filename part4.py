# -*- coding: utf-8 -*-
"""
Created on Mon May 30 10:26:42 2016

@author: U505121
"""
import pandas as pd
from pandas import DataFrame
import csv
import os
import bs4
from bs4 import BeautifulSoup
import zipfile
a=1
b=0
m=1
for m in range(1,5):
    soup=BeautifulSoup(open('C:/Users/U505121/Desktop/xml/'+str(m)+'.xml'))
    result=soup.find_all()
    x1=[]
    x2=[]
    x3=[]
    x4=[]      
    for i in result:
                          tags=i.attrs
                          if tags.has_key('contextref'):
                                x1.append(i.name)
                                x2.append(tags.get('contextref'))
                                x3.append(tags.get('unitref'))
                                x4.append(i.text)
    df=DataFrame({'elementid':x1,'contextref':x2,'unitref':x3,'factid':x4})
    pd.DataFrame.to_csv(df,'C:/Users/U505121/Desktop/full-index/2011/QTR1/file1.csv',sep='|')
    if(a==2):
                    b=b+1
                    pd.DataFrame.to_csv(df,'C:/Users/U505121/Desktop/xml/'+str(b)+'.csv',sep='|')
                    a=1
    else:
                    with open('C:/Users/U505121/Desktop/xml'+str(b)+'.csv',"a"):
                        pd.DataFrame.to_csv(df,header=False)
                    a+=1