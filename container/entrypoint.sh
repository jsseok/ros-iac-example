#!/bin/bash

set -e

source /opt/ros/${ROS_DISTRO}/setup.sh
source /ros2_ws/sdi_pipeline/install/local_setup.sh

export ROS_DOMAIN_ID=${ROS_DOMAIN_ID:-7}

if [ "$3" != "sensing" ]; then
    if [ "$(uname -m)" = "aarch64" ]; then
        echo "ARM64 architecture"
        if [ -d "/usr/local/cuda" ]; then       
            echo "CUDA GPU"
            pip3 install --no-cache-dir --ignore-installed pandas==1.5.3 numpy==1.23.5 torch==2.5 torchvision==0.20 onnx==1.13 onnxruntime-gpu==1.14 onnxslim opencv-python ultralytics==8.2
        else
            echo "No GPU"
            pip3 install --no-cache-dir --ignore-installed pandas==1.5.3 numpy==1.23.5 torch==2.5 torchvision==0.20 onnx==1.13 onnxruntime==1.14 onnxslim opencv-python ultralytics==8.2 --extra-index-url https://download.pytorch.org/whl/cpu
        fi
    else
        echo "AMD64 architecture"
        pip3 install --no-cache-dir --ignore-installed pandas==1.5.3 numpy==1.23.5 torch==2.5 torchvision==0.20 onnx==1.13 onnxruntime-gpu==1.14 onnxslim opencv-python ultralytics==8.2
    fi

    if [ "$3" = "perception" ]; then
        yolo export model=yolov8s-seg.pt imgsz=640 format=onnx opset=12 simplify
        mkdir -p ~/sdi_models && mv ./yolov8s-seg.onnx ~/sdi_models && rm ./yolov8s-seg.pt
    fi
else
    pip3 install --no-cache-dir --ignore-installed "numpy<2" opencv-python 
fi


if [ "$3" != "perception" ]; then
    pip3 install --no-cache-dir --ignore-installed "numpy<2" opencv-python 
else
    if [ "$(uname -m)" = "aarch64" ]; then
        echo "ARM64 architecture"
        if [ -d "/usr/local/cuda" ]; then
            echo "CUDA GPU"
            pip3 install --no-cache-dir --ignore-installed pandas==1.5.3 numpy==1.23.5 torch==2.5 torchvision==0.20 onnx==1.13 onnxruntime-gpu==1.14 onnxslim opencv-python ultralytics==8.2
        else
            echo "No GPU"
            pip3 install --no-cache-dir --ignore-installed pandas==1.5.3 numpy==1.23.5 torch==2.5 torchvision==0.20 onnx==1.13 onnxruntime==1.14 onnxslim opencv-python ultralytics==8.2 --extra-index-url https://download.pytorch.org/whl/cpu
        fi
    else
        echo "AMD64 architecture"
        pip3 install --no-cache-dir --ignore-installed pandas==1.5.3 numpy==1.23.5 torch==2.5 torchvision==0.20 onnx==1.13 onnxruntime-gpu==1.14 onnxslim opencv-python ultralytics==8.2
    fi

    yolo export model=yolov8s-seg.pt format=onnx opset=10 simplify
    mkdir -p ~/sdi_models && mv ./yolov8s-seg.onnx ~/sdi_models && rm ./yolov8s-seg.pt
fi

exec "$@"
