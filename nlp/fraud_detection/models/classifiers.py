from sklearn.decomposition import PCA
from sklearn.metrics import confusion_matrix
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
import pandas as pd
import pickle
import os
import numpy as np
from helpers import preprocess


class Models(object):

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
        self.rf_classifier = RandomForestClassifier()
        #knn_classifier = KNeighborsClassifier()
        self.svc_classifier = SVC(probability=True, kernel="linear")
        self.lr_classifier = LogisticRegression(n_jobs=-1)

        # mnb_classifier.fit(train_input, train_output)
        self.rf_classifier.fit(train_input, train_output)
        #knn_classifier.fit(train_input, train_output)s
        self.svc_classifier.fit(train_input, train_output)
        self.lr_classifier.fit(train_input, train_output)

        with open(os.path.join(os.getcwd(), "SavedClassifiers/rf_classifier.pkl"), "wb") as f:
            pickle.dump(self.rf_classifier,f)
        with open(os.path.join(os.getcwd(), "SavedClassifiers/svc_classifier.pkl"), "wb") as f:
            pickle.dump(self.svc_classifier,f)
        with open(os.path.join(os.getcwd(), "SavedClassifiers/lr_classifier.pkl"), "wb") as f:
            pickle.dump(self.lr_classifier,f)

        pobj = preprocess.PerfMetric()
        rf_precesion, rf_accuracy, rf_f1_score, rf_sensitivity, rf_specificity = pobj.confusion_matrix( test_output,self.rf_classifier.predict(test_input))
        svc_precesion, svc_accuracy, svc_f1_score, svc_sensitivity, svc_specificity = pobj.confusion_matrix(test_output,
                                                                                                       self.svc_classifier.predict(
                                                                                                           test_input))
        lr_precesion, lr_accuracy, lr_f1_score, lr_sensitivity, lr_specificity = pobj.confusion_matrix(test_output,
                                                                                                       self.lr_classifier.predict(
                                                                                                           test_input))

        return {"feature_size": [step_size]*3,
                "classifier_type":["RF","SVC","LR"],
                "accuracy_scores":[rf_accuracy,svc_accuracy,lr_accuracy],
                "precession":[rf_precesion,svc_precesion,lr_accuracy],
                "f1_score":[rf_f1_score,svc_f1_score,lr_f1_score],
                "sensitivity":[rf_sensitivity,svc_sensitivity,lr_sensitivity],
                "specificity":[rf_specificity,svc_specificity,lr_specificity],
                "confusion_matrix": [confusion_matrix( test_output,self.rf_classifier.predict(test_input)),
                                     confusion_matrix( test_output,self.svc_classifier.predict(test_input)),
                                     confusion_matrix( test_output,self.lr_classifier.predict(test_input))],

                "Length of Data":[len(train_input)+len(test_input)]*3
                }

    def pca(self, train_input, test_input, train_output, test_output, step_size):
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
            count += step_size

        l.append(self.train_classifiers(train_input, test_input, train_output, test_output, count_of_features))
        output = pd.DataFrame(l)
        print(output.head())
        # All the models score with model name is stored in a csv file
        output.to_csv("output_score.csv", sep=",")

    def ensemble_predict(self,test_input):
        """
        Ensembled prediction
        :param test_input: features
        :return: array
        """

        with open(os.path.join(os.getcwd(), "data/rf_classifier.pkl"), "wb") as f:
            self.rf_classifier = pickle.load(f)
        with open(os.path.join(os.getcwd(), "data/svc_classifier.pkl"), "wb") as f:
            self.svc_classifier = pickle.load(f)
        with open(os.path.join(os.getcwd(), "data/lr_classifier.pkl"), "wb") as f:
            self.lr_classifier = pickle.load(f)

        ensemble=[]
        # ensemble = [ (class, probability_score,classifier name),   (class, probability_score,classifier name)...... ]

        ensemble.append(( self.svc_classifier.predict(test_input)[0], np.max(self.svc_classifier.predict_proba(test_input), "svc")  ))
        ensemble.append(
            (self.lr_classifier.predict(test_input)[0], np.max(self.lr_classifier.predict_proba(test_input)), "lr"))
        ensemble.append(
            (self.rf_classifier.predict(test_input)[0], np.max(self.rf_classifier.predict_proba(test_input)), "rf" ))

        maximum = ensemble[0][1]
        max_classifier=""
        max_class=0

        # The best conidence score is taken along with classifier name, class
        for i in ensemble:
            if i[1]> maximum:
                max_class=i[0]
                maximum=i[1]
                max_classifier=i[2]

        return maximum, max_classifier,max_class
