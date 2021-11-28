from google.cloud import aiplatform


def create_endpoint(
    project: str,
    display_name: str,
    location: str,
    sync: bool = False,
):
    aiplatform.init(project=project, location=location)

    endpoint = aiplatform.Endpoint.create(
        display_name=display_name,
        project=project,
        location=location,
        sync=sync,
    )
    return {
        "resource_name": endpoint.resource_name,
        "display_name": endpoint.display_name,
    }


def list_endpoints(
    project: str,
    location: str,
    endpoint_name: str,
):
    aiplatform.init(project=project, location=location)

    endpoint = aiplatform.Endpoint.list()
    all_endpoints = []
    for point in endpoint:
        all_endpoints.append(point.resource_name)

    return {"endpoints": all_endpoints}


def delete_endpoint(
    project: str,
    location: str,
    endpoint_name: str,
    force: bool = False,
    sync: bool = False,
):
    aiplatform.init(project=project, location=location)

    endpoint = aiplatform.Endpoint(endpoint_name=endpoint_name)
    endpoint = endpoint.delete(force=force, sync=sync)
    return {
        "resource_name": endpoint.resource_name,
        "display_name": endpoint.display_name,
    }


def all_models_on_endpoint(
    project: str,
    location: str,
    endpoint_name: str,
):
    aiplatform.init(project=project, location=location)

    endpoint = aiplatform.Endpoint(endpoint_name=endpoint_name)
    all_models = endpoint.list_models()
    return {"all_models": all_models}


project_id = "bridgescapture-deloitte"
model_display_name = "image_class_model"
location = "us-central1"
model_id = "6037079698536660992"
