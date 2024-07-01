import boto3
import os

aws_access_key_id="/"
aws_secret_access_key="/"
aws_session_token="///////////"
region_name="us-east-1"
 
s3_client = boto3.client(
    's3',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    aws_session_token=aws_session_token,
    region_name=region_name
)

bucket_name = 'dic-bucket-for-uni-123'

def upload_image(image_path):
    image_name = os.path.basename(image_path)
    s3_client.upload_file(image_path, bucket_name, image_name)
    print(f"Uploaded {image_name} to {bucket_name}")

if __name__ == '__main__':
    upload_image('input_folder/000000000016.jpg')