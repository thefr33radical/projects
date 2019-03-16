
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC


class Bayseian(object):
    def __init__(self):
        pass

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
        rf_classifier = RandomForestClassifier()
        knn_classifier = KNeighborsClassifier()
        svc_classifier = SVC(probability=True, kernel="linear")
        lr_classifier = LogisticRegression(n_jobs=-1)

        # mnb_classifier.fit(train_input, train_output)
        rf_classifier.fit(train_input, train_output)
        knn_classifier.fit(train_input, train_output)
        svc_classifier.fit(train_input, train_output)
        lr_classifier.fit(train_input, train_output)

        return {"feature_size": str(step_size),
                "RF": accuracy_score(test_output, rf_classifier.predict(test_input)) * 100,
                "KNN": accuracy_score(test_output, knn_classifier.predict(test_input)) * 100,
                "SVC": accuracy_score(test_output, svc_classifier.predict(test_input)) * 100,
                "LR": accuracy_score(test_output, lr_classifier.predict(test_input)) * 100
                }


if __name__=="__main__":
    pass




