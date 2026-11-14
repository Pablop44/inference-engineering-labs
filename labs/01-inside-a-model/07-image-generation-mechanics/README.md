# Lab 1.7 · Image generation inference mechanics

**Time** 15–20 minutes · **Hardware** CPU · **Software** Python 3 and Jupyter

Why does an image generator call its denoiser repeatedly?

A diffusion-style pipeline starts with random values. At each step the model estimates a direction for changing the current sample. A **scheduler** determines the noise levels or timesteps to visit and how to use each prediction to update the sample. The updated sample becomes the next model input. In many pipelines this loop runs on a latent grid, which is decoded into pixels at the end.

We will use a 6 × 6 pixel grid and a supplied **oracle** that knows the target. This makes the update easy to follow. A trained denoiser has to estimate its direction from noisy input and conditioning. In this lab, if the current pixel is 0.8 and the oracle target is 0.2, the direction is −0.6. A step of size 0.5 produces 0.5. Repeating the same rule gives 0.35.

![Four pixel grids show seeded noise approaching a bright diamond after one, two, and four updates.](diagram.png)

| Exercise | What you will do | What to inspect |
| --- | --- | --- |
| 1. Update a grid | Apply one predicted direction with two step sizes. | Compare the same pixel before and after the update. |
| 2. Run the loop | Feed each updated grid into the next prediction. | Inspect the snapshots, error, and number of model calls. |

## Run the lab

Open [lab.ipynb](lab.ipynb) in Jupyter and select a Python 3 kernel. Run the setup, make the predictions, then complete each TODO and run its check. The notebook uses only the standard library and includes all inputs.

| Time | Activity |
| --- | --- |
| 3 min | Read the setup and predict the first result. |
| 6 min | Complete and check the first implementation. |
| 6 min | Complete the second exercise and inspect the results. |
| 2–4 min | Explain what changed using the wrap-up questions. |

Reading companion for Section 2.3 of *Inference Engineering* by Philip Kiely (Baseten Books).

[Back to the learning roadmap](../../../README.md#learning-roadmap)
