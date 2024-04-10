import boto3

s3_client = boto3.client('s3')

def upload_image_s3(file_path, bucket_name):
    key = "[key-name]"

    try:
        s3_client.upload_file(file_path, bucket_name, key)
        print(f"Image uploaded successfully to S3 with key: {key}")
        return key
    
    except Exception as e:
        print(f"Error uploading image to S3: {e}")
        return None
    

def generate_presigned_url(bucket_name, key):
    try:
        url = s3_client.generate_presigned_url(
            'get_object',
            Params={'Bucket': bucket_name, 'Key': key},
            ExpiresIn=3600
        )
        print(f"Pre-signed URL generated successfully: {url}")
        return url
    except Exception as e:
        print(f"Error generating pre-signed URL: {e}")
        return None
    
if __name__=="__main__":
    file_path = 'picture.png'
    bucket_name = '[bucket-name]'
    image_key = upload_image_s3(file_path, bucket_name)
    if image_key:
        presigned_url = generate_presigned_url(bucket_name, image_key)
        if presigned_url:
            print(f"Access the image at: {presigned_url}")
        else:
            print("Failed to generate pre-signed URL.")
    else:
        print("Failed to upload image to S3.")