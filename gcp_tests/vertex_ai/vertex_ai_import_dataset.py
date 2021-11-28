from google.cloud import aiplatform


def import_image_dataset(
    project: str,
    location: str,
    src_uris: list,
    dataset_id: str,
    single_label: bool,
    sync: bool = False,
):
    if single_label:
        import_schema_uri = "gs://google-cloud-aiplatform/schema/dataset/ioformat/image_classification_single_label_io_format_1.0.0.yaml"
    else:
        import_schema_uri = "gs://google-cloud-aiplatform/schema/dataset/ioformat/image_classification_multi_label_io_format_1.0.0.yaml"

    aiplatform.init(project=project, location=location)

    ds = aiplatform.ImageDataset(dataset_id)
    ds = ds.import_data(
        gcs_source=src_uris,
        import_schema_uri=import_schema_uri,
        sync=sync,
    )
    return {"resource_name": ds.resource_name, "display_name": ds.display_name}


def import_object_detection_dataset(
    project: str,
    location: str,
    src_uris: list,
    dataset_id: str,
    sync: bool = False,
):
    aiplatform.init(project=project, location=location)

    ds = aiplatform.ImageDataset(dataset_id)
    import_schema_uri = "gs://google-cloud-aiplatform/schema/dataset/ioformat/image_bounding_box_io_format_1.0.0.yaml"
    ds = ds.import_data(
        gcs_source=src_uris,
        import_schema_uri=import_schema_uri,
        sync=sync,
    )
    return {"resource_name": ds.resource_name, "display_name": ds.display_name}


def import_text_dataset(
    project: str,
    location: str,
    src_uris: list,
    dataset_id: str,
    single_label: bool,
    sync: bool = False,
):
    if single_label:
        import_schema_uri = "gs://google-cloud-aiplatform/schema/dataset/ioformat/text_classification_single_label_io_format_1.0.0.yaml"
    else:
        import_schema_uri = "gs://google-cloud-aiplatform/schema/dataset/ioformat/text_classification_multi_label_io_format_1.0.0.yaml"

    aiplatform.init(project=project, location=location)

    ds = aiplatform.TextDataset(dataset_id)

    ds = ds.import_data(
        gcs_source=src_uris,
        import_schema_uri=import_schema_uri,
        sync=sync,
    )
    return {"resource_name": ds.resource_name, "display_name": ds.display_name}


def import_ner_dataset(
    project: str,
    location: str,
    src_uris: list,
    dataset_id: str,
    sync: bool = False,
):
    aiplatform.init(project=project, location=location)

    ds = aiplatform.TextDataset(dataset_id)
    import_schema_uri = aiplatform.schema.dataset.ioformat.text.extraction
    ds = ds.import_data(
        gcs_source=src_uris,
        import_schema_uri=import_schema_uri,
        sync=sync,
    )
    return {"resource_name": ds.resource_name, "display_name": ds.display_name}


def import_video_dataset(
    project: str,
    location: str,
    src_uris: list,
    dataset_id: str,
    use_case: str,
    sync: bool = False,
):
    aiplatform.init(project=project, location=location)

    ds = aiplatform.VideoDataset(dataset_id)

    if use_case == "action_recognition":
        import_schema_uri = aiplatform.schema.dataset.ioformat.video.action_recognition
    elif use_case == "video_classification":
        import_schema_uri = aiplatform.schema.dataset.ioformat.video.classification
    elif use_case == "object_tracking":
        import_schema_uri = aiplatform.schema.dataset.ioformat.video.object_tracking
    ds = ds.import_data(
        gcs_source=src_uris,
        import_schema_uri=import_schema_uri,
        sync=sync,
    )
    return {"resource_name": ds.resource_name, "display_name": ds.display_name}


project_id = "bridgescapture-deloitte"
location = "us-central1"
gcs_path = ["gs://mlops_data_storage/NL_classification_happiness.csv"]
dataset_id = "4389558281337569280"
# Sample Output
# {'resource_name': 'projects/307982079966/locations/us-central1/datasets/4389558281337569280', 'display_name': 'text_class_dataset'}

response = import_text_dataset(
    project=project_id,
    location=location,
    src_uris=gcs_path,
    dataset_id=dataset_id,
    single_label=True,
)
print(response)
