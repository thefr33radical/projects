from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import balanced_accuracy_score, f1_score
from sklearn.model_selection import cross_validate
from sklearn.model_selection import StratifiedKFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import RFE
from sklearn.model_selection import RandomizedSearchCV, GridSearchCV
import pandas as pd
import numpy as np
import warnings
/root_insurance_case_study/"+ "logs/app.log", filemode='w+')
warnings.filterwarnings("ignore")

def model(path_):
    data_path = "/media/gear/Data/workdir/projects/others/root_insurance_case_study/data/"
    data = pd.read_csv(data_path + "model_data_train.csv"[:-4] + "_features.csv")
    # data validation &
    data.drop(columns=['Unnamed: 0', 'filename'], inplace=True)
    data.replace({False: 0, True: 1}, inplace=True)

    X = data[
        ['feature1', 'feature2', 'feature3', 'feature4', 'feature5', 'feature6', 'feature7', 'feature8', 'feature9',
         'feature10', 'feature11', 'feature12', 'feature13', 'feature14', 'nturns', 'nstops']]
    Y = data[["y"]]

    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=42)
    '''model_std = StandardScaler()
    X_train = model_std.fit_transform(X_train)
    X_test=model_std.fit_transform(X_test)'''
    param = {
        'scale_pos_weight': 1.22,
        'objective': 'binary:logistic',
        'eval_metric': 'auc'
    }
    scoring = ['precision_macro', 'recall_macro','f1','balanced_accuracy']
    model_xgboost = XGBClassifier(learning_rate=0.001,
                          n_estimators=100,
                          max_depth=5,
                          min_child_weight=1,
                          gamma=0,
                          subsample=1,
                          colsample_bytree=0.8,
                          objective='binary:logistic',
                          nthread=4,
                          scale_pos_weight=2.22,
                          seed=27,verbosity=0)
    kfold = StratifiedKFold(n_splits=3, shuffle=True, random_state=1)
    results = cross_validate(model_xgboost, X_train, y_train, cv=kfold,verbose=0,scoring=scoring)

    logging.info([(i,np.mean(results[i])*100) for i  in results])

    model_rf=RandomForestClassifier(verbose=0)
    kfold2 = StratifiedKFold(n_splits=3, shuffle=True, random_state=1)
    results2 = cross_validate(model_rf, X_train, y_train, cv=kfold2,scoring=scoring)
    logging.info("\n","Xgboost : ",[{i:np.mean(results2[i])*100} for i  in results2])

    model3=RandomForestClassifier(verbose=0,n_estimators=1000)
    model3.fit(X_train,y_train)
    pred=model3.predict(X_test)
    logging.info("\n","RandomForest : ", balanced_accuracy_score(y_test,pred),f1_score(y_test,pred))

    model4 = RFE(model3, n_features_to_select=7, step=1)
    model4.fit(X_train, y_train)
    pred = model4.predict(X_test)
    logging.info("\n","RandomForest with RFE: ",balanced_accuracy_score(y_test, pred), f1_score(y_test, pred))
model()
