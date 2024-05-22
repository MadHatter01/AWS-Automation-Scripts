import boto3
import datetime
import json

# subscribe an existing sqs to an sns topic

def create_sqs_subscription(sns_client, topic_arn, queue_arn):
    sqs_subscription = sns_client.subscribe(
        TopicArn = topic_arn, 
        Protocol = 'sqs',
        Endpoint = queue_arn
    )
    print(f"SQS Subscription successful. Subscription Arn: {sqs_subscription['SubscriptionArn']}")

# you have to explicitly confirm email subscription to receive emails. Use an existing subscription
def create_email_subscription(sns_client, topic_arn, email_address):
    email_subscription = sns_client.subscribe(
        TopicArn = topic_arn, 
        Protocol = 'email',
        Endpoint = email_address
    )
    print(f"Email Subscription successful. Subscription Arn: {email_subscription['SubscriptionArn']}")


def simulate_activity(sns_client, topic_arn):
    user_activity = {
        'event_type':'Order Placement',
        'user_id':'Jane123',
        'timestamp':datetime.datetime.utcnow().isoformat(),
        'details':'Order for Shoes Model X placed'

    }
    response = sns_client.publish(
        TopicArn = topic_arn, 
        Message = json.dumps(user_activity)
    )
    print(f"Published Message to subscribers (SQS, Email)", response)


def main():
    sns_client = boto3.client('sns')
    queue_arn = "[queue arn]"
    email_address="[email]"
    topic_arn = "[topic arn]"
    create_sqs_subscription(sns_client, topic_arn, queue_arn)
    create_email_subscription(sns_client, topic_arn, email_address)

    simulate_activity(sns_client, topic_arn)


if __name__=="__main__":
    main()


