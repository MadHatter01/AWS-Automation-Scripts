import boto3


ssm_client = boto3.client('ssm', region_name = 'us-west-1')

parameter_name = "/myapp/database/password"

try:
    response = ssm_client.get_parameter(
        Name = parameter_name,
        WithDecryption = True
    )
    parameter_value = response['Parameter']['Value']
    print(parameter_value)
except ssm_client.exceptions.ParameterNotFound as e:
    print("Invalid Parameter")

except Exception as others:
    print(f"Error occured {others}")




