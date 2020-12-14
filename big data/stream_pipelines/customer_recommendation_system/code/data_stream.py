from kafka import KafkaConsumer, KafkaProducer
import pandas as pd
import time
import json
class Data:
    def __init__(self):
        """
        Constructor to set parameters
        """
        self.KAFKA_TOPIC_NAME = "customers"
        self.KAFKA_BOOTSTRAP_SERVER_CONN = "192.168.99.100:9092"
        pass

    def create_stream(self,path):
        """
        Function to create streams from features generated from twitter
        :param path: str
        :return: None
        """
        kafka_producer_object = KafkaProducer(bootstrap_servers=self.KAFKA_BOOTSTRAP_SERVER_CONN,
              value_serializer=lambda x: json.dumps(x).encode('utf-8'))

        df = pd.read_csv(path)
        data= df.to_dict(orient="records")

        for data_point in data:
            kafka_producer_object.send(self.KAFKA_TOPIC_NAME,data_point)
            time.sleep(0.05)