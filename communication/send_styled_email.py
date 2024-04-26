import boto3
from botocore.exceptions import ClientError

def send_welcome_email(sender, recipient, username):
    ses_client = boto3.client('ses', region_name='us-west-1')
    subject = 'Welcome to Our Service!'
    html_body = """
    <html>
    <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                margin: 0;
                padding: 0;
            }}
            .container {{
                max-width: 600px;
                margin: 50px auto;
                padding: 20px;
                background-color: #fff;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
            }}
            h1 {{
                color: #333;
            }}
            p {{
                color: #666;
                line-height: 1.6;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Welcome to Our Service, {}!</h1>
            <p>Thank you for signing up. We're thrilled to have you as a new member of our community.</p>
            <p>If you have any questions or need assistance, feel free to contact us.</p>
            <p>Best regards,<br/>The Service Team</p>
        </div>
    </body>
    </html>
    """.format(username)

    message = {
        'Subject': {'Data': subject},
        'Body': {'Html': {'Data': html_body}}
    }

    # Try to send the email
    try:
        response = ses_client.send_email(
            Source=sender,
            Destination={'ToAddresses': [recipient]},
            Message=message
        )
        print("Welcome email sent! Message ID:", response['MessageId'])
    except ClientError as e:
        print("Failed to send welcome email:", e.response['Error']['Message'])


sender_email = '[sending-domain]'
recipient_email = '[receipt email]'
new_user = 'Vaishnavi' 

send_welcome_email(sender_email, recipient_email, new_user)
