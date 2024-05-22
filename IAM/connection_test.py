import boto3

def test_connection():
    try:
        iam_client = boto3.client('iam')
        user_info = iam_client.get_user()
        print('User ARN: ', user_info['User']['Arn'])
        print('Connection successful')
    except Exception as e:
        print(f"Connection failed: {str(e)}")

if __name__=="__main__":
    test_connection()