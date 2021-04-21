import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import time
import seaborn as sns
from paths import reports_dir,data_dir,log_path
fig = plt.figure(num=None, figsize=(6, 4), dpi=100, facecolor='w', edgecolor='k')
import logging
logging.basicConfig(level=logging.INFO,filename=log_path+"/eda.log", filemode='w+')

# Function to Box plot/Detect Outliers
def boxplot(data,column):
    sns.boxplot(y=data[column])
    plt.show()

#Function to check Regression plot
def regressionplot(data):
    plt.scatter(data["X1"], data["actual"], color="red")
    plt.plot(data["X1"], data["LGBM"], color="green")
    plt.show()

# Function to pair plot features
def pairplot(data,columns):
    data = data[columns]
    sns.pairplot(data)
    plt.show()

# Function to check ddddddddddddddistributiom
def histogram(data,column):
    cols = ['SubAffiliateCost']  # one or more
    Q1 = data[cols].quantile(0.25)
    Q3 = data[cols].quantile(0.75)
    IQR = Q3 - Q1
    #data = data[~((data[cols] < (Q1 - 1.5 * IQR)) | (data[cols] > (Q3 + 1.5 * IQR))).any(axis=1)]
    data = data[data['SubAffiliateCost'] > 0]
    data = data[data['OnSiteTime'] > 0]
    sns.histplot(data=data, x=column,bins=50,kde=True,hue="PriorityId")
    plt.savefig(reports_dir+"right_skewed.png")

# Data Distribution plot
def eda(data):
    logging.info(len(data))

    for col in data.columns:
        typ = ""
        try:
            rr = pd.plotting.scatter_matrix(data[[col]], c=data[["SubAffiliateCost"]], figsize=(15, 5), marker='o',
                                            hist_kwds={'bins': 50}, s=60, alpha=.8)
            data[col].fillna(0,inplace=True)
            z = len(data[col].astype(int).unique())
            if col in categorical_labels:
                typ = "categorical"
            else:
                typ = "continious"
            plt.title("Data Distribution : " + str(col) + " [" + typ + "]")
            plt.show()
        except Exception as e:
            logging.error(e)

if __name__=="__main__":
    logging.info("Started EDA")
    df = pd.read_csv(data_dir + "global/processed/main_processed.csv")
    #eda(df)
    logging.info(" EDA Completed")
    #df=pd.read_csv(reports_dir+"results.csv")
    #pairplot(df,df.columns)
    #regressionplot(df)
    #histogram(df,"SubAffiliateCost")