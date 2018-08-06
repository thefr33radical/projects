
# Imports the Google Cloud client library
from google.cloud import storage
import json
import glob
import pandas as pd
import os
from StringIO import StringIO

class GcpTransfer(object):

    def __init__(self):
        self.client = storage.Client.from_service_account_json("/home/kuliza227/works/google-cloud-sdk/gcp_cred.json")

    def upload_blob(self,bucket_name, source_file_name, destination_blob_name):
        """

    :param bucket_name: name of bucket on google cloud
    :param source_file_name: local filename
    :param destination_blob_name: destination folder+ filename
    :return:
    """
        storage_client = self.client
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)

        blob.upload_from_filename(source_file_name)

        print('File {} uploaded to {}.'.format(source_file_name,destination_blob_name))

    def download_blob(self,bucket_name, source_blob_name,destination_file_name):
        """

    :param bucket_name: name of bucket on google cloud
    :param source_blob_name: folder+filename
    :param destination_file_name: local filename
    :return:
    """
        storage_client = self.client
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(source_blob_name)
        blob.download_to_filename(destination_file_name)
        print('Blob {} downloaded to {}.'.format(source_blob_name,destination_file_name))

    def read_json_files(self,bucket_name, source_dir_name, destination_blob_name):
        """

        :param bucket_name:
        :param source_file_name:
        :param destination_blob_name:
        :return:
        """

        storage_client = self.client

        bucket = storage_client.get_bucket(bucket_name=bucket_name)
        blobs = bucket.list_blobs(prefix=source_dir_name)  # Get list of files
        folder = 0


        for i in blobs:
            # Initial folder name to be ignored
            if folder == 0:
                folder =1
                continue
            file_contents = i.download_as_string()
            z = json.loads(file_contents)
           

if __name__=="__main__":
    obj = GcpTransfer()
    for file in glob.glob(os.path.join("/home/kuliza227/github/projects/repo_projects/hyperparameter_tuning/csv_files/","*.json")):
        foldername, filename = os.path.split(file)

        obj.upload_blob("mm_ml_training_data", "/home/kuliza227/github/projects/repo_projects/hyperparameter_tuning/csv_files/"+filename,"phishing_data/"+filename)
    #obj.download_blob("bucket_name", "source_blob_name","destination_file_name")
   # obj.read_json_files("mm_ml_training_data", "feedback_phishing", "")
