# Chapter 1 · Inside a model

[Learning roadmap](../README.md#learning-roadmap)

Work from linear layers to attention, generation loops, and inference bottlenecks. Each lab has a guide and a notebook with embedded diagrams.

## How this chapter maps to the book

This chapter follows Chapter 2, *Models*, of Philip Kiely's *Inference Engineering* (Baseten Books), pp. 39–69. The labs use small CPU examples to make the mechanisms and cost calculations visible.

| Book section | Repo coverage | Scope |
| --- | --- | --- |
| §2.1 Neural Networks | [Lab 1.1](#neural-network-building-blocks) | Affine layers, batched matrix multiplication, and ReLU. Hidden states and encoder/decoder roles recur in Labs 1.3 and 1.8. |
| §2.2 LLM Inference Mechanics | [Labs 1.2–1.6](#llm-inference-and-architecture) | Prefill, decode, model shapes, transformer blocks, causal attention, and expert routing. Lab 1.2 starts with token IDs and uses greedy selection, with a top-k example. Tokenization, chat templates, and temperature and top-p sampling have no hands-on exercise here. |
| §2.3 Image Generation Inference Mechanics | [Labs 1.7–1.10](#image-and-video-generation) | Denoising, guidance, latent pipelines, few-step methods, and temporal consistency. The exercises simulate selected mechanisms. Learned denoisers, VAEs, and video models are reading topics here. |
| §2.4 Calculating Inference Bottlenecks | [Labs 1.11–1.14](#inference-bottlenecks) | Compute and memory time floors, arithmetic intensity, the roofline, KV traffic, and image attention work. Profiling a real model is planned. |
| §2.5 Optimizing Attention | [Lab 1.15](#memory-efficient-attention) | Online softmax, exact chunked causal attention, and sliding-window attention. The guide explains KV paging conceptually. GPU kernels, KV page allocation, and other attention variants are reading topics here. |

## Neural network building blocks

**Done**

- [1.1. Linear layers, matrix multiplication, and ReLU](01-neural-network-building-blocks/01-linear-layers-and-relu/README.md) · Build a linear layer, batch inputs, and compare outputs with and without ReLU.

## LLM inference and architecture

**Done**

- [1.2. LLM inference mechanics](02-llm-inference-and-architecture/02-llm-inference-mechanics/README.md) · Implement prefill and decode, then count how many input token IDs caching saves.
- [1.3. LLM architecture](02-llm-inference-and-architecture/03-llm-architecture/README.md) · Trace tensor shapes from token embeddings to next-token logits.
- [1.4. Transformer blocks](02-llm-inference-and-architecture/04-transformer-blocks/README.md) · Assemble a transformer block and disable each branch to isolate its effect.
- [1.5. Causal attention](02-llm-inference-and-architecture/05-causal-attention/README.md) · Implement causal masking and test how a future value affects earlier outputs.
- [1.6. Mixture of experts](02-llm-inference-and-architecture/06-mixture-of-experts/README.md) · Implement top-k routing and compare the load on each expert.

## Image and video generation

**Done**

- [1.7. Image generation inference mechanics](03-image-and-video-generation/07-image-generation-mechanics/README.md) · Run a toy denoising loop and count the evaluations added by guidance.
- [1.8. Image generation model architecture](03-image-and-video-generation/08-image-generation-architecture/README.md) · Condition a latent grid on a prompt and decode it into pixels.
- [1.9. Few-step image generation](03-image-and-video-generation/09-few-step-image-generation/README.md) · Compare update rules and endpoint error at different step budgets.
- [1.10. Video generation inference](03-image-and-video-generation/10-video-generation/README.md) · Measure flicker along a moving point and test smoothing across frames.

## Inference bottlenecks

**WIP**

- [1.11. Diagnosing inference bottlenecks](04-inference-bottlenecks/11-diagnosing-bottlenecks/README.md) · Estimate compute and memory time floors and compare hardware upgrades.
- [1.12. Arithmetic intensity and the roofline](04-inference-bottlenecks/12-arithmetic-intensity/README.md) · Count matrix multiplication FLOP and bytes, then locate the roofline limit.
- [1.13. LLM prefill and decode bottlenecks](04-inference-bottlenecks/13-llm-inference-bottlenecks/README.md) · Compare weight reuse in prefill and decode and estimate KV cache traffic.
- [1.14. Image generation inference bottlenecks](04-inference-bottlenecks/14-image-generation-bottlenecks/README.md) · Estimate how latent resolution, step count, and guidance affect attention work.
- **Planned** · Profile prefill and decode on a real model and measure KV cache growth.

## Memory-efficient attention

**Done**

- [1.15. Optimizing attention](05-memory-efficient-attention/15-optimizing-attention/README.md) · Match dense attention with chunked softmax and test what changes with a sliding window.
