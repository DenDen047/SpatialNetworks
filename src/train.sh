#!/bin/bash

python main.py --labels 50 train \
    --hyperparams hyperparameters.json \
    --layers 128 128 128 256 \
    --where 2 3 \
    --type linear \
    --input sequential \
    --activation Sigmoid \
    --save /result/models \
    --tensorboard /result/tensorboard \
    --norm l1