#!/bin/bash

set -e

cd $(dirname $0)

sudo docker buildx build \
    --platform linux/amd64,linux/arm64 \
    -t docker.io/jsseok/sdi-pipeline-apps:update\
    -f Dockerfile \
    --cache-from=type=registry,ref=docker.io/jsseok/sdi-pipeline-apps:update_cache \
    --cache-to=type=registry,ref=docker.io/jsseok/sdi-pipeline-apps:update_cache,mode=max \
    --push .
