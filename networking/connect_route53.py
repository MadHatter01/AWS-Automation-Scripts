import boto3



def list_hosted_zones(client):
    try:
        response = client.list_hosted_zones()

        hosted_zones = response['HostedZones']
        for zone in hosted_zones:
            print("Name:", zone['Name'])
            print("ID:", zone['Id'])
            print("Resource Record Set Count:", zone['ResourceRecordSetCount'])
            print("---------------------------")

    except Exception as e:
        print("Error: ",e)



def main():
    client = boto3.client("route53")
    list_hosted_zones(client)

if __name__=="__main__":
    main()
