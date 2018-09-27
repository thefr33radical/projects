import pandas as pd
import math
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

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

    def regression_plots(self,dataset):
        """
        Function to plot continious plots
        :param dataset: dataframe
        :return:
        """
        pass

    def categorical_plots(self,dataset):
        """
        Function to plot categorical features
        :param dataset:
        :return: None
        """

        plt.rcdefaults()
        fig, ax = plt.subplots()
        variables = Counter(dataset["feature"])

        names = list(variables.keys())
        values = list(variables.values())
        y_pos = np.arange(min(names), max(names) + 1)
        print(names, values)

        ax.barh(names, values, color='blue', align='center')
        ax.set_yticks(y_pos)
        ax.set_yticklabels(names)
        ax.invert_yaxis()  # labels read top-to-bottom
        ax.set_xlabel("COUNTS")
        ax.set_title(dataset.columns.values[0])

        plt.show()

if __name__=="__main__":
    #obj =FeatureAnalys
    np.random.seed(19680801)

    dataset = pd.DataFrame([9, 2, 5, 4, 12, 7, 8, 11, 9, 3, 7, 4, 12, 5, 4, 10, 9, 6, 9, 4],columns=["feature"])


    #obj.class_distribution([9, 2, 5, 4, 12, 7, 8, 11, 9, 3, 7, 4, 12, 5, 4, 10, 9, 6, 9, 4])