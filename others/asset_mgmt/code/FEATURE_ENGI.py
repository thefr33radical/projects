import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import time
import os
from scipy import stats
from sklearn import preprocessing

reports_dir="/media/gear/Data/workdir/projects/others/asset_mgmt/reports/"
data_dir="/media/gear/Data/workdir/projects/others/asset_mgmt/data/"
processed_data = pd.read_csv("/home/gear/Downloads/cost.csv")
fig = plt.figure(num=None, figsize=(6, 4), dpi=100, facecolor='w', edgecolor='k'    )
print("load train data")

# Function to perform data seggregation
def feature_maker(file_name):
    data=pd.read_csv(data_dir +"processed/"+ file_name+'.csv')
    #print(data.columns)
    data.drop(columns=['Unnamed: 0', 'Id', 'WONum', 'WOClientId', 'Region', 'City',
       'Lat', 'Lng',  'LotSize', 'AffiliateId'],inplace=True)

    # Feature Age of the property - Tranform to ordinal value
    # Categories (5, interval[float64]): [(1876.999, 1970.0] < (1970.0, 1984.0] < (1984.0, 1995.0] <
    # (1995.0, 2004.0] < (2004.0, 2018.0]]
    # Observation - May be important
    data['YearBuilt'].fillna(data['YearBuilt'].median(),inplace=True)
    # equal frequency binning
    data['YearBuilt'] = pd.qcut(data['YearBuilt'], q=5,labels=False)
    data['YearBuilt']=data['YearBuilt'].astype(int)

    # Feature TTSQFT - Already ordinal
    # Observation - May be important
    data['TTSQFT'].fillna(data['TTSQFT'].median(),inplace=True)
    #print(data['TTSQFT'])

    # Feature BathRooms - Categorical
    # Observation - May be important
    data['BathRooms'].fillna(data['BathRooms'].median(), inplace=True)
    data['BathRooms'] = data['BathRooms'].astype(int)
    #print(data['BathRooms'])

    # Feature BedRooms - Categorical
    # Observation - May be important
    data['BedRooms'].fillna(data['BedRooms'].median(), inplace=True)
    data['BedRooms'] = data['BedRooms'].astype(str)
    #print(data['BedRooms'])

    # Priority - Ordinal
    # Observation - might be important
    data['PriorityId'].fillna(0)
    data["PriorityId"] = data["PriorityId"].astype(int)

    # Feature Pool - Categorial
    # Observation - Unbalanced, mostly not important
    data["Pool"] = data["Pool"].astype(str)
    data["Pool"] = data['Pool'].apply(lambda x: x.upper() if x is not None else "")
    data["Pool"]=data['Pool'].apply(lambda x :0 if x is None or x=="NO" else 1)
    data["Pool"]=data["Pool"].astype(int)
    #print(data.groupby("Pool").count())

    # Feature call time - Categorical
    # 1. ignoring year, day, extracting only month
    # 2. Converting to winter,spring,fall,summer
    # Observation - May be important as seasons might influence
    z=data['CallTime'].apply(lambda x : x.split("-")[1] if len(x.split("-"))>2 else None)
    z=map(lambda x : int(x),z)
    z=map(lambda x : 0 if x <3 else 1 if (x>=3 and x<5) else 3 if (x>=5 and x<8) else 2 if (x>=8 and x<10) else 0,z)
    data['CallTime']=list(z)
    data['CallTime'] = data['CallTime'].astype(int)

    # Feature Zipcode - Categorical
    # 1. keep first 3 digits of the zipcode, 125 categories overall, within states should be less
    # Observation - Important within a state
    data['ZipCode']=data['ZipCode'].astype(str)
    data['ZipCode'] = data['ZipCode'].apply(lambda x:x[:3] if len(x)>3 else None)
    data['ZipCode'] = data['ZipCode'].astype(int)

    #  AffiliateId - ignored/Categorical
    # Observation - May be important but ignored for now as there are 1000+ ids

    # Service Category, Service Type, Service Code
    # Observation unbalanced

    print(data.columns)
    # purposeid - categorical
    # Observation unbalanced
    data["PurposeId"] = data['PurposeId'].apply(lambda x: 1 if x is None or x == 1 else 2)
    data["PurposeId"] = data["PurposeId"].astype(int)

    # worktype - categorical
    # Observation unbalanced / 16 categories
    data['WOTypeId']=data['WOTypeId'].fillna(0)
    data["WOTypeId"] = data["WOTypeId"].astype(int)

    #Remove outlier
    print(data["SubAffiliateCost"].describe())
    data=data[(np.abs(stats.zscore(data[["SubAffiliateCost"]])) < 3)]
    data.boxplot(column=["SubAffiliateCost"])

    # Fill importqant feaature with null value
    data['OnSiteTime'].fillna(data['OnSiteTime'].median(), inplace=True)
    print(data["SubAffiliateCost"].describe())
    data.to_csv(data_dir+file_name+"_processed.csv")


    """
    ignore -
    ['Unnamed: 0', 'Id', 'WONum', 'WOClientId', 'Region', 'City',
       'Lat', 'Lng',  'LotSize', 'AffiliateId',]
       
    use -  'WOTypeId', 'PurposeId',
       ('ServiceCategory', 'ServiceType', 'ServiceCode') 'CallTime',
       'PriorityId', 'ClientNTE', 'AffiliateNTE', 'State', 'ZipCode',
       'YearBuilt', 'BathRooms', 'BedRooms', 'TTSQFT',
       'Pool', 'SubAffiliateCost', 'OnSiteTime', 
       'DefaultAffiliateNTE', 'DefaultClientNTE'
    """


for root, dirs, files in os.walk(data_dir):
    for file in files:
        if file.endswith(".csv"):
            print(file, root, dirs)
            feature_maker(file)

