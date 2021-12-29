#!/bin/sh

docker build -f Dockerfile -t data-science-knowledge-management .
docker run -it -v $PWD/src:/analyse --hostname gallifrey data-science-knowledge-management /bin/bash