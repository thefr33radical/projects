
# Imports the Google Cloud client library
from google.cloud import storage


class GcpTransfer(object):

    def __init__(self):
        self.client = storage.Client.from_service_account_json("path to secret key")

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


if __name__=="__main__":
    obj = GcpTransfer()
    obj.upload_blob("bucket_name", "source_blob_name","destination_file_name")
    obj.download_blob("bucket_name", "source_blob_name","destination_file_name")