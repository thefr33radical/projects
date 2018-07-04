"""
GridSearch class implements brute force selection of hyperparameters for Classification model and Regression models.

"""

from sklearn import linear_model
from sklearn import svm
from sklearn import datasets
from sklearn.model_selection import  GridSearchCV
import numpy as np


class GridSearch(object):

    class Regression(object):
        def __init__(self,cross_val_num=3):
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

        def svr(self,train_input,train_output,test_input,test_output):
            """
            FUNCTION RETURNS BEST HYPERPARAMETERS
            :param train_input: training features
            :param train_output: training target
            :param test_input: test features
            :param test_output: test target
            :return: hyperparameters
            """
            svr_grid_param= {'kernel': ('rbf','poly','linear'), 'C':[0.1,1,1.5, 10,100],'gamma': [1e-7, 1e-4],'epsilon':[0.1,0.2,0.5,0.3],'degree':[2,3,4]}
            model=svm.SVR()
            data = datasets.load_diabetes()
            x = data["data"]
            y = data["target"]
            # Grid Search of SVR model with kernels in svr_grid_params and cross validation of 3
            grid_search = GridSearchCV(model, svr_grid_param, cv = 3)

            grid_search.fit(train_input + test_input, train_output + test_output)
            best_params=grid_search.best_params_
            best_score = grid_search.best_score_

            return best_params, best_score

        def ridge(self,train_input,train_output,test_input,test_output):
            """
            FUNCTION RETURNS BEST HYPERPARAMETERS
            :param train_input: training features
            :param train_output: training target
            :param test_input: test features
            :param test_output: test target
            :return: hyperparameters
            """

            model = linear_model.Ridge()
            ridge_grid_param = {"alpha": [0, 0.1, 0.001, 0.0001, 1]}
            grid_search = GridSearchCV(model, ridge_grid_param)
            grid_search.fit(train_input + test_input, train_output + test_output)

            grid_search.fit(train_input + test_input, train_output + test_output)
            best_params = grid_search.best_params_
            best_score = grid_search.best_score_

            return best_params, best_score

        def lasso(self,train_input,train_output,test_input,test_output):
            """
            FUNCTION RETURNS BEST HYPERPARAMETERS
            :param train_input: training features
            :param train_output: training target
            :param test_input: test features
            :param test_output: test target
            :return: hyperparameters
            """

            model = linear_model.Ridge()
            lasso_grid_param = {"alpha":[ 0, 0.1,0.001,0.0001,1]}
            grid_search = GridSearchCV(model, lasso_grid_param,cv=self.cross_val)
            grid_search.fit(train_input + test_input, train_output + test_output)

            grid_search.fit(train_input + test_input, train_output + test_output)
            best_params = grid_search.best_params_
            best_score = grid_search.best_score_

            return best_params, best_score

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

if __name__=="__main__":
    obj1= GridSearch.Regression(3)
    obj1.svr()
    