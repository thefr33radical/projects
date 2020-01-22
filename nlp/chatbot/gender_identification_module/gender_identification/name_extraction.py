# -*- coding: utf-8 -*-

import pandas as pd
import os
import sys
import re
import requests
import nltk
from nltk.corpus import stopwords
from fake_useragent import UserAgent

'''
Required Files
    
        1. new_indian_male_names.csv    -> abspath/data
        2. new_indian_female_names.csv  -> abspath/data
        3. stoplist.txt                 -> abspath/data        
        
'''

abs_path=os.path.abspath(os.path.dirname(sys.argv[0]))
path_male="/data/new_male_names.csv"
path_female="/data/new_female_names.csv"

stoplist=[]
try:
    with open(abs_path+"/data/stoplist.txt","r") as f:
        temp=f.read()
        stoplist=str.split(str(temp),"\n")  
except Exception:
    print("reading stoplist exception") 
    
try:
    dat=pd.read_csv(abs_path+path_male)
    dict1=dat['name'].dropna().tolist()
    dat=pd.read_csv(abs_path+path_female)
    dict2=dat['name'].dropna().tolist()
except Exception:
    print("reading names exception")

names_list=set()
try:
    names_list=set(dict1)
    names_list=set((dict2))
except Exception:
    print("dict excetpyion")
    

#5.
def ner(string):
    
    sent=nltk.sent_tokenize(string)
    words=[nltk.word_tokenize(i) for i in sent]
    taggedwords=[nltk.pos_tag(i) for i in words]

    names=[]
    for i in taggedwords:
        for j in i:
            if j[1]=='NN':
                #print(j)
                names.append(j[0])
    return names
    
              
#4.
def check_online(value):
    print("checking online")
    try:
            url = "http://www.gpeters.com/names/baby-names.php?name="+value+"&button=Go"
            ua = UserAgent()
            header = {'User-Agent':str(ua.chrome)}
            f = requests.get(url,headers=header)
            get_page=re.findall("<b>It's a(.*)!</b>",f.text)
            
            ident= get_page[0]
            ident=str(ident)
           
            if(' boy' == ident):
               # print(1)
                temp=pd.DataFrame({'name':list(set(dict1))})
                print(temp)
                temp.to_csv((abs_path+path_male),mode='w+')
                return 1
            if(' girl' == ident):
               # print(1)
                temp=pd.DataFrame({'name':list(set(dict2))})
                temp.to_csv((abs_path+path_female),mode='w+')
                return 1
            return 0
    except Exception:
             print ("exception")
             return 0
            
#3.           
def check_in_dict(names):
   # print(names,names_list)
    if(names in names_list):
        return 1
    else:
        return 0

 
#2.
def remove_stopwords(string):
    #input string
    value = string
    value=value.lower()
    value=re.sub('[^A-Za-z\s]',"",value)
    stop=stopwords.words('english')
    string=value
    value=' '.join([i for i in string.split() if i not in stop])
    value=' '.join([i for i in value.split() if i not in stoplist])
    return(value)
    #output list
          
#1.
def starter(real_name):
    names=remove_stopwords(real_name)
    names=str.split(names," ")
    output=[]
    real_name=str.split(real_name," ")
    output1=[[i,0] for i in real_name]
    flag=0
    
    for i in names:
        value=0
        
        value=check_in_dict(i)
        if(value==0 and len(i)>4):
            value=check_online(i)
            pass
        if(flag==1 and value ==0):
            break
        output.append([i,value])

    prev_name=""
    str_name=""
    post_name=""

    for i in range(len(output)):
        for j in range(len(output1)):
            if(output[i][0]==output1[j][0]):
                    if(output[i][1]==1):
                        output1[j][1]=1
                        break
    flag=0
    pre_flag=0
    for i in range(len(output1)):
        if(int(output1[i][1])==1):
            flag=1
            str_name+=output1[i][0]+" "
            if(i>0 and pre_flag ==0):
                prev_name+=output1[i-1][0]
                pre_flag=1
        if(flag==1 and int(output1[i][1])==0):
            if(i<len(output1)):
                post_name+=output1[i][0]
                break
    #print(output,"\n",output1,"\n",prev_name,"\n",str_name,"\n",post_name)
    return [prev_name,str_name,post_name]
   # print("\n",prev_name,"\n",str_name,"\n",post_name)
    
            

if __name__=='__main__':
    real_name="i am not so much interested in the price"
    print(starter(real_name))
        
        
