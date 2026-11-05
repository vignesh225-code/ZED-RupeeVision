# 🇮🇳 Indian ₹50 Banknote Detector

## 📌 Project Overview

This project detects the new Indian ₹50 banknote (light blue-green) using **YOLO11** and **OpenCV** with ONNX Runtime support.

The detector identifies the front and back sides of the ₹50 note through a live webcam feed.

## ✨ Features

- Detects Indian ₹50 banknotes.
- Supports front and back sides.
- Uses a trained YOLO11 model.
- ONNX model for inference.
- Live webcam detection using OpenCV.
- Displays bounding boxes and confidence scores.

## 📂 Project Structure

```text
ZED-RupeeVision/
│
├── dataset/
│   ├── images/
│   │   ├── train/
│   │   ├── val/
│   │   └── test/
│   │
│   └── labels/
│       ├── train/
│       ├── val/
│       └── test/
│
├── model/
│   └── model.onnx
│
├── data.yaml
├── train.py
├── test.py
├── split_dataset.py
└── README.md
```

## 🛠️ Requirements

- Python 3.11
- OpenCV
- NumPy
- ONNX Runtime

## 📥 Install Dependencies

```bash
pip install opencv-python numpy onnxruntime
```

## ▶️ Run the Detector

```bash
python test.py --model model/model.onnx
```

Press **q** to close the webcam window.

## 🤖 Model

The trained YOLO11 model is exported to ONNX format and loaded directly using OpenCV DNN.

## 📊 Dataset

The dataset contains self-captured images of Indian ₹50 notes and other denominations as negative samples.

## 🔮 Future Improvements

- Support for additional Indian currency denominations.
- Improve detection accuracy.
- Real-time currency recognition.
- Mobile application integration.

## 👨‍💻 Project

**Indian ₹50 Banknote Detector**

Built using Python, YOLO11, OpenCV and ONNX Runtime.
