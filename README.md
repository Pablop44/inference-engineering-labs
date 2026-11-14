# Inference Engineering Labs

Ejercicios prácticos inspirados en *Inference Engineering*, de Philip Kiely (Baseten Books). El objetivo es entender qué ocurre al ejecutar un modelo y aprender a medir, optimizar y servir inferencia mediante notebooks, scripts de Python y servicios pequeños.

Está dirigido a desarrolladores con conocimientos básicos de Python y familiaridad con modelos de aprendizaje automático. Para empezar, lee los capítulos 0 y 1 del libro. Presentan el alcance de la inferencia, la selección de modelos y las métricas que usaremos en los ejercicios. Las primeras prácticas se plantean para CPU o modelos pequeños. Las que requieran una GPU o varias indicarán ese requisito.

## Índice de contenidos

La numeración conserva los números de capítulo del libro.

| Módulo | Estado |
| --- | --- |
| [2. Models](#2-models) | Coming soon |
| [4. Software](#4-software) | Coming soon |
| [5. Techniques](#5-techniques) | Coming soon |
| [6. Modalities](#6-modalities) | Coming soon |
| [7. Production](#7-production) | Coming soon |

- **Done** — Ejercicios disponibles y verificados.
- **WIP** — Ejercicios en desarrollo.
- **Coming soon** — Ejercicios previstos.

## 2. Models

- Implementar una capa lineal y comparar la ejecución por muestra con la multiplicación matricial por lotes.
- Construir atención causal a pequeña escala y examinar qué cambia al variar la longitud de la secuencia.
- Instrumentar la generación de un LLM pequeño para medir por separado el *prefill* y el *decode*. Registrar el tiempo hasta el primer token, el tiempo por token y el crecimiento de la KV cache.
- Comparar operaciones de distinta intensidad aritmética y contrastar las mediciones con una estimación de bytes movidos y operaciones realizadas.

## 4. Software

- Exportar un modelo pequeño de PyTorch a ONNX. Comprobar la equivalencia de las salidas y comparar latencia y throughput con ONNX Runtime.
- Servir un LLM pequeño con un motor de inferencia y medir latencia p50 y p95, tokens por segundo y tiempo hasta el primer token al variar la concurrencia.
- Perfilar una inferencia para localizar copias y operaciones costosas. En GPU, comparar una secuencia de kernels con una variante fusionada.

## 5. Techniques

- Cuantizar un modelo y medir el efecto en memoria, latencia y calidad sobre un conjunto fijo de entradas.
- Comparar decodificación normal y especulativa. Medir cuántos tokens del modelo borrador se aceptan y cuándo mejora el tiempo de generación.
- Medir la reutilización de la KV cache con prefijos compartidos y distintos tamaños de contexto.
- Comparar inferencia en una GPU con paralelismo tensorial en dos GPU. Medir latencia y coste de comunicación.
- Simular colas separadas para *prefill* y *decode*. Medir cómo la mezcla de solicitudes y el coste de transferir la KV cache afectan a la latencia.

## 6. Modalities

- Comparar el efecto de la resolución de entrada en la latencia y la calidad de las respuestas de un modelo de visión y lenguaje.
- Generar embeddings por lotes y medir throughput y calidad de recuperación con un conjunto pequeño de consultas anotadas.
- Transcribir audio con distintos tamaños de fragmento y medir latencia y tasa de error de palabras. En síntesis de voz, medir el tiempo hasta el primer fragmento de audio.
- Comparar la latencia y las imágenes generadas al variar los pasos de denoising con un conjunto fijo de prompts y semillas. En GPU, extender la medición a clips cortos y variar el número de fotogramas.

## 7. Production

- Empaquetar un servicio de inferencia en un contenedor y medir el tiempo de arranque en frío.
- Aplicar carga al servicio para estudiar el efecto de la concurrencia, las colas y el batching sobre la latencia p95.
- Simular escalado a cero y comparar políticas de escalado con tráfico por ráfagas. Estimar el coste a partir del tiempo activo de las réplicas.
- Instrumentar tiempos de cola, cómputo y respuesta. Comparar un cliente que recibe la respuesta completa con otro que consume tokens en streaming.
- Desplegar dos versiones de un servicio local y comprobar durante el cambio si aparecen errores o se interrumpen solicitudes en curso.

## Lecturas de referencia

- **Hardware** — Capítulo 3 de *Inference Engineering* para arquitectura de GPU, jerarquía de memoria, generaciones de aceleradores y tipos de instancia.
- **Capacidad e infraestructura** — Sección 7.3 para aprovisionamiento de GPU y gestión de capacidad entre proveedores.
- **Glosario y lecturas complementarias** — Apéndices A y B.
