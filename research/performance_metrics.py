
from sklearn.metrics import confusion_matrix
class PerfMetric(object):
    class Regression(object):
        pass

    class Classification(object):

        def confusion_matrix(self,predicted_output,actual_output):
            """

            :param predicted_output:
            :param actual_output:
            :return:
            """

            sensitivity = 0.0
            specificity = 0.0
            precesion = 0.0



        def auc(self,predicted_output,actual_output):
            """

            :param predicted_output:
            :param actual_output:
            :return:
            """

        pass
