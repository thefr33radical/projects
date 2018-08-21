
# Imports the Google Cloud client library
from google.cloud import storage
import json
import glob
import pandas as pd
import os
from StringIO import StringIO

class GcpTransfer(object):
	"""
	Class to transfer files between google cloud 
	"""

    def __init__(self):
	# path to json file which contains google credentials       
        self.client = storage.Client.from_service_account_json("")

    def upload_blob(self, bucket_name, source_file_name, destination_blob_name):
        """
        Function to upload file to GCB

        :param bucket_name: name of bucket on google cloud
        :param source_file_name: local filename
        :param destination_blob_name: destination folder+ filename
        :return: 1 on succcess -1 on failure
    """
        storage_client = self.client
        try:
            bucket = storage_client.get_bucket(bucket_name)
            blob = bucket.blob(destination_blob_name)

            blob.upload_from_filename(source_file_name)

            print('File {} uploaded to {}.'.format(source_file_name, destination_blob_name))
            return 1
        except Exception as e:
            print (e)
            return -1

    def download_blob(self, bucket_name, source_blob_name, destination_file_name):
        """
        Function to download file to GCB

        :param bucket_name: name of bucket on google cloud
        :param source_blob_name: folder+filename
        :param destination_file_name: local filename
        :return: 1 on succcess -1 on failure
    	"""
        storage_client = self.client

        try:
            bucket = storage_client.get_bucket(bucket_name)
            blob = bucket.blob(source_blob_name)
            blob.download_to_filename(destination_file_name)
            print('Blob {} downloaded to {}.'.format(source_blob_name, destination_file_name))
            return 1
        except Exception as e:
            print (e)
            return -1

    def read_csv_file(self, bucket_name, source, dest):
        """
        Function to read csv fiels fom google bucket and return pandas dataframe
        :param source_dir_name:
        :param dest_dir_name:
        :return: pandas dataframe
        """

        storage_client = self.client

        try:
            bucket = storage_client.get_bucket(bucket_name=bucket_name)
            blob = bucket.get_blob(source)

            data = blob.download_as_string()
            dataframe = pd.read_csv(StringIO(data),index_col=False,low_memory=False)
            dataframe.to_csv(dest,index=False)
            return dataframe
        except Exception as e:
            print (e)

if __name__=="__main__":
	pass
	# create instance of class and call the functions
	
