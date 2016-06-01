# -*- coding: utf-8 -*-
"""
Created on Mon May 30 09:47:53 2016

@author: U505121
"""


import pandas as pd
from pandas import DataFrame
import csv
import os
import bs4
from bs4 import BeautifulSoup
import zipfile
a=0
b=0
#Entering year and quarter
i="C:/Users/U505121/Desktop/full-index"
f=[2011,2012]
g=['QTR1','QTR2','QTR3','QTR4']
k=f[0]
l=g[0]
for k in f:
    j=i+'/'+str(k)
    for l in g:
        m=j+'/'+str(l)
        zip_ref = zipfile.ZipFile(m+'/xbrl.zip', 'r')
        zip_ref.extractall(m)
        zip_ref.close()
        f=open("temp.idx","wb")
        f1=open(m+'/xbrl.idx',"r")
        for line in f1:
            if 'l' not in line:
                continue
            else:
                f.write(line)
        f.close()
        f1.close()
        df=pd.read_csv("temp.idx","|")
        #accessing files
       # df['Filename']="ftp://ftp.sec.gov/"+df['Filename']
       # df['Filename']=df['Filename'].map(lambda x:x.rstrip('.txt'))
       # for z in df.index:
        #    r=df['Filename'][z].split('/')
        #    df['Filename'][z]=df['Filename'][z].replace('-','')
         #   df['Filename'][z]=df['Filename'][z]+'/'+r[6]+'-xbrl.zip'