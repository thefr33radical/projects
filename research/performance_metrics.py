
from sklearn.metrics import confusion_matrix
class PerfMetric(object):
    class Regression(object):
        pass

    class Classification(object):

        def confusion_matrix(self,predicted_output,actual_output):
            """
            Function to Compute Precesion, Accuracy, Sensitivity, Specificity

            :param predicted_output:
            :param actual_output:
            :return: Precesion, Accuracy, Sensitivity, Specificity
            """

            conf_matrix = confusion_matrix(actual_output,predicted_output)
            true_p = conf_matrix[0][0]
            true_n = conf_matrix[1][1]
            false_p =  conf_matrix[0][1]
            false_n  = conf_matrix[1][0]

            # Sensitivity = TP /(TP + FN).Maximize Sensitivity/Penalize False N,eg in Fraud Detection,Cancer Prediction.
            sensitivity = true_p / (true_p + false_n)

            # Specificity = TN/(TN+FP) Penalize FP/Maximize specificity in case of phishing filter..
            specificity = true_n/(true_n+false_p)

            precesion = true_p/ (true_n+true_p)

            # Use accuracy metric when classes are balanced
            accuracy = true_p / (true_p + true_n + false_p + false_n)

            # F1_score is the harmonic mean on Precesion & Recall
            f1_score = (2 * precesion * sensitivity) / (precesion + sensitivity)

            return precesion, accuracy, f1_score, sensitivity, specificity

        def auc(self,predicted_output,actual_output):
            """

            :param predicted_output:
            :param actual_output:
            :return:
            """

        pass

if __name__ =="__main__":
    obj = PerfMetric()
    class_obj = obj.Classification()
    class_obj.confusion_matrix([1,1,1,1,1,0,0,0,0,0],[0,0,1,1,1,0,0,0,0,1])