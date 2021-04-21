from paths import reports_dir,data_dir,log_path
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import time

# Function to split data by State or other feature. Used for MetaLearning
def data_seggregator(data,division):
    val=[]
    field=[]
    grp=data.groupby([division])
    if grp.ngroups < 80:
        for s in grp:
            if division=="State":
                s[1].to_csv(data_dir+s[0]+".csv")
                s[1][[division,"SubAffiliateCost"]].describe().to_csv(reports_dir + s[0] + "_summary.csv")
            val.append(len(s[1]))
            field.append(s[0])

# Function to preprocess Data
def data_preprocess(data):
    data["State"] = data["State"].apply(lambda x: x.upper())
    data["City"]=data['City'].astype(str)
    data["City"] = data["City"].apply(lambda x: x.upper())
    data["Pool"] = data['Pool'].astype(str)
    data["Pool"] = data["Pool"].apply(lambda x: x.upper())
    data["Region"] = data["Region"].apply(lambda x: x.upper())

    data.drop(columns=['Unnamed: 0'],axis=1,inplace=True)
    data.describe().to_csv(reports_dir + "main_summary.csv")
    #data.to_parquet(data_dir+"main.parq",compression='gzip')
    data.to_csv(data_dir + 'main.csv')
    return data
# Execute all functions
def compute():
    processed_data = pd.read_csv(data_dir + "cost.csv")
    data_preprocess(processed_data)
if __name__=="__main__":
    compute()
