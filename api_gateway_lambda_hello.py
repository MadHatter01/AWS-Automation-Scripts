import boto3

lambda_client = boto3.client('lambda')
apigateway_client = boto3.client('apigateway')

function_name = 'TestAPIG'
try:
    function_response = lambda_client.get_function(FunctionName=function_name)
    function_arn = function_response['Configuration']['FunctionArn']
    print("Lambda function ARN:", function_arn)
except lambda_client.exceptions.ResourceNotFoundException:
    print(f"The Lambda function '{function_name}' does not exist.")
except Exception as e:
    print("Error:", e)


# Add necessary invoke permissions to the execution role so that it can invoke lambda 

api_response = apigateway_client.create_rest_api(name='MySimpleAPI')
api_id = api_response['id']

root_resource_response = apigateway_client.get_resources(restApiId=api_id, limit=500)
root_resource = next(resource for resource in root_resource_response['items'] if resource['path'] == '/')
parent_resource_id = root_resource['id']

resource_response = apigateway_client.create_resource(
    restApiId=api_id,
    parentId=parent_resource_id,
    pathPart='hello'
)
resource_id = resource_response['id']

method_response = apigateway_client.put_method(
    restApiId=api_id,
    resourceId=resource_id,
    httpMethod='GET',
    authorizationType='NONE'
)

integration_uri = f"arn:aws:apigateway:us-west-1:lambda:path/2015-03-31/functions/{function_arn}/invocations"

integration_response = apigateway_client.put_integration(
    restApiId=api_id,
    resourceId=resource_id,
    httpMethod='GET',
    type='AWS_PROXY',
    integrationHttpMethod='POST',
    uri=integration_uri
)

deployment_response = apigateway_client.create_deployment(
    restApiId=api_id,
    stageName='prod'
)

print("API URL:", f"https://{api_id}.execute-api.us-east-1.amazonaws.com/prod/hello")
