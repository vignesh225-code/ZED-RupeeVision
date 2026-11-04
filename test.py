import cv2
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--model", required=True)
args = parser.parse_args()

net = cv2.dnn.readNetFromONNX(args.model)

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Webcam not found!")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    height, width = frame.shape[:2]

    blob = cv2.dnn.blobFromImage(
        frame, 1/255.0, (640, 640),
        swapRB=True, crop=False
    )

    net.setInput(blob)
    output = net.forward()

    predictions = np.squeeze(output).T

    boxes = []
    scores = []

    for detection in predictions:
        confidence = detection[4]

        if confidence > 0.50:
            cx, cy, w, h = detection[:4]

            x = int((cx - w/2) * width / 640)
            y = int((cy - h/2) * height / 640)
            bw = int(w * width / 640)
            bh = int(h * height / 640)

            boxes.append([x, y, bw, bh])
            scores.append(float(confidence))

    indexes = cv2.dnn.NMSBoxes(
        boxes, scores, 0.50, 0.45
    )

    if len(indexes) > 0:
        for i in np.array(indexes).flatten():
            x, y, w, h = boxes[i]

            cv2.rectangle(
                frame, (x, y), (x+w, y+h),
                (0, 255, 0), 2
            )

            cv2.putText(
                frame,
                f"50 Rupee Note {scores[i]:.2f}",
                (x, y-10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7, (0, 255, 0), 2
            )

    cv2.imshow("50 Rupee Note Detector", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()