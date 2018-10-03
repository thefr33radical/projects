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
        """
        Function returns the Dictionary of count of classes
        :param dataset: pandas columns
        :return: Dict
        """
        x = set(dataset)
        dist=[]
        for  i in x:
            dist.append({str(i):dataset.count(i)})

        z = Counter(dataset)
        return z

    def regression_plots(self,dataset):
        """
        Function to plot continious values
        :param dataset: dataframe
        :return: None
        """
        variables = Counter(dataset.iloc[:, 0])
        names = list(variables.keys())
        values = list(variables.values())

        fig, ax = plt.subplots()
        ax.scatter(names, values,color="black")
        ax.plot(names, values,color="red")

        ax.set(xlabel="NA", ylabel='NA',
               title=dataset.columns.values[0])
        ax.grid()

        fig.savefig(dataset.columns.values[0]+".png")
        plt.show()


    def categorical_pie(self,dataset):
        """
        Function to plot categorical values
        :param dataset:
        :return: None
        """

        variables = Counter(dataset.iloc[:, 0])
        names = list(variables.keys())
        values = list(variables.values())

        fig, ax = plt.subplots()
        ax.pie(values, labels=names, autopct='%1.1f%%', startangle=0)
        ax.axis('equal')
        plt.show()

    def categorical_bar(self,dataset):
        """
        Function to plot categorical features
        :param dataset:
        :return: None
        """

        variables = Counter(dataset.iloc[:,0])

        names = list(variables.keys())
        values = list(variables.values())
        y_pos = np.arange(min(names), max(names) + 1)

        plt.rcdefaults()
        fig, ax = plt.subplots()
        ax.barh(names, values, color='blue', align='center')
        ax.set_yticks(y_pos)
        ax.set_yticklabels(names)
        ax.invert_yaxis()  # labels read top-to-bottom
        ax.set_xlabel("COUNTS")
        ax.set_title(dataset.columns.values[0])

        plt.savefig(dataset.columns.values[0]+".png")
        plt.show()


if __name__=="__main__":
    obj =FeatureAnalysis()
    dataset = pd.DataFrame([9, 2, 5, 4, 12, 7, 8, 11, 9, 3, 7, 4, 12, 5, 4, 10, 9, 6, 9, 4],columns=["feature"])

    obj.regression_plots(dataset)
    #obj.class_distribution([9, 2, 5, 4, 12, 7, 8, 11, 9, 3, 7, 4, 12, 5, 4, 10, 9, 6, 9, 4])