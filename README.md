# kernel-gym

This repo will contain a collection of kernels (written in CuTe DSL) for NVIDIA GPUs. 

Initial inspiration will draw from studying the work of repos such as [QuACK](https://github.com/Dao-AILab/quack), as well as [CuTe documentation](https://docs.nvidia.com/cutlass/latest/media/docs/pythonDSL/cute_dsl.html) and samples available under the [CUTLASS repo](https://github.com/NVIDIA/cutlass). Additional work will be referenced and linked whenever relevant.

The first goal is to implement Stream-K for `sm_8x` devices, followed by variable seqlen handling. The GEMMs will then be extended to handle `sm_>=9x` devices. From there, priorities will shift to other kernels (TBD).
