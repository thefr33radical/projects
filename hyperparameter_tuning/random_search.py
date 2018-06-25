from sklearn import linear_model
from sklearn import svm
from sklearn.model_selection import RandomizedSearchCV


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

            pass
        def lasso(self,train_input,train_output,test_input,test_output):
            pass

        def ridge(self, train_input, train_output, test_input, test_output):
            """
            :param train_input:
            :param train_output:
            :param test_input:
            :param test_output:
            :return:
            """
            ridge_random_param = {"alpha" : []}
            model = linear_model.Ridge()
            random_search =  RandomizedSearchCV(model, param_distributions = ridge_random_param)


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

