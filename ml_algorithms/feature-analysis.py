import pandas as pd
import math
from collections import Counter

class FeatureAnalysis(object):
    def __init(self):
        pass

    def compute_SD(self,data):
        """
        1. compute mean M
        2. Z= ((X-M)^2) for each X
        3. Var = Mean(Z)
        4. SD= sqrt(Var)

        Bessel's Correction needed if we are computing SD for a sample

        :param data: list of numbers
        :return: float
        """
        total=0
        for i in data:
            total+=i
        mean_val = total/len(data)
        Z= 0
        for i in data:
            Z+=(i - mean_val) * ( i - mean_val)

        variance = Z/len(data)
        std_dev = math.sqrt(variance)
        return std_dev

    def class_distribution(self,dataset):
        x = set(dataset)
        dist=[]
        for  i in x:
            dist.append({str(i):dataset.count(i)})

        z = Counter(dataset)
        return z

    def generate_plots(self,dataset):

        pass


if __name__=="__main__":
    obj =FeatureAnalysis()
    obj.class_distribution([9, 2, 5, 4, 12, 7, 8, 11, 9, 3, 7, 4, 12, 5, 4, 10, 9, 6, 9, 4])