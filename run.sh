#!/bin/bash

cd docker && \
docker-compose build && \
docker-compose run main /bin/bash -c "./train.sh && ./split.sh && ./score.sh"
