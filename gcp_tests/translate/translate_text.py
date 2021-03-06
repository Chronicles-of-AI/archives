import six
from google.cloud import translate_v2 as translate

translate_client = translate.Client()


def translate_text(target, text):
    """Translates text into the target language.

    Target must be an ISO 639-1 language code.
    See https://g.co/cloud/translate/v2/translate-reference#supported_languages
    """

    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.translate(text, target_language=target)

    print(u"Text: {}".format(result["input"]))
    print(u"Translation: {}".format(result["translatedText"]))
    print(u"Detected source language: {}".format(result["detectedSourceLanguage"]))


sample_text = "hey hi my name is Mark my case ID is 974-200-2000 actually wanted to know what is the status of my Medicaid application you can call me back on my phone number my number is 900-377-9537 or 5 p.m. would be good thank you"
translate_text(target="es", text=sample_text)
