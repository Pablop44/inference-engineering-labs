# Lab 3.2 · CUDA kernel selection

**15–20 minutes · CPU**

[Open notebook](lab.ipynb) · [Exercise plan](#exercise-plan) · [Setup](#setup)

A runtime dispatches a kernel based on device capability, input dtype, shape, and other constraints such as alignment or layout. The fastest candidate that fails a constraint is unusable for that request. First filter for compatibility and output parity, then choose with measurements for the matching workload.

The fixture below represents fictional benchmark results at two GEMM row counts. The fast implementation requires a recent device, BF16, and an aligned input width. The baseline supports every configuration in the exercise. Use the small batch and large batch measurements independently. Real runtimes may autotune or cache a dispatch plan.

![Filter. Device, dtype and shape → Verify. Reject parity failures → Rank. Use matching measurements](../../../assets/03-running-and-benchmarking-models/01-cuda/02-cuda-kernel-selection/diagram.png)

## Exercise plan

| Exercise | What you will do | What to look for |
| --- | --- | --- |
| 1. Filter candidates | Return the names of compatible kernels with passing parity, in fixture order. A dtype of None accepts any dtype. | Alignment, device generation and parity can each remove a faster candidate. |
| 2. Select by shape | Find the eligible kernel with the lowest measured time for the specified row count. Return None if there is no measurement for any eligible kernel. | A winner at batch one can lose for a larger operation. Record dtype, layout, shape, hardware, and measurement method with a dispatch decision. |

Spend about four minutes on setup and the example, six minutes on each exercise, and a few minutes interpreting the results.

## Setup

Start with the [local notebook setup](../../../README.md#run-the-notebooks-locally). The core exercises use only the Python standard library.

## Optional extension

Add a new shape to the measurements and explain when you would re-run autotuning after a runtime or GPU change.

## Reading

Philip Kiely, *Inference Engineering* (Baseten Books), §4.1.2, pp. 98–99.

- [NVIDIA CUDA programming guide](https://docs.nvidia.com/cuda/cuda-programming-guide/02-basics/writing-cuda-kernels.html)

[Back to Chapter 3](../../README.md) · [Learning roadmap](../../../README.md#learning-roadmap)
