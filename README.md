# Inference Engineering Labs

Cuaderno de prácticas para acompañar la lectura de *Inference Engineering*. Cada ejercicio parte de una pregunta, mide un comportamiento y deja constancia de cómo reproducirlo.

## Primer laboratorio · Latencia y throughput

Mide una inferencia de CPU sobre un modelo lineal pequeño con datos sintéticos. El script usa solo la biblioteca estándar de Python 3.10+.

```bash
python3 scripts/benchmark.py --batch-sizes 1 8 32 --runs 100
```

El [notebook](notebooks/01-latencia-y-throughput.ipynb) usa el mismo script y propone experimentos con el tamaño del lote y el número de repeticiones. Para abrirlo en JupyterLab, ejecuta lo siguiente desde la raíz del repositorio.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install jupyterlab
jupyter lab
```

Al guardar resultados, anota el hardware, la versión de Python, los parámetros y qué parte de la inferencia se midió.
