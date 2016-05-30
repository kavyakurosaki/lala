#REquired libraries
import pandas as pd
from pandas import DataFrame
import csv
import bs4
from bs4 import BeautifulSoup
import zipfile
a=0
b=0
#PART 1:Entering year and quarter
i="ftp://ftp.sec.gov/full-index"
f=[2011,2012,2013,2014,2015]
g=['QTR1','QTR2','QTR3','QTR4']
k=f[0]
l=g[0]
for k in f: #Entering year
    j=i+'/'+str(k)
    for l in g: #Entering quarter
        m=j+'/'+str(l)
        urlretrieve=(m+'/xbrl.zip','C:/Users/U505121/Desktop/full-index1/'+str(k)+'/'+str(l)+'/')
        zip_ref = zipfile.ZipFile(m+'/xbrl.zip', 'r')
        zip_ref.extractall('C:/Users/U505121/Desktop/full-index1/'+str(k)+'/'+str(l)+'/') #Extracting zip file
        zip_ref.close()
        
#PART2:converting file to dataframe
        f=open("temp.idx","wb")
        f1=open('C:/Users/U505121/Desktop/full-index1/'+str(k)+'/'+str(l)+'/xbrl.idx',"r")
        for line in f1:
            if 'l' not in line:
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
        for z in df.index:
            r=df['Filename'][z].split('/')
            df['Filename'][z]=df['Filename'][z].replace('-','')
            df['Filename'][z]=df['Filename'][z]+'/'+r[6]+'-xbrl.zip'
            
#PART 4:extracting xml file from modified link
            urlretrieve=(df['Filename'][z],'C:/Users/U505121/Desktop/full-index1/'+str(k)+'/'+str(l)+'/')
            zip_ref = zipfile.ZipFile(df['Filename'][z], 'r')
            u=zip_ref.namelist()#storing the files in zipfile in a list
            zip_ref.extract(u[0],'C:/Users/U505121/Desktop/full-index1/'+str(k)+'/'+str(l)+'/')#Since namelist presents in sorted manner,first member .xml is the required file
            zip_ref.close()
            
#PART 5:converting xml to df to csv
            soup=BeautifulSoup(open('C:/Users/U505121/Desktop/full-index1/'+str(k)+'/'+str(l)+'/'+str(u[0])))
            result=soup.find_all()
            y = soup.findAll('xbrl')[0].attrs #storing all the ns values of different xmlns 
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
                            elif 'link' in result[i].name:
                                        xm= y['xmlns:link']
                            elif 'dei' in result[i].name:
                                        xm= y['xmlns:dei']
                            elif 'hrl' in result[i].name:
                                        xm= y['xmlns:hrl']
                            elif 'us-gaap' in result[i].name:
                                        xm= y['xmlns:us-gaap']
                            elif 'xbrli' in result[i].name:
                                        xm = y['xmlns:xbrli']
                            elif 'xbrldi' in result[i].name:
                                        xm = y['xmlns:xbrldi']
                            elif 'xlink' in result[i].name:
                                        xm = y['xmlns:xlink']
                            elif 'xsi' in result[i].name:
                                        xm = y['xmlns:xsi']
                            x9.append(xm)
                            x10.append(t[z])#obtaining CIK
                            x11.append(v[z])#obtaining company name
                            x12.append(s[z])#obtaining form type
            df=DataFrame({'elementId':x1, 'contextId':x2, 'unitId':x3, 'fact':x4, 'decimals':x5, 'scale':x6, 'sign':x7, 'factid':x8, 'ns':x9,'CIK':x10,'Company Name':x11,'Form Type':x12})#assigning each tags to its respective columns
            
#PART 6:for appending csv files
            if(a==301):#As soon as 300 files are put into one csv,a news csv is made and files will be stored in that
                b=b+1
                pd.DataFrame.to_csv(df,'C:/Users/U505121/Desktop/full-index1/'+str(k)+'/'+str(l)+'/'+'/'+str(b)+'.csv',sep='|',index=False)
                a=1
            else:
                with open('C:/Users/U505121/Desktop/full-index1/'+str(k)+'/'+str(l)+'/'+str(b)+'/'+'.csv',"a"):#appending 300 xml files into a single csv
                    pd.DataFrame.to_csv(df,header=False,index=False,sep='|')
                    a+=1