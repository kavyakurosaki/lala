# -*- coding: utf-8 -*-
"""
Created on Mon May 30 09:37:07 2016

@author: U505121
"""

import pandas as pf
from pandas import DataFrame
import csv
import os
import bs4
from bs4 import BeautifulSoup
import zipfile
a=0
b=0
sy=int(raw_input("Input start year"))
ey=int(raw_input("Input end year"))
while sy not in  range(2011,2016):
    print "Sorry.Input years are not between 2011 and 2016"
    sy=int(raw_input("Input start year"))
while ey not in  range(2011,2016):
    print "Sorry.Input years are not between 2011 and 2016"
    ey=int(raw_input("Input end year"))
sqtr=int(raw_input("Input start quarter:[1,2,3,4]"))
eqtr=int(raw_input("Input end quarter:[1,2,3,4]"))
while sqtr not in  range(2011,2016):
    print "Sorry.Input years are not between 2011 and 2016"
    sqtr=int(raw_input("Input start year"))
while eqtr not in  range(2011,2016):
    print "Sorry.Input years are not between 2011 and 2016"
f=range(sy,ey+1)
g=['QTR1','QTR2','QTR3','QTR4']
k=f[0]
le=f.__len__()
l=g[sqtr]
#Entering year and quarter
i="C:/Users/U505121/Desktop/full-index"
for k in f:
    j=i+'/'+str(k)
    if k==sy:
        if k==ey and l==g[eqtr]:
                break
        while sqtr<5:
            print sqtr
            l=g[sqtr-1]
            if k==ey and l==g[eqtr]:
                break
            m=j+'/'+str(l)
            zip_ref = zipfile.ZipFile(m+'/xbrl.zip', 'r')
            zip_ref.extractall(m)
            zip_ref.close()
            sqtr=sqtr+1
            
    else:
        for l in g: #Entering quarter
            if k==ey and l==g[eqtr]:
                break
            m=j+'/'+str(l)
            urlretrieve=(m+'/xbrl.zip','C:/Users/U505121/Desktop/full-index/'+str(k)+'/'+str(l)+'/')
            zip_ref = zipfile.ZipFile(m+'/xbrl.zip', 'r')
            zip_ref.extractall('C:/Users/U505121/Desktop/full-index/'+str(k)+'/'+str(l)+'/') #Extracting zip file
            zip_ref.close()
