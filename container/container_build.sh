#!/bin/bash

set -e

cd $(dirname $0)

docker build -t sdi-pipeline-perception-yolov8 -f Dockerfile .
#docker buildx build  --platform=linux/amd64,linux/arm64 -t docker.io/jsseok/sdi-pipeline-perception-yolov8:latest --push .