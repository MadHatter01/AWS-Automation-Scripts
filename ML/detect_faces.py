import boto3

def detect_faces(image, rek_client):
    

    with open(image, 'rb') as img:
        data = img.read()


    res = rek_client.detect_faces(
        Image={
            'Bytes':data,
            
        },
        Attributes=['ALL']
    )

    # print(res)
    if 'FaceDetails' in res:
        print(f"Detected {len(res['FaceDetails'])} faces in the picture")
        for id, face_detail in enumerate(res['FaceDetails'], start=1):
            print(f"Face: {id}")
            print(f"Age Range: {face_detail['AgeRange']['Low']} - {face_detail['AgeRange']['High']} years old")
            print(f"Gender: {face_detail['Gender']['Value']}")
            print(f"Emotions:")
            for emotion in face_detail['Emotions']:
                print(f"{emotion['Type']} : {emotion['Confidence']}%")
            
            print(" ")
    else:
        print(f"No faces detected in the image")

def main():
    rek_client = boto3.client('rekognition')
    image = 'people_picture_unsplash.jpg'
    detect_faces(image, rek_client)

    

if __name__=="__main__":
    main()


# Output
    
# Detected 3 faces in the picture
# Face: 1
# Age Range: 24 - 32 years old
# Gender: Female
# Emotions:
# HAPPY : 100.0%
# ANGRY : 0.0%
# DISGUSTED : 0.0%
# FEAR : 0.0%
# CALM : 0.0%
# SAD : 0.0%
# SURPRISED : 0.0%
# CONFUSED : 0.0%

# Face: 2
# Age Range: 27 - 35 years old
# Gender: Female
# Emotions:
# HAPPY : 100.0%
# CALM : 0.002175569534301758%
# CONFUSED : 5.9604644775390625e-06%
# ANGRY : 0.0%
# DISGUSTED : 0.0%
# FEAR : 0.0%
# SAD : 0.0%
# SURPRISED : 0.0%

# Face: 3
# Age Range: 27 - 35 years old
# Gender: Female
# Emotions:
# HAPPY : 100.0%
# CALM : 1.7881393432617188e-05%
# ANGRY : 0.0%
# DISGUSTED : 0.0%
# FEAR : 0.0%
# SAD : 0.0%
# SURPRISED : 0.0%
# CONFUSED : 0.0%