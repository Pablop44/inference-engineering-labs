# Lab 1.3 · LLM architecture

**Time** 15–20 minutes · **Hardware** CPU · **Software** Python 3 and Jupyter

How do token IDs become scores over a vocabulary?

A decoder-only model looks up a vector for each input token, processes those vectors through a stack of blocks, then projects the hidden vectors into vocabulary-sized scores. Those scores are called **logits**. The logits for the final sequence position predict the next token. A position signal helps distinguish positions in the sequence.

This notebook supplies two deterministic toy blocks in place of a real transformer. Follow the shapes at each boundary and inspect how selecting a row of logits changes the predicted token. The weight convention is the same as Lab 1.1, with one column per output.

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
