#!/bin/bash

cd docker && \
docker-compose build && \
docker-compose run main /bin/bash -c "./split.sh && ./score.sh"
