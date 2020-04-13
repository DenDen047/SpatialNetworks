#!/bin/bash

# split networks into task-specific subnetworks via some method
python main.py --labels 10 split \
    --method greedy \
    --where 4 5 6 7 \
    --data /data/split \
    --model /result/models/model \
    --save /result/split