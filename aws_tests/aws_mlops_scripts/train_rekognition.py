import boto3
import json


def train_model(
    project_arn, version_name, output_config, training_dataset, testing_dataset
):

    client = boto3.client("rekognition")

    print("Starting training of: " + version_name)

    try:
        response = client.create_project_version(
            ProjectArn=project_arn,
            VersionName=version_name,
            OutputConfig=output_config,
            TrainingData=training_dataset,
            TestingData=testing_dataset,
        )

        # Wait for the project version training to complete
        project_version_training_completed_waiter = client.get_waiter(
            "project_version_training_completed"
        )
        project_version_training_completed_waiter.wait(
            ProjectArn=project_arn, VersionNames=[version_name]
        )

        # Get the completion status
        describe_response = client.describe_project_versions(
            ProjectArn=project_arn, VersionNames=[version_name]
        )
        for model in describe_response["ProjectVersionDescriptions"]:
            print("Status: " + model["Status"])
            print("Message: " + model["StatusMessage"])
    except Exception as e:
        print(e)

    print("Done...")


def main():

    project_arn = "arn:aws:rekognition:us-east-2:142339138776:project/rekognition_image_classification/1624553003220"
    version_name = "rekognition_image_classification_v1"

    output_config = json.loads(
        '{"S3Bucket":"mlops-manifest-files", "S3KeyPrefix":"output_models"}'
    )
    training_dataset = json.loads(
        '{"Assets": [{ "GroundTruthManifest": { "S3Object": { "Bucket": "mlops-manifest-files", "Name": "rekog_image_class.manifest" } } } ] }'
    )
    testing_dataset = json.loads('{"AutoCreate":true}')
    # testing_dataset= json.loads('{"Assets": [{ "GroundTruthManifest": { "S3Object": { "Bucket": "testing_bucket", "Name": "testing_output" } } } ]}')

    train_model(
        project_arn, version_name, output_config, training_dataset, testing_dataset
    )


if __name__ == "__main__":
    main()
