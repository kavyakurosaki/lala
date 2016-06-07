# -*- coding: utf-8 -*-
"""
Created on Sun Jun 05 19:41:35 2016

@author: Kavya
"""
import bs4
from bs4 import BeautifulSoup

import zipfile
import urllib 
import urllib2
a=1
b=1
import pandas as pd
from pandas import DataFrame
 #PART2:converting file to datafram
f=open("temp.idx","wb")
f1=open('C:/Users/Kavya/Desktop/full-index/2015/QTR1/xbrl.idx',"r")
for line in f1:
                    if '|' not in line:
                        continue
                    else:
                        f.write(line)
f.close()
f1.close()
df=pd.read_csv("temp.idx","|")
t=df['CIK']
v=df['Company Name']
s=df['Form Type']

#PART 3:getting link from dataframe and modifying it to obtain xbrl zip file
df['Filename']="ftp://ftp.sec.gov/"+df['Filename']
df['Filename']=df['Filename'].map(lambda x:x.rstrip('.txt'))
for z in xrange(0,5):
                     #r=df['Filename'][z].split('/')
                     #df['Filename'][z]=df['Filename'][z].replace('-','')
                     #df['Filename'][z]=df['Filename'][z]+'/'+r[6]+'-xbrl.zip'
                     store=df['Filename'][0][-29:]

                     #urllib.urlretrieve(str(df['Filename'][z]),'C:/Users/Kavya/Desktop/full-index/2015/QTR1/forms/'+str(store))
                     zip_ref = zipfile.ZipFile('C:/Users/Kavya/Desktop/full-index/2015/QTR1/forms/'+str(store), 'r')
                     u=zip_ref.namelist()#storing the files in zipfile in a list
                     #zip_ref.extract(u[0],'C:/Users/Kavya/Desktop/full-index/2015/QTR1/forms/')#Since namelist presents in sorted manner,first member .xml is the required file
                     zip_ref.close()
                     soup=BeautifulSoup(open('C:/Users/Kavya/Desktop/full-index/2015/QTR1/forms/'+str(u[0])))
                     result=soup.find_all()
                     at= soup.find('xbrl')
                     if at==None:
                         at=soup.find('xbrli:xbrl')
                     y = at.attrs #storing all the ns values of different xmlns
                     k=y.keys()
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
                     ke1=[] 
                     for i in range(0,k.__len__()):
                         ke=k[i].split(':')
                         ke1.append(ke[1])
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
                                                        for j in ke1:
                                                            if j in i.name:
                                                                xm=y['xmlns:'+j]
                                                            else:
                                                                xm=None
                                                        x9.append(xm)
                                                        x10.append(t[z])#obtaining CIK
                                                        x11.append(v[z])#obtaining company name
                                                        x12.append(s[z])#obtaining form type
                     df1=DataFrame({'elementId':x1, 'contextId':x2, 'unitId':x3, 'fact':x4, 'decimals':x5, 'scale':x6, 'sign':x7, 'factid':x8, 'ns':x9,'CIK':x10,'Company Name':x11,'Form Type':x12})#assigning each tags to its respective column
                     
                     if(a==1 or a==301):#As soon as 300 files are put into one csv,a news csv is made and files will be stored in that
                                        pd.DataFrame.to_csv(df1,'C:/Users/Kavya/Desktop/full-index/2015/QTR1/forms/'+str(b)+'.csv',sep='|',index=False)
                                        a+=1
                                        if a==301:
                                            b=b+1
                                            a=1
                     else:
                                        with open('C:/Users/Kavya/Desktop/full-index/2015/QTR1/forms/'+str(b)+'.csv',"a") as f:#appending 300 xml files into a single csv
                                            pd.DataFrame.to_csv(df1,f,header=False,index=False,sep='|')
                                            a+=1  
