# Lab 1.11 · Diagnosing inference bottlenecks

**Time** 15–20 minutes · **Hardware** CPU · **Software** Python 3 and Jupyter

[Open notebook](lab.ipynb) · [Exercise plan](#lab-plan) · [Results to look for](#results-to-look-for)

Which resource should you improve first?

Kiely starts with two resources. **Compute throughput** tells you how many floating-point operations the hardware can execute per second. **Memory bandwidth** tells you how many bytes it can move per second. Work divided by throughput gives a compute time floor. Traffic divided by bandwidth gives a movement time floor. If both resources could overlap perfectly, execution would still take at least the larger of the two. Real latency can be longer because of imperfect overlap, synchronization, or overhead.

For 3 GFLOP and 100 MB on a device with 6 TFLOP/s and 200 GB/s, the two floors are both 0.5 ms. Doubling only compute leaves the movement floor at 0.5 ms. The point of the calculation is to rule in promising optimizations before measuring them.

![Compute and memory time floors in milliseconds for two workloads.](diagram.png)

A speedup of 1× means the modeled floor stayed the same. Compare the two component times again after an upgrade. If they were close to begin with, reducing one can make the other the new bottleneck.

## Results to look for

![Compare time floors in milliseconds. Workload A: 2.00 vs 0.25. Compute floor is larger; Workload B: 0.25 vs 1.50. Memory floor is larger; Upgrade: Recompute both. A different floor can dominate.](result-preview.png)

1. Compute both times in seconds, then convert for display. Compare the larger value separately for each workload.
2. A gain applies to the modeled floor. Check where the two floors cross before extrapolating the speedup.

## Lab plan

| Exercise | What you will do | What to inspect |
| --- | --- | --- |
| 1. Calculate time floors | Compute the two resource times and identify the larger. | Which workload is limited by which resource? |
| 2. Change one resource | Try faster compute and faster memory separately. | Which intervention improves the modeled latency? |

## Apply it to an inference system

**When a bottleneck moves.** For workload A, estimate the compute multiplier at which the memory floor first becomes limiting. If a profiler reports a large gap between the model's floor and measured latency, list one source of that gap you could isolate with timing events.

## Run the lab

Follow the [local setup](../../../README.md#run-the-notebooks-locally), then open [lab.ipynb](lab.ipynb). Run the setup, make the predictions, then replace each `return None` placeholder and run its check. The notebook uses only the standard library and includes all inputs.

| Time | Activity |
| --- | --- |
| 3 min | Read the setup and predict the first result. |
| 6 min | Complete and check the first implementation. |
| 6 min | Complete the second exercise and inspect the results. |
| 2–4 min | Explain what changed using the wrap-up questions. |

Reading companion for Section 2.4, pp. 61–62 of *Inference Engineering* by Philip Kiely (Baseten Books).

[Back to Chapter 1](../../README.md#inference-bottlenecks) · [Learning roadmap](../../../README.md#learning-roadmap)
