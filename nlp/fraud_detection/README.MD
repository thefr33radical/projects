# Fraud Detection


## Problem Statement
#### To detect whether the given transaction is fraudulent or not.
#### Usually in a dataset the number of cases of fraudulent transaction as compared to geniune transaction is miniscule. Class imbalance is usually encountered, which usually transforms into anamoly detection problem.
#### Solution :  We can solve this problem by
####            1.Balancing number of samplesis done by using -> [Oversampling, SMOTE, ADASYN]
####            2.Classifiers -> False Negatives need to be penalized more. Penalized Wrapper models.
####            3.Metrics -> Accuracy cannot be used to measure the performance of the model. Sensitivity, Specificity, F1Score, Logloss have to be taken into account

## Dataset
#### https://www.kaggle.com/mlg-ulb/creditcardfraud
#### https://www.kaggle.com/ntnu-testimon/paysim1
#### https://www.kaggle.com/ntnu-testimon/banksim1



