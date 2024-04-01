import boto3
import time

athena_client = boto3.client('athena')

query = 'SELECT COUNT(*) FROM "[database]"."[table]"';

response = athena_client.start_query_execution(
    QueryString = query,
    QueryExecutionContext = {
        'Database': '[database]' # database in which the query execution occurred
    },
    ResultConfiguration = {
        'OutputLocation':'[Output Location]' # location in Amazon S3 where your query and calculation results are stored,
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


print(status)