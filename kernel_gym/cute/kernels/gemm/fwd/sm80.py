import cutlass.cute as cute

from kernel_gym.cute.kernels.gemm.base import GemmBase

def GemmFwdSm80(GemmBase):

    def __init__(self):
        pass

    @cute.jit
    def __call__(self):
        pass

    @cute.kernel
    def kernel(self):
        pass
