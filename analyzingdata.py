# -*- coding: utf-8 -*-
"""
Created on Wed Jun 01 14:46:58 2016

@author: U505121
"""

#Extract dataframe from part 3
df1=[]
df2=[]
for i in df.index:
    if "div" in df['fact'][i]:
        df1.append(df['fact'][i])
for i in xrange(0,df1.__len__()):
    df1[i]=df1[i].encode('UTF8')
    if 'sales' in df1[i]:
        df2.append(df1[i])
    elif 'revenues' in df1[i]:
        df2.append(df1[i])
    elif 'approximately' in df1[i]:
        df2.append(df1[i])
for i in xrange(0,df2.__len__()):
    df2[i]=" ".join((df2[i]).split())