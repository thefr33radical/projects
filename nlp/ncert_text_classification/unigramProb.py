# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 22:03:24 2016

@author: Kalyani
"""

from itertools import tee, izip
from pprint import pprint
import re

def bigrams(iterable):
    a, b = tee(iterable)
    next(b, None)
    return izip(a, b)

#with open("input.txt", 'r') as f:
#bi = bigrams(words)
#print list(bi)
def clean_str(string):
    """
    Tokenization/string cleaning
    """
    string = re.sub(r"[^A-Za-z0-9(),!?\'\`]", " ", string)     
    string = re.sub(r"\'s", " \'s", string) 
    string = re.sub(r"\'ve", " \'ve", string) 
    string = re.sub(r"n\'t", " n\'t", string) 
    string = re.sub(r"\'re", " \'re", string) 
    string = re.sub(r"\'d", " \'d", string) 
    string = re.sub(r"\'ll", " \'ll", string) 
    string = re.sub(r",", " , ", string) 
    string = re.sub(r"!", " ! ", string) 
    string = re.sub(r"\(", " \( ", string) 
    string = re.sub(r"\)", " \) ", string) 
    string = re.sub(r"\?", " \? ", string) 
    string = re.sub(r"\s{2,}", " ", string)
   # string = re.sub(r"[.]", " ", string)

    words=string.lower()
    return words;

wordList = list()
countList = list()
uniProb = list()
wordCount = 0
f = open("input.txt", 'r')

for line in f:
    newline=clean_str(line)   
    print newline
    for word in newline.split():
        wordCount = wordCount +1       
        ##uni = wordnet_lemmatizer.lemmatize(word) 
        uni = word;
        if uni in wordList :
            index = wordList.index(uni)
            countList[index] = countList[index]+1
        else :
            wordList.append(uni)
            countList.append(1)
f.close()

# NN NNS NNP NNPS

#pprint(wordList)
#pprint(countList)
total= len(wordList)
print total
#print wordCount
for i in xrange(0, total-1) :
    uniProb.append (float(countList[i])/float(total))

writeFile = open('unigram.txt', 'w')
for j in xrange(0, total-1) :
    #print "%20s \t%f" %(wordList[j], uniProb[j])
    writeFile.write ("%20s \t%f\n" %(wordList[j], uniProb[j]))
writeFile.close()
