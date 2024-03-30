import redis

redis_endpoint = "[Primary Endpoint]"
redis_port=6379
redis_client = redis.StrictRedis(host=redis_endpoint, port=redis_port, decode_responses=True)

key = "test_key"
value = "test_value"

redis_client.set(key, value)

response = redis_client.get(key)

if response==value:
    print("Connection successful")
else:
    print("connection failed")

