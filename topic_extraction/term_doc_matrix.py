
from sklearn.feature_extraction.text import CountVectorizer as CV
from sklearn.feature_extraction.text import TfidfVectorizer as TF
import pandas as pd
import glob
import os

"""

Module to transform plain text to Term Document Matrix/ TF-IDF Matrix. 

"""


class TextTransform(object):

    def __init__(self):
        self.maximum_features = 10000

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

    def transform_td_matrix(self,id, data):
        """

        :param data: list of strings
        :return: dataframe
        """
        cv = CV(analyzer = 'word', ngram_range=(1,2),max_features=self.maximum_features, stop_words='english')
        cv_sparse_matrix = cv.fit_transform(data)
        cv_dense_matrix = cv_sparse_matrix.todense()
        data_frame=pd.DataFrame(cv_dense_matrix, columns=cv.get_feature_names())
        #data_frame.to_csv("result_td.csv")
        #print(data_frame)
        return data_frame

    def transform_tfidf_matrix(self,id, data):
        """

        :param data: list of strings
        :return: dataframe
        """
        tf = TF(ngram_range=(1, 2), max_features=self.maximum_features, stop_words='english')
        tf_sparse_matrix = tf.fit_transform(data)
        tf_dense_matrix = tf_sparse_matrix.todense()
        data_frame = pd.DataFrame(tf_dense_matrix, columns=tf.get_feature_names(),index=id)
        #data_frame.to_csv("result_td.csv")
        #print(data_frame)
        return data_frame


if __name__ == "__main__":
    obj = TextTransform()
    id, data = obj.read_txt_file("path")
    obj.transform_tfidf_matrix(id,data)


