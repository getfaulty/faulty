#!/bin/bash
# Script to pin Python requirements in a Docker container
ROOTDIR="`pwd -P`/src/"
docker run \
    --rm \
    --entrypoint bash \
    -v $ROOTDIR:/mnt/app \
    -e CUSTOM_COMPILE_COMMAND='./scripts/pip-compile.sh' \
    -it python:3.7 \
    -c 'cd /mnt/app && pip install pip-tools==5.4.0 && pip-compile'