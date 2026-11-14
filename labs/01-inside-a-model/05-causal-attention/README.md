# Lab 1.5 · Causal attention

**Time** 15–20 minutes · **Hardware** CPU · **Software** Python 3 and Jupyter

Which earlier positions can influence the hidden state at the current position?

Attention compares a **query** with each **key**, scales the dot products, and converts scores to weights using softmax. Those weights mix the corresponding **value** vectors. The causal mask excludes keys from future positions before softmax so those positions contribute zero weight.

You'll start with fixed queries, keys, and values to isolate attention itself. Inspect the weight rows, flip the mask off as a baseline, then change the final input value to test where it can have an effect.

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
