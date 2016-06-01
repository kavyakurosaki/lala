# -*- coding: utf-8 -*-
"""
Created on Mon May 30 10:12:12 2016

@author: U505121
"""
import pandas as pd
from pandas import DataFrame
import csv
import os
import bs4
from bs4 import BeautifulSoup
import zipfile
soup=BeautifulSoup(open('C:/Users/U505121/Desktop/1.xml'))
result=soup.find_all()
a = soup.find('xbrl')
if a==None:
   a=soup.find('xbrli:xbrl')
y = a.attrs #storing all the ns values of different xmlns 
x1=[]
x2=[]
x3=[]
x4=[]  
x5=[]
x6=[]
x7=[]
x8=[]
x9=[]
x10=[]
x11=[]
x12=[]
for i in result: #extracting values for each row and column to form dataframe
                      tags=i.attrs
                      if tags.has_key('contextref'):
                            x1.append(i.name) #obtaining element id
                            x2.append(tags.get('contextref')) #obtaining context ref
                            x3.append(tags.get('unitref')) #obtaining unit ref
                            x4.append(i.text) #obtaining fact
                            x5.append(tags.get('decimals')) #obtaining decimals
                            x6.append(tags.get('scale'))#obtaining scale
                            x7.append(tags.get('sign'))#obtaining sign
                            x8.append(tags.get('factid'))#obtaining factid
                            if tags.has_key('xmlns'):#obtaining ns value based on the keys stored in y
                                        xm = y['xmlns']
                            elif 'link' in i.name:
                                        xm= y['xmlns:link']
                            elif 'dei' in i.name:
                                        xm= y['xmlns:dei']
                            elif 'hrl' in i.name:
                                        xm= y['xmlns:hrl']
                            elif 'us-gaap' in i.name:
                                        xm= y['xmlns:us-gaap']
                            elif 'xbrli' in i.name:
                                        xm = y['xmlns:xbrli']
                            elif 'xbrldi' in i.name:
                                        xm = y['xmlns:xbrldi']
                            elif 'xlink' in i.name:
                                        xm = y['xmlns:xlink']
                            elif 'xsi' in i.name:
                                        xm = y['xmlns:xsi']
                            x9.append(xm)
                            #x10.append(t[z])#obtaining CIK
                           # x11.append(v[z])#obtaining company name
                            #x12.append(s[z])#obtaining form type
df=DataFrame({'elementId':x1, 'contextId':x2, 'unitId':x3, 'fact':x4, 'decimals':x5, 'scale':x6, 'sign':x7, 'factid':x8, 'ns':x9})#,'CIK':x10,'Company Name':x11,'Form Type':x12})#assigning each tags to its respective columns
            