# Lab 1.2 · LLM inference mechanics

**Time** 15–20 minutes · **Hardware** CPU · **Software** Python 3 and Jupyter

What work happens before the first token, and what repeats for every later token?

During **prefill**, a decoder processes the prompt and produces scores for the first new token. During **decode**, it repeatedly feeds the last generated token back in and uses cached attention state from earlier positions. The latest sampled token enters the cache when it is processed as input on the next step.

You'll use a deterministic stand-in that stores token IDs in place of key and value tensors. Counting input tokens processed by this toy model makes the effect of reusing state easy to see. The count measures work in this example. Real attention still reads prior cache entries, and elapsed time depends on the runtime and hardware.

## Run the lab

Open [lab.ipynb](lab.ipynb) in Jupyter and select a Python 3 kernel. Run the setup, make the predictions, then complete each TODO and run its check. The notebook uses only the standard library and includes all inputs.

| Time | Activity |
| --- | --- |
| 3 min | Read the setup and predict the first result. |
| 6 min | Complete and check the first implementation. |
| 6 min | Complete the second exercise and inspect the results. |
| 2–4 min | Explain what changed using the wrap-up questions. |

Reading companion for Section 2.2 of *Inference Engineering* by Philip Kiely (Baseten Books).

[Back to the learning roadmap](../../../README.md#learning-roadmap)
