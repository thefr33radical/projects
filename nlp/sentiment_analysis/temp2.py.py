from sklearn.externals.joblib import Memory
from sklearn.datasets import load_svmlight_file
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import metrics
import numpy as np
from sklearn.naive_bayes import MultinomialNB
import pandas as pd
import os
from sklearn.datasets import load_files
import glob
import sys
import re
import pickle

mem = Memory("/home/gowtham/drive/codes/racetrack/sentiment_analysis/aclImdb/mycache")
subset = load_files('/home/gowtham/drive/codes/racetrack/sentiment_analysis/aclImdb/train',shuffle='False',encoding='utf-8')
subset2=load_files('/home/gowtham/drive/codes/racetrack/sentiment_analysis/aclImdb/test',shuffle='False',encoding='utf-8')


for i in range(0,len(subset.data)):
    f_name=subset.filenames[i]
    temp=f_name.split("_")
    temp2=temp[2].split(".")
    subset.target[i]=int(temp2[0])
  #  print((subset.data[i]), subset.filenames[i],subset.target[i])
v=CountVectorizer()
X=v.fit_transform(subset.data)
#print(v.get_feature_names())
model=MultinomialNB()
model.fit(X,subset.target)
#print(v.vocabulary_)
for i in range(0,len(subset2.data)):
    f_name=subset2.filenames[i]
    temp=f_name.split("_")
    temp2=temp[2].split(".")
    subset2.target[i]=int(temp2[0])
  #  print((subset.data[i]), subset.filenames[i],subset.target[i])
 

pickle.dump(model,open('mnb.sav',"w+"))



#--------------------------Testing-------------------------------------------------------





       
X2=v.transform(subset2.data)
expected=subset2.target
predicted=model.predict(X2)

c=pd.DataFrame({'test_data':subset2.data,'actual_value':subset2.target,'predicted':predicted})
c.to_csv("output.csv")

l=['this is very good.',
                'this is bad.',
                'this is very bad.',
                'this is not good.',    
                'this is not what i had expected.',
                'you are taking too much time.',
                'this is good',
                'this is awesome',
                'this is slighly good',
                'i expected better than this',
                'this is much more than my expectation',
                'this is something i love',
                'this is something i hate',
                 
                'you are taking a hell lot of time.']
                
X3=v.transform(l)
predicted2=model.predict(X3)

c2=pd.DataFrame({'test_data':l,'predicted':predicted2})
c2.to_csv("output2.csv")

report=(metrics.classification_report(expected, predicted))
con_matrix=(metrics.confusion_matrix(expected, predicted))

with open("report.txt","w+") as f:
    f.write(report)
    f.write(for i in con_matrix)
    
















