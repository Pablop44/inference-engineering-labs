# Lab 1.13 · LLM prefill and decode bottlenecks

**Time** 15–20 minutes · **Hardware** CPU · **Software** Python 3 and Jupyter

Why can the limiting resource change between the prompt and the generated tokens?

In Kiely's comparison, prefill processes many prompt positions together and can reuse model weights across those positions. One decode step processes one new position per active sequence and typically has less weight reuse. Batching decode requests increases reuse, while longer contexts can increase traffic from reading cached keys and values. These are tendencies. Shapes, hardware, and implementation can change the result.

We use two separate estimates. First, a FP16 projection has ideal intensity `2MKN / [2(MK + KN + MN)]` for M rows. For K=N=1024, M=1 gives about 1 FLOP/byte and M=256 about 171 FLOP/byte. Second, a cached attention step reads K and V for earlier tokens. With 4 key/value positions, 2 KV heads, a head width of 8, and 2 bytes per value, that is `2 × 4 × 2 × 8 × 2 = 256` bytes per layer per sequence. The factor of two counts the K and V arrays. A single cached query uses one row of scores per query head. A full multi-query attention calculation has more than one row.

![Projection intensity rises from about 1 to 30 to 171 FLOP per byte across the three scenarios.](diagram.png)

Here, M counts rows processed together by a projection. Those rows can come from one long prompt or from several sequences during decode. The projection estimate assumes one weight read, while the KV estimate counts separate reads for each sequence. Compare them as two sources of work and traffic before reasoning about the whole model.

## Lab plan

| Exercise | What you will do | What to inspect |
| --- | --- | --- |
| 1. Compare projection reuse | Vary rows for unbatched decode, batched decode, and prefill. | Which scenarios reach the ridge? |
| 2. Estimate KV reads | Vary context and batch size with a fixed KV head layout. | How much cache traffic grows independently of the shared weights? |

## Run the lab

Follow the [local setup](../../../README.md#run-the-notebooks-locally), then open [lab.ipynb](lab.ipynb). Run the setup, make the predictions, then replace each `return None` placeholder and run its check. The notebook uses only the standard library and includes all inputs.

| Time | Activity |
| --- | --- |
| 3 min | Read the setup and predict the first result. |
| 6 min | Complete and check the first implementation. |
| 6 min | Complete the second exercise and inspect the results. |
| 2–4 min | Explain what changed using the wrap-up questions. |

Reading companion for Section 2.4.2, pp. 63–66 of *Inference Engineering* by Philip Kiely (Baseten Books).

[Back to the learning roadmap](../../../README.md#learning-roadmap)
