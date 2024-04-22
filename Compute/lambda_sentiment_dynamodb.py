import json
import boto3

comprehend_client = boto3.client('comprehend', region_name='us-east-1')
dynamo_client = boto3.resource('dynamodb', region_name='us-east-1')
sns_client = boto3.client('sns', region_name='us-east-1')

table_name = "ProductReviews"
table = dynamo_client.Table(table_name)


# Lambda function that stores product reviews to dynamodb. When negative review is received, it will send an SNS notification. Sentiment analysis is performed by comprehend.


def lambda_handler(event, context):
    print(event['review_id'], event['review_text'])
    review_text = event['review_text']
    
    response = comprehend_client.detect_sentiment(Text=review_text, LanguageCode='en')
    sentiment = response['Sentiment']
    
    table.put_item(Item = {"ReveiwID": event['review_id'],"ReviewText":  review_text,"Sentiment": sentiment})
    
    if sentiment == 'NEGATIVE':
        sns_client.publish(TopicArn='[topic-arn]', Message=f"Negative review detected:\n{review_text}",Subject='Negative Review Alert')
    
   

    return {
        'statusCode': 200,
        'body': json.dumps(sentiment)
    }
