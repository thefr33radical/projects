
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np


class FeatureSelection(object):

    def read_data(self,path):
        """
        Read data from CSV file
        :param path: string
        :return: pandas dataframe
        """
        dataset = pd.read_csv(path,low_memory=False)
        return dataset

    def split_dataset(self,dataset):
        """
        Fucnction to split datset into train & test sets
        :param dataset: pandas dataframe
        :return: train/test split data
        """
        data=dataset[:,:-1]
        y=dataset[:,-1]
        train_input, test_input, train_output, test_output = train_test_split(data, y, test_size=0.3,
                                                                              shuffle=True)
        return train_input, test_input, train_output, test_output

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