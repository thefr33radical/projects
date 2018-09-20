from feature_selection import  pca
from feature_selection import  rfe


class FraudDetection(object):

    def __init__(self):

        pass

    def compute(self,path):
        obj =pca.FeatureSelection()
        print("start")
        dataset = obj.read_data(path)
        dataset = dataset.iloc[:1000,:]
        train_input, test_input, train_output, test_output = obj.split_dataset(dataset)
        obj.pca_model_classification(train_input, test_input, train_output, test_output, 25)
        print("complete")

if __name__=="__main__":
    fraud = FraudDetection()
    fraud.compute("/home/kuliza227/github/projects/fraud_detection/data/creditcard.csv")
