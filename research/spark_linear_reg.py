from pyspark import SparkContext
from pyspark import SparkConf
from pyspark.sql import SQLContext
import pandas as pd
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression


def read_data(path):
    """
    Function to read data from csv file
    :param path: 
    :return: spk dataframe
    """
    sc = SparkContext()
    sqlsc = SQLContext(sc)

    df = sqlsc.read.format("com.databricks.spark.csv").options(header="true", inferschema="true").load(
        path)
    # print(df.take(10))
    # print(df.cache())
    # print(df.printSchema())
    # print(df.describe().toPandas().transpose)
    return df

def compute(df):
    """
    Function to split data and perform Linear Regression
    :param df: 
    :return: None
    """
    vector =  VectorAssembler(inputCols=["Rank","Previous Rank"], outputCol="parameters")
    t_df = vector.transform(df)
    t_df = t_df.select(["parameters","Rank"])
    print(t_df.show(3))
        
    data = t_df.randomSplit([0.7,0.3])
    train_set = data[0]
    test_set = data[1]
    
    lr = LinearRegression(featuresCol= "parameters", labelCol="Rank", maxIter=10, regParam=0.3, elasticNetParam=0.8)
    lr_model = lr.fit(train_set)
    
    print(" Coeffiecients ",str(lr_model.coefficients))
    print("Intercept ", str(lr_model.intercept))


if __name__=="__main__":
    path =""
    read_data(path)
