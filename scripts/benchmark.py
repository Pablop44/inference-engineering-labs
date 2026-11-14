import argparse
import math
import random
import statistics
from time import perf_counter


def infer(batch, weights):
    return [
        max(
            range(len(weights)),
            key=lambda label: sum(x * w for x, w in zip(features, weights[label])),
        )
        for features in batch
    ]


def benchmark(batch_size, runs):
    rng = random.Random(42)
    weights = [[rng.uniform(-1, 1) for _ in range(128)] for _ in range(16)]
    batch = [[rng.random() for _ in range(128)] for _ in range(batch_size)]
    for _ in range(5):
        infer(batch, weights)

    durations = []
    for _ in range(runs):
        start = perf_counter()
        infer(batch, weights)
        durations.append(perf_counter() - start)

    return {
        "batch_size": batch_size,
        "p50_ms": statistics.median(durations) * 1000,
        "p95_ms": sorted(durations)[math.ceil(0.95 * runs) - 1] * 1000,
        "samples_per_second": batch_size * runs / sum(durations),
    }


def positive_int(value):
    number = int(value)
    if number < 1:
        raise argparse.ArgumentTypeError("expected a positive integer")
    return number


def main():
    parser = argparse.ArgumentParser(description="Benchmark a toy CPU classifier.")
    parser.add_argument("--batch-sizes", type=positive_int, nargs="+", default=[1, 8, 32])
    parser.add_argument("--runs", type=positive_int, default=100)
    args = parser.parse_args()

    print("batch_size,p50_ms,p95_ms,samples_per_second")
    for size in args.batch_sizes:
        result = benchmark(size, args.runs)
        print(f"{size},{result['p50_ms']:.3f},{result['p95_ms']:.3f},{result['samples_per_second']:.1f}")


if __name__ == "__main__":
    main()
