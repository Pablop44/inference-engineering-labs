# Lab 1.5 · Causal attention

**Time** 15–20 minutes · **Hardware** CPU · **Software** Python 3 and Jupyter

[Open notebook](lab.ipynb) · [Exercise plan](#lab-plan) · [Results to look for](#results-to-look-for)

## Concepts you will use

Attention uses a **query** to ask what information is relevant, a **key** to score how well each source position matches, and a **value** to supply the information to mix. For one query, take its dot product with each key and divide by the square root of the key width. Softmax turns the resulting scores into nonnegative weights that sum to one.

For query `[1, 0]` and keys `[1, 0]` and `[0, 1]`, the scaled scores are about `[0.707, 0]`. If both keys are visible, the weights are about `[0.67, 0.33]`. With values `[3, 0]` and `[0, 6]`, the weighted output is about `[2.01, 1.98]`.

**Causal** attention means position i can read positions up to and including i. For the first query in the example, masking the second score before softmax gives weights `[1, 0]` and output `[3, 0]`. The notebook holds queries, keys, and values fixed so you can isolate what scoring and masking do. In a model, learned projections produce these vectors. Self-attention projects them from the same sequence. Cross-attention takes queries from one sequence and keys and values from another.

![A three-by-three causal mask with six visible query-key pairs. Scaled query-key scores are masked before softmax, then used to mix value vectors.](diagram.png)

## Results to look for

![Follow the weight, then the value. Score: [0.707, 0]. Scaled matches for one query; Mask + softmax: [1, 0]. Remove the future key; Value mix: [3, 0]. All weight on the first value.](result-preview.png)

1. Check visibility before interpreting the output. A future key should have zero probability after masking and softmax.
2. Change the last value and inspect earlier rows. Their exact match is evidence that future values cannot leak into them.

## Lab plan

| Exercise | What you will do | What to look for |
| --- | --- | --- |
| 1. Score and mask keys | Compute one scaled dot product per key. Use negative infinity for future keys when the causal mask is enabled. | Inspect the first softmax row. The first position can only attend to itself, so all weight goes to that key. |
| 2. Mix values and test causality | Use the weights to build the output vector, then change only the final value and compare masked and unmasked runs. | With masking, the final value can affect the last output, while earlier outputs stay fixed. The unmasked run provides a comparison. |

Spend about 3–4 minutes on the worked example, 10–13 minutes on the exercises, and the last few minutes explaining the results.

## Prefill versus cached decode attention

Kiely distinguishes self-attention from cross-attention and connects the KV cache to repeated decoding. This lab uses causal self-attention. For a length-L prompt, the causal mask allows L(L+1)/2 query-key pairs during prefill. A single subsequent decode query can attend to L cached keys and its own new key, so that step has L+1 pairs. These are logical counts. A kernel can perform a different amount of work.

**Optional extension.** Double the prompt length from 4 to 8. Compare how the visible prefill pairs and the pairs for one cached decode query grow.

## Apply it to an inference system

At fixed head width, one cached decode query scores a number of keys proportional to the current context length. For a prompt of P tokens and G decode queries, the total number of pairs across decode is GP + G(G+1)/2. The cache saves recomputing earlier key and value projections, while the context still grows.

**Causality as an output invariant.** Repeat the future-value perturbation with a larger magnitude and verify that earlier causal outputs are still unchanged. Explain why this is a stronger check than verifying only that each probability row sums to one.

## Run the lab

Follow the [local setup](../../../README.md#run-the-notebooks-locally), then open [lab.ipynb](lab.ipynb). Run the setup cell, replace each `return None` with your implementation, and run the check below it. Allow 15–20 minutes for the core exercises. The extension is optional.

**Reading** · Philip Kiely, *Inference Engineering* (Baseten Books), §2.2.3, pp. 52–53.

[Back to the learning roadmap](../../../README.md#learning-roadmap)
