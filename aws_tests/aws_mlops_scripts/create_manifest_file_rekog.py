import boto3
import datetime
import json

client = boto3.client("s3")


def read_objects(bucket_name: str, job_name: str, all_data: list, marker: str):
    response = client.list_objects(Bucket=bucket_name, Delimiter=" ", Marker=marker)
    truncated = response.get("IsTruncated")
    next_marker = response.get("NextMarker")
    contents = response.get("Contents")
    if contents:
        for obj in contents:
            if (".jpg" in obj.get("Key")) or (".jpeg" in obj.get("Key")):
                label = obj.get("Key").split("/")[0]
                s3_uri = "s3://" + bucket_name + "/" + obj.get("Key")
                final_dict = {
                    "source-ref": s3_uri,
                    job_name: 1,
                    job_name
                    + "-metadata": {
                        "confidence": 1,
                        "job-name": "labeling-job/" + job_name,
                        "class-name": label,
                        "human-annotated": "yes",
                        "creation-date": "T".join(
                            str(datetime.datetime.today()).split(" ")
                        ),
                        "type": "groundtruth/image-classification",
                    },
                }
                all_data.append(final_dict)
        if truncated and next_marker:
            read_objects(
                bucket_name=bucket_name,
                job_name=job_name,
                all_data=all_data,
                marker=next_marker,
            )
    return all_data


bucket_name = "mlops-documents-dataset"
job_name = "rekognition_image_classification"
data = read_objects(bucket_name=bucket_name, job_name=job_name, all_data=[], marker="")

with open("rekog_doc_class.manifest", "w") as annot_train:
    for sentence in data:
        json.dump(sentence, annot_train)
        annot_train.write("\n")
