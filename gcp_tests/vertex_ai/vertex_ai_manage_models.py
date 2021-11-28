from typing import Optional
from google.cloud import aiplatform


def deploy_model(
    project,
    location,
    model_id: str,
    traffic_percentage: Optional[int] = 100,
    min_replica_count: int = 1,
    max_replica_count: int = 1,
    sync: bool = False,
):

    aiplatform.init(project=project, location=location)
    model_name = f"projects/{project}/locations/{location}/models/{model_id}"
    model = aiplatform.Model(model_name=model_name)

    response = model.deploy(
        deployed_model_display_name=model_name,
        traffic_percentage=traffic_percentage,
        min_replica_count=min_replica_count,
        max_replica_count=max_replica_count,
        sync=sync,
    )
    return {"response": response.resource_name}


def undeploy_model(
    project: str,
    location: str,
    endpoint_name: str,
    model_id: str,
):
    aiplatform.init(project=project, location=location)

    endpoint = aiplatform.Endpoint(endpoint_name=endpoint_name)
    _ = endpoint.undeploy(deployed_model_id=model_id)
    return {"model_id": model_id, "endpoint_name": endpoint_name}


def delete_model(
    project,
    location,
    model_id: str,
    sync: bool = False,
):

    aiplatform.init(project=project, location=location)
    model_name = f"projects/{project}/locations/{location}/models/{model_id}"
    model = aiplatform.Model(model_name=model_name)

    response = model.delete(sync=sync)
    return {"response": response.resource_name}


def list_models(
    project,
    location,
    model_id: str,
):

    aiplatform.init(project=project, location=location)
    model_name = f"projects/{project}/locations/{location}/models/{model_id}"
    model = aiplatform.Model(model_name=model_name)

    response = model.list()
    return {"response": response}


def export_model(
    project,
    location,
    model_id: str,
    export_format_id: str,
    gcs_path: str,
    sync: bool = False,
):
    # Supported Export Formats -
    # tflite
    # edgetpu-tflite
    # tf-saved-model
    # core-ml
    # tf-js

    aiplatform.init(project=project, location=location)
    model_name = f"projects/{project}/locations/{location}/models/{model_id}"
    model = aiplatform.Model(model_name=model_name)

    response = model.export_model(
        export_format_id=export_format_id,
        artifact_destination=gcs_path,
        sync=sync,
    )
    response = model.list()
    return {"response": response}


project_id = "bridgescapture-deloitte"
model_display_name = "image_class_model"
location = "us-central1"
model_id = "6037079698536660992"

resp = deploy_model(
    project=project_id,
    location=location,
    model_id=model_id,
)
print(resp)
