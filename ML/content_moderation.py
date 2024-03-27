import boto3


def moderate_content(client, image):
    with open(image, 'rb') as img:
        data = img.read()


    res = client.detect_moderation_labels(
        Image={
            'Bytes':data
        }
    )

    if 'ModerationLabels' in res:
        print("Moderation Labels Detected")
        for label in res['ModerationLabels']:
            print(f"{label['Name']} (Confidence: {label['Confidence']}%)")
    else:
        print(f"No moderation labels detected in this image")


def main():
    client = boto3.client('rekognition')
    image = 'unmoderated_content.jpg' # Add any unmoderated content picture 
    moderate_content(client, image)

if __name__=="__main__":
    main()


# Example Output
# Moderation Labels Detected
# Attribute1 or Attribute2 (Confidence: 96.24819946289062%)
# Attribute3 or Attribute4 (Confidence: 96.24819946289062%)