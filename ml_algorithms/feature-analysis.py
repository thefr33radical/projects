import pandas as pd
import math


class FeatureAnalysis(object):
    def __init(self):
        pass


    def compute_SD(self,data):
        """
        1. compute mean M
        2. Z= ((X-M)^2) for each X
        3. Var = Mean(Z)
        4. SD= sqrt(Var)

        :param data: list of numbers
        :return: float
        """
        total=0
        for i in data:
            total+=i
        mean_val = total/len(data)

        variance= 0
        for i in data:
            variance+=(i - mean_val) * ( i - mean_val)

        variance = variance/len(data)
        std_dev = math.sqrt(variance)
        print(std_dev)
        return std_dev

    def generate_plots(self,dataset):

        pass


if __name__=="__main__":
    obj =FeatureAnalysis()
    obj.compute_SD([9, 2, 5, 4, 12, 7, 8, 11, 9, 3, 7, 4, 12, 5, 4, 10, 9, 6, 9, 4])