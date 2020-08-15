from statsmodels.tsa.holtwinters import ExponentialSmoothing,SimpleExpSmoothing, Holt
# prepare data
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
path='/media/gear/Data/workdir/projects/big data/real time forecasting/covid19_forecasting/data/processed/'
fig_save_path='/media/gear/Data/workdir/projects/big data/real time forecasting/covid19_forecasting/reports/figures/'
data = pd.read_csv(path+'covid19_forecast_dataset_week_group.csv')
print(data.columns)
result=pd.DataFrame()
fig = plt.figure(frameon=False)
fig.set_size_inches(8,5)


def generate_plots(data):
    corr=data.corr()
    sns.heatmap(corr,
                xticklabels=corr.columns.values,
                yticklabels=corr.columns.values)
    for c in data.columns:
        if c!='Week Ending':
            #fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(16,10), sharex=True)
            data.plot.line(x = 'Week Ending',y = c)
            plt.savefig(fig_save_path+c+'.jpg')

#generate_plots(data)
sns.set_style("darkgrid")
data[data.columns[:10]].plot(figsize=(10,6)).legend(title='COVID Forecvasting', bbox_to_anchor=(1, 1))
plt.show()

def model_exp_smooth(data3,train_X,train_y,col_name):
    # create class
    model = SimpleExpSmoothing(data3).fit(smoothing_level=0.3,optimized=False)
    # fit model
    for i in range(5):
        model_fit = model.forecast(1)
        model_fit.columns=[col_name]
        data3=pd.concat([data3,model_fit])
        data3.iloc[-1,0]=data3.iloc[-1,-1]
        data3.drop(data3.columns[-1],inplace=True,axis=1)
        data3.columns=[col_name]
        model = SimpleExpSmoothing(data3).fit(smoothing_level=0.2, optimized=True)
    return model,data3

def compute(data):
    global  result
    for i in data.columns:
        if i!='Week Ending':
            col_name=i
            data2=data[['Week Ending',i]]
            data2.set_index('Week Ending',inplace=True)
            data2.index=pd.to_datetime(data2.index)
            model,data3=model_exp_smooth(data2,data[['Week Ending']],data[[col_name]],col_name)
            if len(result) <=1:
                result=data3
            else:
                result=pd.merge(result,data3,how='inner',left_index=True,right_index=True)
    #print(result)
    result.to_csv(fig_save_path+"forecast.csv")


#compute(data)



