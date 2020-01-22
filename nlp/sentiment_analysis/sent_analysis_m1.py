from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *
n_instances = 100

subj_docs = [(sent, 'subj') for sent in subjectivity.sents(categories='subj')[:n_instances]]
obj_docs = [(sent, 'obj') for sent in subjectivity.sents(categories='obj')[:n_instances]]
#len(subj_docs), len(obj_docs)
#(100, 100)

#print(subj_docs[1])
train_subj_docs = subj_docs[:80]
test_subj_docs = subj_docs[80:100]
train_obj_docs = obj_docs[:80]
test_obj_docs = obj_docs[80:100]
training_docs = train_subj_docs+train_obj_docs
testing_docs = test_subj_docs+test_obj_docs
sentim_analyzer = SentimentAnalyzer()

all_words_neg = sentim_analyzer.all_words([mark_negation(doc) for doc in training_docs])
unigram_feats = sentim_analyzer.unigram_word_feats(all_words_neg, min_freq=4)
print ((unigram_feats))

#mark_negation() function assigns - (_NEG) to all words till it encounters full stop.
# if double negation is present then words after the 2nd neg are not marked with (_NEG).
'''
example 1:
(['that', "'alabama'", 'manages', 'to', 'be', 'pleasant', 'in', 'spite', 'of', 'its',
 'predictability', 'and', 'occasional', 'slowness', 'is', 'due', 'primarily', 'to', 'the', 
 'perkiness', 'of', 'witherspoon', '(', 'who', 'is', 'always', 'a', 'joy', 'to', 'watch', 
 ',', 'even', 'when', 'her', 'material', 'is', 'not', 'first-rate_NEG', ')_NEG', '.', '.',
 '.'], 'subj') 
 
original text: 
 (['that', "'alabama'", 'manages', 'to', 'be', 'pleasant', 'in', 'spite', 'of',
 'its', 'predictability', 'and', 'occasional', 'slowfor key,value in sorted(sentim_analyzer.evaluate(test_set).items()):
...     print('{0}: {1}'.format(key, value))ness', 'is', 'due', 'primarily', 'to',
 'the', 'perkiness', 'of', 'witherspoon', '(', 'who', 'is', 'always', 'a', 'joy', 'to', 
 'watch', ',', 'even', 'when', 'her', 'material', 'is', 'not', 'first-rate', ')', '.', 
 '.', '.'], 'subj'
 
 example 2:
 (['if', 'the', 'story', 'lacks', 'bite', ',', 'the', 'performances', 'are', 'never', 
 'less_NEG', 'than_NEG', 'affectionate_NEG', '.'], 'subj')
 
original text: 
 (['if', 'the', 'story',  'lacks', 'bite', ',', 'the', 'performances', 'are', 'never', 'less', 'than', 
 'affectionate', '.'], 'subj')

'''
sentim_analyzer.add_feat_extractor(extract_unigram_feats, unigrams=unigram_feats)
training_set = sentim_analyzer.apply_features(training_docs)
test_set = sentim_analyzer.apply_features(testing_docs)

trainer = NaiveBayesClassifier.train
classifier = sentim_analyzer.train(trainer, training_set)


for key,value in sorted(sentim_analyzer.evaluate(test_set).items()):
    print('{0}: {1}'.format(key, value))