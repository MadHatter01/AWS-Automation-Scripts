import boto3
import datetime

def create_db_snapshot(client, db_instance_id, snapshot_id):
    
    try:
        res = client.create_db_snapshot(
            DBSnapshotIdentifier = snapshot_id,
            DBInstanceIdentifier=db_instance_id
        )

        print("Snapshot creation initiated successfully")
        print("Snapshot ID:", res['DBSnapshot']['DBSnapshotIdentifier'])
        print("Snapshot creation status: ", res['DBSnapshot']['Status'])

    except client.exceptions.DBInstanceNotFoundFault:
        print(f"DB Instance not found")
    except client.exceptions.DBSnapshotAlreadyExistsFault:
        print(f"DB snapshot already exists. Try a different id")
    except Exception as e:
        print(f"Error occured: {str(e)}")

def getInstances(client):
    try:
        response = client.describe_db_instances()

        for db_instance in response['DBInstances']:
            print("DB Instance Identifier:", db_instance['DBInstanceIdentifier'])
    except Exception as e:
        print("Error: ", str(e))

def main():
    client = boto3.client('rds', region_name = "us-west-1") #Make sure you are in the right region as the RDS instance

    # Retrieve available database instance ids
    # getInstances(client)

    db_instance_id = '[database_identifier]' # Add your database name
    snapshot_id = 'backup'+datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S');
    create_db_snapshot(client, db_instance_id, snapshot_id)

if __name__=="__main__":
    main()