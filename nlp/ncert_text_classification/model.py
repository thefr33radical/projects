import csv
from sklearn.linear_model import LogisticRegression, LinearRegression
import numpy as np

with open('feature.csv', 'rb') as f:
    reader = csv.reader(f)
    your_list = list(reader)

feature = []
label = []
for data in your_list:
	feature.append(data[0:12])
	label.append(int(data[12]))

feature_f = []
for row in feature:
	feature_f.append(map(float, row))

#Numbers are class of tag
resultsNER = label

#Acording to resultNER every row is another class so is another features
#but in this way every row have the same features
xNER = feature_f[0:15]

#Assing resultsNER to y
y = resultsNER[0:15]
#Create LogReg
logit = LogisticRegression(C=1.0)
#Learn LogReg
logit.fit(xNER,y)

#Some test vector to check wich class will be predict
xPP = feature_f[15:17]

#print "expected: ", y
print "predicted:", logit.predict_proba(xPP)

	
