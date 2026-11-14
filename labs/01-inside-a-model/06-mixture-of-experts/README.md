# Lab 1.6 · Mixture of experts

**Time** 15–20 minutes · **Hardware** CPU · **Software** Python 3 and Jupyter

How can a model have many expert parameters while running only a few experts per token?

A mixture-of-experts layer can replace the feed-forward branch with several expert networks and a **router** that scores the experts for each token. A top-k router selects a small subset and combines their outputs with routing weights. If many tokens select the same expert, it may have more work than its peers.

You'll supply the routing and combination logic for three scalar experts, then compare top-1 and top-2 routing on deliberately skewed scores. Inspect the trade-off between expert calls and load balance. The counts are a proxy for work. Real throughput also depends on how tokens are batched and moved between devices.

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
