from os import name
from google.cloud import aiplatform


def get_model_description(
    project: str,
    model_id: str,
    location: str = "us-central1",
    api_endpoint: str = "us-central1-aiplatform.googleapis.com",
):
    # The AI Platform services require regional API endpoints.
    client_options = {"api_endpoint": api_endpoint}
    # Initialize client that will be used to create and send requests.
    # This client only needs to be created once, and can be reused for multiple requests.

    # client = aiplatform.gapic.DatasetServiceClient(client_options=client_options)
    client = aiplatform.gapic.ModelServiceClient(client_options=client_options)

    name = client.model_path(
        project=project,
        location=location,
        model=model_id,
    )
    response = client.get_model(name=name)
    print("response:", response)


project_id = "bridgescapture-deloitte"
location = "us-central1"
pipeline_id = "369932886188490752"

get_model_description(
    project=project_id,
    model_id=pipeline_id,
    location=location,
)

# Sample Output - For Get Model
# response: name: "projects/307982079966/locations/us-central1/models/369932886188490752"
# display_name: "NLCM"
# metadata_schema_uri: "https://storage.googleapis.com/google-cloud-aiplatform/schema/model/metadata/automl_text_classification_1.0.0.yaml"
# training_pipeline: "projects/307982079966/locations/us-central1/trainingPipelines/6427795553513373696"
# supported_deployment_resources_types: AUTOMATIC_RESOURCES
# supported_input_storage_formats: "jsonl"
# supported_output_storage_formats: "jsonl"
# create_time {
#   seconds: 1637259184
#   nanos: 753750000
# }
# update_time {
#   seconds: 1637278084
#   nanos: 725216000
# }
# etag: "AMEw9yN8gFpT46ojSkrrEugWZFV_UNlQQ3ZXcBOZE9TQCeNB-Vz_N_t99Z2IBXxVVNFl"
