# ARG settings for build
ARG GITHUB_PAT=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
ARG ROS_DISTRO=humble

# Stage 0 for builder
FROM ros:${ROS_DISTRO}-ros-base AS builder

RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-colcon-common-extensions \
    git \
    curl \
    unzip \
    rsync \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --no-cache-dir --ignore-installed setuptools==58.2.0 

RUN mkdir -p /ros2_ws/sdi_pipeline
WORKDIR /ros2_ws

ARG GITHUB_PAT
RUN curl -H "Authorization: token ${GITHUB_PAT}" -L \
https://github.com/open-SDI/CI-CV-CD_Pipeline_Example/archive/refs/heads/feature/dockerfile.zip -o ./main.zip
RUN unzip main.zip -d ./tmp && \
    rsync -av --remove-source-files ./tmp/*/ ./sdi_pipeline && \
    rm -rf ./tmp main.zip

WORKDIR /ros2_ws/sdi_pipeline
RUN . /opt/ros/${ROS_DISTRO}/setup.sh
RUN colcon build



# Stage 1 for runtime
FROM ros:${ROS_DISTRO}-ros-core

RUN apt-get update && apt-get install -y \
    python3-pip \
    libgl1-mesa-glx \
    ros-${ROS_DISTRO}-cv-bridge \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /ros2_ws/sdi_pipeline

RUN pip3 install --no-cache-dir --ignore-installed "numpy<2" onnx onnxruntime ultralytics opencv-python

COPY --from=builder /ros2_ws/sdi_pipeline/install /ros2_ws/sdi_pipeline/install

RUN yolo export model=yolov8s-seg.pt imgsz=640 format=onnx opset=12 simplify
RUN mkdir -p ~/sdi_models && mv ./yolov8s-seg.onnx ~/sdi_models && rm ./yolov8s-seg.pt

RUN echo "source /opt/ros/${ROS_DISTRO}/setup.sh" >> ~/.bashrc
RUN echo "source /ros2_ws/sdi_pipeline/install/local_setup.sh" >> ~/.bashrc
