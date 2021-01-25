
#### Requirement 0 
* using python with depedencies in requirements.txt

#### Requirement I
~~~
Input : python aggregator.py mm/dd/yyyy
output : csv files in out put folder
~~~


#### Requirement II Functions in Aggreator class 

* initate - starts the aggregation process
* isprocessed - checks if the files under specified date (mm/dd/yyyy) is already processed. Info is stored in .json under history folder. If already present no further action is taken.
* load_logs - loads all .csv under the specified mm/dd/yyy
* process - splits timestamp column, writes the data to respective mm--dd--yyyy.csv file, reads previous files if present & checks for duplicates before writing new data that are present in backlogs.

#### Requirement III
* Daily scheduler using crontab. 
~~~
1. crontab -e
2. * 23 * * * * (which python) "path to aggregator.py"
##### I have not implemented a script as I having conflict with cron package with my Python version.
~~~


* Integeration tests - All functions are seperated out to the most granular level. Unit testing on each functions before integration testing.(Big bang approach). Incremental approach if the modules get bigger.

~~~
Examples of integration tests -
No records for the day (throws exception), 
number of records exceeding memory size (not handled, process by chunks/commented in code), 
max read/write retries on failure(not handled, can be implented on airflow - due to file lock ),
etc
~~~

* Improvements
~~~

* transform  pandas DF to Spark DF. Minimal effort required. Deploy on EMR
* seperate functions to most granular level. schedule tasks using airflow.
* integrate logging to cloudwatch.
~~~

### Notes
* This module will run only for the specified date, can be extended to run over entire inputs folder(Not mentioned in requirements)
* Range function (yearly,monthly,daily) can be built over basic aggregator module.
* Dataframe has been used to read/manipulate so that module an be easily migrated to dask/spark dataframes
* All info/errors are logged. needs to be more refined.
* Cron job runs daily at 11pm. 


