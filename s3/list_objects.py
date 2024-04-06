import boto3

def list_objects(bucket_name, s3_client):
    try:
        response = s3_client.list_objects_v2(Bucket = bucket_name)

        total_size = 0
        most_recent = None
        most_recent_date = None

        if 'Contents' in response:
            print("Images stored in the bucket: ")

            for obj in response['Contents']:
                file_key = obj['Key']
                size = obj['Size']
                last_modified = obj['LastModified']

                total_size += size

                if most_recent_date is None or last_modified > most_recent_date:
                    most_recent = file_key
                    most_recent_date = last_modified

                print(f"File Key: {file_key}, Size: {size} bytes, Last Modified: {last_modified}")
            
            print(f"Total number of images: {len(response['Contents'])}")
            print(f"Total size of all images: {total_size} bytes")
            print(f"Most recent image: {most_recent}, Last Modified: {most_recent_date}")
        else:
            print("No images found in the bucket.")
    except Exception as e:
        print(f"Error listing images: {e}")


def main():
    s3_client = boto3.client('s3')
    list_objects('[Bucket Name]', s3_client)

if __name__ == "__main__":
    main()