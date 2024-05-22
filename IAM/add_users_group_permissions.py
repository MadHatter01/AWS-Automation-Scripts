import boto3


def create_group(group_name, iam_client):
    try:
        iam_client.create_group(GroupName=group_name)
        print(f"IAM group {group_name} created successfully")

    except iam_client.exceptions.EntityAlreadyExistsException:
        print(f"Group already exists")
    except Exception as e:
        print("Error", e)

def create_user(user_name, iam_client):
    try:
        iam_client.create_user(UserName=user_name)
        print(f"User {user_name} created successfully")

    except iam_client.exceptions.EntityAlreadyExistsException:
        print(f"User name already exists")
    except Exception as e:
        print("Error", e)

def attach_policy_group(group_name, policy_name, iam_client):
    try:
        iam_client.attach_group_policy(GroupName = group_name, PolicyArn = policy_name)
        print(f"Policy attached to the group {group_name}")
    except iam_client.exceptions.NoSuchEntityException:
        print(f"Group '{group_name}' or policy '{policy_name}' not found")
    except iam_client.exceptions.PolicyNotAttachableException:
        print(f"IAM Policy '{policy_name}' cannot be attached to group '{group_name}'")
    except Exception as e:
        print("Error", e)


def add_user_group(user_name, group_name, iam_client):
    try:
        iam_client.add_user_to_group(GroupName = group_name, UserName = user_name)
        print(f"User {user_name} added to the group {group_name} successfully")
    except iam_client.exceptions.NoSuchEntityException:
        print(f"User '{user_name}' or group '{group_name}' not found")
    except Exception as e:
        print("Error", e)




def main():
    iam_client = boto3.client('iam')
    group_name ="Operations"
    policy_name = "arn:aws:iam::aws:policy/ReadOnlyAccess"
    user_name = "jane"

    create_group(group_name, iam_client)
    attach_policy_group(group_name, policy_name, iam_client)
    create_user(user_name, iam_client)
    add_user_group(user_name, group_name, iam_client)

if __name__=="__main__":
    main()