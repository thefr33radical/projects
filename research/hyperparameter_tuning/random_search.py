from sklearn import linear_model
from sklearn import svm
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import uniform


class RandomSearch(object):

    class Regression(object):
        def linear_regression(self,train_input,train_output,test_input,test_output):
            pass

        def svr(self,train_input,train_output,test_input,test_output):
            """
            :param train_input:
            :param train_output:
            :param test_input:
            :param test_output:
            :return:
            """
            model=svm.SVR()
            svr_random_param ={}

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

            ridge_random_param = {"alpha" : uniform()}
            model = linear_model.Ridge()
            random_search =  RandomizedSearchCV(model, param_distributions = ridge_random_param, n_iter=20)
            best_score = random_search.best_score_
            best_estimator = random_search.best_estimator_


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

