#!/bin/sh

docker build -f Dockerfile -t xelatex-knowledge-management .
docker run -it -v $PWD/src:/home -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=unix$DISPLAY  xelatex-knowledge-management /bin/bash