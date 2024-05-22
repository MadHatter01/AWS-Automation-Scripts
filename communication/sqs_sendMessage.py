import boto3

def send_message(sqs_client, queue_url, message):
    response = sqs_client.send_message(
        QueueUrl = queue_url,
        MessageBody = message,
        DelaySeconds=100
    )
    print(f"Sent message: {message}, MessageId: {response['MessageId']}")

def main():
    sqs_client = boto3.client('sqs')
    queue_url = "[queue url]"
    message = "Hello world"
    send_message(sqs_client, queue_url, message)

if __name__ == "__main__":
    main()
