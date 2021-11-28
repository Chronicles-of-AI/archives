from os import name
from google.cloud import aiplatform


def get_dataset_description(
    project: str,
    dataset_id: str,
    location: str = "us-central1",
    api_endpoint: str = "us-central1-aiplatform.googleapis.com",
):
    # The AI Platform services require regional API endpoints.
    client_options = {"api_endpoint": api_endpoint}
    # Initialize client that will be used to create and send requests.
    # This client only needs to be created once, and can be reused for multiple requests.

    # client = aiplatform.gapic.DatasetServiceClient(client_options=client_options)
    client = aiplatform.gapic.DatasetServiceClient(client_options=client_options)

    name = client.dataset_path()(
        project=project,
        location=location,
        model=dataset_id,
    )
    response = client.get_dataset()(name=name)
    print("response:", response)


project_id = "bridgescapture-deloitte"
location = "us-central1"
pipeline_id = "369932886188490752"

get_dataset_description(
    project=project_id,
    dataset_id=pipeline_id,
    location=location,
)

# Sample Output - For Get dataset
# response: name: "projects/307982079966/locations/us-central1/datasets/699667627265490944"
# display_name: "text_class_dataset_v3"
# metadata_schema_uri: "gs://google-cloud-aiplatform/schema/dataset/metadata/text_1.0.0.yaml"
# create_time {
#   seconds: 1637315191
#   nanos: 572734000
# }
# update_time {
#   seconds: 1637315191
#   nanos: 997781000
# }
# etag: "AMEw9yP2W3-YTxCy8phRPySE_2ZjH7H2lNXYQR6t6xD0mybgMRzxMTuk9EOq6OwCSPu4"
# labels {
#   key: "aiplatform.googleapis.com/dataset_metadata_schema"
#   value: "TEXT"
# }
# metadata {
#   struct_value {
#     fields {
#       key: "dataItemSchemaUri"
#       value {
#         string_value: "gs://google-cloud-aiplatform/schema/dataset/dataitem/text_1.0.0.yaml"
#       }
#     }
#     fields {
#       key: "gcsBucket"
#       value {
#         string_value: "cloud-ai-platform-de238973-f7df-47ad-9b53-ab1992c1a0da"
#       }
#     }
#   }
# }
