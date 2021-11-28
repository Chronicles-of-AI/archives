import boto3


def create_project(project_name):

    client = boto3.client("rekognition")

    # Create a project
    print("Creating project:" + project_name)
    response = client.create_project(ProjectName=project_name)
    print("project ARN: " + response["ProjectArn"])
    print("Done...")


def delete_project(project_arn):

    client = boto3.client("rekognition")

    # Delete a project
    print("Deleting project:" + project_arn)
    response = client.delete_project(ProjectArn=project_arn)
    print("Status: " + response["Status"])
    print("Done...")


# create_project(project_name="rekognition_image_classification")
