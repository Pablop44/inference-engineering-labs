# Inference Engineering Labs

Reproducible labs for running, benchmarking, and serving machine learning models. The roadmap starts with individual model operations and builds toward an inference service tested under load.

Start with [Chapter 0. Introduction to inference engineering](docs/00-introduction.md) for the project's motivation, intended audience, and software and hardware requirements.

## Learning roadmap

| Module | Status |
| --- | --- |
| [0. Introduction to inference engineering](docs/00-introduction.md) | Done |
| [1. Inside a model](#1-inside-a-model) | Coming soon |
| [2. Running and benchmarking models](#2-running-and-benchmarking-models) | Coming soon |
| [3. Optimizing generation](#3-optimizing-generation) | Coming soon |
| [4. Inference beyond text](#4-inference-beyond-text) | Coming soon |
| [5. Operating an inference service](#5-operating-an-inference-service) | Coming soon |

- **Done** — The chapter or exercises are published and verified.
- **WIP** — Exercises are in development.
- **Coming soon** — Exercises are planned.

## What to expect from a lab

Each lab will center on a question and a runnable experiment in a notebook or Python script. A published lab will include the setup and run commands, the model and hardware used, a baseline, and the metrics to compare. Results will record the conditions that affect them, such as batch size, sequence length, or concurrency, so readers can rerun the experiment and interpret differences.

## 1. Inside a model

- Implement a linear layer and compare processing one sample at a time with batched matrix multiplication.
- Build a small causal attention implementation and observe what changes as sequence length grows.
- Instrument a small LLM to time prefill and decode separately. Record time to first token, time per output token, and KV cache growth.
- Compare operations with different arithmetic intensities and relate the measurements to estimates of bytes moved and operations performed.

## 2. Running and benchmarking models

- Export a small PyTorch model to ONNX. Check that the outputs match within a numerical tolerance and compare latency and throughput between PyTorch and ONNX Runtime.
- Serve a small LLM with an inference engine. Vary concurrency and measure p50 and p95 latency, tokens per second, and time to first token.
- Profile an inference run to find data copies and expensive operations. On a GPU, compare a sequence of kernels with a fused implementation.

## 3. Optimizing generation

- Quantize a model and measure the effects on memory usage, latency, and output quality using a fixed set of inputs.
- Compare standard and speculative decoding. Measure the draft token acceptance rate and identify when speculation speeds up generation.
- Measure KV cache reuse with shared prefixes and different context lengths.
- Compare inference on one GPU with tensor parallelism across two GPUs. Measure latency and communication overhead.
- Simulate separate prefill and decode queues. Measure how the request mix and KV cache transfer costs affect latency.

## 4. Inference beyond text

- Vary input image resolution and measure its effect on response latency and quality in a vision-language model.
- Generate embeddings in batches and measure throughput and retrieval quality on a small set of annotated queries.
- Transcribe audio with different chunk sizes and measure latency and word error rate. For speech synthesis, measure time to first audio chunk.
- Vary the number of denoising steps and compare latency and generated images using fixed prompts and seeds. On a GPU, extend the experiment to short video clips and vary the frame count.

## 5. Operating an inference service

- Package an inference service in a container and measure its cold-start time.
- Load-test the service to see how concurrency, queueing, and batching affect p95 latency.
- Simulate scaling to zero and compare autoscaling policies under bursty traffic. Estimate cost from active replica time.
- Instrument queueing, compute, and response times. Compare a client that waits for the full response with one that consumes tokens as they arrive.
- Roll out a new version of a local service under load. Check for errors and interrupted requests during the rollout.

## Contributing

If you reproduce a lab and get a different result, open an issue with your hardware, software versions, run command, and measurements. Pull requests are welcome for reproducibility fixes, clearer explanations, and focused experiments that fit the roadmap.

## Credits and further reading

Thanks to Philip Kiely for *Inference Engineering* (Baseten Books), the primary reference for these labs. These sections provide background for the experiments.

- **Foundations and metrics** — Chapters 0 and 1 cover inference fundamentals, model selection, latency, and throughput.
- **Hardware** — Chapter 3 covers GPU architecture, memory hierarchy, accelerator generations, and instance types.
- **Capacity and infrastructure** — Section 7.3 covers GPU provisioning and capacity across providers.
- **Glossary and further reading** — Appendices A and B.
