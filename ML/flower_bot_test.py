import boto3

lex_client = boto3.client('lexv2-runtime', region_name ="us-east-1")

print("Hi, this is Flower Bot. How can I help you?") 

# This bot is pretty limited in what it can do because it's a test exanple

# Make sure you use lexv2 runtime. lex is supported only in few regions so change the region name accordingly

user_input = input("You: ")

response = lex_client.recognize_text(
    botId="[add your bot id]",
    botAliasId ="[add your alias id]", #Make sure you create a alias version and add the ID here. Default test alias "TestBotAlias" is only for development
    text = user_input,
    localeId="en_US",
    sessionId="Jane123"

)

lex_response = response['messages'][0]['content']


print("Flower Bot: " + lex_response)
