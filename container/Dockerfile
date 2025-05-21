# Base ARG
ARG ROS_DISTRO=humble

###############################
# Stage 0 - Build Stage
###############################
FROM ros:${ROS_DISTRO}-ros-core AS builder

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-pip \
    python3-colcon-common-extensions \
    git \
    curl \
    unzip \
    rsync \
    python3-rosdep \
    build-essential \
    cmake \
    gcc \
    g++ \
    libopencv-dev \
    python3-opencv \
    python3-numpy \
    python3-yaml

RUN python3 -m pip install --upgrade pip setuptools==58.0.4 wheel pytest argcomplete

RUN apt-get clean && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /ros2_ws
WORKDIR /ros2_ws
COPY . ./src

WORKDIR /ros2_ws
RUN . /opt/ros/${ROS_DISTRO}/setup.sh && colcon build


###############################
# Stage 1 - Runtime Stage
###############################
FROM ros:${ROS_DISTRO}-ros-core

# 환경 변수 설정
ENV ROS_DOMAIN_ID=0
ENV YOLO_CLASSES_PATH=/ros2_ws/data/coco8.yaml
ENV YOLO_SEG_MODEL_PATH=/ros2_ws/data/yolov8n-seg.onnx
ENV YOLO_MODEL_PATH=/ros2_ws/data/yolov8n.onnx

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-pip \
    python3-colcon-common-extensions \
    ros-${ROS_DISTRO}-cv-bridge \
    python3-numpy \
    python3-opencv \
    libglib2.0-0 \
    libgl1-mesa-glx

RUN python3 -m pip install --no-cache-dir onnx==1.17.0 onnxruntime==1.12.0

RUN apt-get clean && rm -rf /var/lib/apt/lists/*

COPY ./container/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

COPY --from=builder /ros2_ws/install /ros2_ws/install
COPY  ./data /ros2_ws/data

ENTRYPOINT ["/entrypoint.sh"]
# CMD ["ros2", "launch", "bringup", "bringup.launch.py"]
# CMD ["ros2", "run", "perception", "seg_yolov8s"]
# CMD ["ros2", "run", "perception", "class_yolov8s"]
# CMD ["ros2", "run", "sensing", "usb_cam"]
CMD ["ros2", "run", "test_pkg", "img_broker"]