import boto3
import time

athena_client = boto3.client('athena', region_name="us-west-1")

query = 'SELECT COUNT(*) FROM "s3_access_logs_db"."mybucket_logs"';

response = athena_client.start_query_execution(
    QueryString = query,
    QueryExecutionContext = {
        'Database': '' # database in which the query execution occurred
    },
    ResultConfiguration = {
        'OutputLocation':'' # location in Amazon S3 where your query and calculation results are stored,
    }
)

query_execution_id = response['QueryExecutionId']
print(query_execution_id)


while True:
    query_exec = athena_client.get_query_execution(QueryExecutionId=query_execution_id)
    status = query_exec['QueryExecution']['Status']['State']

    if status in ['SUCCEEDED', 'FAILED', 'CANCELLED']:
        break

    time.sleep(1)


if status == 'SUCCEEDED':
    results_location = query_exec['QueryExecution']['ResultConfiguration']['OutputLocation']
    s3_bucket, s3_key = results_location.replace('s3://', '').split('/',1)

    print(s3_bucket, s3_key)

    s3_client = boto3.client('s3', region_name="us-west-1")
    s3_client.download_file(s3_bucket, s3_key, 'query_results.csv')

    with open('query_results.csv', 'r') as file:
        print(file.read())

else:
    print("Query Execution Failed or Was Cancelled")