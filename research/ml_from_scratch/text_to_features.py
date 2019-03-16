
from sklearn.feature_extraction.text import CountVectorizer as CV
from sklearn.feature_extraction.text import TfidfVectorizer as TF
from sklearn.feature_extraction.text import TfidfTransformer as TFF
from nltk.corpus import stopwords
import pandas as pd
import glob
import os
import nltk
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem import PorterStemmer

"""

Module to transform plain text to Term Document Matrix/ TF-IDF Matrix. 

Algorithm to  convert text of words into BagofWords words model.

1. Remove stopwords
2. POS tag
3. lemmatize
   Stem (After stemming POS wont work)
3. ngrams 
4. generate Countvector/Tfidf vector
5. average sentence length
6. average word length
7. average character length/word
8. average character length/sentence

"""


class TextTransform(object):

    def __init__(self):
        self.maximum_features = 10000
        self.ngram=2

    def tag_noun_pronoun(self, data):
        """

           :param data: LIST - text documents
           :return: String- Text comprising of only, nouns,verbs. Int - Count of nouns/verbs
        """

        data = [ i for i in data]
        candidate_word_list = []
        count = 0
        tagged_words = nltk.pos_tag(nltk.word_tokenize(data))
        try:
            for word, tag in tagged_words:
                try:
                    if str(tag[0]).lower() in ['n', 'v']:
                        if len(word) > 2:
                            candidate_word_list.append(word)
                        count += 1
                except:
                    print(word, tag)
                    continue
            data = ' '.join(candidate_word_list)
            return data, count
        except Exception as e:
            print(e)
            print("error in tagging words")

    def avg_character_count_per_word(self, data):
        """
               :param data: List-strings
               :return:  List-avg count of character, [1.0] on error        """

        avg_char_count=[]
        for  doc in data:
            word_list = doc.split()
            char_count=0
            for word in word_list:
                try:
                    char_count+=len(word)
                except:
                    continue
            avg_char_count.append(char_count/len(word_list))
        return  avg_char_count

    def avg_sentence_length(self, data):
        """
        :param data: List-strings
        :return:  List-avg length of sentences, [1.0] on error        """
        avg_sentence_list = []
        try:
            for doc in data:
                try:
                    sentence_list = doc.split(".")
                    word_list = doc.split()
                    avg_sentence_list.append(float(len(word_list)) / float(len(sentence_list)))
                except:
                    avg_sentence_list.append(1.0)

            return avg_sentence_list
        except Exception as e:
            print(e)
            return [1.0] * len(data)

    def avg_word_length(self, data):
        """
        :param data: List -strings
        :return: List of avg length of words for each doc in list, None
        """
        avg_word_len = []
        try:
            for text in data:
                words = text.split()
                words_len = float(len(words))
                count = 0.0
                for word in words:
                    for letter in word:
                        count += 1.0
                avg_word_len.append(count / words_len)
            return avg_word_len
        except Exception as e:
            print(e)
            return [1.0]*len(data)


    def lemmatize(self,data):
        """
        :param data: list of strings
        :return: list of lemmatized strings, None
        """
        try:
            new_data=[]
            lemmatizer =WordNetLemmatizer()
            for file in data:
                new_file = ""
                for word in file.split():
                    try:
                        new_file+=lemmatizer.lemmatize(word)+" "
                    except:
                        continue
            return new_data
            new_data.append(new_file)
        except Exception as e:
            print(e)

    def stem(self,data):
        """
        :param data: list of strings
        :return: list of lemmatized strings,None
        """
        try:
            new_data=[]
            stemmer=PorterStemmer()
            for file in data:
                new_file = ""
                for word in file.split():
                    try:
                        new_file+=stemmer.stem(word)+" "
                    except:
                        continue
                new_data.append(new_file)
            return new_data

        except Exception as e:
            print(e)

    def remove_stopwords(self,data):
        """
        :param data: string
        :return: string
        """
        stop_words=set(stopwords.words('english'))
        stop_words.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{','@,'
                           '}'])  # remove it if you need punctuation
        sentence=data.split()
        for word in sentence:
            if word.lower() in stop_words:
                sentence.remove(word)

        new_data = " ".join(sentence)

        return new_data

    def read_txt_file(self,path):
        """
        :param : path to text files
        :return: list of string
        """
        id=[]
        data=[]

        for i in glob.glob(os.path.join(path,"*.txt")):
            pathname, filename = os.path.split(i)
            fp = open(i,"r")
            temp_data = fp.read().encode("utf-8")
            fp.close()
            temp_data = str(temp_data)
            data.append(temp_data)
            id.append(filename)
        return id,data

    def transform_td_matrix(self, data):
        """
        :param data: list of strings
        :return: dataframe
        """
        cv = CV(analyzer = 'word', ngram_range=(1,self.ngram),max_features=self.maximum_features,lowercase=True,decode_error='ignore')
        cv_sparse_matrix = cv.fit_transform(data)
        cv_dense_matrix = cv_sparse_matrix.todense()
        data_frame=pd.DataFrame(cv_dense_matrix, columns=cv.get_feature_names())
        #data_frame.to_csv("result_td.csv")
        #print(data_frame)
        return cv, data_frame

    def transform_tfidf_matrix(self,data):
        """
        :param data: list of strings
        :return: dataframe
        """
        tf = TF(ngram_range=(1, self.ngram), max_features=self.maximum_features, stop_words='english',lowercase=True,decode_error='ignore')
        tf_sparse_matrix = tf.fit_transform(data)
        tf_dense_matrix = tf_sparse_matrix.todense()
        data_frame = pd.DataFrame(tf_dense_matrix, columns=tf.get_feature_names(),index=id)
        #data_frame.to_csv("result_td.csv")
        #print(data_frame)
        return tf,data_frame

    def td_to_tfidf(self,data,column_names):
        """
        :param data: dataframe
        :return: dataframe
        """
        temp_data = data
        tfidf = TFF(norm='l2',smooth_idf=True,sublinear_tf=True)
        t_data = tfidf.fit_transform(temp_data)
        tf_dense_matrix = t_data.todense()
        data = pd.DataFrame(tf_dense_matrix,columns=column_names)
        return data


if __name__ == "__main__":

     '''data=["i am here","you are there","lets go to ooty"]
     test=["breaking bad is awesome"]
     obj=TextTransform()
     model,resp=obj.transform_td_matrix(data)
     cv_sparse_matrix = model.fit_transform(test)

     cv_dense_matrix = cv_sparse_matrix.todense()
     data_frame = pd.DataFrame(cv_dense_matrix, columns=model.get_feature_names())
     print(pd.concat([data_frame,resp],axis=0))
     obj = TextTransform()
     obj.td_to_tfidf(None,None)
     '''
     data = ["i am here", "you are there", "lets go to ooty"]
     obj = TextTransform()
     for i in data:
         print(obj.remove_stopwords(i))
     #x=obj.avg_character_count_per_word(data)
     #print(x)
