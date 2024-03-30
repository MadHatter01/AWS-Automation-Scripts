import boto3


# Check the Sample PDF in the folder to see an example of the data available at the source
# I have used an S3 connector at the index. Set up the data sources at the kendra console and copy the index id for usage in the code
# Make sure you are in the right region and the role has sufficient permissions to acess S3 bucket. 
# Also, be sure to sync if you have enabled on demand sync. 


client = boto3.client('kendra', region_name='us-east-1')

query_text = "I need to set up my account for software tools used within the company. How do I do that?"

kendra_index_id = "[Your-Kendra-index-id]"

res = client.query(
    QueryText = query_text,
    IndexId = kendra_index_id
)

for result in res['ResultItems']:
    print('Document ID:', result['DocumentId'])
    print('Score:', result['ScoreAttributes'])
    print('Document Title:', result['DocumentTitle']['Text'])
    print('Document Excerpt:', result['DocumentExcerpt']['Text'])
    print('------------------------------')



# Example output
# Document ID: s3://[bucket-name]/Important Links.pdf
# Score: {'ScoreConfidence': 'HIGH'}
# Document Title: Important Links.pdf
# Document Excerpt: IT Support - Need technical assistance with your computer, software, or network access? Reach
# out to our IT support team via email at: it@ AwesomeCompanyThatDoesNotExist.com.


# Manager Contacts - Find contact information for your direct manager and other team leaders at:
# https://www. AwesomeCompa
# ------------------------------
# Document ID: s3://[bucket-name]/Important Links.pdf
# Score: {'ScoreConfidence': 'MEDIUM'}
# Document Title: Important Links.pdf
# Document Excerpt: ...Tasks
# Email Account Setup - Follow the step-by-step instructions to set up your company email account.
# Access the guide at: https://www.AwesomeCompanyThatDoesNotExist.com/email-setup.


# Software Accounts - Set up your accounts for essential software tools used within the company...
# ------------------------------