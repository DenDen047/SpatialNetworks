# [Spatial Neural Networks](https://arxiv.org/abs/1910.02776)

| Version | Docs | Style | Python | PyTorch | Contribute | Roadmap |
|---------|------|-------|--------|---------|------------|---------|
| [![Version](https://img.shields.io/static/v1?label=&message=0.0.1&color=377EF0&style=for-the-badge)](https://arxiv.org/abs/1910.02776) | [![Documentation](https://img.shields.io/static/v1?label=&message=docs&color=EE4C2C&style=for-the-badge)](TBD)  | [![style](https://img.shields.io/static/v1?label=&message=CB&color=27A8E0&style=for-the-badge)](TBD) | [![Python](https://img.shields.io/static/v1?label=&message=3.7&color=377EF0&style=for-the-badge&logo=python&logoColor=F8C63D)](https://www.python.org/) | [![PyTorch](https://img.shields.io/static/v1?label=&message=1.2.0&color=EE4C2C&style=for-the-badge)](https://pytorch.org/) | [![Contribute](https://img.shields.io/static/v1?label=&message=guide&color=009688&style=for-the-badge)](https://github.com/szymonmaszke/torchdata/blob/master/CONTRIBUTING.md) | [![Roadmap](https://img.shields.io/static/v1?label=&message=roadmap&color=f50057&style=for-the-badge)](https://github.com/szymonmaszke/torchdata/blob/master/ROADMAP.md)

## 1. Paper abstract ([arxiv](https://arxiv.org/abs/1910.02776))

We introduce bio-inspired artificial neural networks consisting of neurons that are additionally characterized by spatial positions.
To simulate properties of biological systems we add the costs penalizing long connections and the proximity of neurons in a two-dimensional space.
Our experiments show that in the case where the network performs two different tasks, the neurons naturally split into clusters,
where each cluster is responsible for processing a different task. This behavior
not only corresponds to the biological systems, but also allows for further insight into interpretability or continual learning.

## 2. Dependencies

Dependencies are gathered inside `requirements.txt`.
We advise to use `conda` environment for easier package management.

### 2.1 Setup `conda` [optional]

- Install conda for your specific OS, see instructions [here](https://docs.conda.io/projects/conda/en/latest/user-guide/install/)
- Create new environment by issuing from shell: `$ conda create --name SpatialNetworks`
- Activate environment: `$ conda activate SpatialNetworks`
- Install `pip` within environment: `$ conda install pip`

### 2.2 Install packages

Make sure you have `pip` installed (see [documentation](https://packaging.python.org/tutorials/installing-packages/#ensure-you-can-run-pip-from-the-command-line)) and run:

```
pip install -r requirements.txt
```

Specify `--user` flag if needed.

## 3. Performing experiments

Experiments are divided into subsections.
To perform specific part use `python main.py <subsection>`.

Currently following options are available

- [x] `train` - train neural network
- [ ] `record` - record per task activations of neural network for later user with **cuda**
- [ ] `plot` - plot spatial locations of each layer
- [ ] `split` - split networks into task-specific subnetworks via some method
- [ ] `score` - score each network on specific task

Issue `python main.py <subsection> --help` to see available options for each subsection.

To help with reproducibility later, please wrap your experiments commands with `dvc` (see their [documentation](https://dvc.org/doc)).


## Basic Command

usage: main.py [-h] [--cuda] --labels LABELS {train,record,plot,split,score} ...

positional arguments:
  {train,record,plot,split,score}
                        Actions to perform:
    train               Fit neural network
    record              Record activations of saved network.
    plot                Plot recorded activations.
    split               Split neural network into per-task networks.
    score               Check performance of splitted neural networks.

optional arguments:
  -h, --help            show this help message and exit
  --cuda                Whether to use GPU instance.
  --labels LABELS       How many labels are used for classification. If more classes in dataset available, modulo will be taken from this dataset (e.g. 50
                        labels will become 5 datasets, 10 labels each).


## Train

usage: main.py train [-h] --hyperparams HYPERPARAMS [--datasets DATASETS [DATASETS ...]] [--root ROOT] --layers LAYERS [LAYERS ...]
                     [--where WHERE [WHERE ...]] --type {linear,convolution} --input {sequential,concatenate,mix} --activation ACTIVATION --save SAVE
                     --tensorboard TENSORBOARD [--task] [--proximity PROXIMITY] [--transport TRANSPORT] [--norm {l1,l2}]

optional arguments:
  -h, --help            show this help message and exit
  --hyperparams HYPERPARAMS
                        JSON file containing hyperparameters.
                        Defaults probably shouldn't be changed as those are more related to hyperparameters search rather than experiments.
  --datasets DATASETS [DATASETS ...]
                        Name of torchvision datasets used in experiment.
                        Restrictions and traits:
                        - Provided datasets have to be proper object from torchvision.datasets.
                        - Provided datasets need the same input shape.
                        - Provided datasets CAN HAVE varying number of labels (modulo will be taken).
                        This option is case sensitive.
                        Default: ['MNIST', 'FashionMNIST', 'KMNIST', 'QMNIST']
  --root ROOT           Where downloaded datasets will be saved. By default inside your temporary folder.
  --layers LAYERS [LAYERS ...]
                        Size of each hidden layer specified as integer (specify as many as you want).
                        Length of layers has to be greater than maximum index specified by '--where' option
  --where WHERE [WHERE ...]
                        Indices of layers to which we apply the spatial costs.
                        Those are calculated based on modules function, not children.
                        Check whether your model is as you desired (will be printed at the beginning of training).
                        If unspecified, the spatial costs won't be applied to any layers (default behaviour).
  --type {linear,convolution}
                        Type of layer. One of "Linear" or "Convolution" available.This option is case insensitive.
  --input {sequential,concatenate,mix}
                        Type of input (how data will be presented for the neural net). Available modes:
                        - "Sequential"
                        - "Mix"
                        - "Concatenate"
                        This option is case insensitive.
  --activation ACTIVATION
                        torch.nn module to be used as network's activation.
                        This option is case sensitive and has to be specified EXACTLY as respective class inside 'torch.nn' package.
  --save SAVE           Where best model will be saved.
  --tensorboard TENSORBOARD
                        Where tensorboard data will be saved.
  --task                Type of Sampler used for sequential inputs.
                        Either 'Random' (for random access across all tasks)or 'Task' (iterate over task sequentially as well).
                        Only used when --input is chosen to be sequential and has to be specified in this case.
                        Default: Random
  --proximity PROXIMITY
                        Proximity loss parameter specified as float for all Spatial Layers (if any).
                         Default: 0 (acts just like Linear)
  --transport TRANSPORT
                        Transport loss parameter specified as float for all Spatial Layers (if any).
                         Default: 0 (acts just like Linear)
  --norm {l1,l2}        Norm used in transport loss. Either L1 or L2. Case insensitive

## Record

usage: main.py record [-h] --model MODEL --input {sequential,concatenate,mix} [--datasets DATASETS [DATASETS ...]] --reduction {mean,variance} --save SAVE
                      [--task] [--train] [--root ROOT]

optional arguments:
  -h, --help            show this help message and exit
  --model MODEL         Path to trained model.
  --input {sequential,concatenate,mix}
                        Type of input (how data will be presented for the neural net). Available modes:
                        - "Sequential"
                        - "Mix"
                        - "Concatenate"
                        This option is case insensitive.
  --datasets DATASETS [DATASETS ...]
                        Name of torchvision datasets used in experiment.
                        Restrictions and traits:
                        - Provided datasets have to be proper object from torchvision.datasets.
                        - Provided datasets need the same input shape.
                        - Provided datasets CAN HAVE varying number of labels (modulo will be taken).
                        This option is case sensitive.
                        Default: ['MNIST', 'FashionMNIST', 'KMNIST', 'QMNIST']
  --reduction {mean,variance}
                        What reduction to use. Available options:
                        - "Mean"
                        - "Variance"
                        This option is case insensitive.
  --save SAVE           Path where recorded data will be saved.
                        Folder should be provided, structure will be created automatically.
  --task                Type of Sampler used for sequential inputs.
                        Either 'Random' (for random access across all tasks)or 'Task' (iterate over task sequentially as well).
                        Only used when --input is chosen to be sequential and has to be specified in this case.
                        Default: Random
  --train               Whether to use training or validation dataset for plot generation. If specified, use training. Default: validation dataset.
  --root ROOT           Where downloaded datasets will be saved. By default inside your temporary folder.

## Plot

usage: main.py plot [-h] [--data DATA] [--model MODEL] --save SAVE

optional arguments:
  -h, --help     show this help message and exit
  --data DATA    Folder where recorded activations from record step are stored. If specified, will plot per-task activations strength within every layer.
  --model MODEL  Path to model whose spatial parameters will be plotted.
  --save SAVE    Path where generated plots will be saved.