import boto3
import signal
import sys
import time

def receive_message(client, queue_url):
    response = client.receive_message(
        QueueUrl = queue_url,
        MaxNumberOfMessages = 1,
        WaitTimeSeconds= 5, #Long Polling
        VisibilityTimeout=30 #Message visibility timeout
    )

    if 'Messages' in response:
        message = response['Messages'][0]
        receipt_handle = message['ReceiptHandle']
        body = message['Body']
        print(f"Received message: {body}, Receipt Handle: {receipt_handle}")


        client.delete_message(
            QueueUrl = queue_url,
            ReceiptHandle = receipt_handle
        )

        print(f"Deleted the message: {body}. Will not be reprocessed again.")

def main():
    client = boto3.client('sqs')
    queue_url = "[queue url]"

    try:
        while True:
            receive_message(client, queue_url)
            time.sleep(2)
    except KeyboardInterrupt:
        print("Interrupted")

        
    

if __name__== "__main__":
    main()