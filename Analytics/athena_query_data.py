import boto3
import time


def get_query_execution(athena_client, query, database, output_location):
    response = athena_client.start_query_execution(
        QueryString = query,
        QueryExecutionContext = {
            'Database': database # database in which the query execution occurred
        },
        ResultConfiguration = {
            'OutputLocation':output_location  # location in Amazon S3 where your query and calculation results are stored,
        }
    )
    query_execution_id = response['QueryExecutionId']
    return query_execution_id


def download_file(s3_bucket, s3_key, output_file):
    s3_client = boto3.client('s3', region_name="us-west-1")
    s3_client.download_file(s3_bucket, s3_key, output_file)



def extract_data(athena_client, query_execution_id, output_file):
    while True:
        query_exec = athena_client.get_query_execution(QueryExecutionId=query_execution_id)
        status = query_exec['QueryExecution']['Status']['State']

        if status in ['SUCCEEDED', 'FAILED', 'CANCELLED']:
            break

        time.sleep(1)


    if status == 'SUCCEEDED':
        results_location = query_exec['QueryExecution']['ResultConfiguration']['OutputLocation']
        s3_bucket, s3_key = results_location.replace('s3://', '').split('/',1)
        download_file(s3_bucket, s3_key, output_file)

        # Read and output the file
        print("Output: ")
        with open(output_file, 'r') as file:
            print(file.read())

    else:
        print("Query Execution Failed or Was Cancelled")



def main():
    athena_client = boto3.client('athena', region_name="us-west-1") 
    # The data source is s3 access logs enabled with server access logging on an existing bucket
    # query = 'SELECT COUNT(*) FROM "s3_access_logs_db"."mybucket_logs"';

    query = 'SELECT requesturi_operation, httpstatus, count(*) FROM "s3_access_logs_db"."mybucket_logs" GROUP BY requesturi_operation, httpstatus'
    database = '[database_name]'
    output_location = '[query_result_location]'
    query_execution_id = get_query_execution(athena_client, query, database, output_location)
    print("Query Execution Id: ", query_execution_id)
    
    extract_data(athena_client, query_execution_id, 'query_results.csv')


if __name__ == "__main__":
    main()