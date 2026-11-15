# Chapter 4 · Optimizing generation

[Learning roadmap](../README.md#learning-roadmap)

Measure how generation techniques affect latency, memory use, and output quality.

| Subtopic | Status | Planned work |
| --- | --- | --- |
| Quantization | Coming soon | Quantize a model and measure the effects on memory usage, latency, and output quality using a fixed set of inputs. |
| Speculative decoding | Coming soon | Compare standard and speculative decoding. Measure the draft token acceptance rate and identify when speculation speeds up generation. |
| Prefix caching and KV reuse | Coming soon | Measure KV cache reuse with shared prefixes and different context lengths. |
| Tensor parallelism | Coming soon | Compare inference on one GPU with tensor parallelism across two GPUs. Measure latency and communication overhead. |
| Prefill and decode disaggregation | Coming soon | Simulate separate prefill and decode queues. Measure how the request mix and KV cache transfer costs affect latency. |
