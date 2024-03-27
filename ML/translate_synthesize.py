import boto3


def translate_text(source_text, source_lang, target_lang):
    t_client = boto3.client('translate', region_name = 'us-east-1')
    params = {
        'Text' : source_text,
        'SourceLanguageCode' : source_lang,
        'TargetLanguageCode' :target_lang,
        'Settings': {
            'Formality' :'INFORMAL',
            'Profanity':'MASK'
        }
   }
    translate_text = t_client.translate_text(**params)
    return translate_text['TranslatedText']


def synthesize_speech(text, lang_code, voice_id, output_format):
    p_client = boto3.client('polly', region_name ='us-east-1') 
    params = {
        'Engine':'neural',
        'Text':text,
        'OutputFormat':output_format,
        'VoiceId':voice_id,
        'LanguageCode': lang_code
    }

    stream = p_client.synthesize_speech(**params)['AudioStream'].read()
    with open('synthesized_speech.'+output_format, 'wb') as f:
        f.write(stream)


def main():
    source_text = "Hello, How are you doing? The weather looks great today"
    source_lang = "en"
    target_lang_tamil = "ta"
    target_lang_hindi="hi"

    print("Translated Text in Tamil")
    translated_text_tamil = translate_text(source_text, source_lang, target_lang_tamil)
    print(translated_text_tamil)
    print("")
    print("Translated Text in Hindi")
    translated_text_hindi = translate_text(source_text, source_lang, target_lang_hindi)
    print(translated_text_hindi)

    voice_id = 'Kajal' #Neural is supported for this voice (https://docs.aws.amazon.com/polly/latest/dg/ntts-voices-main.html)
    output_format = 'mp3'

    lang_code_polly = "hi-IN" #Tamil is not supported
    print('Converted to speech in Hindi')
    synthesize_speech(translated_text_hindi, lang_code_polly, voice_id, output_format)

if __name__=="__main__":
    main()