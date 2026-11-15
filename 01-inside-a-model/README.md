# Chapter 1 · Inside a model

[Learning roadmap](../README.md#learning-roadmap)

Work from linear layers to attention, generation loops, and inference bottlenecks. Each lab folder bundles its guide, notebook, and diagrams.

## Neural network building blocks

**Done**

- [1.1. Linear layers, matrix multiplication, and ReLU](neural-network-building-blocks/01-linear-layers-and-relu/README.md) · Build a linear layer, batch inputs, and compare outputs with and without ReLU.

## LLM inference and architecture

**Done**

- [1.2. LLM inference mechanics](llm-inference-and-architecture/02-llm-inference-mechanics/README.md) · Implement prefill and decode, then count how many input token IDs caching saves.
- [1.3. LLM architecture](llm-inference-and-architecture/03-llm-architecture/README.md) · Trace tensor shapes from token embeddings to next-token logits.
- [1.4. Transformer blocks](llm-inference-and-architecture/04-transformer-blocks/README.md) · Assemble a transformer block and disable each branch to isolate its effect.
- [1.5. Causal attention](llm-inference-and-architecture/05-causal-attention/README.md) · Implement causal masking and test how a future value affects earlier outputs.
- [1.6. Mixture of experts](llm-inference-and-architecture/06-mixture-of-experts/README.md) · Implement top-k routing and compare the load on each expert.

## Image and video generation

**Done**

- [1.7. Image generation inference mechanics](image-and-video-generation/07-image-generation-mechanics/README.md) · Run a toy denoising loop and count the evaluations added by guidance.
- [1.8. Image generation model architecture](image-and-video-generation/08-image-generation-architecture/README.md) · Condition a latent grid on a prompt and decode it into pixels.
- [1.9. Few-step image generation](image-and-video-generation/09-few-step-image-generation/README.md) · Compare update rules and endpoint error at different step budgets.
- [1.10. Video generation inference](image-and-video-generation/10-video-generation/README.md) · Measure flicker along a moving point and test smoothing across frames.

## Inference bottlenecks

**WIP**

- [1.11. Diagnosing inference bottlenecks](inference-bottlenecks/11-diagnosing-bottlenecks/README.md) · Estimate compute and memory time floors and compare hardware upgrades.
- [1.12. Arithmetic intensity and the roofline](inference-bottlenecks/12-arithmetic-intensity/README.md) · Count matrix multiplication FLOP and bytes, then locate the roofline limit.
- [1.13. LLM prefill and decode bottlenecks](inference-bottlenecks/13-llm-inference-bottlenecks/README.md) · Compare weight reuse in prefill and decode and estimate KV cache traffic.
- [1.14. Image generation inference bottlenecks](inference-bottlenecks/14-image-generation-bottlenecks/README.md) · Estimate how latent resolution, step count, and guidance affect attention work.
- **Planned** · Profile prefill and decode on a real model and measure KV cache growth.

## Memory-efficient attention

**Done**

- [1.15. Optimizing attention](memory-efficient-attention/15-optimizing-attention/README.md) · Match dense attention with chunked softmax and test what changes with a sliding window.
