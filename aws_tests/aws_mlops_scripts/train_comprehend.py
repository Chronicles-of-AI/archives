import boto3

client = boto3.client("comprehend")

response = client.create_document_classifier(
    DocumentClassifierName="comprehend-text-classification-v1",
    DataAccessRoleArn="arn:aws:iam::142339138776:role/DocuEdge-AI-Comprehend",
    InputDataConfig={
        "DataFormat": "AUGMENTED_MANIFEST",
        "AugmentedManifests": [
            {
                "S3Uri": "s3://mlops-manifest-files/comp_text_class.manifest",
                "AttributeNames": [
                    "TextClassification",
                ],
            },
        ],
    },
    LanguageCode="en",
    Mode="MULTI_CLASS",
)
