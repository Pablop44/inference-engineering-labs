# Lab 1.2 · LLM inference mechanics

**Time** 15–20 minutes · **Hardware** CPU · **Software** Python 3 and Jupyter

## Concepts you will use

A decoder generates text one token at a time. A token is an integer ID representing a piece of text. A forward pass produces scores for possible next tokens, and greedy selection picks the highest score.

**Prefill** processes the entire prompt and gives you the scores used to pick the first generated token. In a real transformer, this pass also saves attention keys and values for the prompt positions in a **KV cache**. **Decode** then processes the latest generated token, reads the cached state, and picks another token. The last generated token has yet to enter the cache until it is fed back in.

For a two-token prompt and three generated tokens, the cached path processes input lengths `2 + 1 + 1 = 4`. Recomputing from scratch processes `2 + 3 + 4 = 9`. Both should generate the same tokens. The notebook stores IDs as a stand-in for key/value tensors and counts IDs passed to the model. Real attention still reads earlier cache entries. The toy predictor also scans the stored IDs when it computes a score. The counter tracks only new IDs passed into its interface, so it is useful for tracing reuse and cannot estimate elapsed time.

![Three steps show each model input, its generated token, and the cache after the call. The output enters the cache on the following step.](diagram.png)

## Lab plan

| Exercise | What you will do | What to look for |
| --- | --- | --- |
| 1. Prefill once | Pass the entire prompt into a fresh cache, then choose the first generated token from the scores. | Inspect the returned cache and first token separately. The cache contains the prompt while the token is ready for the next call. |
| 2. Decode and compare | Build the cached loop, then compare its token sequence and work count with the supplied recomputation loop. | Identical generated IDs establish that reuse preserved the result. Compare the input counts for one output token and for a longer generation. |

Spend about 3–4 minutes on the worked example, 10–13 minutes on the exercises, and the last few minutes explaining the results.

## From logits to the next input

Kiely breaks generation into formatting and tokenizing the request, running the model, and selecting a token from the resulting logits. The lab starts after tokenization and uses greedy selection. Sampling can retain several candidates, and a stop token or a token budget can end the decode loop.

**Optional extension.** Compare greedy selection with sampling restricted to the top two candidates. Predict which IDs remain eligible and explain which selected ID would be fed into the next decode call.

## Apply it to an inference system

**A decode budget that matches the request.** Consider two requests with the same prompt but budgets of 1 and 64 generated tokens. Predict how many times each request enters decode after prefill. Then vary the notebook's step count and explain why counting only input IDs misses the cost of scanning cached state.

## Run the lab

Follow the [local setup](../../../README.md#run-the-notebooks-locally), then open [lab.ipynb](lab.ipynb). Run the setup cell, replace each `return None` with your implementation, and run the check below it. Allow 15–20 minutes for the core exercises. The extension is optional.

**Reading** · Philip Kiely, *Inference Engineering* (Baseten Books), §2.2, pp. 46–49.

[Back to the learning roadmap](../../../README.md#learning-roadmap)
