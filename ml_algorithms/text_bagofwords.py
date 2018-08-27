
from sklearn.feature_extraction.text import CountVectorizer as CV
from sklearn.feature_extraction.text import TfidfVectorizer as TF
from sklearn.feature_extraction.text import TfidfTransformer as TFF
from nltk.corpus import stopwords

import pandas as pd
import glob
import os
import gensim
import nltk
#nltk.download('stopwords')
#nltk.download('wordnet')
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk.tokenize import wordpunct_tokenize
"""

Module to transform plain text to Term Document Matrix/ TF-IDF Matrix. 

Algorithm to  convert text of words into BagofWords words model.

1. Remove stopwords
2. POS tag
3. lemmatize
   Stem (After stemming POS wont work)
3. ngrams
4. generate Countvector/Tfidf vector

"""


class TextTransform(object):

    def __init__(self):
        self.maximum_features = 10000
        self.ngram=2


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

        :param data: list of strings
        :return: dataframe
        """
        stop_words=set(stopwords.words('english'))
        stop_words.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{','@,'
                           '}'])  # remove it if you need punctuation

        new_data=[]
        for doc in data:
            words = doc.split()
            new_word=""
            for word in words:
                if word.lower() not in stop_words:
                    new_word+=" "+word.lower()

            new_data.append(new_word)
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
     print(gensim.parsing.stem_text("trying writing nonsense"))

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

