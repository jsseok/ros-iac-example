#!/bin/bash

yolo export model=yolov8s-seg.pt imgsz=640 format=onnx opset=12 simplify
mkdir -p ~/sdi_models && mv ./yolov8s-seg.onnx ~/sdi_models && rm ./yolov8s-seg.pt
exec "$@"
