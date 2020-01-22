import pandas as pd
from nltk.corpus import stopwords

path =""
p=pd.read_csv(path)
#newfile=set(p['names'])
q=pd.read_csv(path)
female_names=set(q['name'])
print(len(female_names))
temp=[]
stopw=set(stopwords.words('english'))
female_names2=set()
for j in female_names:
     j=str(j)
     if("s/o" in j):
         j=str.replace(j,"s/o","")
     if("d/o" in j):
        j=str.replace(j,"d/o","")
     if("w/o" in j):
        j=str.replace(j,"w/o","")
        
     if("@" in j):
         j=str.replace(j,"@","")
     if("s/0" in j):
                j=str.replace(j,"s/0","")
     if("w/0" in j):
                j=str.replace(j,"w/0","")  
     if("d/0" in j):
               ## print(j)
                j=str.replace(j,"d/0","")
               # print(j)
               # print("ffFFFF")
                
     female_names2.add(j)


for i in female_names2:
    for j in str.split(str(i)," "):
        if(j not in stopw):
          
              
            temp.append(j)
                

for z in temp:
    female_names2.add(z)
#print(female_names2)

female_names2=list(female_names2)

dat=pd.DataFrame({'name':female_names2})
#print((dat))
#
dat.to_csv("new_female_names.csv")

q=pd.read_csv(path)
male_names=set(q['name'])

male_names=list(male_names)



for i in male_names:
    for j in str.split(str(i)," "):
        if(j not in stopw):
          
              
            temp.append(j)
                

for z in temp:
    male_names.append(z)

male_names=set(male_names)
male_names=list(male_names)
dat=pd.DataFrame({'name':male_names})
dat.to_csv("new_male_names.csv")
