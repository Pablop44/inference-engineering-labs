# Data center accelerator catalog

[Hardware for inference](README.md) · [Lab 2.1](01-choosing-an-inference-instance/README.md)

A reference for reading instance specifications before sizing or benchmarking a workload. It covers major generations of NVIDIA data center GPUs, AMD Instinct, and Intel data center accelerators, with representative models, selected legacy hardware, and publicly documented newer designs. The vendor indexes cover additional SKUs. Cloud availability depends on the provider, region, and instance. The presence of a specification here does not establish availability.

## How to compare rows

- **Capacity** is the advertised device memory, unless the row explicitly describes a shared pool. Check usable memory in the actual runtime or partition before budgeting weights and KV cache.
- **Bandwidth** is peak device memory bandwidth. It is a different figure from PCIe, NVLink, Infinity Fabric, or network bandwidth.
- **Compute** figures in the notes are theoretical peaks. Compare the same precision and sparsity mode. The linked specifications provide the full precision, interconnect, and power tables where published.
- **Topology** is a property of the instance as well as the accelerator. Check the exact PCIe, SXM, OAM, or rack configuration and the usable directional bandwidth for your data path.

## NVIDIA

CUDA GPUs across the major data center generations discussed in the book and selected predecessors. NVIDIA's [data center hardware index](https://docs.nvidia.com/ai-enterprise/release-8/latest/infra-software/vgpu/reference/index.html) lists further supported configurations, and the [MIG guide](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/latest/supported-gpus.html) lists partition-capable devices.

| Architecture | Model or configuration | Memory | Peak memory bandwidth | Compute or deployment detail | Official specs |
| --- | --- | --- | --- | --- | --- |
| Pascal | Tesla P4 | 8 GB GDDR5 | 192 GB/s | Legacy PCIe inference accelerator | [NVIDIA platform comparison](https://www.nvidia.com/en-gb/deep-learning-ai/solutions/inference-platform/hpc/) |
| Pascal | Tesla P40 | 24 GB GDDR5 | 346 GB/s | Legacy PCIe inference accelerator | [NVIDIA platform comparison](https://www.nvidia.com/en-gb/deep-learning-ai/solutions/inference-platform/hpc/) |
| Pascal | Tesla P100, SXM2 | 16 GB HBM2 | 732 GB/s | Legacy SXM2 configuration | [P100 datasheet](https://www.nvidia.com/content/dam/en-zz/Solutions/Data-Center/tesla-p100/pdf/nvidia-tesla-p100-datasheet.pdf) |
| Volta | Tesla V100, PCIe or SXM2 | 16 or 32 GB HBM2 | 900 GB/s | Separate V100S variant in the linked table | [V100 specification table](https://www.nvidia.com/en-in/data-center/v100/) |
| Turing | T4 | 16 GB GDDR6 | 320+ GB/s | 70 W PCIe card | [T4 specifications](https://www.nvidia.com/en-us/data-center/tesla-t4/) |
| Ampere | A100 80 GB, PCIe | 80 GB HBM2e | 1,935 GB/s | 312 TFLOP/s dense BF16 | [A100 specifications](https://www.nvidia.com/en-us/data-center/a100/) |
| Ampere | A100 80 GB, SXM | 80 GB HBM2e | 2,039 GB/s | 312 TFLOP/s dense BF16 | [A100 specifications](https://www.nvidia.com/en-us/data-center/a100/) |
| Ada Lovelace | L4 | 24 GB GDDR6 | 300 GB/s | Low-profile PCIe card | [L4 specifications](https://www.nvidia.com/en-us/data-center/l4/) |
| Ada Lovelace | L40S | 48 GB GDDR6 | 864 GB/s | About 362 TFLOP/s dense BF16 | [L40S specifications](https://www.nvidia.com/en-us/data-center/l40s/) |
| Hopper | H100 SXM | 80 GB HBM3 | 3.35 TB/s | NVLink and MIG support | [H100 specifications](https://www.nvidia.com/en-us/data-center/h100/) |
| Hopper | H100 NVL, per GPU | 94 GB HBM3 | 3.9 TB/s | PCIe form factor, NVLink bridge | [H100 specifications](https://www.nvidia.com/en-us/data-center/h100/) |
| Hopper | H200 SXM | 141 GB HBM3e | 4.8 TB/s | HGX configuration | [HGX specifications](https://docs.nvidia.com/enterprise-reference-architectures/whitepaper/hgx-servers-and-spectrum-x.pdf) |
| Blackwell | B200 SXM, HGX | 180 GB HBM3e | Up to 8 TB/s | Per-GPU figure for the cited HGX configuration | [HGX specifications](https://docs.nvidia.com/enterprise-reference-architectures/whitepaper/hgx-servers-and-spectrum-x.pdf) |
| Blackwell | RTX PRO 6000 Blackwell Server Edition | 96 GB GDDR7 | 1,597 GB/s | PCIe card with MIG support | [RTX PRO 6000 specifications](https://www.nvidia.com/en-us/data-center/rtx-pro-6000-blackwell-server-edition/) |
| Blackwell Ultra | B300 SXM, HGX | 288 GB HBM3e | Up to 8 TB/s | Per-GPU figure for the cited HGX configuration | [HGX specifications](https://docs.nvidia.com/enterprise-reference-architectures/whitepaper/hgx-servers-and-spectrum-x.pdf) |
| Rubin | Rubin GPU | Up to 288 GB HBM4 | Up to 22 TB/s | Published architecture figures, NVLink 6 | [Rubin architecture specifications](https://developer.nvidia.com/blog/inside-nvidia-rubin-gpu-architecture-powering-the-era-of-agentic-ai/) |

## AMD Instinct

AMD's [accelerator specification index](https://www.amd.com/en/products/specifications/accelerators.html) provides SKU-level details. The [ROCm hardware documentation](https://rocm.docs.amd.com/projects/ai-ecosystem/en/latest/optimization/workload-optimization.html) also describes data formats and partition modes for several Instinct models.

| Architecture | Model or configuration | Memory | Peak memory bandwidth | Compute or deployment detail | Official specs |
| --- | --- | --- | --- | --- | --- |
| CDNA | MI100 | 32 GB HBM2 | 1.2 TB/s | PCIe card | [AMD accelerator specs](https://www.amd.com/en/products/specifications/accelerators.html) |
| CDNA 2 | MI210 | 64 GB HBM2e | 1.6 TB/s | PCIe card | [AMD accelerator specs](https://www.amd.com/en/products/specifications/accelerators.html) |
| CDNA 2 | MI250 / MI250X | 128 GB HBM2e | 3.2 TB/s | Aggregate per dual-die module | [MI200 series specifications](https://www.amd.com/en/products/accelerators/instinct/mi200.html) |
| CDNA 3 | MI300A | 128 GB HBM3, shared CPU/GPU | ~5.3 TB/s | APU with a coherent memory pool | [MI300A specifications](https://www.amd.com/en/products/accelerators/instinct/mi300/mi300a.html) |
| CDNA 3 | MI300X | 192 GB HBM3 | 5.3 TB/s | ~1.31 PFLOP/s dense BF16 | [MI300 series specifications](https://www.amd.com/en/products/accelerators/instinct/mi300.html) |
| CDNA 3 | MI325X | 256 GB HBM3e | 6 TB/s | ~1.31 PFLOP/s dense BF16 | [MI325X specifications](https://www.amd.com/en/products/accelerators/instinct/mi300/mi325x.html) |
| CDNA 4 | MI350P | 144 GB HBM3e | 4 TB/s | PCIe add-in card | [AMD accelerator specs](https://www.amd.com/en/products/specifications/accelerators.html) |
| CDNA 4 | MI350X / MI355X | 288 GB HBM3e | 8 TB/s | OAM modules with MX formats | [MI350X specs](https://www.amd.com/en/products/accelerators/instinct/mi350/mi350x.html), [MI355X specs](https://www.amd.com/en/products/accelerators/instinct/mi350/mi355x.html) |
| CDNA 5 | MI450X | 288 GB HBM4 | 23.3 TB/s | Published MI400-series specification | [MI450X datasheet](https://www.amd.com/content/dam/amd/en/documents/products/accelerators/instinct/amd-instinct-mi450x-brochure.pdf) |
| CDNA 5 | MI455X | 432 GB HBM4 | Up to 23.3 TB/s | Published per-accelerator figure for Helios | [CDNA 5 architecture](https://www.amd.com/en/technologies/cdna.html) |

## Intel

Gaudi devices are dedicated AI accelerators. Intel Flex and Max are GPUs with different execution stacks from Gaudi. Check the linked hardware and runtime documentation before porting an inference workload. Intel's [data center GPU index](https://www.intel.com/content/www/us/en/ark/products/series/210574/data-center-gpu.html) covers additional GPU variants.

| Architecture or family | Model or configuration | Memory | Peak memory bandwidth | Compute or deployment detail | Official specs |
| --- | --- | --- | --- | --- | --- |
| Habana Gaudi | Gaudi (first generation) | 32 GB | See vendor reference | Legacy generation | [Intel Gaudi launch comparison](https://download.intel.com/newsroom/2022/corporate/vision/Habana-Gaudi2-Launch-Fact-Sheet.pdf) |
| Habana Gaudi | Gaudi 2 | 96 GB HBM2e | 2.45 TB/s | BF16, FP16, and FP8 support | [Gaudi 2 white paper](https://cdrdv2-public.intel.com/839363/Intel-Gaudi2-AI-Accelerators-whitepaper.pdf) |
| Habana Gaudi | Gaudi 3 | 128 GB HBM2e | 3.7 TB/s | Dedicated AI accelerator | [Gaudi 3 white paper](https://cdrdv2-public.intel.com/817486/gaudi-3-ai-accelerator-white-paper.pdf) |
| Xe-HPG | Data Center GPU Flex 170 | 16 GB GDDR6 | 576 GB/s | PCIe 4.0 x16 | [Flex 170 specifications](https://www.intel.com/content/www/us/en/products/sku/230019/intel-data-center-gpu-flex-170/specifications.html) |
| Xe-HPC | Data Center GPU Max 1550 | 128 GB HBM2e | 3,276.8 GB/s | PCIe 5.0 x16 host interface | [Max 1550 specifications](https://www.intel.com/content/www/us/en/products/sku/232873/intel-data-center-gpu-max-1550/specifications.html) |
| Xe3P | Crescent Island | 160 GB LPDDR5X (announced) | Unspecified in cited announcement | Published design details | [Intel announcement](https://www.intel.com/content/www/us/en/newsroom/news/artificial-intelligence/intel-to-expand-ai-accelerator-portfolio-with-new-gpu.html) |

## Use the catalog in the lab

Choose two configurations with enough memory for the same model and compare their dense compute rates at the model's execution precision. If the model is sharded, compare the actual interconnects offered by the two instances. Use the lab to calculate a transfer floor, then benchmark the same workload on both.
