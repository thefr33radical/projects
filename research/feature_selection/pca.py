from sklearn.decomposition import PCA
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
import pandas as pd
import numpy as np
import random


class FeatureSelection(object):

    def pca_model_regression(self, train_input, test_input, train_output, test_output):
        """
        PCA model to generate and select the best features

        :param train_input:
        :param test_input:
        :param train_output:
        :param test_output:
        :return:
        """
        output = pd.DataFrame()
        count_of_features = len(train_input.columns)

        global_r2_score = 0
        global_mean_score = 999999
        MODELS_GENERAL = [RandomForestRegressor(), linear_model.LinearRegression(), svm.SVR(kernel='rbf'),
                          linear_model.Ridge(alpha=3), linear_model.ElasticNet(alpha=1)]
        l = []
        # MODELS_GENERAL comprises of models that are used to train newly constructed features.
        for model in MODELS_GENERAL:
            for i in range(1, count_of_features):
                selector = PCA(n_components=i)
                selector = selector.fit(train_input, train_output)

                temp_test_input = selector.transform(test_input)
                temp_train_input = selector.transform(train_input)
                model_name = str(model)
                model.fit(temp_train_input, train_output)
                pred = model.predict(temp_test_input)
                temp = {"MODEL_NAME": model_name[:7], " DIMENSION": i,
                        "RMSE": np.sqrt(mean_squared_error(test_output, pred)),
                        " R2_SCORE ": r2_score(test_output, pred)}
                l.append(temp)

                if global_mean_score > np.sqrt(mean_squared_error(test_output, pred)) and global_r2_score < r2_score(
                        test_output, pred):
                    global_mean_score = np.sqrt(mean_squared_error(test_output, pred))
                    global_r2_score = r2_score(test_output, pred)

        output = pd.DataFrame(l)
        # All the models score with model name is stored in a csv file
        output.to_csv("output_score.csv", sep=",")

    def train_classifiers(self, train_input, test_input, train_output, test_output, step_size):
        """

        :param train_input:
        :param test_input:
        :param train_output:
        :param test_output:
        :param step_size:
        :return: dictionary of results
        """
        mnb_classifier = MultinomialNB()
        rf_classifier = RandomForestClassifier(n_estimators=100, oob_score=True, criterion="entropy", n_jobs=-1,
                                               random_state=50,
                                               max_depth=200)
        knn_classifier = KNeighborsClassifier()
        svc_classifier = SVC(probability=True, kernel="linear")
        lr_classifier = LogisticRegression(n_jobs=-1)

       # mnb_classifier.fit(train_input, train_output)
        rf_classifier.fit(train_input, train_output)
        knn_classifier.fit(train_input, train_output)
        svc_classifier.fit(train_input, train_output)
        lr_classifier.fit(train_input, train_output)

        return { "feature_size" : str(step_size),
                                 "RF": accuracy_score(test_output, rf_classifier.predict(test_input)) * 100,
                                 "KNN": accuracy_score(test_output, knn_classifier.predict(test_input)) * 100,
                                 "SVC": accuracy_score(test_output, svc_classifier.predict(test_input)) * 100,
                                 "LR":accuracy_score(test_output, lr_classifier.predict(test_input)) * 100
            }

    def pca_model_classification(self, train_input, test_input, train_output, test_output, step_size):
        """
        PCA model to generate and select the best features
        :param train_input:
        :param test_input:
        :param train_output:
        :param test_output:
        :return: None
        """
        count_of_features = len(train_input.columns)

        l = []
        # MODELS_GENERAL comprises of models that are used to train newly constructed features.
        count = 10
        while count < count_of_features:
            selector = PCA(n_components=count)
            selector = selector.fit(train_input, train_output)
            temp_train_input = selector.transform(train_input)
            temp_test_input = selector.transform(test_input)

            # Ensemble models with KFOLD
            l.append(self.train_classifiers(temp_train_input, temp_test_input, train_output, test_output, count))
            count+=step_size

        l.append(self.train_classifiers(train_input, test_input, train_output, test_output, count_of_features))
        output = pd.DataFrame(l)
        print(output.head())
        # All the models score with model name is stored in a csv file
        output.to_csv("output_score.csv", sep=",")

'''
if __name__ == "__main__":
    obj = FeatureSelection()
    dataset = obj.read_data("path")
    train_input, test_input, train_output, test_output = obj.split_dataset(dataset)
    obj.pca_model_classification(train_input, test_input, train_output, test_output, 25)
'''