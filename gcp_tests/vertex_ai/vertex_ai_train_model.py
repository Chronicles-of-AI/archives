from google.cloud import aiplatform
from google.cloud.aiplatform.gapic.schema import trainingjob


def run_job(
    job,
    dataset,
    model_display_name,
    training_fraction_split,
    validation_fraction_split,
    test_fraction_split,
    budget_milli_node_hours,
    disable_early_stopping,
    sync,
):
    model = job.run(
        dataset=dataset,
        model_display_name=model_display_name,
        training_fraction_split=training_fraction_split,
        validation_fraction_split=validation_fraction_split,
        test_fraction_split=test_fraction_split,
        budget_milli_node_hours=budget_milli_node_hours,
        disable_early_stopping=disable_early_stopping,
        sync=sync,
    )
    return {
        "resource_name": model.resource_name,
        "display_name": model.display_name,
        "uri": model.uri,
    }


def train_image_classification(
    project: str,
    location: str,
    display_name: str,
    dataset_id: int,
    model_display_name: str = None,
    model_type: str = "CLOUD",
    training_fraction_split: float = 0.8,
    validation_fraction_split: float = 0.1,
    test_fraction_split: float = 0.1,
    budget_milli_node_hours: int = 8000,
    disable_early_stopping: bool = False,
    sync: bool = False,
    multi_label: bool = False,
):
    # Supported Model Types -
    # MOBILE_TF_HIGH_ACCURACY_1
    # MOBILE_TF_LOW_LATENCY_1
    # MOBILE_TF_VERSATILE_1
    # CLOUD_HIGH_ACCURACY_1
    # CLOUD_LOW_LATENCY_1
    # CLOUD

    aiplatform.init(project=project, location=location)

    job = aiplatform.AutoMLImageTrainingJob(
        display_name=display_name,
        model_type=model_type,
        multi_label=multi_label,
    )
    my_image_ds = aiplatform.ImageDataset(dataset_id)

    return run_job(
        job=job,
        dataset=my_image_ds,
        model_display_name=model_display_name,
        training_fraction_split=training_fraction_split,
        validation_fraction_split=validation_fraction_split,
        test_fraction_split=test_fraction_split,
        budget_milli_node_hours=budget_milli_node_hours,
        disable_early_stopping=disable_early_stopping,
        sync=sync,
    )


def train_object_detection(
    project: str,
    location: str,
    display_name: str,
    dataset_id: int,
    model_display_name: str = None,
    model_type: str = "CLOUD",
    training_fraction_split: float = 0.8,
    validation_fraction_split: float = 0.1,
    test_fraction_split: float = 0.1,
    budget_milli_node_hours: int = 8000,
    disable_early_stopping: bool = False,
    sync: bool = False,
):
    # Supported Model Types -
    # MOBILE_TF_HIGH_ACCURACY_1
    # MOBILE_TF_LOW_LATENCY_1
    # MOBILE_TF_VERSATILE_1
    # CLOUD_HIGH_ACCURACY_1
    # CLOUD_LOW_LATENCY_1
    # CLOUD

    aiplatform.init(project=project, location=location)

    job = aiplatform.AutoMLImageTrainingJob(
        display_name=display_name,
        model_type=model_type,
        prediction_type="object_detection",
    )
    my_image_ds = aiplatform.ImageDataset(dataset_id)

    return run_job(
        job=job,
        dataset=my_image_ds,
        model_display_name=model_display_name,
        training_fraction_split=training_fraction_split,
        validation_fraction_split=validation_fraction_split,
        test_fraction_split=test_fraction_split,
        budget_milli_node_hours=budget_milli_node_hours,
        disable_early_stopping=disable_early_stopping,
        sync=sync,
    )


def train_text_model(
    project: str,
    location: str,
    display_name: str,
    dataset_id: int,
    model_display_name: str = None,
    prediction_type: str = "classification",
    training_fraction_split: float = 0.8,
    validation_fraction_split: float = 0.1,
    test_fraction_split: float = 0.1,
    budget_milli_node_hours: int = 8000,
    disable_early_stopping: bool = False,
    sync: bool = False,
    multi_label: bool = False,
):
    aiplatform.init(project=project, location=location)

    if prediction_type == "classification":
        job = aiplatform.AutoMLTextTrainingJob(
            display_name=display_name,
            prediction_type=prediction_type,
            multi_label=multi_label,
        )
    elif prediction_type == "extraction":
        job = aiplatform.AutoMLTextTrainingJob(
            display_name=display_name,
            prediction_type=prediction_type,
        )

    text_dataset = aiplatform.TextDataset(dataset_id)

    return run_job(
        job=job,
        dataset=text_dataset,
        model_display_name=model_display_name,
        training_fraction_split=training_fraction_split,
        validation_fraction_split=validation_fraction_split,
        test_fraction_split=test_fraction_split,
        budget_milli_node_hours=budget_milli_node_hours,
        disable_early_stopping=disable_early_stopping,
        sync=sync,
    )


def train_video_model(
    project: str,
    location: str,
    display_name: str,
    dataset_id: int,
    model_display_name: str = None,
    model_type: str = "CLOUD",
    prediction_type: str = "classification",
    training_fraction_split: float = 0.8,
    validation_fraction_split: float = 0.1,
    test_fraction_split: float = 0.1,
    budget_milli_node_hours: int = 8000,
    disable_early_stopping: bool = False,
    sync: bool = False,
):
    # Supported Model Types -
    # MOBILE_VERSATILE_1
    # MOBILE_CORAL_VERSATILE_1
    # MOBILE_CORAL_LOW_LATENCY_1
    # MOBILE_JETSON_VERSATILE_1
    # MOBILE_JETSON_LOW_LATENCY_1

    aiplatform.init(project=project, location=location)

    job = aiplatform.AutoMLVideoTrainingJob(
        display_name=display_name,
        prediction_type=prediction_type,
        model_type=model_type,
    )
    my_image_ds = aiplatform.ImageDataset(dataset_id)

    return run_job(
        job=job,
        dataset=my_image_ds,
        model_display_name=model_display_name,
        training_fraction_split=training_fraction_split,
        validation_fraction_split=validation_fraction_split,
        test_fraction_split=test_fraction_split,
        budget_milli_node_hours=budget_milli_node_hours,
        disable_early_stopping=disable_early_stopping,
        sync=sync,
    )


project_id = "bridgescapture-deloitte"
location = "us-central1"
dataset_id = "2538578834488295424"
display_name = "image_class_model"

# Sample Output
# {'resource_name': 'projects/307982079966/locations/us-central1/models/6037079698536660992', 'display_name': 'image_class_model', 'uri': None}

response = train_image_classification(
    project=project_id,
    location=location,
    display_name=display_name,
    dataset_id=dataset_id,
    model_display_name=display_name,
)
print(response)
