import boto3


client = boto3.client('ses')

def send_email(sender, recipient, subject, body):
    try:
        response = client.send_email(
            Source=sender,
            Destination = {'ToAddresses':[recipient]},
            Message = {
                'Subject':{'Data':subject},
                'Body':{'Text':{'Data':body}}
            }
        )

        print("Email sent successfully")
        print("Message ID: ", response['MessageId'])


    except Exception as e:
        print("Error: ", e)


sender = '[email]'
recipient = '[email]'
subject = 'Test Email'
body = 'This is a test email sent through Amazon SES.'
send_email(sender, recipient, subject, body)

