import torch

from ._dev_utils import modules


class StochasticDepth(torch.nn.Module):
    """Randomly skip module during training with specified `p`, leaving inference untouched.

    Originally proposed by Gao Huang et. al in
    `Deep Networks with Stochastic Depth <www.arxiv.org/abs/1512.03385>`__.

    Originally devised as regularization, though `other research <https://web.stanford.edu/class/cs331b/2016/projects/kaplan_smith_jiang.pdf>`__  suggests:

    - "[...] StochasticDepth Nets are less tuned for low-level feature extraction
    but more tuned for higher level feature differentiation."
    - "[...] Stochasticity does not help with the ”dead neurons” problem;
    in fact the problem is actually more pronounced in the early layers.
    Nonetheless, the Stochastic Depth Network has relatively fewer dead neurons in later layers."

    It might be useful to employ this technique onto layers closer to the bottleneck.

    Parameters
    ----------
    module: torch.nn.Module
            Any module whose output might be skipped
            (output shape of it has to be equal to the shape of inputs).
    p: float
            Probability to skip the module.

    """

    def __init__(self, module: torch.nn.Module, p: float = 0.5):
        super().__init__()
        if not 0 < p < 1:
            raise ValueError(
                "Stochastic Depth p has to be between 0 and 1, " f"but got {p}"
            )
        self.module: torch.nn.Module = module
        self.p: float = p
        self._sampler = torch.nn.Parameter(torch.Tensor(1), requires_grad=False)

    def forward(self, inputs):
        if self._sampler.uniform_() < self.p and self.training:
            return inputs
        return self.module(inputs)


class Dropout(modules.InferDimension):
    """Randomly zero out some of the tensor elements.

    Based on input shape it either creates `2D` or `3D` version of dropout for inputs of shape
    `4D`, `5D` respectively (including batch as first dimension).
    For every other dimension, standard `torch.nn.Dropout` will be used.

    Otherwise works like standard PyTorch's `Dropout <https://pytorch.org/docs/stable/nn.html#dropout-layers>`__

    Parameters
    ----------
    p: float, optional
        Probability of an element to be zeroed. Default: ``0.5``
    inplace: bool, optional
        If ``True``, will do this operation in-place. Default: ``False``

    """

    def __init__(self, p=0.5, inplace=False):
        super().__init__(p=p, inplace=inplace)

    # Dropout can have any input shape according to documentation
    def _module_not_found(self, inputs):
        return torch.nn.Dropout
