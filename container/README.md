# [FOR DEMO] SDI CI/CD PIPELINE EXAMPLE 
[![en](https://img.shields.io/badge/Lang-en-green.svg)](./README.en.md) ![license](https://img.shields.io/badge/License-MIT-blue.svg)

도커 container 빌드 및 k8s 배포를 위한 파일들을 포함하는 하위 디렉토리입니다.

## 동작 구성

![sdi_pipeline](./docs/images/sdi_pipeline.jpg)


### Remote Multi-Architecture 구성
 * 컨데이너로 동작하는 Jenkins 서버 특성상 원격지 Native 빌드 환경을 사용
 * buildx 기반 동작 환경 설정
    ```
    export DOCKER_CLI_EXPERIMENTAL=enabled
    sudo docker run --privileged --rm tonistiigi/binfmt --install all

    docker buildx create --name mybuilder --use
    docker buildx inspect --bootstrap
    docker buildx build -f <Dockerfile> --platform=linux/amd64,linux/arm64 -t <repo_name>:<tag> --push .
    ```
  * Docker TCP socket open
    * /etc/docker/daemon.json 내 다음 내용 설정
        ```
        {
            "hosts": ["unix:///var/run/docker.sock", "tcp://0.0.0.0:2375"]
        }
        ```
    * /usr/lib/systemd/system/docker.service 서비스 수정
        ```
        # "-H fd://" 삭제
        # ExecStart=/usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock
        # to
        ExecStart=/usr/bin/dockerd --containerd=/run/containerd/containerd.sock
        ```
    * 서비스 재시작
        ```
        sudo systemctl daemon-reload
        sudo systemctl restart docker.socket
        sudo systemctl restart docker
        ```