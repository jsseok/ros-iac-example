#!/bin/bash

set -e

if [ "$(uname -m)" = "aarch64" ]; then
    echo "ARM64 architecture"
    if [ -d "/usr/local/cuda" ]; then       
        echo "CUDA GPU"
        pip install --no-cache-dir --ignore-installed torch torchvision onnx onnxruntime onnxruntime-gpu onnxslim opencv-python ultralytics
    else
        echo "No GPU"
        pip install --no-cache-dir --ignore-installed torch torchvision onnx onnxruntime onnxslim opencv-python ultralytics --extra-index-url https://download.pytorch.org/whl/cpu
    fi
else
    echo "AMD64 architecture"
    pip install --no-cache-dir --ignore-installed torch torchvision onnx onnxruntime onnxruntime-gpu onnxslim opencv-python ultralytics
fi

source /opt/ros/${ROS_DISTRO}/setup.sh
source /ros2_ws/sdi_pipeline/install/local_setup.sh

yolo export model=yolov8s-seg.pt imgsz=640 format=onnx opset=12 simplify
mkdir -p ~/sdi_models && mv ./yolov8s-seg.onnx ~/sdi_models && rm ./yolov8s-seg.pt

exec "$@"
