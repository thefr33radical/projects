from paths import reports_dir,data_dir,log_path
import pandas as pd
import numpy as np
import time
import os
from scipy import stats
from sklearn import preprocessing
import logging
logging.basicConfig(level=logging.INFO,filename=log_path+"/feature_eng.log", filemode='w+')

cat_var=[]
ord_var=[]
logging.info("\n...Feature Eng Module Started...\n")
import prince

def MCA(X):
  #X = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/balloons/adult+stretch.data')
  #X.columns = ['Color', 'Size', 'Action', 'Age', 'Inflated']

  print(X.head())
  mca = prince.MCA()

  mca = mca.fit(X) # same as calling ca.fs_r(1)
  mca = mca.transform(X) # same as calling ca.fs_r_sup(df_new) for *another* test set.
  return mca
	
def feature_maker(file_name):
    """
    Function to Generate Features
    Remove Outliers
    Bin Continious Features into Ordinal bins
    """
    data=pd.read_csv(data_dir +file_name+".csv")

    #logging.info(data.columns)
    data.drop(columns=['Unnamed: 0', 'Id', 'Region','WOClientId','WONum',
        'LotSize'],inplace=True)

    # Feature Age of the property - Tranform to ordinal value
    # Categories (5, interval[float64]): [(1876.999, 1970.0] < (1970.0, 1984.0] < (1984.0, 1995.0] <
    # (1995.0, 2004.0] < (2004.0, 2018.0]]
    # Observation - May be important
    data['YearBuilt'].fillna(0,inplace=True)
    # equal frequency binning/Quantile binning
    #data['YearBuilt'] = pd.qcut(data['YearBuilt'], q=5,labels=False)
    data['YearBuilt']=data['YearBuilt'].astype(int)
    ord_var.append('YearBuilt')

    # Feature TTSQFT - Already ordinal
    # Observation - May be important
    data['TTSQFT'].fillna(0,inplace=True)
    ord_var.append('TTSQFT')
    #logging.info(data['TTSQFT'])

    # Feature BathRooms - Categorical
    # Observation - May be important
    data['BathRooms'].fillna(0, inplace=True)
    data['BathRooms'] = data['BathRooms'].astype(int)
    cat_var.append('BathRooms')
    #logging.info(data['BathRooms'])

    # Feature BedRooms - Categorical
    # Observation - May be important
    data['BedRooms'].fillna(0, inplace=True)
    data['BedRooms'] = data['BedRooms'].astype(str)
    cat_var.append('BedRooms')
    #logging.info(data['BedRooms'])

    # Priority - Ordinal
    # Observation - might be important
    data['PriorityId'].fillna(0)
    data["PriorityId"] = data["PriorityId"].astype(int)
    ord_var.append('PriorityId')

    # Feature Pool - Categorial
    # Observation - Unbalanced, mostly not important
    data["Pool"] = data["Pool"].astype(str)
    data["Pool"] = data['Pool'].apply(lambda x: x.upper() if x is not None else "")
    data["Pool"]=data['Pool'].apply(lambda x :0 if x is None or x=="NO" else 1)
    data["Pool"]=data["Pool"].astype(int)
    cat_var.append('Pool')
    #logging.info(data.groupby("Pool").count())

    # Feature call time - Categorical
    # 1. ignoring year, day, extracting only month
    # 2. Converting to winter,spring,fall,summer
    # Observation - May be important as seasons might influence
    z=data['CallTime'].apply(lambda x : x.split("-")[1] if len(x.split("-"))>2 else None)
    z=map(lambda x : int(x),z)
    z=map(lambda x : 0 if x <=3 else 1 if (x>=4 and x<=6) else 3 if (x>6 and x<=10) else 2 if (x>10 and x<13) else 0,z)
    data['CallTimequarter']=list(z)
    data['CallTimemonth'] = pd.DatetimeIndex(data['CallTime']).month
    data['CallTimeday'] = pd.DatetimeIndex(data['CallTime']).day
    data['CallTimequarter'] = data['CallTimequarter'].astype(int)
    data.drop(columns=['CallTime'],inplace=True)

    # Feature Zipcode - Categorical
    # 1. keep first 3 digits of the zipcode, 125 categories overall, within states should be less
    # Observation - Important within a state
    data['ZipCode']=data['ZipCode'].astype(str)
    data['ZipCode'] = data['ZipCode'].apply(lambda x:int(float(x[:3])) if len(x)>3 else 0)
    data['ZipCode'] = data['ZipCode'].astype(int)
    cat_var.append('ZipCode')

    # State - Categorical
    state_label_encoder = preprocessing.LabelEncoder()
    data["State"]=state_label_encoder.fit_transform(data["State"])

    # City - Categorical
    city_label_encoder = preprocessing.LabelEncoder()
    data["City"]= data["City"].astype(str)
    data["City"]= data["City"].apply(lambda x :x.lower())
    data["City"] = city_label_encoder.fit_transform(data["City"])

    #  AffiliateId - Categorical
    # Observation - Very important after first pass

    # Service Category, Service Type, Service Code
    # Observation unbalanced - important

    logging.info(data.columns)
    # purposeid - categorical
    # Observation unbalanced
    data["PurposeId"] = data['PurposeId'].apply(lambda x: 1 if x is None or x == 1 else 2)
    data["PurposeId"] = data["PurposeId"].astype(int)
    cat_var.append('PurposeId')

    # worktype - categorical
    # Observation unbalanced / 16 categories
    data['WOTypeId']=data['WOTypeId'].fillna(0)
    data["WOTypeId"] = data["WOTypeId"].astype(int)
    cat_var.append('WOTypeId')

    # Fill importqant feature with null value
    data['OnSiteTime'].fillna(0, inplace=True)
    data.to_csv(data_dir+"/global/processed/"+file_name+"_processed.csv")

    cat_var.extend(['CallTimequarter', 'CallTimeday', 'CallTimemonth', 'ServiceCategory',
                    'ServiceType', 'ServiceCode', 'AffiliateId', 'State', 'City', ])
    var_data=pd.DataFrame.from_dict({"catvar":cat_var,"ordvar":ord_var},orient='index')
    var_data=var_data.transpose()
    var_data.to_csv(data_dir + "/global/processed/feature_category.csv")
    logging.info("\n...Feature Eng Module End...\n")

if __name__=="__main__":
    feature_maker("main")


