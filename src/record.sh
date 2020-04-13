#!/bin/bash

python main.py --labels 10 --cuda record \
    --model /result/models/model \
    --input sequential \
    --datasets MNIST FashionMNIST \
    --reduction variance \
    --save /result/record