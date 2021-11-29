import boto3

client = boto3.client("comprehend")

# Sample language codes
# "es"
# "fr"
# "de"
# "it"
# "pt"


def detect_dominant_language(text: str):
    response = client.detect_dominant_language(Text=text)
    return response


def detect_entities(text: str, lang_code: str = "en"):
    response = client.detect_entities(
        Text=text,
        LanguageCode=lang_code,
    )
    return response


def detect_pii_entities(text: str, lang_code: str = "en"):
    response = client.detect_pii_entities(
        Text=text,
        LanguageCode=lang_code,
    )
    return response


def detect_sentiment(text: str, lang_code: str = "en"):
    response = client.detect_sentiment(
        Text=text,
        LanguageCode=lang_code,
    )
    return response


def detect_syntax(text: str, lang_code: str = "en"):
    response = client.detect_syntax(
        Text=text,
        LanguageCode=lang_code,
    )
    return response
