import hashlib
url_mappings = {}

def lambda_handler(event, context):
    long_url = event['body']
    short_url = hashlib.sha256(long_url.encode()).hexdigest()[:8]
    url_mappings[short_url] = long_url
    
    return {
        'statusCode': 200,
        'body': short_url
    }