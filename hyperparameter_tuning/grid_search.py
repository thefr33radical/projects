from sklearn import linear_model
from sklearn import svm
from sklearn import li

class GridSearch(object):

    class Regression(object):
        def linear_regression(self,train_input,train_output,test_input,test_output):
            pass
        def svr(self,train_input,train_output,test_input,test_output):
            svm_paramters={{'kernel'="rbf",'c'=[]},{'kernel'="rbf",'c'=[]}}
            model=svm.SVR()
            pass
        def lasso(self,train_input,train_output,test_input,test_output):
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

