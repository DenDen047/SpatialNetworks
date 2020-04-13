#!/bin/bash

# plot spatial locations of each layer
python main.py --labels 10 split \
    --method greedy \
    --where 2 3 \
    --data /data/split \
    --model /result/models/model \
    --save /result/split