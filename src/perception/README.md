# SDI Perception Nondes

## Seg_yolov8s

카메라 이미지(Topic: `/rgb_image`)를 받아 Yolov8s의 segmentation 을 수행 후 결과를 `/seg_image` 토픽으로 발행합니다.

범용성을 위해 onnx 모델을 사용하고 노드 실행 전 onnx 형식의 모델을 가지고 있어야 합니다.

테스트를 위해 sdi노드들의 ai모델들은 ~/sdi_models/ 경로에 위치한다고 가정합니다. (컨테이너 변환 시 working_dir 에 위치될 것으로 예상됨)

사전에 아래와 같은 사전 준비가 필요합니다.

``` bash
pip install ultralytics
pip install onnxruntime-gpu
# pip install onnxruntime # Use this instead if you don't have an NVIDIA GPU
pip install numpy opencv-python

yolo export model=yolov8s-seg.pt imgsz=640 format=onnx opset=12 simplify
mkdir -p ~/sdi_models
mv ./yolov8s-seg.onnx ~/sid_models
```