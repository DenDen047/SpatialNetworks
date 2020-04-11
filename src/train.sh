#!/bin/bash

python main.py --labels 10 train \
    --hyperparams hyperparameters.json \
    --datasets MNIST FashionMNIST \
    --layers 128 128 128 256 \
    --where 2 3 \
    --type linear \
    --input sequential \
    --activation Sigmoid \
    --save /result/models/model \
    --tensorboard /result/tensorboard \
    --proximity 3 \
    --transport 1 \
    --norm l1