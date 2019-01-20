from pyspark import SparkContext
from pyspark import SparkFiles

import os


def convert(data):
    data =data.upper()
    return data

sc = SparkContext("local","demo2")
path = os.path.join("/media/compaq/WORKSPACE/NE/prob_stat/module1/project/solution/","solution1.csv")
sc.addFile(path)


print(SparkFiles.get(path))
print(SparkFiles.getRootDirectory())

rdd = sc.textFile(path)

# There are two types of opeation on RDD
# Action - applied on the same data
print(rdd.count())
print(rdd.take(5))
print(rdd.top(5))

#Transforamtion - applied on replicated dataset
#map - operation on each element
#filter - remove elements

rdd = sc.map(convert)
rdd =  sc.filter( lambda x :  x not in ["abc","Wewe","rwerwe"])

