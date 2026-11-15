# Chapter 6 · Operating an inference service

[Learning roadmap](../README.md#learning-roadmap)

Measure the service as clients experience it, from cold starts and queueing to streaming and rollouts.

| Subtopic | Status | Planned work |
| --- | --- | --- |
| Containers and cold starts | Coming soon | Package an inference service in a container and measure its cold-start time. |
| Concurrency, queues, and batching | Coming soon | Load-test the service to see how concurrency, queueing, and batching affect p95 latency. |
| Autoscaling and cost | Coming soon | Simulate scaling to zero and compare autoscaling policies under bursty traffic. Estimate cost from active replica time. |
| Observability and streaming | Coming soon | Instrument queueing, compute, and response times. Compare a client that waits for the full response with one that consumes tokens as they arrive. |
| Rollouts under load | Coming soon | Roll out a new version of a local service under load. Check for errors and interrupted requests during the rollout. |
