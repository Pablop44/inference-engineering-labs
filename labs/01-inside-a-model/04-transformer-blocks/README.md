# Lab 1.4 · Transformer blocks

**Time** 15–20 minutes · **Hardware** CPU · **Software** Python 3 and Jupyter

What changes in a hidden state as it passes through a transformer block?

In a pre-normalization decoder block, an attention branch mixes information across positions and adds its output to the incoming hidden state. A separate feed-forward branch transforms each position's features and adds another residual update. Both branches preserve the hidden width at the point where their outputs are added.

You'll assemble the residual wiring around two supplied branches. The attention stand-in averages the current and preceding normalized rows. The feed-forward branch applies a small feature transform with ReLU. Comparing full output with branch ablations shows which positions and features each branch affects.

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
