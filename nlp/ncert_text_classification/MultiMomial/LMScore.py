# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 10:04:47 2016

@author: Kalyani
"""

mypath ="D:\\NLP_SP\\myPythonCode\\enlp"
import os
import nltk
#nltk.download('wordnet')
import codecs
import nltk.data
from nltk.tokenize import RegexpTokenizer
from nltk.stem.wordnet import WordNetLemmatizer
from collections import Counter
from nltk.corpus import stopwords
from PyPDF2 import PdfFileReader
import csv
import math
#writeSenLength = open('sen.csv', 'a')
#writeWordLength = open('word.csv', 'a')

pdfFileObj = PdfFileReader(open("gess301.pdf", "rb"))
f = open('input.txt','w')
try :
    j = 0
    while j < pdfFileObj.numPages:
        pageObj = pdfFileObj.getPage(j)
        f.write((pageObj.extractText()).encode('utf-8')+'\n')
        print pageObj.extractText()
        j+=1
except:
    print ""
f.close()

file = "input.txt"
fp = codecs.open(file, "r", "utf-8")
data = fp.read()
        
        #word_tokenizer = RegexpTokenizer(r'\w+')
word_tokenizer = RegexpTokenizer(r'[A-Z]\w+|[a-z]\w+')
temp_words = word_tokenizer.tokenize(data)
stop = stopwords.words('english') 
words = [w.lower() for w in temp_words]
        #print words
        
word_lemmatizer = WordNetLemmatizer()
words_lemma = []
for word in words:
    temp=word_lemmatizer.lemmatize(word) 
    if  temp not in stop and len(temp) >1:
     #print temp
        words_lemma.append(temp)
        
myset = set(words_lemma)
lemmas = list( myset)
        
counts = Counter(words_lemma)

countList = list()
        
for lemma in lemmas:
    countList.append(counts[lemma])
print "\nLemma length is %d\n" %len(lemmas)
print "\nList length is %d\n" %len(countList)

############################ Find average sentence length ############################
        
        
from nltk.tokenize import RegexpTokenizer
        
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
fp = open(file)
data = fp.read()
        
sentences = '\n-----\n'.join(tokenizer.tokenize(data.decode('utf-8')))
tot_sentences = sentences.count("-----")
        
word_tokenizer = RegexpTokenizer(r'\w+')
words = word_tokenizer.tokenize(data)
tot_words = len(words)
        
avg_sent_length = tot_words/tot_sentences
        
print "\nThe avg sentence length is %d\n" % avg_sent_length
#writeSenLength.write ("%s\n" %(avg_sent_length))
 
        ############################# Find average word length ################################
        
##Average Sentence Length Calculation Module
#Open a File, for multiple files put this in a loop
sentence = open(file,'r')
x=sentence.read()
#Split into individual terms, including charecters which might not be a meaningful word
terms = x.split()
#Calculate the length of all the charecters in the file
s=0
for i in terms:
    s=s+len(i)
total_length=s
no_of_terms=len(terms)
        
#Find average by dividing total length of charecters by number of terms presesnt
averageWL = total_length/no_of_terms
print "\nThe avg word length is %d\n" % averageWL
#writeWordLength.write ("%s\n" %(averageWL))
        ##########################################################################################
fp.close()
   
       
print "\nLemma length is %d\n" %len(lemmas)
print "\nList length is %d\n" %len(countList)

mypath ="D:\NLP_SP\\myPythonCode\\enlp\\FinalENLP"
import os

filelist=[]
for file in os.listdir(mypath):
    if file.endswith(".csv"):
        filelist.append(file)
        #header.append(file.replace(".csv",""))

writeFile = open('LMScore.csv', 'a+')
writeFile.write ('Grade01,Grade02,Grade03,Grade04,Grade05,Grade06,Grade07,Grade08,Grade09,Grade10,Grade11,Grade12\n')
score = [0] * 12
grd= 0
print score

for file in filelist :
    readFile = open(file, 'r')
    print file
    myreader = csv.reader(readFile)
    sum=0
    for row in myreader:
        getword = row[0]
        getprob = float(row[1])
            #totcount=totcount+ int(row[1])
        if getword in lemmas : 
            ind = lemmas.index(getword)
            getcount=countList[ind]
            mult = getcount*(math.log(getprob))
            sum = sum + math.log(-mult)
    score[grd]=float(sum)
    grd = grd+1
    readFile.close()
writeFile.write("%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f\n" %(score[0],score[1],score[2],score[3],score[4],score[5],score[6],score[7],score[8],score[9],score[10],score[11]))
writeFile.close()
