import bs4 
import re 
from bs4 import BeautifulSoup 
import pandas 
from pandas import DataFrame 
soup=BeautifulSoup(open('C:/Users/U505121/Desktop/xml/10_K/outt2101.csv')) 
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
         x = re.split(r'(\. [A-Z])',i) 
         sentences.append(x)
 
 
flattened = [val for sublist in sentences for val in sublist] 
 
 
final_count=[] 
for i in flattened: 
     x = " ".join((i).split()) 
     if x!='': 
         final_count.append(x) 
if final_count[0][0]=='.':
    fc = []
else:
    fc=[final_count[0]]
i=1
while True:
    if i>=len(final_count):
        break
    if final_count[i][0]=='.':
        i=i+1
        continue
    if final_count[i-1][0]=='.':
        temp = str(final_count[i-1][2])
        fc.append(temp+final_count[i])
    else:
        fc.append(final_count[i])
    i = i+1