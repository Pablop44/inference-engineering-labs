# Lab 1.3 · LLM architecture

**Time** 15–20 minutes · **Hardware** CPU · **Software** Python 3 and Jupyter

## Concepts you will use

A decoder-only language model takes token IDs and produces next-token scores. An **embedding** is a lookup table with one vector per vocabulary entry. Each token gets its own row in the sequence, even when the same ID occurs twice. A position signal gives the model information about where each token appears.

The transformer stack updates those vectors while preserving the hidden width at its boundaries. A final projection, often called the **language model head**, gives each row one score per vocabulary entry. These raw scores are **logits**. During generation, the last row supplies the scores for the next token.

For two tokens, a hidden width of three, and a vocabulary size of five, the embedding output is `(2, 3)` and the head projection is `(2, 3) @ (3, 5) → (2, 5)`. Taking the final row leaves five candidate scores. The notebook uses deterministic row-wise placeholder blocks so you can focus on these interfaces. Real transformer blocks can mix information across positions through attention.

![Embedding and position signals produce three rows of width two. Decoder blocks preserve that shape. The vocabulary head produces three rows of width four. The last row predicts the next token.](diagram.png)

## Lab plan

| Exercise | What you will do | What to look for |
| --- | --- | --- |
| 1. Build the input vectors | Look up one vector per token ID and apply the supplied position convention to its first feature. | Check both the shape and the values. The embedding table should still contain its original vectors after the lookup. |
| 2. Project hidden states to logits | Complete the vocabulary projection, trace the shape after each block, and use the final logits row to choose a token. | When you append a token, the number of rows changes. The number of candidate scores per row stays tied to the vocabulary. |

Spend about 3–4 minutes on the worked example, 10–13 minutes on the exercises, and the last few minutes explaining the results.

## Reading a model configuration

Kiely uses the model configuration to connect architectural choices to runtime support. Hidden width and vocabulary size set the dimensions used in this lab. The number of blocks tells you how many times a hidden state passes through the block interface.

**Optional extension.** Change only the vocabulary size in the toy configuration. Predict which matrix shapes change, then vary the number of layers and compare again.

## Run the lab

Open [lab.ipynb](lab.ipynb) in Jupyter with a Python 3 kernel. Run the setup, replace each `return None` placeholder, and run the check directly below it. The notebook uses only the Python standard library and includes the inputs.

**Reading** · Philip Kiely, *Inference Engineering* (Baseten Books), §§2.2.1–2.2.2, pp. 49–50.

[Back to the learning roadmap](../../../README.md#learning-roadmap)
