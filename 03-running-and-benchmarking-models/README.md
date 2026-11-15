# Chapter 3 · Running and benchmarking models

[Learning roadmap](../README.md#learning-roadmap)

Start at the CUDA execution model, then move up the stack to tensor frameworks, artifact formats, and inference runtimes. The exercises separate dispatch, numerical correctness, and performance measurements.

| Subtopic | Status | What you will do |
| --- | --- | --- |
| [CUDA](#cuda) | Done | Trace a kernel launch, choose a compatible implementation, and count the traffic removed by fusion. |
| [Frameworks and libraries](#frameworks-and-libraries) | Done | Run PyTorch in inference mode, inspect weights, verify an ONNX export, and use Transformers and Diffusers components. |
| Inference engines and load testing | Coming soon | Measure p50 and p95 latency, tokens per second, and time to first token under concurrent traffic. |
| Runtime profiling | Coming soon | Profile inference to identify data movement and expensive operators, and measure fusion on a real GPU. |

## CUDA

CUDA exposes the GPU execution and memory model. A kernel is one device operation. The runtime handles launches and memory operations, the driver connects those operations to the device, and CUDA Graphs can capture repeated workflows. The core exercises model launch indexing, dispatch, and array traffic on CPU. Lab 3.1 also includes a CUDA C++ launch for a machine with an NVIDIA GPU and CUDA toolkit.

- [3.1. CUDA kernels for inference](01-cuda/01-cuda-kernels/README.md) · Map logical threads to tensor elements and handle tail elements.
- [3.2. CUDA kernel selection](01-cuda/02-cuda-kernel-selection/README.md) · Filter incompatible kernels and choose from shape-specific measurements.
- [3.3. Kernel fusion and memory traffic](01-cuda/03-kernel-fusion/README.md) · Check output parity and count the traffic saved by removing an intermediate.

## Frameworks and libraries

Frameworks expose tensor programs, artifact formats capture weights or graphs, and runtimes execute them on a target device. The core exercises run on CPU. Lab 3.6 includes an optional TensorRT path on NVIDIA hardware.

- [3.4. PyTorch inference execution](02-frameworks-and-libraries/04-pytorch-inference/README.md) · Separate evaluation behavior from autograd and verify batch parity.
- [3.5. Model file formats](02-frameworks-and-libraries/05-model-file-formats/README.md) · Inspect Safetensors metadata and restore weights into a known architecture.
- [3.6. ONNX Runtime and TensorRT](02-frameworks-and-libraries/06-onnx-runtime-and-tensorrt/README.md) · Export a dynamic ONNX graph and verify ONNX Runtime output against PyTorch.
- [3.7. Transformers and Diffusers](02-frameworks-and-libraries/07-transformers-and-diffusers/README.md) · Trace causal-LM logits and the state updates of a diffusion scheduler.

## Reading

Philip Kiely, *Inference Engineering* (Baseten Books), Chapter 4, §§4.1–4.2.4, pp. 96–105.
