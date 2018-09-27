from feature_selection import  pca,read_split
from feature_selection import  rfe

class FraudDetection(object):

    def __init__(self):

        pass

    def compute(self,path):
        obj1 = read_split.ReadSplit()
        obj2 =pca.FeatureSelection()
        print("start")
        dataset = obj1.read_data(path)
        dataset = dataset.iloc[:10000,:]
        train_input, test_input, train_output, test_output = obj1.split_dataset(dataset)
        if train_input is None:
            return
        obj2.pca_model_classification(train_input, test_input, train_output, test_output, 10)
        print("complete")


if __name__=="__main__":
    fraud = FraudDetection()
    fraud.compute("")
