from abc import ABC, abstractmethod

import cutlass.cute as cute

class GemmBase(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def __call__(self):
        pass
