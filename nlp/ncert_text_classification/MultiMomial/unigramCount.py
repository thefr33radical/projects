# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 00:32:54 2016

@author: Kalyani
"""
###################################################################
# Do separately for each grade 
# Keep all the converted .txt files of a grade in mypath
# run this code
#   newgram.csv     will contain unigram with count
#   sen.csv         avg sentence length of each doc
#   word.csv        avg word length of each doc
#Now run uniqueUnio.py
#   unigram.csv     will have each unigram with its probability
####################################################################
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
import csv

writeFile = open('unigramCount.csv', 'a')
writeSenLength = open('avgSenLength.csv', 'a')
writeWordLength = open('avgWordLength.csv', 'a')
for file in os.listdir(mypath):
    if file.endswith(".txt"):
        print file
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
        
        #oldwords = zip(myreader)
        #oldwords = oldwords+  words_lemma
        #print "\nLemma length is %d\n" %len(oldwords)
        #myset = set(oldwords)
        myset = set(words_lemma)
        lemmas = list( myset)
        
        counts = Counter(words_lemma)

        countList = list()
        
        for lemma in lemmas:
        	countList.append(counts[lemma])
        print "\nLemma length is %d\n" %len(lemmas)
        print "\nList length is %d\n" %len(countList)
        #counts = Counter(words_lemma)
        #countList = list()
        
        
        
        #writer = csv.DictWriter(csvfile,"uni")
        #writer.writeheader()
        #print len(lemmas)
        for j in xrange(0, len(lemmas)) :
            #print lemmas[j]
            writeFile.write ("%s,%d\n" %(lemmas[j],countList[j]))         
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
        writeSenLength.write ("%s\n" %(avg_sent_length))
 
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
        writeWordLength.write ("%s\n" %(averageWL))
        ##########################################################################################
writeFile.close()
writeSenLength.close()
writeWordLength.close()

    