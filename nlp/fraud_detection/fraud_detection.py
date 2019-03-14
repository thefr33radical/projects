from flask import Flask, jsonify,request
import flasgger
from helpers import preprocess
from models import classifiers
import time
import pandas as pd


class FraudDetection(object):
    """
        Module to find Fraudulent Transaction
    """

    def __init__(self):
        self.obj1 = preprocess.ReadSplit()
        self.obj2 = classifiers.Models()

    def read_data(self,path):
        """
        Function to read dataset
        :param path:
        :return:
        """
        obj1 = preprocess.ReadSplit()
        dataset = obj1.read_data(path)
        return dataset

    def compute(self,path):
        """
        Function to perform the all computations
        :param path: string
        :return:None
        """

        dataset = self.read_data(path)
        #print(len(dataset))

        dataset = dataset.iloc[:5000,:]

        start = time.time()
        train_input, test_input, train_output, test_output = self.obj1.split_dataset(dataset,1)
        #obj2.pca_model_classification(train_input, test_input, train_output, test_output,200)

        output = pd.DataFrame.from_dict(self.obj2.train_classifiers(train_input, test_input, train_output, test_output,len(dataset.columns.values)-1))
        print(output.head())
        # All the models score with model name is stored in a csv file
        output.to_csv("output_score.csv", sep=",")
        end=time.time()

        print("Total time taken for training Oversampling", end - start)

        """start = time.time()
        train_input, test_input, train_output, test_output = obj1.split_dataset(dataset, 2)
        #obj2.pca_model_classification(train_input, test_input, train_output, test_output, 200)
        l = []
        l.append(
        obj2.train_classifiers(train_input, test_input, train_output, test_output, len(dataset.columns.values) - 1))
        output = pd.DataFrame(l)
        print(output.head())
        # All the models score with model name is stored in a csv file
        output.to_csv("output_score.csv", sep=",")
        end = time.time()

        print("Total time taken for training ADASYN", end - start)
        
        start = time.time()
        train_input, test_input, train_output, test_output = obj1.split_dataset(dataset, 3)
        #obj2.pca_model_classification(train_input, test_input, train_output, test_output, 200)
        obj2.train_classifiers(train_input, test_input, train_output, test_output, 200)
        end = time.time()

        print("Total time taken for training SMOTE", end-start)
        """
    def predict(self,test_case):
        """
        Function to predict test case
        :param test_case: Feature array
        :return: None
        """
        print(self.obj2.ensemble_predict(test_case))


if __name__=="__main__":
    fraud = FraudDetection()
    path =input()
    fraud.compute(path)
