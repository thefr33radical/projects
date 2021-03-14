import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import time

reports_dir="/media/gear/Data/workdir/projects/others/asset_mgmt/reports/"
data_dir="/media/gear/Data/workdir/projects/others/asset_mgmt/data/"
processed_data = pd.read_csv("/home/gear/Downloads/cost.csv")
fig = plt.figure(num=None, figsize=(6, 4), dpi=100, facecolor='w', edgecolor='k'    )
print("load train data")

# Function to perform data seggregation
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

        # Plot different states denoting  imbalance
        plt.bar(field, val, color=['blue', 'red', 'green'], width=0.4,align='center')
        plt.xlabel(division)
        plt.ylabel("Instances")
        plt.title("Data by "+division)
        plt.xticks(rotation=90)

        # Make space for and rotate the x-axis tick labels
        plt.savefig(reports_dir+division+"_data_spread.jpg")
        time.sleep(0.1)
        plt.pause(0.0001)
        return
        # plot Correlation
        # Plot Distribution of features

def data_preprocess(data):
    data["State"] = data["State"].apply(lambda x: x.upper())
    data["City"]=data['City'].astype(str)
    data["City"] = data["City"].apply(lambda x: x.upper())
    data["Pool"] = data['Pool'].astype(str)
    data["Pool"] = data["Pool"].apply(lambda x: x.upper())
    data["Region"] = data["Region"].apply(lambda x: x.upper())

    data.drop(columns=['Unnamed: 0'],axis=1,inplace=True)
    data = data[data["SubAffiliateCost"] > 0]
    data.describe().to_csv(reports_dir + "main_summary.csv")
    data.to_parquet(data_dir+"main.parq",compression='gzip')
    data.to_csv(data_dir + 'main.csv')
    return data
print("statred")
#processed_data=data_preprocess(processed_data)

categorical_labels=['PurposeId', 'ServiceCategory',
       'ServiceType', 'ServiceCode',  'PriorityId',
       'State', 'Region', 'City', 'ZipCode',
       'YearBuilt', 'BathRooms', 'BedRooms',  'Pool']

#data_seggregator(processed_data,"State")
#data_seggregator(processed_data,"Region")
data_seggregator(processed_data,"Pool")
print("completed")