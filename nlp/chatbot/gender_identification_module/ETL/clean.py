import pandas as pd
import os
import sys
import re
import requests
import nltk
from nltk.corpus import stopwords
from fake_useragent import UserAgent


abs_path=os.path.abspath(os.path.dirname(sys.argv[0]))
path_male="/data/new_male_names.csv"
path_female="/data/new_female_names.csv"

stoplist=[]
with open(abs_path+"/data/stoplist.txt","r") as f:
    temp=f.read()
stoplist=str.split(str(temp),"\n")  

dat=pd.read_csv(abs_path+path_male)
m_defnames=["sri","mr","mohammad","muhammad",'md','mister','master','lord','rev','revd']
f_defnames=["smt","mrs","ms","kaur","begum","jahan","kumari","bai",'lady','maam']
        
dict1=set(dat['name'].dropna().tolist())
dat=pd.read_csv(abs_path+path_female)
dict2=set(dat['name'].dropna().tolist())
names_list=set()
dict1.update(m_defnames)
dict2.update(f_defnames)

#dict1=filter(lambda v: v is not None, dict1)
#dict2=[i for i in dict2 if i is not None]
try:
    names_list=set(dict1)
    names_list=set((dict2))
except Exception:
    print("dict excetpyion")

temp=pd.DataFrame({'name':list(set(dict2))})
temp.to_csv((abs_path+path_female),mode='w+')

temp=pd.DataFrame({'name':list(set(dict1))})
temp.to_csv((abs_path+path_male),mode='w+')
#print (temp)