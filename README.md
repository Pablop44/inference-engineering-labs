# Inference Engineering Labs

Reproducible labs for running, benchmarking, and serving machine learning models. The roadmap starts with individual model operations and builds toward an inference service tested under load.

Start with [Chapter 0. Introduction to inference engineering](docs/00-introduction.md) for the project's motivation, intended audience, and software and hardware requirements.

## Learning roadmap

[0. Introduction to inference engineering](#0-introduction-to-inference-engineering) · [1. Inside a model](#1-inside-a-model) · [2. Running and benchmarking models](#2-running-and-benchmarking-models) · [3. Optimizing generation](#3-optimizing-generation) · [4. Inference beyond text](#4-inference-beyond-text) · [5. Operating an inference service](#5-operating-an-inference-service)

- **Done** — The reading or all listed labs for the subtopic are published and verified.
- **WIP** — The subtopic is partially published or in development.
- **Coming soon** — The work is planned.

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

## 0. Introduction to inference engineering

| Subtopic | Status | Reading |
| --- | --- | --- |
| Motivation | Done | [Read section](docs/00-introduction.md#motivation) |
| Workloads and metrics | Done | [Read section](docs/00-introduction.md#choose-the-workload-before-the-metric) |
| Audience | Done | [Read section](docs/00-introduction.md#who-this-is-for) |
| Software and hardware | Done | [Read section](docs/00-introduction.md#software-and-hardware) |

## 1. Inside a model

| Subtopic | Status | Labs and planned work |
| --- | --- | --- |
| Neural network building blocks | Done | [1.1. Linear layers, matrix multiplication, and ReLU](labs/01-inside-a-model/01-linear-layers-and-relu/README.md) · Build a linear layer, batch inputs, and compare outputs with and without ReLU. |
| LLM inference and architecture | Done | [1.2. LLM inference mechanics](labs/01-inside-a-model/02-llm-inference-mechanics/README.md) · Implement prefill and decode, then count how many input token IDs caching saves.<br>[1.3. LLM architecture](labs/01-inside-a-model/03-llm-architecture/README.md) · Trace tensor shapes from token embeddings to next-token logits.<br>[1.4. Transformer blocks](labs/01-inside-a-model/04-transformer-blocks/README.md) · Assemble a transformer block and disable each branch to isolate its effect.<br>[1.5. Causal attention](labs/01-inside-a-model/05-causal-attention/README.md) · Implement causal masking and test how a future value affects earlier outputs.<br>[1.6. Mixture of experts](labs/01-inside-a-model/06-mixture-of-experts/README.md) · Implement top-k routing and compare the load on each expert. |
| Image and video generation | Done | [1.7. Image generation inference mechanics](labs/01-inside-a-model/07-image-generation-mechanics/README.md) · Run a toy denoising loop and count the evaluations added by guidance.<br>[1.8. Image generation model architecture](labs/01-inside-a-model/08-image-generation-architecture/README.md) · Condition a latent grid on a prompt and decode it into pixels.<br>[1.9. Few-step image generation](labs/01-inside-a-model/09-few-step-image-generation/README.md) · Compare update rules and endpoint error at different step budgets.<br>[1.10. Video generation inference](labs/01-inside-a-model/10-video-generation/README.md) · Measure flicker along a moving point and test smoothing across frames. |
| Inference bottlenecks | WIP | [1.11. Diagnosing inference bottlenecks](labs/01-inside-a-model/11-diagnosing-bottlenecks/README.md) · Estimate compute and memory time floors and compare hardware upgrades.<br>[1.12. Arithmetic intensity and the roofline](labs/01-inside-a-model/12-arithmetic-intensity/README.md) · Count matrix multiplication FLOP and bytes, then locate the roofline limit.<br>[1.13. LLM prefill and decode bottlenecks](labs/01-inside-a-model/13-llm-inference-bottlenecks/README.md) · Compare weight reuse in prefill and decode and estimate KV cache traffic.<br>[1.14. Image generation inference bottlenecks](labs/01-inside-a-model/14-image-generation-bottlenecks/README.md) · Estimate how latent resolution, step count, and guidance affect attention work.<br>**Planned** · Profile prefill and decode on a real model and measure KV cache growth. |
| Memory-efficient attention | Done | [1.15. Optimizing attention](labs/01-inside-a-model/15-optimizing-attention/README.md) · Match dense attention with chunked softmax and test what changes with a sliding window. |

## 2. Running and benchmarking models

| Subtopic | Status | Planned work |
| --- | --- | --- |
| Model export and runtime parity | Coming soon | Export a small PyTorch model to ONNX. Check that the outputs match within a numerical tolerance and compare latency and throughput between PyTorch and ONNX Runtime. |
| Inference engines and load testing | Coming soon | Serve a small LLM with an inference engine. Vary concurrency and measure p50 and p95 latency, tokens per second, and time to first token. |
| Profiling and kernel fusion | Coming soon | Profile an inference run to find data copies and expensive operations. On a GPU, compare a sequence of kernels with a fused implementation. |

## 3. Optimizing generation

| Subtopic | Status | Planned work |
| --- | --- | --- |
| Quantization | Coming soon | Quantize a model and measure the effects on memory usage, latency, and output quality using a fixed set of inputs. |
| Speculative decoding | Coming soon | Compare standard and speculative decoding. Measure the draft token acceptance rate and identify when speculation speeds up generation. |
| Prefix caching and KV reuse | Coming soon | Measure KV cache reuse with shared prefixes and different context lengths. |
| Tensor parallelism | Coming soon | Compare inference on one GPU with tensor parallelism across two GPUs. Measure latency and communication overhead. |
| Prefill and decode disaggregation | Coming soon | Simulate separate prefill and decode queues. Measure how the request mix and KV cache transfer costs affect latency. |

## 4. Inference beyond text

| Subtopic | Status | Planned work |
| --- | --- | --- |
| Vision-language models | Coming soon | Vary input image resolution and measure its effect on response latency and quality in a vision-language model. |
| Embedding models | Coming soon | Generate embeddings in batches and measure throughput and retrieval quality on a small set of annotated queries. |
| Speech recognition and synthesis | Coming soon | Transcribe audio with different chunk sizes and measure latency and word error rate. For speech synthesis, measure time to first audio chunk. |
| Image and video generation benchmarks | Coming soon | Vary the number of denoising steps and compare latency and generated images using fixed prompts and seeds. On a GPU, extend the experiment to short video clips and vary the frame count. |

## 5. Operating an inference service

| Subtopic | Status | Planned work |
| --- | --- | --- |
| Containers and cold starts | Coming soon | Package an inference service in a container and measure its cold-start time. |
| Concurrency, queues, and batching | Coming soon | Load-test the service to see how concurrency, queueing, and batching affect p95 latency. |
| Autoscaling and cost | Coming soon | Simulate scaling to zero and compare autoscaling policies under bursty traffic. Estimate cost from active replica time. |
| Observability and streaming | Coming soon | Instrument queueing, compute, and response times. Compare a client that waits for the full response with one that consumes tokens as they arrive. |
| Rollouts under load | Coming soon | Roll out a new version of a local service under load. Check for errors and interrupted requests during the rollout. |

## Contributing

If you reproduce a lab and get a different result, open an issue with your hardware, software versions, run command, and measurements. Pull requests are welcome for reproducibility fixes, clearer explanations, and focused experiments that fit the roadmap.

## Credits and further reading

Thanks to Philip Kiely for *Inference Engineering* (Baseten Books), the primary reference for these labs. These sections provide background for the experiments.

- **Foundations and metrics** — Chapters 0 and 1 cover inference fundamentals, model selection, latency, and throughput.
- **Hardware** — Chapter 3 covers GPU architecture, memory hierarchy, accelerator generations, and instance types.
- **Capacity and infrastructure** — Section 7.3 covers GPU provisioning and capacity across providers.
- **Glossary and further reading** — Appendices A and B.
