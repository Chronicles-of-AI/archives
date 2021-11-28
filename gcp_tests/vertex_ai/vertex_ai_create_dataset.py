from google.cloud import aiplatform


def create_image_dataset(
    project: str,
    location: str,
    display_name: str,
    sync: bool = False,
):
    aiplatform.init(project=project, location=location)

    ds = aiplatform.ImageDataset.create(
        display_name=display_name,
        sync=sync,
    )
    return {"resource_name": ds.resource_name, "dataset_name": ds.display_name}


def create_text_dataset(
    project: str,
    location: str,
    display_name: str,
    sync: bool = False,
):
    aiplatform.init(project=project, location=location)

    ds = aiplatform.TextDataset.create(
        display_name=display_name,
        sync=sync,
    )
    return {"resource_name": ds.resource_name, "dataset_name": ds.display_name}


def create_tabular_dataset(
    project: str,
    location: str,
    display_name: str,
    sync: bool = False,
):
    aiplatform.init(project=project, location=location)

    ds = aiplatform.TabularDataset.create(
        display_name=display_name,
        sync=sync,
    )
    return {"resource_name": ds.resource_name, "dataset_name": ds.display_name}


def create_video_dataset(
    project: str,
    location: str,
    display_name: str,
    sync: bool = False,
):
    aiplatform.init(project=project, location=location)

    ds = aiplatform.VideoDataset.create(
        display_name=display_name,
        sync=sync,
    )
    return {"resource_name": ds.resource_name, "dataset_name": ds.display_name}


def create_time_series_dataset(
    project: str,
    location: str,
    display_name: str,
    sync: bool = False,
):
    aiplatform.init(project=project, location=location)

    ds = aiplatform.TimeSeriesDataset.create(
        display_name=display_name,
        sync=sync,
    )
    return {"resource_name": ds.resource_name, "dataset_name": ds.display_name}


project_id = "bridgescapture-deloitte"
display_name = "text_class_dataset"
location = "us-central1"
# path = "gs://test_bucket_automl_nl/decision_caller_api_maps.csv"
response = create_text_dataset(
    project=project_id,
    location=location,
    display_name=display_name,
)
print(response)
