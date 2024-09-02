#!/bin/bash

set -e

cd $(dirname $0)

docker buildx build \
    --builder builderx \
    --platform linux/amd64,linux/arm64 \
    -t docker.io/jsseok/sdi-pipeline-apps:latest \
    -f Dockerfile \
    --cache-from=type=registry,ref=docker.io/jsseok/sdi-pipeline-apps:cache \
    --cache-to=type=registry,ref=docker.io/jsseok/sdi-pipeline-apps:cache,mode=max \
    --push .
