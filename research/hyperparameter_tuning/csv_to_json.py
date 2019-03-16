

import pandas as pd


class Convert(object):

    def __init__(self,path):
        try:
            self.dataset = pd.read_csv(path)
        except Exception as e:
            print(e)
            return

    def transform_simple(self,path):
        try:
            self.dataset.to_json(path)
        except Exception as e:
            print(e)
            return


if __name__=="__main__":
    print("Enter path of CSV file")
    obj = Convert(input())
    print("Enter path where json needs to be stored")
    obj.transform_simple(input())
