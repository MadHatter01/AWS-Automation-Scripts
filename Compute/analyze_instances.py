import boto3

def get_instance_info(client):
    try:
        response = client.describe_instances()
        instance_info = []

        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                i_id = instance['InstanceId']
                i_type = instance['InstanceType']
                i_platform = instance.get('Platform', 'Linux')
                i_state = instance['State']['Name']

                instance_info.append({
                    'InstanceId':i_id,
                    'InstanceType':i_type,
                    'Platform':i_platform,
                    'State':i_state
                })
        print(instance_info)
        return instance_info

    except Exception as e:
        print(f"Exception: {e}")
        return
    

def parse_instance_info(instance_info):
    if not instance_info:
        print(f"You have no running instances")
        return
    
    total = len(instance_info)
    linux = sum(1 for instance in instance_info if instance['Platform']=='linux')
    windows = sum(1 for instance in instance_info if instance['Platform']=='windows')
    

    running = sum(1 for instance in instance_info if instance['State']=='running')
    stopped = sum(1 for instance in instance_info if instance['State']=='stopped' )

    print("Summary Stats:")
    print(f"Linux Instances: {linux}")
    print(f"Windows Instances: {windows}")
    print(f"Running Instances: {running}")
    print(f"Stopped Instances: {stopped}")
    


def main():
    client = boto3.client('ec2')
    instance_info = get_instance_info(client)
    parse_instance_info(instance_info)
    pass


if __name__=="__main__":
    main()