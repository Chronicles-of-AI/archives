from google.cloud import storage

storage_client = storage.Client()

bucket_name = "mlops-triton-models"
destination_blob_name = "audio/test.wav"
# file_path = "/Users/vsatpathy/Desktop/off_POCs/test/server-main/docs/examples/model_repository/intel_image_class/1/model.savedmodel/variables/variables.data-00000-of-00001"
file_path = "/Users/vsatpathy/Documents/Brain Dump/dhiti/childwelfare.wav"

with open(file_path, "rb") as f:
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    url = blob.create_resumable_upload_session()
    print(url)
    resp = blob._initiate_resumable_upload(
        client=storage_client,
        stream=f,
        content_type="application/octet-stream",
        size=None,
        num_retries=1,
    )
    print(resp)
