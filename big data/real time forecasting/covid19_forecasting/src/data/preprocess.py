import pandas as pd
path="/media/gear/Data/workdir/projects/big data/real time forecasting/covid19_forecasting/data/"
data=pd.read_csv(path+"raw/COVID-19_Nursing_Home_Dataset.csv")

data2=data.copy(deep=True)

data.drop(columns=['Federal Provider Number', 'Provider Name',
       'Provider Address', 'Provider City', 'Provider State',
       'Provider Zip Code', 'Submitted Data', 'Passed Quality Assurance Check','Resident Access to Testing in Facility',
       'Laboratory Type Is State Health Dept',
       'Laboratory Type Is Private Lab', 'Laboratory Type Is Other','Shortage of Nursing Staff', 'Shortage of Clinical Staff',
       'Shortage of Aides', 'Shortage of Other Staff',
       'Any Current Supply of N95 Masks', 'One-Week Supply of N95 Masks',
       'Any Current Supply of Surgical Masks',
       'One-Week Supply of Surgical Masks',
       'Any Current Supply of Eye Protection',
       'One-Week Supply of Eye Protection', 'Any Current Supply of Gowns',
       'One-Week Supply of Gowns', 'Any Current Supply of Gloves',
       'One-Week Supply of Gloves', 'Any Current Supply of Hand Sanitizer',
       'One-Week Supply of Hand Sanitizer', 'Ventilator Dependent Unit','Any Current Supply of Ventilator Supplies',
       'One-Week Supply of Ventilator Supplies','Three or More Confirmed and Suspected COVID-19 Cases This Week',
       'Initial Confirmed COVID-19 Case This Week', 'Geolocation'],inplace=True)
print(data.columns)

df2=data.groupby(["Week Ending"])['Residents Weekly Admissions COVID-19',
       'Residents Total Admissions COVID-19',
       'Residents Weekly Confirmed COVID-19',
       'Residents Total Confirmed COVID-19',
       'Residents Weekly Suspected COVID-19',
       'Residents Total Suspected COVID-19', 'Residents Weekly All Deaths',
       'Residents Total All Deaths', 'Residents Weekly COVID-19 Deaths',
       'Residents Total COVID-19 Deaths', 'Number of All Beds',
       'Total Number of Occupied Beds', 'Staff Weekly Confirmed COVID-19',
       'Staff Total Confirmed COVID-19', 'Staff Weekly Suspected COVID-19',
       'Staff Total Suspected COVID-19', 'Staff Weekly COVID-19 Deaths',
       'Staff Total COVID-19 Deaths', 'Number of Ventilators in Facility',
       'Number of Ventilators in Use for COVID-19',
       'Total Resident Confirmed COVID-19 Cases Per 1,000 Residents',
       'Total Resident COVID-19 Deaths Per 1,000 Residents',
       'Total Residents COVID-19 Deaths as a Percentage of Confirmed COVID-19 Cases',
       'County'].sum()


df2.to_csv(path+"processed/covid19_forecast_dataset_week_group.csv")

data2.drop(columns=['Week Ending','Provider Name',
       'Provider Address',
       'Provider Zip Code', 'Submitted Data', 'Passed Quality Assurance Check','Resident Access to Testing in Facility',
       'Laboratory Type Is State Health Dept',
       'Laboratory Type Is Private Lab', 'Laboratory Type Is Other', 'County','Geolocation'],inplace=True)


data2.fillna(value=0,inplace=True)
data2.to_csv(path+"processed/covid19_classification_dataset.csv")
