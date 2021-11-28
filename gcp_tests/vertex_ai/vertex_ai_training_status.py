from google.cloud import aiplatform


def get_training_pipeline_sample(
    project: str,
    training_pipeline_id: str,
    location: str = "us-central1",
    api_endpoint: str = "us-central1-aiplatform.googleapis.com",
):
    # The AI Platform services require regional API endpoints.
    client_options = {"api_endpoint": api_endpoint}
    # Initialize client that will be used to create and send requests.
    # This client only needs to be created once, and can be reused for multiple requests.
    client = aiplatform.gapic.PipelineServiceClient(client_options=client_options)
    name = client.training_pipeline_path(
        project=project, location=location, training_pipeline=training_pipeline_id
    )
    response = client.get_training_pipeline(name=name)
    print("response:", response)


project_id = "bridgescapture-deloitte"
location = "us-central1"
pipeline_id = "6427795553513373696"

get_training_pipeline_sample(
    project=project_id, training_pipeline_id=pipeline_id, location=location
)

# Sample Output
# response: name: "projects/307982079966/locations/us-central1/trainingPipelines/5374797665638809600"
# display_name: "text_class_model"
# input_data_config {
#   dataset_id: "7869398234039320576"
#   fraction_split {
#     training_fraction: 0.8
#     validation_fraction: 0.1
#     test_fraction: 0.1
#   }
# }
# training_task_definition: "gs://google-cloud-aiplatform/schema/trainingjob/definition/automl_text_classification_1.0.0.yaml"
# training_task_inputs {
#   struct_value {
#   }
# }
# model_to_upload {
#   display_name: "text_class_model"
# }
# state: PIPELINE_STATE_RUNNING
# create_time {
#   seconds: 1637314306
#   nanos: 208712000
# }
# start_time {
#   seconds: 1637314306
#   nanos: 930052000
# }
# update_time {
#   seconds: 1637314306
#   nanos: 930052000
# }
