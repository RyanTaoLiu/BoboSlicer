from abc import ABC, abstractmethod
import torch
import math


## ABC
class ImplicitFunction(ABC):
    def __init__(self, **kwargs):
        pass

    def __call__(self):
        pass


class Gyroid(ImplicitFunction):
    def __init__(self):
        pass

    def __call__(self, x, y, z):
        x, y, z = x * torch.pi * 2, y* torch.pi * 2, z * torch.pi * 2
        value = torch.sin(x) * torch.cos(y) + \
            torch.sin(y) * torch.cos(z) + \
            torch.sin(z) * torch.cos(x)
        return (value > 0).type(torch.int) * 255