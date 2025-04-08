# ARG settings for build
ARG GITHUB_PAT
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

ENV ROS_DOMAIN_ID=7

RUN apt-get update && apt-get install -y \
     cmake python3-pip libgl1-mesa-glx libglib2.0-0 gstreamer1.0* \
     ros-${ROS_DISTRO}-cv-bridge \
     && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /ros2_ws/sdi_pipeline

COPY --from=builder /ros2_ws/sdi_pipeline/install /ros2_ws/sdi_pipeline/install

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
