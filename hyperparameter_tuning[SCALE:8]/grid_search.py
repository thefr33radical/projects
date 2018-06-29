"""
GridSearch class implements brute force selection of hyperparameters for Classification model and Regression models.

"""

from sklearn import linear_model
from sklearn import svm
from sklearn import datasets
import numpy as np

class GridSearch(object):

    class Regression(object):
        """

        """

        def __init__(self,cross_val_num):
            self.cross_val=cross_val_num

        def linear_regression(self,train_input,train_output,test_input,test_output):
            """
            :param train_input:
            :param train_output:
            :param test_input:
            :param test_output:
            :return:
            """
            pass

        def svr(self, train_input, train_output, test_input, test_output):
            """

            :param train_input:
            :param train_output:
            :param test_input:
            :param test_output:
            :return:
            """
            svr_grid_param= {{'C': [1, 10, 100, 1000], 'gamma': [0.001, 0.0001], 'kernel': ['rbf']}, {'c': [1, 10, 100, 1000], 'kernel': ['linear']} }
            model=svm.SVR()

            # Grid Search of SVR model with kernels in svr_grid_params and cross validation of 3
            grid_search = GridSearch(model, svr_grid_param, cv = 3)

            grid_search.fit(train_input, train_output)

            best_alpha = grid_search.best_estimator_.alpha
            best_score = grid_search.best_score_


            pass
        def lasso(self,train_input,train_output,test_input,test_output):
            pass

        def ridge(self, train_input, train_output, test_input, test_output):
            """
            :param train_input: training features
            :param train_output: training target
            :param test_input: test features
            :param test_output: test target
            :return:
            """

            dataset = datasets.load_diabetes()
            model = linear_model.Ridge()
            ridge_grid_param = {"alpha":[ 0, 0.1,0.001,0.0001,1]}
            grid_search = GridSearch(model, ridge_grid_param ,cv = 3)
            grid_search.fit(dataset.data , dataset.target)

            best_alpha = grid_search.best_estimator_.alpha
            best_score = grid_search.best_score_
            pass


    class Classification(object):
        def svm(self,train_input,train_output,test_input,test_output):
            pass
        def logistic_regression(self,train_input,train_output,test_input,test_output):
            pass
        def naive_bayes(self,train_input,train_output,test_input,test_output):
            pass
        def random_forest(self,train_input,train_output,test_input,test_output):
            pass
        def decesion_tree(self,train_input,train_output,test_input,test_output):
            pass

