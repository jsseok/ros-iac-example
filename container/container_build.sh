#!/bin/bash

set -e

cd $(dirname $0)

# docker build -t sdi-pipeline-apps -f Dockerfile .
docker buildx build --builder builderx --platform linux/amd64,linux/arm64 -t sdi-pipeline-apps -f Dockerfile .