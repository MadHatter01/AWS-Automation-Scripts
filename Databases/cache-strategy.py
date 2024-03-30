import json
import redis


# Tested on EC2 instance connect. Make sure to add ssh in the security group. 

class CacheManager:
    def __init__(self, cache_endpoint):
        self.client = redis.StrictRedis(host = cache_endpoint, port=6379, decode_responses=True)
        self.cache_endpoint = cache_endpoint

    
    def simulate_get_data_db(self, key):
        print(f"Fetching data from database for key: {key} ")

        sample_data = {
            "userid1":{"name":"Jane Doe"},
            "userid2":{"name":"Michael Scott"},
            "userid3":{"name":"Sesshomaru"},
            "userid4":{"name" :"Saber Lily"}
        }

        if key in sample_data:
            return sample_data[key]
        else:
            return None
        

    def fetch_data_cache(self, key):
        res = self.client.get(key)
        if res:
            return json.loads(res)
        else:
            print("no cache")
            return None

    def write_to_cache(self, key, data):
        print("Writing data to cache for key: ", key)
        self.client.set(key, json.dumps(data))


    #Lazy loading strategy
    def get_data(self, key):
        cache_available = self.fetch_data_cache(key)
        if cache_available:
            print("Data found in cache for key: ", key)
            return cache_available
        
        else:
            print("Data not found in cache, fetching from DB")
            data = self.simulate_get_data_db(key)
            if data:
                self.write_to_cache(key, data)
                print("data loaded into cache - lazy loading for key: ", key)
                return data



def main():
    cache_endpoint = "[Primary endpoint Redis]" #Don't include the port number in the endpoint link
    cache_manager = CacheManager(cache_endpoint)
    cache=cache_manager.get_data("userid2")
    print(cache)


if __name__ == "__main__":
    main()