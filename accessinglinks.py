#REquired libraries
import pandas as pd
from pandas import DataFrame
import csv
import bs4
from bs4 import BeautifulSoup
import zipfile
def parse(path,sy,ey):
    a=0
    b=0
    #PART 1:Entering year and quarter
    path=raw_input("Final path to save the csv files")
    sy=int(raw_input("Input start year"))
    ey=int(raw_input("Input end year"))
    while sy not in  range(2011,2016):
        print "Sorry.Input years are not between 2011 and 2016"
        sy=int(raw_input("Input start year"))
    while ey not in  range(2011,2016):
        print "Sorry.Input years are not between 2011 and 2016"
        ey=int(raw_input("Input end year"))
    sqtr=int(raw_input("Input start quarter"))
    eqtr=int(raw_input("Input end quarter"))
    i="ftp://ftp.sec.gov/full-index"
    f=range(sy,ey+1)
    g=['QTR1','QTR2','QTR3','QTR4']
    k=f[0]
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
                    zip_ref = zipfile.ZipFile('C:/Users/U505121/Desktop/full-index1/'+str(k)+'/'+str(l)+r[6]+'-xbrl.zip', 'r')
                    u=zip_ref.namelist()#storing the files in zipfile in a list
                    zip_ref.extract(u[0],'C:/Users/U505121/Desktop/full-index1/'+str(k)+'/'+str(l)+'/')#Since namelist presents in sorted manner,first member .xml is the required file
                    zip_ref.close()
                    
        #PART 5:converting xml to df to csv
                    soup=BeautifulSoup(open('C:/Users/U505121/Desktop/full-index1/'+str(k)+'/'+str(l)+'/'+str(u[0])))
                    result=soup.find_all()
                    at= soup.find('xbrl')
                    if at==None:
                        at=soup.find('xbrli:xbrl')
                    y = at.attrs #storing all the ns values of different xmlns 
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
                                    x10.append(t[z])#obtaining CIK
                                    x11.append(v[z])#obtaining company name
                                    x12.append(s[z])#obtaining form type
                    df=DataFrame({'elementId':x1, 'contextId':x2, 'unitId':x3, 'fact':x4, 'decimals':x5, 'scale':x6, 'sign':x7, 'factid':x8, 'ns':x9,'CIK':x10,'Company Name':x11,'Form Type':x12})#assigning each tags to its respective columns
                    
        #PART 6:for appending csv files
                    if(a==301):#As soon as 300 files are put into one csv,a news csv is made and files will be stored in that
                        b=b+1
                        pd.DataFrame.to_csv(df,path+'/'+str(b)+'.csv',sep='|',index=False)
                        a=1
                    else:
                        with open(path+'/'+str(b)+'.csv',"a"):#appending 300 xml files into a single csv
                            pd.DataFrame.to_csv(df,header=False,index=False,sep='|')
                            a+=1