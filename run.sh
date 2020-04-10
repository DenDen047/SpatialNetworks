#!/bin/bash

cd docker && \
docker-compose build && \
docker-compose run main python main.py -h
