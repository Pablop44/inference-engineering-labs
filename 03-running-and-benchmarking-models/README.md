# Chapter 3 · Running and benchmarking models

[Learning roadmap](../README.md#learning-roadmap)

Compare runtimes, verify numerical parity, and profile inference under load.

| Subtopic | Status | Planned work |
| --- | --- | --- |
| Model export and runtime parity | Coming soon | Export a small PyTorch model to ONNX. Check that the outputs match within a numerical tolerance and compare latency and throughput between PyTorch and ONNX Runtime. |
| Inference engines and load testing | Coming soon | Serve a small LLM with an inference engine. Vary concurrency and measure p50 and p95 latency, tokens per second, and time to first token. |
| Profiling and kernel fusion | Coming soon | Profile an inference run to find data copies and expensive operations. On a GPU, compare a sequence of kernels with a fused implementation. |
