import boto3

s3_client = boto3.client('s3')

bucket_name = "[bucket name]"
object_key = "sampledata.csv"

# sql_query = "SELECT * from S3Object s"
sql_query = "SELECT Name, Email FROM S3Object s WHERE s.Age > '30' AND s.City LIKE 'S%'"

def s3_select(bucket_name, object_key, sql_query):
    try:
        response = s3_client.select_object_content(
            Bucket=bucket_name,
            Key=object_key,
            ExpressionType='SQL',
            Expression=sql_query,
            InputSerialization={'CSV': {'FileHeaderInfo': 'USE'}},
            OutputSerialization={'CSV': {}}
        )

        for event in response['Payload']:
            if 'Records' in event:
                records = event['Records']['Payload'].decode('utf-8')
                print(records)
            elif 'Stats' in event:
                stats_details = event['Stats']['Details']
                print("Bytes scanned:", stats_details['BytesScanned'])
                print("Bytes processed:", stats_details['BytesProcessed'])

    except Exception as e:
        print(f"Error performing S3 Select: {e}")

s3_select(bucket_name, object_key, sql_query)