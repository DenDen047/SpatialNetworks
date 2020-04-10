#!/bin/bash

cd docker && \
docker-compose build && \
docker-compose run main ls -l .
