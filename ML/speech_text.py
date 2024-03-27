import boto3
import time

def start_transcribing(client, input_file, output_file):
    job = "Redact_PII_speech3"
    params = {
        'TranscriptionJobName': job,
        'LanguageCode':"en-US",
        'Media':{
            'MediaFileUri':f'{input_file}'
        },
        'OutputBucketName':f'{output_file}',
           'ContentRedaction':{
        'RedactionType': 'PII',
        'RedactionOutput': 'redacted',
        'PiiEntityTypes': ['ALL']

    }
    }
    res = client.start_transcription_job(**params)

    print('Transcription Job Started')
    print(res)



    while True:
        status = client.get_transcription_job(TranscriptionJobName=job)
        print(status)
        if status['TranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
            break
        time.sleep(5)

    if status['TranscriptionJob']['TranscriptionJobStatus'] == 'COMPLETED':
        print(status['TranscriptionJob']['Transcript'])
        print(f"Transcription saved to {output_file}")
    else:
        print("Transcription Job Failed")


def main():
    input_file = '[s3 Recording URI]'
    output_file='[Bucket Name]'
    client = boto3.client('transcribe', region_name="us-west-1") #Make sure you start the transcription job from same region as the bucket
    start_transcribing(client, input_file, output_file)


if __name__=="__main__":
    main()