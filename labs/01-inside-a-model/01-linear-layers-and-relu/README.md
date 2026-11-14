# Lab 1.1 · Linear layers, matrix multiplication, and ReLU

**Time** 15–20 minutes · **Hardware** Any CPU · **Prerequisites** Python lists, loops, and functions

A linear layer turns input features into output features. This lab uses a model with three input features and two outputs, small enough to check by hand. You'll implement the layer, apply it to several inputs at once, and see what changes when you add an activation between two layers.

## Before you open the notebook

A single output is a dot product plus a bias. Multiply each input feature by its corresponding weight, add the products, then add the bias. The notebook stores the weights as `W` with shape `(2, 3)`. Each row contains the three weights for one output. The batch calculation uses `W.T`, which has shape `(3, 2)`. There is one bias value per output, so `b` has shape `(2,)`.

For a batch of four samples, the input matrix `X` has shape `(4, 3)`. The calculation `X @ W.T + b` produces shape `(4, 2)`, adding the same bias to every sample. A tensor library can hand this work to a matrix multiplication kernel. The lab uses Python loops so you can inspect the calculation. It focuses on shapes and correctness.

ReLU turns negative values into zero and leaves positive values alone. Two affine layers in sequence can be collapsed into one affine map. Adding ReLU between them lets the slope of the output change with the input. You'll see that change directly in a tiny network.

## Run the lab

Open [the notebook](lab.ipynb) in a Python 3 notebook environment. To use JupyterLab locally, install it in a virtual environment and run `jupyter lab` from the repository root. The notebook code uses only the Python standard library. Inputs and weights are included.

| Time | Activity |
| --- | --- |
| 5 min | Predict one output by hand, implement the layer, and run checks. |
| 6 min | Inspect the shapes, complete batch matrix multiplication, and compare with an independent reference. |
| 5–7 min | Implement ReLU and compare two-layer networks with and without it. |

Keep the weight layout fixed throughout. When the checks pass, try changing one bias and predict which outputs will move before rerunning the cells.

Inspired by the neural networks section of Philip Kiely's *Inference Engineering* (Baseten Books).

[Back to the learning roadmap](../../../README.md#learning-roadmap)
