from google.cloud import texttospeech

client = texttospeech.TextToSpeechClient()


def synthesize_text(text, audio_output_path):
    """Synthesizes speech from the input string of text."""

    input_text = texttospeech.SynthesisInput(text=text)

    # Note: the voice can also be specified by name.
    # Names of voices can be retrieved with client.list_voices().
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        name="en-US-Standard-C",
        ssml_gender=texttospeech.SsmlVoiceGender.FEMALE,
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        request={"input": input_text, "voice": voice, "audio_config": audio_config}
    )

    # The response's audio_content is binary.
    with open(audio_output_path, "wb") as out:
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')


audio_output_path = "/Users/vsatpathy/Desktop/output.mp3"
sample_text = "Hola, mi nombre es Mark, mi número de identificación de caso es 974-200-2000. En realidad, quería saber cuál es el estado de mi solicitud de Medicaid. Puede devolverme la llamada a mi número de teléfono. gracias"
synthesize_text(text=sample_text, audio_output_path=audio_output_path)
