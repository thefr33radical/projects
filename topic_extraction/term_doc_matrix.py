
from sklearn.feature_extraction.text import CountVectorizer as CV
from sklearn.feature_extraction.text import TfidfVectorizer as TF
import pandas as pd


class TermDocMatrix(object):

    def __init__(self):
        self.maximum_features = 10000

    def read_txt_file(self,path):


        fp = open(path,"r")
        data = fp.read().encode("utf-8")
        fp.close()
        data = str(data)
        data = data.split("::")
        #data= [data]
        print(data)
        return data

    def transform_td_matrix(self,data):
        matrix = CV(ngram_range=(1,2),
                                max_features=self.maximum_features,
                                stop_words='english')
        t= matrix.fit_transform(data)
        f = t.todense()
        data_frame=pd.DataFrame(f,columns=matrix.get_feature_names())
        data_frame.to_csv("result_td.csv")
        print(data_frame)

    def transform_tfidf_matrix(self,data):
        matrix = TF(ngram_range=(1,2),
                                max_features=self.maximum_features,
                                stop_words='english')
        t= matrix.fit_transform(data)
        f = t.todense()
        data_frame=pd.DataFrame(f,columns=matrix.get_feature_names())
        data_frame.to_csv("result_tfidf.csv")
        print(data_frame)


if __name__=="__main__":
    obj = TermDocMatrix()
    data = obj.read_txt_file()
    obj.transform_tfidf_matrix(data)


