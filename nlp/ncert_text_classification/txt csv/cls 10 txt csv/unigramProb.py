# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 08:29:34 2016

@author: Kalyani
"""
import csv
items=[]
readFile = open('unigramCount.csv', 'r')
      
myreader = csv.reader(readFile)
totcount=0
wordCount=[]
for row in myreader:
    #print row
    getword = row[0]
    getcount = int(row[1])
    totcount=totcount+ int(row[1])
    if getword not in items : 
        items.append(row[0])
        wordCount.append(getcount)
    else: #if getword in items :
       ind = items.index(getword)
       getcount=getcount+wordCount[ind]
       wordCount[ind]=getcount

tot= len(wordCount)
print len(items)
readFile.close()

writeFile = open('unigramProb.csv', 'a')

for j in range(0, tot) :
    #print lemmas[j]
    prob = float(wordCount[j])/float(totcount)
    print prob
    writeFile.write ("%s,%f\n" %(items[j],prob))   
#list(OrderedDict.fromkeys(items))
writeFile.close()