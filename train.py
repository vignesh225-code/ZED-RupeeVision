from ultralytics import YOLO

model = YOLO("yolo11n.pt")

model.train(
    data="data.yaml",
    epochs=50,
    imgsz=640,
    batch=8,
    name="rupee50_detector"
)

best_model = YOLO("runs/detect/rupee50_detector/weights/best.pt")
best_model.export(format="onnx")