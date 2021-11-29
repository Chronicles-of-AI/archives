from google.cloud import speech
import io

client = speech.SpeechClient()


def transcribe_file(speech_file):
    """Transcribe the given audio file."""

    with io.open(speech_file, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        language_code="en-US",
        enable_automatic_punctuation=True,
    )

    response = client.recognize(config=config, audio=audio)

    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    for result in response.results:
        # The first alternative is the most likely one for this portion.
        print(u"Transcript: {}".format(result.alternatives[0].transcript))

    return {"transcript": result.alternatives[0].transcript}


def transcribe_gcs(gcs_uri):
    """Transcribes the audio file specified by the gcs_uri."""

    audio = speech.RecognitionAudio(uri=gcs_uri)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        language_code="en-US",
        enable_automatic_punctuation=True,
    )

    response = client.recognize(config=config, audio=audio)

    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    for result in response.results:
        # The first alternative is the most likely one for this portion.
        print(u"Transcript: {}".format(result.alternatives[0].transcript))


audio_path = "/Users/vsatpathy/Documents/Brain Dump/dhiti/short_audio.wav"
response = transcribe_file(speech_file=audio_path)
