
import numpy as np


class Knn(object):
    """
    Implementation of Kmeans algorithm

    """
    def __init__(self,train_input,train_output,test_input,test_output):
        self.train_input=train_input
        self.train_output=train_output
        self.test_input=test_input
        self.train_output=test_output

    def compute_eucledian(self,row1,row2,length):
        """
        Function to compute eucledian distance
        :param row1: list
        :param row2: list
        :param length: length
        :return: eucledian distance
        """

        dist=0
        for i in range(0,length):
            dist+= np.square(row1[i]-row2[i])

        dist= np.sqrt(dist)
        return dist

    def fit(self,traiin_input,train_output):
        pass

    def predict(self,test_input):
        pass

    def predict_prob(self,test_input):
        pass

    def comparison(self):
        pass





