import nltk.data
from nltk.tokenize import RegexpTokenizer

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
fp = open("input.txt")
data = fp.read()

sentences = '\n-----\n'.join(tokenizer.tokenize(data.decode('utf-8')))

tot_sentences = sentences.count("-----")
#print tot_sentences

#corpusReader = nltk.corpus.PlaintextCorpusReader('.', 'input.txt')
#tot_words = len([word for sentence in corpusReader.sents() for word in sentence])


word_tokenizer = RegexpTokenizer(r'\w+')
words = word_tokenizer.tokenize(data)
tot_words = len(words)
#print tot_words
avg_sent_length = tot_words/tot_sentences

print "\nThe avg sentence length is %d\n" % avg_sent_length

