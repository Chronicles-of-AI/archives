import os
import sagemaker
from sagemaker import get_execution_role
from sagemaker.tensorflow.estimator import TensorFlow

sagemaker_session = sagemaker.Session()

# role = get_execution_role()
region = sagemaker_session.boto_session.region_name

training_input_path = "s3://intel-edge-poc/mask_dataset_datagen/train/"
validation_input_path = "s3://intel-edge-poc/mask_dataset_datagen/val/"

hyperparam = {
    "save_model_dir": "s3://intel-edge-poc/saved/",
    "batch_size": 32,
    "epochs": 2,
    "optimizer": "adam",
    "learning_rate": 1e-3,
}
#'train_dir': 'mask_dataset_datagen/train/',
#'val_dir': 'mask_dataset_datagen/val/'
#'bucket' : 'intel-edge-poc',


tf_estimator = TensorFlow(
    entry_point="TrainingJob.py",
    role="intel-edge-poc-role",
    instance_count=1,
    instance_type="ml.c4.xlarge",
    framework_version="2.3",
    py_version="py37",
    hyperparameters=hyperparam,
    script_mode=True,
)


# tf_estimator.fit()
tf_estimator.fit({"training": training_input_path, "validation": validation_input_path})
