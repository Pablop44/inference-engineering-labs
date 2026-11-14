# Lab 1.4 · Transformer blocks

**Time** 15–20 minutes · **Hardware** CPU · **Software** Python 3 and Jupyter

## Concepts you will use

A decoder block has two different jobs. Its attention branch lets earlier positions influence the current one. Its feed-forward branch transforms features within each position. Both branches return the same shape as their input so the block can add their outputs back to the hidden state. These additions are called **residual connections**.

In a pre-normalized block, the branch sees normalized features while the residual path carries the incoming features directly. For example, if a row is `[3, 1]` and the branch returns `[-1, 2]`, the updated row is `[2, 3]`. The second branch reads this updated row after normalization.

The notebook supplies prefix averaging as a stand-in for causal attention and a tiny ReLU feature transform as the feed-forward branch. Turning branches off lets you separate cross-position mixing from within-position transformations. Lab 1.5 replaces the averaging idea with explicit attention scores.

![The input goes through normalization and attention, and bypasses both via a residual connection. The updated state then does the same for the feed-forward branch.](diagram.png)

## Lab plan

| Exercise | What you will do | What to look for |
| --- | --- | --- |
| 1. Wire a residual update | Implement elementwise addition for two matrices of identical shape, then use it for the mixing branch. | Each feature receives its own update and the output has the same sequence length and hidden width. |
| 2. Assemble and ablate | Run both updates in order and compare with runs that disable one branch at a time. | Change an early input and inspect later rows. Without the mixing branch, an earlier row cannot change a later row. |

Spend about 3–4 minutes on the worked example, 10–13 minutes on the exercises, and the last few minutes explaining the results.

## Hidden width and feed-forward weights

The book separates the embedding, repeated blocks, and vocabulary head. Within a block it distinguishes attention, normalization, and the feed-forward network. The toy feed-forward function stands in for a position-wise network. In a simple two-projection version, the intermediate width can be larger than the residual width.

**Optional extension.** Count the weights for the expansion and contraction of a width-4 feed-forward branch with intermediate widths 8 and 16. Explain why the output can still be added to a width-4 residual.

## Run the lab

Open [lab.ipynb](lab.ipynb) in Jupyter with a Python 3 kernel. Run the setup, replace each `return None` placeholder, and run the check directly below it. The notebook uses only the Python standard library and includes the inputs.

**Reading** · Philip Kiely, *Inference Engineering* (Baseten Books), §2.2.2, pp. 50–51.

[Back to the learning roadmap](../../../README.md#learning-roadmap)
