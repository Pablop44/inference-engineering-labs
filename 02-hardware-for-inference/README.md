# Chapter 2 · Hardware for inference

[Learning roadmap](../README.md#learning-roadmap)

A GPU model name tells you only part of what you need to know. This chapter looks at the precision, usable memory, and interconnect of the instance you would provision for an inference workload.

| Subtopic | Status | Lab |
| --- | --- | --- |
| Choosing an inference instance | Done | [2.1. Choosing an inference instance](01-choosing-an-inference-instance/README.md) · Compare dense compute quotes, test whether a replica fits a MIG partition, and check a two-GPU link against a transfer budget. |

## Hardware reference

[Data center accelerator catalog](accelerator-catalog.md) compares NVIDIA, AMD Instinct, Intel, and Google Cloud accelerators by architecture, memory capacity, and bandwidth, with links to official specifications.

## Reading map

| Book section | How it fits here |
| --- | --- |
| §3.1 GPU Architecture | Compare dense throughput at a fixed precision and separate capacity from bandwidth. |
| §3.2 GPU Architecture Generations | Use the book as a reference for accelerator families and supported data formats. |
| §3.3 Instances | Size the usable memory of a partition and evaluate a link along a multi-GPU data path. |
| §§3.4–3.5 Other Accelerators and Local Inference | Read for backend and deployment trade-offs. Local inference measurements belong in [Running and benchmarking models](../03-running-and-benchmarking-models/README.md). |

**Reading** · Philip Kiely, *Inference Engineering* (Baseten Books), Chapter 3.
