import boto3


client = boto3.client('textract')

image = "handwriting.jpg"

with open(image, 'rb') as image_file:
    image_data = image_file.read()


res = client.detect_document_text(Document={'Bytes': image_data})

extracted_text = ""
extracted_words = []
for item in res['Blocks']:
    # print(item)
    if item['BlockType'] == 'LINE':
        extracted_text += item['Text'] + '\n'

    if item['BlockType'] == 'WORD':
        extracted_words.append(item['Text'])

print("Extracted Lines: ")
print(extracted_text)

print("--------------------")
print("Extracted Words: ")
print(extracted_words)


# Sample data output
# {'BlockType': 'WORD', 'Confidence': 97.07061767578125, 'Text': 'NOT?', 'TextType': 'HANDWRITING', 'Geometry': {'BoundingBox': {'Width': 0.12239757180213928, 'Height': 0.05005558952689171, 'Left': 0.8416175246238708, 'Top': 0.6270521283149719},
#  'Polygon': [{'X': 0.8416175246238708, 'Y': 0.6278578042984009}, {'X': 0.9636988043785095, 'Y': 0.6270521283149719}, {'X': 0.9640151262283325, 'Y': 0.6762914061546326}, {'X': 0.841968297958374, 'Y': 0.6771076917648315}]}, 'Id': 'f120a6bc-e0a3-4727-993a-1ce2c00eea6a'}
