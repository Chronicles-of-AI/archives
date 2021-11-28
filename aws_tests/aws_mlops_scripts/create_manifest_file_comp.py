import json
import pandas as pd
import datetime

csv_path = (
    "/Users/vsatpathy/Desktop/off_POCs/automl_nl_data/NL-classification_happiness.csv"
)


def create_manifest(job_name: str):
    all_data = []
    df = pd.read_csv(csv_path)

    for index, row in df.iterrows():
        # print(row[0], row[1])
        final_dict = {
            "source": row[0],
            job_name: 1,
            job_name
            + "-metadata": {
                "confidence": 1,
                "job-name": "labeling-job/" + job_name,
                "class-name": row[1],
                "human-annotated": "yes",
                "creation-date": "T".join(str(datetime.datetime.today()).split(" ")),
                "type": "groundtruth/text-classification",
            },
        }
        all_data.append(final_dict)
    return all_data


data = create_manifest(job_name="TextClassification")
with open("comp_text_class.manifest", "w") as annot_train:
    for sentence in data:
        json.dump(sentence, annot_train)
        annot_train.write("\n")
