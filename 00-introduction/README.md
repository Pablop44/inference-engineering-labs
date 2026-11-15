# Chapter 0. Introduction to inference engineering

Inference is what happens when a trained model turns an input into an output. Inference engineering covers the work of making that process fast, reliable, and economical on the hardware and under the traffic a product actually sees. A request can spend time waiting in a queue, preparing the input, running the model, or sending the output back. Measuring those stages separately tells you where to start.

## Motivation

I started this project while reading *Inference Engineering* by Philip Kiely. I wanted to put the ideas into practice by writing code, running benchmarks, and checking where my intuition held up. I'm sharing the experiments so other developers can reproduce them, compare results on their own hardware, and build on what they find.

## Why inference engineering matters now

Generative models are used in workloads with very different requirements. A coding assistant should start responding quickly, while a pipeline embedding millions of documents can trade response time for higher throughput. Every request consumes compute, and small changes in how requests are served can make a feature more affordable or usable. Stanford's 2025 AI Index reported that the price of querying models at a fixed benchmark capability fell more than 280-fold between November 2022 and October 2024. That is one historical comparison of API prices across models. [Stanford AI Index 2025](https://hai.stanford.edu/ai-index/2025-ai-index-report).

Autoregressive generation changes what a serving system has to manage. The model processes a prompt during **prefill** and produces scores used to select the first output token. During **decode**, the model feeds that token back in to predict the next one and repeats until generation stops. Intermediate attention state stored in the **KV cache** grows as the sequence grows. Different requests finish at different times, and the server has to decide which ones to run together and how much memory to give each one. PagedAttention is an example of how improving cache allocation can free memory for more concurrent requests. [PagedAttention paper](https://arxiv.org/abs/2309.06180).

The interesting part is that the best choice depends on the workload. A larger batch can increase throughput while making some users wait longer. Quantization can reduce memory use, but its effect on speed depends on the hardware and kernels, and its effect on quality needs to be measured. Learning to test these trade-offs helps you pick a runtime, size a deployment, and explain why a change helped.

## Choose the workload before the metric

Kiely's chapters on inference and prerequisites frame optimization around the application, model, and traffic. An interactive assistant might have a strict time-to-first-token target, while an offline embedding job might optimize documents per second. Decide what quality the workload needs and what delay or cost it can tolerate before comparing serving options.

Measure both model execution and client-observed latency when the lab includes a service. For example, a request with 20 ms of queueing, 50 ms of model execution, and 10 ms of delivery takes 80 ms in this simplified breakdown. Even halving model execution leaves 55 ms end to end. For interactive generation, **time to first token** is the delay from sending the request to receiving the first token. **Time per output token** describes the pace after the first token. Report a latency percentile such as p95 alongside throughput so slow requests stay visible. A p95 of 300 ms means approximately 95% of observed requests finished within 300 ms.

**Reading** · Philip Kiely, *Inference Engineering*, Chapters 0–1, especially pp. 25–26 and §§1.4.1–1.4.2, pp. 36–37.

## Who this is for

These labs are for software engineers comfortable with Python, debugging, and basic complexity analysis who want to understand inference systems. Familiarity with machine learning helps, and the labs introduce model-specific concepts as they use them. ML engineers can use them to investigate model execution. Backend and infrastructure engineers can use them to study queues, concurrency, and the cost of serving models. Familiarity with tensors and HTTP is useful as the labs progress.

## What we will build and measure

1. **[Inside a model](../01-inside-a-model/README.md)** — Implement small operations and inspect causal attention, prefill, and decode.
2. **[Hardware for inference](../02-hardware-for-inference/README.md)** — Compare instance specifications, GPU partitions, and interconnects.
3. **[Running and benchmarking models](../03-running-and-benchmarking-models/README.md)** — Compare runtimes, profile execution, and measure latency and throughput under different loads.
4. **[Optimizing generation](../04-optimizing-generation/README.md)** — Test quantization, speculative decoding, and cache reuse against baselines, then explore parallelism and disaggregation.
5. **[Inference beyond text](../05-inference-beyond-text/README.md)** — Run experiments on embeddings, images, audio, and video using metrics suited to each workload.
6. **[Operating an inference service](../06-operating-an-inference-service/README.md)** — Package a service, load-test it, and measure how cold starts, scaling, streaming, and rollouts affect clients.

We will track time to first token, time per output token, throughput, and tail latency where relevant. Each lab will state what is held fixed and what is varied, such as input length, batch size, or request concurrency. See the [roadmap](../README.md#learning-roadmap) for the current status of each module.

## Software and hardware

| Stage | Software | Hardware |
| --- | --- | --- |
| First labs | Python and an isolated environment. Use Jupyter for notebooks and install PyTorch when an exercise calls for it. | A laptop or desktop CPU for small tensor examples and models. |
| Runtime comparisons | PyTorch, Hugging Face Transformers, and ONNX Runtime as needed. Each lab will specify compatible versions. | CPU for small comparisons. PyTorch MPS is an option on supported Apple Silicon setups when the lab's operations support it. |
| GPU serving and profiling | A serving engine such as vLLM, plus CUDA-compatible drivers and tooling for NVIDIA-specific exercises. | A compatible NVIDIA GPU with enough VRAM for the selected model, cache, and batch size. Multi-GPU labs will state the number and type of devices they need. |
| Service operations | Docker or a compatible container runtime, a test client, and a load generator. | A local machine for tests with small models. GPU requirements depend on the service being tested. |

Download model weights and install runtime dependencies as each lab calls for them. Model size, precision, and context length determine memory needs. For backend details, see the official [Transformers hardware guide](https://huggingface.co/docs/transformers/main/hardware).

For GPU architecture, memory hierarchy, and accelerator families, see Chapter 3 of Philip Kiely's *Inference Engineering* (Baseten Books).

[Back to the roadmap](../README.md#learning-roadmap)
