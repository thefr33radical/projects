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

print("completed")