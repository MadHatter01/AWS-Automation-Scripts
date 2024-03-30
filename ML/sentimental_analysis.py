import boto3



def analyze_sentiment(client):
    feedback = [
    "The new product is amazing! It exceeded my expectations.",
    "Customer service at XYZ Company is terrible. I'll never buy from them again.",
    "The user interface is intuitive and easy to navigate.",
    "Great experience with the support team. They were very helpful.",
    "The delivery was delayed, which was extremely disappointing."
    ]
    
    for text in feedback:
        response = client.detect_sentiment(Text=text, LanguageCode='en')
        sentiment = response['Sentiment']
        confidence_scores = response['SentimentScore']

        # Detect Entities in the text
        entities_response = client.detect_entities(Text=text, LanguageCode='en')
        entities = entities_response['Entities']

        # Show Key Phrases
        phrases_response = client.detect_key_phrases(Text=text, LanguageCode='en')
        phrases = phrases_response['KeyPhrases']

        print("Feedback: ", text)
        print("Sentiment: ", sentiment)
        print("Confidence Scores: ", confidence_scores)
        print("Entities: ", entities)
        print("KeyPhrases: ", phrases)
        print("--------------------------------------")
        


def main():
    client = boto3.client(service_name="comprehend", region_name="us-east-1")
    analyze_sentiment(client)

if __name__ == "__main__":
    main()
