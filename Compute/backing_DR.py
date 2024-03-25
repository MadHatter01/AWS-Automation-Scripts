import boto3
import datetime

def create_snapshot(description, volume_id):
    ec2_client = boto3.client('ec2')

    try:
        res = ec2_client.create_snapshot(
            Description = description,
            VolumeId = volume_id
        )
        s_id = res['SnapshotId']
        print(f"Snapshot created successfully : {s_id}")
        return s_id
    except Exception as e:
        print(f"Error occured {e}")
        return 
    

def copy_snapshot(s_id, source, destination):
    ec2_client = boto3.client('ec2')
    try:
        res = ec2_client.copy_snapshot(
            SourceSnapshotId = s_id,
            SourceRegion = source,
            DestinationRegion = destination,
            Description=f"Copy of snapshot {s_id} from {source}"
        )

        copy_id = res['SnapshotId']

        print(f"Snapshot copied to {destination} from {source}")
        return copy_id
    except Exception as e:
        print(f"Error occured {e}")


def main():
    source = 'us-east-1'
    destination='us-west-1'
    today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ec2_client = boto3.client('ec2')
    res = ec2_client.describe_instances()

    for reservation in res['Reservations']:
        for instance in reservation['Instances']:
            i_id = instance['InstanceId']
            print(f"Instance ID: {i_id}")
            # print(instance)
            for device in instance['BlockDeviceMappings']:

                if 'Ebs' in device:
                    v_id = device['Ebs']['VolumeId']
                    s_description = f"Created snapshot on {today}"
                    s_id = create_snapshot(s_description, v_id)

                    if s_id:
                        copy_snapshot(s_id, source, destination)

if __name__=="__main__":
    main()