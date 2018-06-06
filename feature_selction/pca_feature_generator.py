from sklearn import RandomForestRegressor
from sklearn import linear_model
from sklearn import svm
import pandas as pd
import numpy as np
import traceback
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.decomposition import PCA
from sklearn import datasets
from sklearn.model_selection import train_test_split

"""
package contain function which returns the best PCA feature combination scored across regression models.

"""

class Pca(object):


    def pca_model(self, train_input, test_input, train_output, test_output):
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
        output.to_csv("output/output_score.csv", sep=",")

    @staticmethod
    def split_dataset(self, dataset):
        x = (dataset.iloc[:, :-2])
        y = (dataset.iloc[:, -1])
        train_input, test_input, train_output, test_output = train_test_split(x, y, test_size=0.05, random_state=500)
        return train_input, test_input, train_output, test_output

    @staticmethod
    def data_loader(self):
        try:
            diabetes = datasets.load_diabetes()

            dataset = pd.DataFrame(diabetes["data"])
            dataset.columns = diabetes["feature_names"]
            target = pd.DataFrame(diabetes["target"], columns=["target"])
            dataset = pd.concat([dataset, target], axis=1)

            train_x, test_x, train_y, test_y=self.split_dataset(dataset)
            self.pca_model(train_x, test_x, train_y, test_y)
            return
            
        except Exception:
            traceback.print_exc()
            return None

if __name__=="__main__":
    obj=Pca()
    obj.data_loader()

