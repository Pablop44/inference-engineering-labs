# Inference Engineering Labs

Reproducible labs for running, benchmarking, and serving machine learning models. The roadmap starts with individual model operations and builds toward an inference service tested under load.

Start with [Chapter 0. Introduction to inference engineering](docs/00-introduction.md) for the project's motivation, intended audience, and software and hardware requirements.

## Learning roadmap

| Module | Status | Subtopics |
| --- | --- | --- |
| [0. Introduction to inference engineering](docs/00-introduction.md) | Done | [Motivation](docs/00-introduction.md#motivation) · [Workloads and metrics](docs/00-introduction.md#choose-the-workload-before-the-metric) · [Audience](docs/00-introduction.md#who-this-is-for) · [Software and hardware](docs/00-introduction.md#software-and-hardware) |
| [1. Inside a model](#1-inside-a-model) | WIP | [Neural network building blocks](#neural-network-building-blocks) · [LLM inference and architecture](#llm-inference-and-architecture) · [Image and video generation](#image-and-video-generation) · [Inference bottlenecks](#inference-bottlenecks) · [Memory-efficient attention](#memory-efficient-attention) |
| [2. Running and benchmarking models](#2-running-and-benchmarking-models) | Coming soon | [Model export and runtime parity](#model-export-and-runtime-parity) · [Inference engines and load testing](#inference-engines-and-load-testing) · [Profiling and kernel fusion](#profiling-and-kernel-fusion) |
| [3. Optimizing generation](#3-optimizing-generation) | Coming soon | [Quantization](#quantization) · [Speculative decoding](#speculative-decoding) · [Prefix caching and KV reuse](#prefix-caching-and-kv-reuse) · [Tensor parallelism](#tensor-parallelism) · [Prefill and decode disaggregation](#prefill-and-decode-disaggregation) |
| [4. Inference beyond text](#4-inference-beyond-text) | Coming soon | [Vision-language models](#vision-language-models) · [Embedding models](#embedding-models) · [Speech recognition and synthesis](#speech-recognition-and-synthesis) · [Image and video generation benchmarks](#image-and-video-generation-benchmarks) |
| [5. Operating an inference service](#5-operating-an-inference-service) | Coming soon | [Containers and cold starts](#containers-and-cold-starts) · [Concurrency, queues, and batching](#concurrency-queues-and-batching) · [Autoscaling and cost](#autoscaling-and-cost) · [Observability and streaming](#observability-and-streaming) · [Rollouts under load](#rollouts-under-load) |

- **Done** — The chapter or exercises are published and verified.
- **WIP** — Exercises are in development.
- **Coming soon** — Exercises are planned.

## What to expect from a lab

The labs assume you can read Python, reason about time and space complexity, and debug a function from its failing checks. Prior experience with model internals or GPU programming is optional.

The current labs use small models and synthetic inputs so you can trace every step on a CPU. Each lab includes a guide, a worked example, and a notebook with implementation exercises and checks. Treat operation counts and toy errors as measurements of the exercise. Each lab ends with an optional systems exercise that connects its toy implementation to an inference workload. Later labs will benchmark real models.

### Run the notebooks locally

From the repository root, create a virtual environment and launch JupyterLab.

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install jupyterlab
python -m jupyterlab
```

On Windows PowerShell, activate with `.venv\Scripts\Activate.ps1`. Open a lab's `lab.ipynb` and select the Python 3 kernel. The current exercises use the Python standard library. If a check asks you to complete a function, edit and rerun its definition before rerunning the check. Restart the kernel and run all cells in order to verify your finished notebook.

## 1. Inside a model

### Neural network building blocks

- **Available** · [Lab 1.1. Linear layers, matrix multiplication, and ReLU](labs/01-inside-a-model/01-linear-layers-and-relu/README.md). Build a linear layer, apply it to a batch, and see how an activation changes a two-layer network.

### LLM inference and architecture

- **Available** · [Lab 1.2. LLM inference mechanics](labs/01-inside-a-model/02-llm-inference-mechanics/README.md)
- **Available** · [Lab 1.3. LLM architecture](labs/01-inside-a-model/03-llm-architecture/README.md)
- **Available** · [Lab 1.4. Transformer blocks](labs/01-inside-a-model/04-transformer-blocks/README.md)
- **Available** · [Lab 1.5. Causal attention](labs/01-inside-a-model/05-causal-attention/README.md)
- **Available** · [Lab 1.6. Mixture of experts](labs/01-inside-a-model/06-mixture-of-experts/README.md)

### Image and video generation

- **Available** · [Lab 1.7. Image generation inference mechanics](labs/01-inside-a-model/07-image-generation-mechanics/README.md)
- **Available** · [Lab 1.8. Image generation model architecture](labs/01-inside-a-model/08-image-generation-architecture/README.md)
- **Available** · [Lab 1.9. Few-step image generation](labs/01-inside-a-model/09-few-step-image-generation/README.md)
- **Available** · [Lab 1.10. Video generation inference](labs/01-inside-a-model/10-video-generation/README.md)

### Inference bottlenecks

- **Available** · [Lab 1.11. Diagnosing inference bottlenecks](labs/01-inside-a-model/11-diagnosing-bottlenecks/README.md)
- **Available** · [Lab 1.12. Arithmetic intensity and the roofline](labs/01-inside-a-model/12-arithmetic-intensity/README.md)
- **Available** · [Lab 1.13. LLM prefill and decode bottlenecks](labs/01-inside-a-model/13-llm-inference-bottlenecks/README.md)
- **Available** · [Lab 1.14. Image generation inference bottlenecks](labs/01-inside-a-model/14-image-generation-bottlenecks/README.md)
- **Planned** · Profile prefill and decode on a real model and measure KV cache growth.

### Memory-efficient attention

- **Available** · [Lab 1.15. Optimizing attention](labs/01-inside-a-model/15-optimizing-attention/README.md)

## 2. Running and benchmarking models

### Model export and runtime parity

- Export a small PyTorch model to ONNX. Check that the outputs match within a numerical tolerance and compare latency and throughput between PyTorch and ONNX Runtime.

### Inference engines and load testing

- Serve a small LLM with an inference engine. Vary concurrency and measure p50 and p95 latency, tokens per second, and time to first token.

### Profiling and kernel fusion

- Profile an inference run to find data copies and expensive operations. On a GPU, compare a sequence of kernels with a fused implementation.

## 3. Optimizing generation

### Quantization

- Quantize a model and measure the effects on memory usage, latency, and output quality using a fixed set of inputs.

### Speculative decoding

- Compare standard and speculative decoding. Measure the draft token acceptance rate and identify when speculation speeds up generation.

### Prefix caching and KV reuse

- Measure KV cache reuse with shared prefixes and different context lengths.

### Tensor parallelism

- Compare inference on one GPU with tensor parallelism across two GPUs. Measure latency and communication overhead.

### Prefill and decode disaggregation

- Simulate separate prefill and decode queues. Measure how the request mix and KV cache transfer costs affect latency.

## 4. Inference beyond text

### Vision-language models

- Vary input image resolution and measure its effect on response latency and quality in a vision-language model.

### Embedding models

- Generate embeddings in batches and measure throughput and retrieval quality on a small set of annotated queries.

### Speech recognition and synthesis

- Transcribe audio with different chunk sizes and measure latency and word error rate. For speech synthesis, measure time to first audio chunk.

### Image and video generation benchmarks

- Vary the number of denoising steps and compare latency and generated images using fixed prompts and seeds. On a GPU, extend the experiment to short video clips and vary the frame count.

## 5. Operating an inference service

### Containers and cold starts

- Package an inference service in a container and measure its cold-start time.

### Concurrency, queues, and batching

- Load-test the service to see how concurrency, queueing, and batching affect p95 latency.

### Autoscaling and cost

- Simulate scaling to zero and compare autoscaling policies under bursty traffic. Estimate cost from active replica time.

### Observability and streaming

- Instrument queueing, compute, and response times. Compare a client that waits for the full response with one that consumes tokens as they arrive.

### Rollouts under load

- Roll out a new version of a local service under load. Check for errors and interrupted requests during the rollout.

## Contributing

If you reproduce a lab and get a different result, open an issue with your hardware, software versions, run command, and measurements. Pull requests are welcome for reproducibility fixes, clearer explanations, and focused experiments that fit the roadmap.

## Credits and further reading

Thanks to Philip Kiely for *Inference Engineering* (Baseten Books), the primary reference for these labs. These sections provide background for the experiments.

- **Foundations and metrics** — Chapters 0 and 1 cover inference fundamentals, model selection, latency, and throughput.
- **Hardware** — Chapter 3 covers GPU architecture, memory hierarchy, accelerator generations, and instance types.
- **Capacity and infrastructure** — Section 7.3 covers GPU provisioning and capacity across providers.
- **Glossary and further reading** — Appendices A and B.
