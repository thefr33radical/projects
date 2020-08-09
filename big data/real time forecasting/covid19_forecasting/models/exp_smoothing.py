from statsmodels.tsa.holtwinters import ExponentialSmoothing,SimpleExpSmoothing, Holt
# prepare data
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
path='/media/gear/Data/workdir/projects/big data/real time forecasting/covid19_forecasting/data/processed/'
fig_save_path='/media/gear/Data/workdir/projects/big data/real time forecasting/covid19_forecasting/reports/figures/'
data = pd.read_csv(path+'covid19_forecast_dataset_week_group.csv')
print(data.columns)
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
def model_exp_smooth(data,train_X,train_y):

    # create class
    model = SimpleExpSmoothing(data).fit(smoothing_level=0.2,optimized=False)
    # fit model
    model_fit = model.forecast(train_X)
    # make prediction
    #print( model_fit.predict(train_X))
    return model

data2=data[data['Week Ending'],data['Residents Weekly Admissions COVID-19']]
model=model_exp_smooth(data2,data['Week Ending'],data['Residents Weekly Admissions COVID-19'])
