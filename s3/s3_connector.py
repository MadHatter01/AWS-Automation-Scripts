import boto3

s3_client = boto3.client('s3')

def upload_file_to_s3(file_path, bucket_name, bucket_key):
    try:
        with open(file_path, "rb") as f:
            s3_client.upload_fileobj(f, bucket_name, bucket_key)
            print(f'File uploaded successfully to S3: {bucket_key}')

    except Exception as e:
        print(f'Error uploading file to S3: {e}')


if __name__ == "__main__":
    bucket_name = "[bucket-name]"
    file_path = "picture.png"
    bucket_key = "pictures/picture.png"
    upload_file_to_s3(file_path, bucket_name, bucket_key)
