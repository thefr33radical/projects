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
        print(x)
        dist=[]

        z = Counter(dataset)
        print(z)
        return z

    def regression_plots(self,dataset,count_features,feature_name):
        """
        Function to plot continious values
        :param dataset: dataframe
        :return: None
        """

        names = list(count_features.keys())
        values = list(count_features.values())

        fig, ax = plt.subplots()
        ax.scatter(names, values,color="black")
        ax.plot(names, values,color="red")

        ax.set(xlabel="NA", ylabel='NA',
               title=feature_name)
        ax.grid()

        fig.savefig(feature_name+".png")
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
        plt.savefig(dataset.columns.values[0] + ".png")
        plt.show()

    def categorical_bar(self,dataset,count_features,feature_name):
        """
        Function to plot categorical features
        :param dataset:
        :return: None
        """

        names = list(count_features.keys())
        values = list(count_features.values())
        y_pos = np.arange(min(names), max(names) + 1)

        plt.rcdefaults()
        fig, ax = plt.subplots()
        ax.barh(names, values, color='blue', align='center')
        ax.set_yticks(y_pos)
        ax.set_yticklabels(names)
        ax.invert_yaxis()  # labels read top-to-bottom
        ax.set_xlabel("COUNTS")
        ax.set_title(feature_name)

        plt.savefig(feature_name+".png")
        plt.show()


    def choose_plot(self,dataset):
        """

        :param dataset:
        :return:
        """

        for i in dataset:
            count_features = self.class_distribution(dataset[i])
            if len(count_features.keys()) > 10:
                self.regression_plots(dataset[i],count_features,i)
            else:
                self.categorical_bar(dataset[i],count_features,i)
                self.categorical_pie(dataset[i],count_features,i)


if __name__=="__main__":
    obj =FeatureAnalysis()
    dataset = pd.DataFrame([9, 2, 5, 4, 12, 7, 8, 11, 9, 3, 7, 4, 12, 5, 4, 10, 9, 6, 9, 4],columns=["feature"])

    obj.choose_plot(dataset)
    #obj.class_distribution([9, 2, 5, 4, 12, 7, 8, 11, 9, 3, 7, 4, 12, 5, 4, 10, 9, 6, 9, 4])
