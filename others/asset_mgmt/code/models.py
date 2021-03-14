import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import time
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error,r2_score,mean_squared_error
import warnings
from sklearn.ensemble import RandomForestRegressor
import lightgbm as lgb
from catboost import CatBoostRegressor
warnings.filterwarnings("ignore")

reports_dir="/media/gear/Data/workdir/projects/others/asset_mgmt/reports/"
data_dir="/media/gear/Data/workdir/projects/others/asset_mgmt/data/"
processed_data = pd.read_csv("/home/gear/Downloads/cost.csv")

print('Loading data...')
# load or create your dataset
df = pd.read_csv(data_dir+"main_processed.csv")
categorical_labels=['WOTypeId','PurposeId', 'ServiceCategory',
       'ServiceType', 'ServiceCode',  'BathRooms', 'BedRooms',
         'Pool','ZipCode']


def Lgboost(df):

    for i in categorical_labels:
        df[i] = df[i].astype(float)

    X = df[['WOTypeId', 'PurposeId', 'ServiceCategory', 'ServiceType',
            'ServiceCode', 'PriorityId', 'ClientNTE', 'AffiliateNTE',
            'ZipCode', 'YearBuilt', 'BathRooms', 'BedRooms', 'TTSQFT',
            'Pool', 'OnSiteTime', 'DefaultAffiliateNTE',
            'DefaultClientNTE']]
    Y = df[['SubAffiliateCost']]

    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    hyper_params = {
        'task': 'train',
        'boosting_type': 'gbdt',
        'objective': 'regression',
        'metric': ['l2', 'auc'],
        'learning_rate': 0.005,
        'feature_fraction': 0.9,
        'bagging_fraction': 0.7,
        'bagging_freq': 10,
        'verbose': 0,
        "max_depth": 8,
        "num_leaves": 128,
        "max_bin": 512,
        "num_iterations": 1000,
        "n_estimators": 5000
    }

    model= lgb.LGBMRegressor(**hyper_params)
    model.fit(X_train, y_train, eval_set=(X_test, y_test), feature_name='auto', categorical_feature = categorical_labels, verbose=False)
    y_train_pred=model.predict(X_train)
    y_pred = model.predict(X_test)
    y_train_pred=model.predict(X_train)
    y_pred = model.predict(X_test)
    # make predictions
    print("Train",mean_squared_error(y_train_pred,y_train))
    print("Test",mean_squared_error(y_pred,y_test))
    print("Train MAE", mean_absolute_error(y_train_pred, y_train))
    print("Test MAE", mean_absolute_error(y_pred, y_test))

def CatBoost(df):
    for i in categorical_labels:
        df[i] = df[i].astype(str)

    X = df[['WOTypeId', 'PurposeId', 'ServiceCategory', 'ServiceType',
            'ServiceCode', 'PriorityId', 'ClientNTE', 'AffiliateNTE',
            'ZipCode', 'YearBuilt', 'BathRooms', 'BedRooms', 'TTSQFT',
            'Pool', 'OnSiteTime', 'DefaultAffiliateNTE',
            'DefaultClientNTE']]
    Y = df[['SubAffiliateCost']]

    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    model2=CatBoostRegressor(iterations=5000, depth=10, learning_rate=0.01, loss_function='MAE')
    model2.fit(X_train, y_train,cat_features=categorical_labels,eval_set=(X_test, y_test),plot=True)
    # make predictions
    y_train_pred=model2.predict(X_train)
    y_pred = model2.predict(X_test)
    print("Train",mean_squared_error(y_train_pred,y_train))
    print("Test",mean_squared_error(y_pred,y_test))
    print("Train MAE",mean_absolute_error(y_train_pred,y_train))
    print("Test MAE",mean_absolute_error(y_pred,y_test))


"""
Another subtle difference is that root mean square error(and by extension mean square error) tends to grow much larger than mean absolute error when the sample size increases. So if you're dealing with different sized samples it becomes harder to compare models.
"""

#Lgboost(df)
CatBoost(df)