from paths import reports_dir,data_dir,log_path
import pandas as pd
import numpy as np
import time
import os
import re
import math
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error,r2_score,mean_squared_error
import lightgbm as lgb
from catboost import CatBoostRegressor
import warnings
warnings.filterwarnings("ignore")
import logging
logging.basicConfig(level=logging.INFO,filename=log_path+"/model.log", filemode='w+')
logging.info("\n...Model Module Started...\n")
labels=pd.read_csv(data_dir+"global/processed/feature_category.csv")
categorical_labels=list(labels["catvar"])

# Function to remove Outliers and inconsistent data
def outlier_control(data):
    # Remove outlier
    cols = ['SubAffiliateCost']  # one or more
    Q1 = data[cols].quantile(0.3)
    Q3 = data[cols].quantile(0.7)
    IQR = Q3 - Q1
    logging.info("Before outlier removal : "+str(len(data)))
    data = data[~((data[cols] < (Q1 - 1.5 * IQR)) | (data[cols] > (Q3 + 1.5 * IQR))).any(axis=1)]
    data['OnSiteTime'].replace(0, 0.000001, inplace=True)
    data = data[data['OnSiteTime'] > 0]
    logging.info("onsite " + str(len(data)))
    data['SubAffiliateCost'].replace(0, 0.000001, inplace=True)
    data = data[data['SubAffiliateCost'] > 0]
    logging.info("After outlier removal : "+str(len(data)))
    return data

def Lgboost(data):
    """
    LGBOOST Model Train/Test. Results logged to file
    """
    logging.info('\n...LGBM training started...\n')
    data = data.rename(columns=lambda x: re.sub('[^A-Za-z0-9_]+', '', x))
    for i in categorical_labels:
        data[i] = data[i].astype(float)
    Y = data[['SubAffiliateCost']]
    X = data[data.columns.difference(['SubAffiliateCost'])]
    use_case=['Unnamed0']
    X.drop(use_case,axis=1,inplace=True)

    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    hyper_params = {
        'task': 'train',
        'boosting_type': 'gbdt',
        'objective': 'regression',
        'metric': ['Huber'],
        'learning_rate': 0.005,
        'feature_fraction': 0.9,
        'bagging_fraction': 0.7,
        'bagging_freq': 10,
        'verbose': -1,
        "alpha":1.35,
        "max_depth": 8,
        "num_leaves": 128,
        "max_bin": 512,
        "num_iterations": 2500,
        "n_estimators": 250
    }
    try:
        model= lgb.LGBMRegressor(**hyper_params)
        model.fit(X_train, y_train, eval_set=(X_test, y_test), feature_name='auto', categorical_feature = categorical_labels, verbose=False)
        y_train_pred=model.predict(X_train)
        y_pred = model.predict(X_test)
        #print(mean_absolute_error(np.exp(y_train),np.exp(y_train_pred)),np.exp(y_test),np.exp(y_pred))
        '''logging.info("Train "+str(math.sqrt(mean_squared_error(np.exp(y_train_pred), np.exp(y_train)))))
        logging.info("Test "+str(math.sqrt(mean_squared_error(np.exp(y_pred),np.exp(y_test)))))
        logging.info("Train MAE "+str(mean_absolute_error(np.exp(y_train_pred), np.exp(y_train))))
        logging.info("Test MAE "+str( mean_absolute_error(np.exp(y_pred), np.exp(y_test))))

        r2_train = r2_score(np.exp(y_train_pred), np.exp(y_train))
        r2_test = r2_score(np.exp(y_pred), np.exp(y_test))
        adj_r2_train = 1 - ((1 - (r2_train) ** 2) * (len(X_train) - 1) / (len(X_train) - len(list(X.columns)) - 1))
        adj_r2_test = 1 - ((1 - (r2_test) ** 2) * (len(X_test) - 1) / (len(X_test) - len(list(X.columns)) - 1))
        logging.info("R2, Adjusted R2 Train : "+str(r2_train)+" "+str(adj_r2_train))
        logging.info("R2, Adjusted R2 Test : "+str(r2_test)+" "+str(adj_r2_test))
        '''

        logging.info("Train " + str(mean_squared_error(y_train_pred, y_train)))
        logging.info("Test " + str(mean_squared_error(y_pred, y_test)))
        logging.info("Train MAE " + str(mean_absolute_error(y_train_pred, y_train)))
        logging.info("Test MAE " + str(mean_absolute_error(y_pred, y_test)))

        r2_train = r2_score(y_train_pred, y_train)
        r2_test = r2_score(y_pred, y_test)
        adj_r2_train = 1 - ((1 - (r2_train) ** 2) * (len(X_train) - 1) / (len(X_train) - len(list(X.columns)) - 1))
        adj_r2_test = 1 - ((1 - (r2_test) ** 2) * (len(X_test) - 1) / (len(X_test) - len(list(X.columns)) - 1))
        logging.info("R2, Adjusted R2 Train : " + str(r2_train) + " " + str(adj_r2_train))
        logging.info("R2, Adjusted R2 Test : " + str(r2_test) + " " + str(adj_r2_test))

        feature_name = zip(X.columns, model.feature_importances_)
        feature_name = sorted(feature_name, key=lambda x: x[1],reverse=True)
        logging.info("Top 15 Features"+str(feature_name[:15]))
        logging.info("\n...LGB Model Train/Test Completed...\n")

        ax = lgb.plot_importance(model, max_num_features=15)
        plt.savefig(reports_dir+"feature_importance.png")

        ax = lgb.plot_split_value_histogram(model, feature='OnSiteTime', bins='auto')
        plt.savefig(reports_dir+"feature_histogram.png")

    except Exception as e:
        logging.error(e)

def CatBoost(data):
    """
    CatBoost Model Training & Testing. Results logged to file
    """
    logging.info('...CatBoost training started...')
    for i in categorical_labels:
        data[i] = data[i].astype(str)

    data = data[data['OnSiteTime'] > 0]
    data = data[data['SubAffiliateCost'] > 0]
    Y = data[['SubAffiliateCost']]
    X = data[data.columns.difference(['SubAffiliateCost'])]
    use_case=['DefaultAffiliateNTE','DefaultClientNTE']
    X.drop(use_case,axis=1,inplace=True)

    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
    try:
        model2=CatBoostRegressor( depth=10, learning_rate=0.01, loss_function='RMSE',n_estimators=350)
        model2.fit(X_train, y_train,cat_features=categorical_labels,eval_set=(X_test, y_test),plot=True)
        # make predictions
        y_train_pred=model2.predict(X_train)
        y_pred = model2.predict(X_test)
        logging.info("Train "+str(mean_squared_error(y_train_pred,y_train)))
        logging.info("Test "+str(mean_squared_error(y_pred,y_test)))
        logging.info("Train MAE "+str(mean_absolute_error(y_train_pred,y_train)))
        logging.info("Test MAE "+str(mean_absolute_error(y_pred,y_test)))

        r2_train = r2_score(y_train_pred, y_train)
        r2_test = r2_score(y_pred, y_test)
        adj_r2_train = 1 - ((1 - (r2_train) ** 2) * (len(X_train) - 1) / (len(X_train) - len(list(X.columns)) - 1))
        adj_r2_test = 1 - ((1 - (r2_test) ** 2) * (len(X_test) - 1) / (len(X_test) - len(list(X.columns)) - 1))
        logging.info("R2, Adjusted R2 Train : " + str(r2_train) + " " + str(adj_r2_train))
        logging.info("R2, Adjusted R2 Test : " + str(r2_test) + " " + str(adj_r2_test))
        logging.info("...CatBoost Model Train/Test Complete ...")
        results=pd.read_csv(reports_dir + "results.csv")
        results["CatBoost"] = y_pred
        results.to_csv(reports_dir + "results.csv")
    except Exception as e:
        logging.error(e)

def compute():
    data = pd.read_csv(data_dir + "global/processed/main_processed.csv")
    data = outlier_control(data)
    Lgboost(data)
    # CatBoost(data)
    logging.info(data[['SubAffiliateCost']].describe())
    logging.info("Median & Mode")
    logging.info(data[['SubAffiliateCost']].median())
    logging.info(data[['SubAffiliateCost']].mode())
    logging.info("\n...Model Module Started...\n")

if __name__=="__main__":
    compute()

