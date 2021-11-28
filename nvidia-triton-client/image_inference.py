import argparse
import sys
import numpy as np
import cv2

import tritonclient.http as httpclient

# Instead of Zero pass the file path of Recorded Video as a string
cam = cv2.VideoCapture(0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        required=False,
        default=False,
        help="Enable verbose output",
    )
    parser.add_argument(
        "-u",
        "--url",
        type=str,
        required=False,
        default="localhost:8000",
        help="Inference server URL. Default is localhost:8000.",
    )

    FLAGS = parser.parse_args()
    try:
        triton_client = httpclient.InferenceServerClient(
            url=FLAGS.url, verbose=FLAGS.verbose
        )
    except Exception as e:
        print("context creation failed: " + str(e))
        sys.exit()

    model_name = "mask_detection"

    while True:
        grabbed, frame = cam.read()
        if grabbed:
            cv2.imshow("Frame", frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

            image = cv2.resize(
                frame,
                (100, 100),
                interpolation=cv2.INTER_CUBIC,
            )
            image = np.expand_dims(image, axis=0)
            image = np.divide(image, 255.0).astype("float32")

            inputs = []
            inputs.append(
                httpclient.InferInput(
                    name="input_1", shape=image.shape, datatype="FP32"
                )
            )
            inputs[0].set_data_from_numpy(image, binary_data=False)

            outputs = []
            # number of class counts represents the number of labels needed in the output
            outputs.append(
                httpclient.InferRequestedOutput(
                    name="dense",
                    class_count=2,
                )
            )

            result = triton_client.infer(
                model_name=model_name, inputs=inputs, outputs=outputs
            )
            output_array = result.as_numpy("dense")[0]

            print(f"Results for current Frame ....  ")
            for res in output_array:
                final_pred = str(res).split(":")
                print(f"Probability: {final_pred[0]}  Prediction: {final_pred[-1]}")
                # This is the expeced JSON that can be pushed to any end point as needed
                predicted_json = {
                    "Probability": final_pred[0],
                    "Prediction": final_pred[-1],
                }
        else:
            break
