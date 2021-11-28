from google.cloud import aiplatform


def delete_image_dataset(
    project: str,
    location: str,
    display_name: str,
    sync: bool = False,
):
    aiplatform.init(project=project, location=location)

    ds = aiplatform.ImageDataset(dataset_name=display_name)
    ds = ds.delete(sync=sync)
    return {"resource_name": ds.resource_name, "dataset_name": ds.display_name}


def delete_text_dataset(
    project: str,
    location: str,
    display_name: str,
    sync: bool = False,
):
    aiplatform.init(project=project, location=location)

    ds = aiplatform.TextDataset(dataset_name=display_name)
    ds = ds.delete(sync=sync)
    return {"resource_name": ds.resource_name, "dataset_name": ds.display_name}


def delete_video_dataset(
    project: str,
    location: str,
    display_name: str,
    sync: bool = False,
):
    aiplatform.init(project=project, location=location)

    ds = aiplatform.VideoDataset(dataset_name=display_name)
    ds = ds.delete(sync=sync)
    return {"resource_name": ds.resource_name, "dataset_name": ds.display_name}


def delete_time_series_dataset(
    project: str,
    location: str,
    display_name: str,
    sync: bool = False,
):
    aiplatform.init(project=project, location=location)

    ds = aiplatform.TimeSeriesDataset(dataset_name=display_name)
    ds = ds.delete(sync=sync)
    return {"resource_name": ds.resource_name, "dataset_name": ds.display_name}


def delete_tabular_dataset(
    project: str,
    location: str,
    display_name: str,
    sync: bool = False,
):
    aiplatform.init(project=project, location=location)

    ds = aiplatform.TabularDataset(dataset_name=display_name)
    ds = ds.delete(sync=sync)
    return {"resource_name": ds.resource_name, "dataset_name": ds.display_name}


def list_image_datasets(
    project: str,
    location: str,
):
    aiplatform.init(project=project, location=location)

    ds = aiplatform.ImageDataset.list()
    all_datasets = []
    for dataset in ds:
        all_datasets.append(dataset.resource_name)

    return {"all_datasets": all_datasets}


def list_text_datasets(
    project: str,
    location: str,
):
    aiplatform.init(project=project, location=location)

    ds = aiplatform.TextDataset.list()
    all_datasets = []
    for dataset in ds:
        all_datasets.append(dataset.resource_name)

    return {"all_datasets": all_datasets}


def list_video_datasets(
    project: str,
    location: str,
):
    aiplatform.init(project=project, location=location)

    ds = aiplatform.VideoDataset.list()
    all_datasets = []
    for dataset in ds:
        all_datasets.append(dataset.resource_name)

    return {"all_datasets": all_datasets}


def list_time_series_datasets(
    project: str,
    location: str,
):
    aiplatform.init(project=project, location=location)

    ds = aiplatform.TimeSeriesDataset.list()
    all_datasets = []
    for dataset in ds:
        all_datasets.append(dataset.resource_name)

    return {"all_datasets": all_datasets}


def list_tabular_datasets(
    project: str,
    location: str,
):
    aiplatform.init(project=project, location=location)

    ds = aiplatform.TabularDataset.list()
    all_datasets = []
    for dataset in ds:
        all_datasets.append(dataset.resource_name)

    return {"all_datasets": all_datasets}


project_id = "bridgescapture-deloitte"
display_name = "text_class_dataset"
location = "us-central1"
