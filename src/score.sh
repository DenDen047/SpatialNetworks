#!/bin/bash

# score each network on specific task
python main.py --labels 10 score \
    --hyperparams hyperparameters.json \
    --models /result/split \
    --input sequential \
    --datasets MNIST FashionMNIST \
    --tensorboard /result/tensorboard \
    --root /datasets
