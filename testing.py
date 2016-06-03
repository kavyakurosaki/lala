# -*- coding: utf-8 -*-
"""
Created on Fri Jun 03 14:37:06 2016

@author: U505121
"""

import bs4
import re
from bs4 import BeautifulSoup
import pandas
from pandas import DataFrame
soup=BeautifulSoup(open('C:/Users/U505121/Desktop/Hormel.xml'))
result=soup.find_all()

fin_text_list = []

for i in result:
    if 'contextref' in i.attrs:
        string_is = ''
        text = i.text.encode('utf-8')
        soup2 = BeautifulSoup(text)
        for j in soup2.find_all('p'):
            string_is = string_is+j.text
        fin_text_list.append(string_is.encode('utf-8'))


sentences = []
for i in fin_text_list:
    if len(i)>10:
        x = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s',i)
        sentences.append(x)

flattened = [val for sublist in sentences for val in sublist]

final_count=[]
for i in flattened:
    x = " ".join((i).split())
    if x!='':
        final_count.append(x)

