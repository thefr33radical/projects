

import requests
import string
from bs4 import BeautifulSoup

from fake_useragent import UserAgent
import pandas as pd
ua = UserAgent()
print(ua.chrome)
header = {'User-Agent':str(ua.chrome)}
dct=[]
switch=0
l1=[ str(e) for e in range(1,70)]
l2=list(string.ascii_lowercase)
#print(l2)
for i in l1:
    for j in l2:
        r=requests.get("http://sss.lcyyy.pcdcdapcogufktgev.lceqo.nl4.gsr.awhoer.net/baby-names/indian/girl/"+i+"/"+j)
        if(r.status_code==requests.codes.ok):
            soup=BeautifulSoup(r.text)
            a=soup.findAll('a')
            for i in a:
                if(i.text=='Z'):
                    switch=1
                if(i.text=='1' or i.text==' Back' or i.text=='2' or i.text=='A'):
                    switch=0
                if(switch==1):  
                   # print(i.text)
                    dct.append(i.text)
        
 
with open("data.txt","w+")as f:
    f.write(dct)
       
#z=pd.DataFrame([dct],columns='names')
#z.to_csv("data.csv")       

        
