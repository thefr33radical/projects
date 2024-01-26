####################### Read from PDF ####################################

#from PyPDF2 import PdfFileWriter, PdfFileReader
#
#pdfFileObj = PdfFileReader(open("gess310.pdf", "rb"))
#
#f = open('gess310.txt','w')
#
#j = 0
#while j < pdfFileObj.numPages:gess310.txt
#	pageObj = pdfFileObj.getPage(j)
#	f.write((pageObj.extractText()).encode('utf-8'))
#	j+=1
#
#f.close()

############################################################################

######################## Unigram Probability ##############################

import nltk
#nltk.download('wordnet')
import codecs
import nltk.data
from nltk.tokenize import RegexpTokenizer
from nltk.stem.wordnet import WordNetLemmatizer
from collections import Counter
import numpy as np

fp = codecs.open("gess310.txt", "r", "utf-8")
data = fp.read()

#word_tokenizer = RegexpTokenizer(r'\w+')
word_tokenizer = RegexpTokenizer(r'[A-Z]\w+|[a-z]\w+')
temp_words = word_tokenizer.tokenize(data)
words = [w.lower() for w in temp_words]
#print words

word_lemmatizer = WordNetLemmatizer()
words_lemma = []
for word in words:
	words_lemma.append(word_lemmatizer.lemmatize(word) )

myset = set(words_lemma)
lemmas = list(myset)

counts = Counter(words_lemma)

countList = list()

for lemma in lemmas:
	countList.append(counts[lemma])

total = len(words_lemma)
uniProb = list()

for i in xrange(0, len(countList)) :
    uniProb.append (float(countList[i])/float(total))

prob_matrix = np.column_stack((lemmas,uniProb))

final_prob = prob_matrix[prob_matrix[:, 1].argsort()]
final_prob = final_prob[::-1]

######################################################################################

############################ Find average sentence length ############################

import nltk.data
from nltk.tokenize import RegexpTokenizer

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
fp = open("gess310.txt")
data = fp.read()

sentences = '\n-----\n'.join(tokenizer.tokenize(data.decode('utf-8')))

tot_sentences = sentences.count("-----")

word_tokenizer = RegexpTokenizer(r'\w+')
words = word_tokenizer.tokenize(data)
tot_words = len(words)

avg_sent_length = tot_words/tot_sentences

#######################################################################################

############################# Find average word length ################################

##Average Sentence Length Calculation Module
    #BEGIN

#Open a File, for multiple files put this in a loop
sentence = open("gess310.txt",'r')
x=sentence.read()
#print(x)

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


##########################################################################################

################################ Build feature vector ####################################

top_10_uni = final_prob[:, 1][:10]
feature_vec = []
for every_uni in top_10_uni:
	feature_vec.append(float(str(every_uni)))
feature_vec.append(float(averageWL))
feature_vec.append(float(avg_sent_length))

#print feature_vec

f = open('feature.csv','a+')

f.write ("%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f\n" %(feature_vec[0], feature_vec[1], feature_vec[2], feature_vec[3], feature_vec[4], feature_vec[5], feature_vec[6], feature_vec[7], feature_vec[8], feature_vec[9], feature_vec[10], feature_vec[11]))

f.close()



