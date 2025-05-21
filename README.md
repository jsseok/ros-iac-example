## ROS On SDI Project
This sub-project serves as a study case for deploying ROS applications via Infrastructure as Code (IaC).


### Prerequisites
- Kubernetes (k8s) cluster configured with macvlan for ROS DDS Discovery.
- Docker or Podman for containerization.
- Buildx multi-architecture build system (for cross-platform builds).

### Usage

##### Build as a container
```
# go to the package directory
cd <path/to/package>

# build using docker buildx for multi-architecture support
docker buildx build  --platform linux/arm64,linux/amd64 -t <repo:tag> -f container/Dockerfile --push .
```

##### Deploy to the k8s
- on k8s CP
```
# go to the ROS package directory
kubectl apply -f container/k8s_deployment.yaml
```

##### Deployments YAML Detatils
- **Namespace:** All resources are deployed within the `sdi-ros-system` namespace (`metadata.namespace`). Ensure this namespace exists in your cluster.
- **Container Images:** Each deployment specifies the container image to use from the `jsseok/ros-iac-apps` repository, corresponding to the tags listed in the **[Available Images](#available-images)** section (e.g., `jsseok/ros-iac-apps:sensing`).
- **Network Attachment (Macvlan):** The `k8s.v1.cni.cncf.io/networks` annotation is used to attach pods to a specific macvlan network (`conf-macvlan-wlan` or `conf-macvlan-eth0`). This is crucial for enabling ROS DDS discovery over a flat network as mentioned in the Prerequisites.

### Available Images
The container images for this project are available under the `jsseok/ros-iac-apps` repository. The following tags are provided:

| Tag | Description |
|----------:|:-------|
| broker    | Relays the `rgb_image` topic from the USB Camera input to the `perception_image` topic used by perception nodes |
| sensing   | Handles streaming from a USB Camera and publishes the `rgb_image` topic |
| class     | Performs image classification on the camera input and publishes the result on the `class_image` topic |
| seg       | Performs image segmentation on the camera input and publishes the result on the `seg_image` topic |
| bringup   | Launches a set of core nodes including sensing, seg, and broker |
