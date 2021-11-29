import boto3

client = boto3.client("textract")


def analyze_document_local(document: bytes):
    response = client.analyze_document(
        Document={
            "Bytes": document,
        },
        FeatureTypes=[
            "TABLES",
            "FORMS",
        ],
    )
    return response


def analyze_document_s3(
    bucket_name: str,
    doc_name: str,
):
    response = client.analyze_document(
        Document={
            "S3Object": {
                "Bucket": bucket_name,
                "Name": doc_name,
            }
        },
        FeatureTypes=[
            "TABLES",
            "FORMS",
        ],
    )
    return response
