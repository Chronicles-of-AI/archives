import boto3

client = boto3.client("transcribe")

# response = client.start_transcription_job(
#     TranscriptionJobName="REe95ffe2fea57a6ccf1429859a5fdf429",
#     MediaFormat="wav",
#     Media={
#         "MediaFileUri": "s3://dhiti-audio-dataset/source/REe95ffe2fea57a6ccf1429859a5fdf429.wav"
#     },
#     OutputBucketName="dhiti-audio-dataset",
#     OutputKey="transcribe/",
#     IdentifyLanguage=True,
# )
# print(response)

response = client.delete_transcription_job(
    TranscriptionJobName="childwelfare_ism_ind.wav"
)
