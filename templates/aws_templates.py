

import boto3
from s3fs.core import S3FileSystem

import io
import pandas as pd
from  credentials import ACCESS_KEY,SECRET_KEY,REGION,bucket_name,aws_folder
s3_client = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY, region_name=REGION)

class AwsTransfer(object):
	def upload_to_s3_folder():
	    """
	    Function which generates a presigned url for uploading files

	    :param folder_path: Folder from which files needs to be uploaded to S3
	    :return: 0 on failure 1 on success
	    """
    	    try:
        	url = s3_client.generate_presigned_url('put_object', Params={'Bucket': bucket_name, 'Key':aws_folder},
                                        ExpiresIn=3600, HttpMethod='PUT')
    	    except Exception as e:
        	print(e)
        return {"url": None}


	def download_file_s3(file_name):
        """
        Function to download CSV files from S3 into dataframe
        :param file_name:
        :return: pandas data frame of CSV file
        """
        	try:
            obj = s3_client.get_object(Bucket=bucket_name,Key=aws_folder+file_name)
            body = obj['Body']
            csv_string = body.read().decode('utf-8')
            data = pd.read_csv(io.StringIO(csv_string))
            return data
        except Exception as e:
            print(e)


if __name__=="__main__":
    upload_to_s3_folder()
    download_file_s3("dataset.csv")
