# Lab 1.1 · Linear layers, matrix multiplication, and ReLU

**Time** 15–20 minutes · **Hardware** CPU · **Software** Python 3 and Jupyter

## Concepts you will use

A linear layer computes one weighted sum per output and adds a bias. Think of a sample as a row of measurements. Each column of the weight matrix answers a different question about those same measurements.

With input `[2, 4]`, weights `[[3, 1], [-1, 2]]`, and bias `[1, -2]`, the first output is `2×3 + 4×(-1) + 1 = 3`. The second is `2×1 + 4×2 - 2 = 8`. The row index picks an input feature and the column index picks an output. The same weights and bias apply to every sample.

A batch stacks samples into rows, so `(batch, input) @ (input, output)` produces `(batch, output)`. The inner dimensions have to match. The outer dimensions tell you how many rows and columns you get. A tensor library can execute this operation with a matrix multiplication kernel. Here we use loops to expose the arithmetic.

ReLU computes `max(0, x)` for each hidden value. Composing two affine layers gives another affine map with a constant slope. ReLU can switch a hidden feature on or off as the input crosses zero, which allows different slopes in different regions.

```text
X (4 samples × 3 features)   W (3 features × 2 outputs)
                 \              /
                  matrix multiply
                         |
                 add b to each row
                         |
                  Y (4 samples × 2 outputs)
```

## Lab plan

| Exercise | What you will do | What to look for |
| --- | --- | --- |
| 1. Build a linear layer | Work through one output by hand, then implement the same calculation for every output column. | The zero-input case isolates the bias. The single-output case checks that your loop works for a different output width. |
| 2. Process a batch | Predict the output shape, then implement a matrix product and add the bias to each row. | The result must agree with applying your first function independently to each input row. Each row is one sample. |
| 3. Add ReLU | Implement the activation and compare two networks with the same weights, one with ReLU between the layers. | Look at the two hidden values before and after ReLU. The output bends at zero because a different hidden value survives on each side. |

Spend about 3–4 minutes on the worked example, 10–13 minutes on the exercises, and the last few minutes explaining the results.

## Run the lab

Open [lab.ipynb](lab.ipynb) in Jupyter with a Python 3 kernel. Run the setup, replace each `return None` placeholder, and run the check directly below it. The notebook uses only the Python standard library and includes the inputs.

Inspired by the neural networks section of Philip Kiely's *Inference Engineering* (Baseten Books).

[Back to the learning roadmap](../../../README.md#learning-roadmap)
