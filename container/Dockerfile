# ARG settings for build
ARG GITHUB_PAT=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
ARG ROS_DISTRO=humble

# Stage 1 for builder
FROM ros:${ROS_DISTRO}-ros-base AS builder

RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-colcon-common-extensions \
    git \
    curl \
    unzip \
    rsync \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /ros2_ws/sdi_pipeline
WORKDIR /ros2_ws

RUN pip3 install --no-cache-dir --ignore-installed setuptools==58.2.0

ARG GITHUB_PAT
RUN curl -H "Authorization: token ${GITHUB_PAT}" -L \
https://github.com/open-SDI/CI-CV-CD_Pipeline_Example/archive/refs/heads/main.zip -o ./main.zip
RUN unzip main.zip -d ./tmp && \
    rsync -av --remove-source-files ./tmp/*/ ./sdi_pipeline && \
    rm -rf ./tmp main.zip

RUN . /opt/ros/${ROS_DISTRO}/setup.sh
WORKDIR /ros2_ws/sdi_pipeline
RUN colcon build



# Stage 2 for runtime
FROM ros:${ROS_DISTRO}-ros-base

RUN apt-get update && apt-get install -y \
    python3-pip \
    libgl1-mesa-glx \
    ros-${ROS_DISTRO}-cv-bridge \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /ros2_ws/sdi_pipeline

COPY --from=builder /ros2_ws/sdi_pipeline/install /ros2_ws/sdi_pipeline/install

RUN pip3 install --no-cache-dir --ignore-installed onnx ultralytics onnxruntime numpy opencv-python

RUN yolo export model=yolov8s-seg.pt imgsz=640 format=onnx opset=12 simplify
RUN mkdir -p ~/sdi_models && mv ./yolov8s-seg.onnx ~/sdi_models && rm ./yolov8s-seg.pt

RUN echo "source /opt/ros/${ROS_DISTRO}/setup.sh" >> ~/.bashrc
RUN echo "source /ros2_ws/sdi_pipeline/install/local_setup.sh" >> ~/.bashrc

# CMD ["ros2", "run", "perception", "seg_yolov8s"]