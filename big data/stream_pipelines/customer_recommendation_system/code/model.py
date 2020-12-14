from pyspark.ml.recommendation import ALS
import trans_detail_write_stream from data_consumer
trainingDF=trans_detail_write_stream[:-100]
testDF=trans_detail_write_stream[-100:]
als = (ALS()
       .setUserCol("userId")
       .setItemCol("no_of_chars")
       .setRatingCol("seniment_score")
       .setPredictionCol("predictions")
       .setMaxIter(2)
       .setSeed(0)
       .setRegParam(0.1)
       .setColdStartStrategy("drop")
       .setRank(12))
alsModel = als.fit(trainingDF)

from pyspark.ml.evaluation import RegressionEvaluator
regEval = RegressionEvaluator(predictionCol="predictions", labelCol="rating", metricName="mse")

predictedTestDF = alsModel.transform(testDF)
testMse = regEval.evaluate(predictedTestDF)