from flask import Flask
from sklearn import datasets
import pandas as pd
from sklearn .model_selection import train_test_split
import json


class MyFlaskApp(object):

    def __init__(self):
        self.app = Flask(__name__)
        self.app.add_url_rule('/<method>', 'index', self.index)
        self.app.run(debug = True)
    def index(self,method):
        return "<h1> testing in progress </h1>"


if __name__ == "__main__":
    a=MyFlaskApp()

    diabetes = datasets.load_diabetes()

    dataset = pd.DataFrame(diabetes["data"])
    dataset.columns = diabetes["feature_names"]
    target = pd.DataFrame(diabetes["target"], columns=["target"])
    dataset = pd.concat([dataset, target], axis=1)
    x = (dataset.iloc[:, :-2])
    y = (dataset.iloc[:, -1])
    train_input, test_input, train_output, test_output = train_test_split(x, y, test_size=0.05, random_state=500)
    test_input=pd.DataFrame(test_input)
    test_output= pd.DataFrame(test_output)
    test_input.to_csv("test.csv")
    test_input.to_json("test_input.json")
    test_output.to_json("test_output.json")
    x=pd.read_json("test_output.json")
    #print((train_output.dimens),len(test_output),len(train_input),len(test_output))

