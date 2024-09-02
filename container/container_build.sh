#!/bin/bash

set -e

cd $(dirname $0)

docker buildx build --builder builderx --platform=linux/amd64,linux/arm64 -t docker.io/jsseok/sdi-pipeline-apps:latest -f Dockerfile --push .
