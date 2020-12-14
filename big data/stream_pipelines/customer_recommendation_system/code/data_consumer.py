
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

KAFKA_TOPIC_NAME_CONS = "customers"
KAFKA_OUTPUT_TOPIC_NAME_CONS = "customer_rec"
KAFKA_BOOTSTRAP_SERVERS_CONS = '192.168.99.100:9092'

if __name__ == "__main__":

    spark = SparkSession \
             .builder \
             .appName("PySpark Structured Streaming with Kafka Demo") \
             .config("spark.jars", "spark-sql-kafka-0-10_2.12-3.0.0-preview.jar,kafka-clients-2.4.1.jar") \
             .config("spark.executor.extraClassPath", "spark-sql-kafka-0-10_2.12-3.0.0-preview.jar,kafka-clients-2.4.1.jar") \
            .config("spark.executor.extraLibrary", "spark-sql-kafka-0-10_2.12-3.0.0-preview.jar,kafka-clients-2.4.1.jar") \
            .config("spark.driver.extraClassPath", "spark-sql-kafka-0-10_2.12-3.0.0-preview.jar,kafka-clients-2.4.1.jar") \
            .getOrCreate()

    spark.sparkContext.setLogLevel("ERROR")
    print(" kafka Started ...")
    # Construct a streaming DataFrame that reads from testtopic
    transaction_detail_df = spark \
        .readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers",KAFKA_BOOTSTRAP_SERVERS_CONS) \
        .option("subscribe", KAFKA_TOPIC_NAME_CONS) \
        .option("startingOffsets", "latest") \
        .load()

    print("Printing Schema of transaction_detail_df: ")
    transaction_detail_df.printSchema()
    # Write final result into console for debugging purpose
    trans_detail_write_stream = transaction_detail_df \
       .writeStream \
        .trigger(processingTime='1 seconds') \
        .outputMode("update") \
        .option("truncate", "false")\
        .format("console") \
        .start()
    trans_detail_write_stream.awaitTermination()
    spark.stop()





