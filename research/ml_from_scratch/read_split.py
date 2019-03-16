from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE, ADASYN
from imblearn.over_sampling import RandomOverSampler
from collections import Counter
import  pandas as pd
import numpy as np
import random


class ReadSplit(object):

    def read_data(self, path):
        """
        Read data from CSV file
        :param path: string
        :return: pandas dataframe
        """

        try:
            dataset = pd.read_csv(path, low_memory=False)
            return dataset
        except Exception as e:
            print(e)

    def undersampling(self,dataframe, n):
        """
        Function returns randomly selected rows from a dataframe

        :param dataframe: pandas dataframe
        :param n: n number of rows
        :return: pandas dataframe
        """

        c = list(range(0, len(dataframe)))
        sample_rows = random.sample(c, n)

        new_data = pd.DataFrame()
        for i in sample_rows:
            new_data = new_data.append(dataframe.iloc[i])

        print("new_data_rows", len(new_data))
        return new_data

    def oversampling(self,dataset,n):
        """
               Function returns randomly selected rows from a dataframe

               :param dataframe: pandas dataframe
               :param n: n number of rows
               :return: pandas dataframe
               """

        initial_copy= dataset.copy(deep=True)
        while (len(dataset)< n):
            dataset =dataset.append(initial_copy)
        return dataset

    def synthetic_sampling_SMOTE(self,dataset):
        """

        :param dataset:
        :return:
        """
        data = dataset.iloc[:, :-2]
        y = dataset.iloc[:, -1]
        X_resampled, y_resampled = SMOTE().fit_sample(data, y)
        X_resampled = pd.DataFrame(X_resampled)
        y_resampled = pd.DataFrame(y_resampled)
        new_dataset = pd.concat([X_resampled, y_resampled], axis=1)
        return new_dataset

    def synthetic_sampling_ADASYN(self,dataset):
        """

        :param dataset:
        :return:
        """
        data = dataset.iloc[:, :-2]
        y = dataset.iloc[:, -1]
        X_resampled, y_resampled = ADASYN().fit_sample(data, y)
        X_resampled = pd.DataFrame(X_resampled)
        y_resampled = pd.DataFrame(y_resampled)
        new_dataset = pd.concat([X_resampled, y_resampled], axis=1)
        return new_dataset

    def random_oversampler(self,dataset):
        """

        :param dataset:
        :return:
        """
        data = dataset.iloc[:, :-2]
        y = dataset.iloc[:, -1]
        X_resampled, y_resampled = RandomOverSampler(random_state=0).fit_sample(data, y)
        X_resampled = pd.DataFrame(X_resampled)
        y_resampled = pd.DataFrame(y_resampled)
        new_dataset = pd.concat([X_resampled, y_resampled], axis=1)
        return new_dataset

    def split_dataset(self, dataset,sampling_type=1):
        """
        Fucnction to split datset into train & test sets
        :param dataset: pandas dataframe
        :return: train/test split data
        """

        y = dataset.iloc[:, -1]
        count_predictors = Counter(y)

        if count_predictors[0] < 0.5*count_predictors[1] or count_predictors[0] > 0.5*count_predictors[1]:
            if sampling_type == 1:
                dataset = self.random_oversampler(dataset)

            elif sampling_type ==2:
                dataset = self.synthetic_sampling_ADASYN(dataset)

            elif sampling_type ==3:
                dataset =self.synthetic_sampling_SMOTE(dataset)

        data = dataset.iloc[:, :-2]
        y = dataset.iloc[:, -1]
        data = data.replace([np.inf, -np.inf], np.nan).dropna(axis=1)
        data = data.replace({np.nan: 0})
        data = data.fillna(0)
        train_input, test_input, train_output, test_output = train_test_split(data, y, test_size=0.2,
                                                                              shuffle=True)
        return train_input, test_input, train_output, test_output


if __name__=="__main__":
    obj =ReadSplit()

    l=[[1,2,3,4,0],[2,3,45,6,0],[23,5,4,3,0],[11,2,3,4,0],[1,2,33,4,0],[1,2,3,4,0],[2,3,45,6,0],[23,5,4,3,0],[11,2,3,4,0],[1,2,33,4,0],[1,2,3,4,0],[2,3,45,6,0],[23,5,4,3,0],[11,2,3,4,0],[1,2,33,4,0],[1,12,3,4,0],[1,12,13,34,1],[1,0,3,7,1],[1,12,13,34,1],[1,0,3,7,1],[1,12,13,34,1],[1,0,3,7,1]]
    dataset = pd.DataFrame(data=l)
    #print(dataset)

    '''
    print(obj.random_oversampler(dataset))
    print("-----")
    print(obj.synthetic_sampling_ADASYN(dataset))
    print("-----")
    print(obj.synthetic_sampling_SMOTE(dataset))
    print("-----")
    '''