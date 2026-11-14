# Lab 1.3 · LLM architecture

**Time** 15–20 minutes · **Hardware** CPU · **Software** Python 3 and Jupyter

## Concepts you will use

A decoder-only language model takes token IDs and produces next-token scores. An **embedding** is a lookup table with one vector per vocabulary entry. Each token gets its own row in the sequence, even when the same ID occurs twice. A position signal gives the model information about where each token appears.

The transformer stack updates those vectors while preserving the hidden width at its boundaries. A final projection, often called the **language model head**, gives each row one score per vocabulary entry. These raw scores are **logits**. During generation, the last row supplies the scores for the next token.

For two tokens, a hidden width of three, and a vocabulary size of five, the embedding output is `(2, 3)` and the head projection is `(2, 3) @ (3, 5) → (2, 5)`. Taking the final row leaves five candidate scores. The notebook uses deterministic row-wise placeholder blocks so you can focus on these interfaces. Real transformer blocks can mix information across positions through attention.

```text
[token IDs] --> embedding lookup + position signal
                            |
                   [sequence × hidden width]
                            |
                       decoder blocks
                            |
                       vocabulary head
                            |
                   [sequence × vocabulary]
                            |
                 last row --> next token scores
```

## Lab plan

| Exercise | What you will do | What to look for |
| --- | --- | --- |
| 1. Build the input vectors | Look up one vector per token ID and apply the supplied position convention to its first feature. | Check both the shape and the values. The embedding table should still contain its original vectors after the lookup. |
| 2. Project hidden states to logits | Complete the vocabulary projection, trace the shape after each block, and use the final logits row to choose a token. | When you append a token, the number of rows changes. The number of candidate scores per row stays tied to the vocabulary. |

Spend about 3–4 minutes on the worked example, 10–13 minutes on the exercises, and the last few minutes explaining the results.

## Run the lab

Open [lab.ipynb](lab.ipynb) in Jupyter with a Python 3 kernel. Run the setup, replace each `return None` placeholder, and run the check directly below it. The notebook uses only the Python standard library and includes the inputs.

Reading companion for Section 2.2 of *Inference Engineering* by Philip Kiely (Baseten Books).

[Back to the learning roadmap](../../../README.md#learning-roadmap)
