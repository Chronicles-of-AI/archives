import boto3

client = boto3.client("translate")

# Sample language codes
# "es"
# "fr"
# "de"
# "it"
# "pt"


def translate_text(
    text: str,
    source_lang_code: str = "en",
    target_lang_code: str = "es",
):
    response = client.translate_text(
        Text=text,
        SourceLanguageCode=source_lang_code,
        TargetLanguageCode=target_lang_code,
        Settings={"Profanity": "MASK"},
    )
    return response
