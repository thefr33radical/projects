from sklearn.model_selection import train_test_split
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
        length = len(dataset)
        initial_copy= dataset.copy(deep=True)
        while (len(dataset)< n):
            dataset =dataset.append(initial_copy)
        return dataset

    def split_dataset(self, dataset):
        """
        Fucnction to split datset into train & test sets
        :param dataset: pandas dataframe
        :return: train/test split data
        """
        # Handling unequal classes
        '''one = dataset.loc[dataset.iloc[:,-1] == 1]
        zero = dataset.loc[dataset.iloc[:,-1] == 0]
        print(    "one",len(one),"zero",len( zero))
        if len(one) == 0 or len( zero) == 0:
            print(" Classes need to be at least two")
            return None,None,None,None

        if len(one) > len(zero):
            one = self.undersampling(one,len(zero))
            dataset = pd.concat([one,zero])

        elif len(one) < len(zero):
            zero =self.undersampling(zero, len(one))
            dataset = pd.concat([one, zero])
            '''

        data = dataset.iloc[:, :-2]
        y = dataset.iloc[:, -1]

        data = data.replace([np.inf, -np.inf], np.nan).dropna(axis=1)
        data = data.replace({np.nan: 0})

        data = data.fillna(0)
        train_input, test_input, train_output, test_output = train_test_split(data, y, test_size=0.2,
                                                                              shuffle=True)
        return train_input, test_input, train_output, test_output