from pyspark.mllib.tree import  RandomForest
from pyspark.mllib.util import MLUtils
from pyspark import SparkContext as sc

data = MLUtils.loadLibSVMFile(sc, "")
(train_set,test_set) = data.randomSplit([0.7,0.3])

model = RandomForest.trainClassifier(train_set, numClasses=2, categoricalFeaturesInfo={}, impurity="gini" )

pred = model.predict(test_set.map(lambda x:x.features))
labelandpredict =test_set.map( lambda  lp: lp.label).zip(pred)

error =labelandpredict.filter( lambda lp  : lp[0] != lp[1].count() /float(test_set.count()) )
print(str(error))
