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
import os
import sys


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


print(report,con_matrix)
#with open("report.txt","w+") as f:
   # f.write(report)
   # f.write(con_matrix)
    
















