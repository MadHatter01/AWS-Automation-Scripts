import boto3

def send_message(client, message, topic):
    response = client.publish(
        TopicArn=topic,
        Message=message
    )
    print(f"Published message: {message}, MessageId: {response['MessageId']}")



def main():
    client = boto3.client('sns');
    message = "Here's your daily subscribed content!"
    topic = "[topic-arn]"
    send_message(client, message, topic)


if __name__=="__main__":
    main()
