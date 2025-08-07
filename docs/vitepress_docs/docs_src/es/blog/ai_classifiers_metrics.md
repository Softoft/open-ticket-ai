---
description: Domina la clasificación de tickets con IA con esta guía de evaluación.
  Aprende por qué la exactitud es engañosa para datos desbalanceados y descubre las
  métricas esenciales que realmente importan, incluyendo precisión, recall, F1-score
  y estrategias multietiqueta.
---
# Evaluando Clasificadores de IA con Datos Reales de Tickets: Las Métricas que Importan

## Introducción

Los datos de los tickets de soporte son desordenados y a menudo están muy sesgados hacia unas pocas categorías comunes. Por ejemplo,
el 80% de los tickets podrían estar etiquetados como **“consulta general”**, lo que hace que los clasificadores se sesguen hacia la `class`
mayoritaria. En la práctica, el ML en datos de tickets se puede utilizar para:

- **Predicción de prioridad** (p. ej., marcar problemas urgentes)
- **Asignación de cola o equipo** (p. ej., enviar preguntas de facturación a finanzas)
- **Clasificación de intención o tema** (p. ej., “solicitud de función” vs. “reporte de error”)

Estos casos de uso demuestran por qué la evaluación es un desafío: los conjuntos de datos de tickets del mundo real son multiclase y
multietiqueta, con texto ruidoso y **clases desbalanceadas**:contentReference[oaicite:0]{index=0}. Un
`model` ingenuo que siempre predice la `class` mayoritaria puede obtener una alta exactitud ignorando casos raros pero importantes.
Examinaremos por qué la exactitud por sí sola es engañosa y discutiremos las métricas que realmente importan.

## Por qué la Exactitud es Engañosa

La **exactitud** (Accuracy) se define como el total de predicciones correctas sobre el total de predicciones:
$ \text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN} $
En términos de fórmula, exactitud = (TP + TN)/(todas las muestras). Aunque
es simple, la exactitud falla estrepitosamente con datos desbalanceados. Por ejemplo, si el 80% de los tickets pertenecen a la `class` A, un
clasificador simple que *siempre* predice A alcanza un 80% de exactitud por defecto, pero ignora por completo
el otro 20% de los tickets. En casos extremos (p. ej., una división de `class` del 99% frente al 1%), predecir
siempre la mayoría produce un 99% de exactitud a pesar de no haber un aprendizaje real. En
resumen, una alta exactitud puede simplemente reflejar la distribución de la `class`, no un rendimiento genuino.

> **“... la exactitud ya no es una medida adecuada [para conjuntos de datos desbalanceados], ya que no distingue entre el número de ejemplos correctamente clasificados de diferentes clases. Por lo tanto, puede llevar a conclusiones erróneas…”.**

## Métricas Centrales: Precisión, Recall, F1

Para evaluar clasificadores en condiciones de desbalance, nos basamos en la **precisión (precision), el recall y el F1-score**, que se centran
en los errores en las `classes` minoritarias. Estas se derivan de la matriz de confusión, por ejemplo, para una clasificación
binaria:

|                     | Predicho Positivo   | Predicho Negativo   |
|---------------------|---------------------|---------------------|
| **Real Positivo**   | Verdadero Positivo (TP)  | Falso Negativo (FN) |
| **Real Negativo**   | Falso Positivo (FP) | Verdadero Negativo (TN)  |

A partir de estos recuentos, definimos:

- **Precisión (Precision)** = TP / (TP + FP) – proporción de positivos predichos que son correctos:
- **Recall** = TP / (TP + FN) – proporción de positivos reales que fueron encontrados:
- **F1-Score** = media armónica de la precisión y el recall:
  \[ \mathrm{F1} = \frac{2 \cdot \mathrm{TP}}{2 \cdot \mathrm{TP} + \mathrm{FP} + \mathrm{FN}}. \]

Cada métrica resalta diferentes errores: la precisión penaliza las falsas alarmas (FP), mientras que el recall
penaliza las omisiones (FN). El F1-score equilibra ambos. Para ser exhaustivos, cabe señalar que la exactitud también se puede
escribir como \( (TP + TN) / (TP+TN+FP+FN) \):contentReference[oaicite:8]{index=8}, pero en datos desbalanceados
enmascara los fallos del `model`.

En la práctica, el `classification_report` de scikit-learn calcula estas métricas por `class`. Por ejemplo:

reporta la precisión, el recall, el F1 (y el soporte) para cada `class` de ticket.

## Promediado Macro vs. Micro

Para problemas multiclase, las métricas se pueden promediar de diferentes maneras. El **promediado micro (micro-averaging)** agrupa todas
las `classes` sumando los TP, FP, FN globales y luego calculando las métricas, ponderando efectivamente por
el soporte de cada `class`. El **promediado macro (macro-averaging)** calcula la métrica para cada `class` por separado y luego
toma la media no ponderada. En otras palabras, el promediado macro trata a todas las `classes` por igual (por lo que las `classes` raras cuentan tanto
como las comunes), mientras que el micro favorece el rendimiento en las `classes` frecuentes. Usa **macro-averaging**
cuando las `classes` minoritarias son críticas (p. ej., detectar un ticket urgente poco común), y **micro-averaging**
cuando la exactitud general en todos los tickets es más importante.

| Promediado | Cómo se calcula                                              | Cuándo usar                                        |
|------------|--------------------------------------------------------------|----------------------------------------------------|
| **Micro**  | Recuentos globales de TP, FP, FN en todas las `classes`      | Proporciona el rendimiento general (favorece a las `classes` grandes) |
| **Macro**  | Promedio de la métrica de cada `class` (cada `class` ponderada por igual) | Asegura que las `classes` pequeñas/raras cuenten por igual           |

## Desafíos Multietiqueta

Los tickets de soporte a menudo llevan múltiples etiquetas a la vez (p. ej., un ticket puede tener tanto una etiqueta de **cola** como
de **prioridad**). En configuraciones multietiqueta (`multi-label`), se aplican métricas adicionales:

*   **Subset Accuracy** (Coincidencia Exacta) – fracción de muestras donde *todas* las etiquetas predichas coinciden exactamente
    con el conjunto real de etiquetas. Es una métrica muy estricta: una etiqueta incorrecta significa un fallo.
*   **Hamming Loss** – la fracción de predicciones de etiquetas individuales que son incorrectas. La pérdida de Hamming
    es más permisiva: cada etiqueta se juzga de forma independiente. Una pérdida de Hamming más baja (cercana a 0) es mejor.
*   **Label Ranking Loss** – mide cuántos pares de etiquetas están ordenados incorrectamente por confianza. Es
    relevante cuando el `model` genera puntuaciones para cada etiqueta y nos importa clasificar las etiquetas para cada
    ticket.

Scikit-learn proporciona funciones como `accuracy_score` (exactitud de subconjunto en modo multietiqueta) y
`hamming_loss`. En general, se elige la métrica que se alinea con las necesidades del negocio: coincidencia exacta si
se necesitan todas las etiquetas correctas, o pérdida de Hamming/Ranking si la corrección parcial es aceptable.

## La Matriz de Confusión en la Práctica

Una matriz de confusión es a menudo el primer vistazo al comportamiento de un clasificador. En `Python` puedes calcularla y
mostrarla con scikit-learn:

```python
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

cm = confusion_matrix(y_test, y_pred, labels=classes)
print("Confusion Matrix:\n", cm)

# To visualize:
ConfusionMatrixDisplay(cm, display_labels=classes).plot()
```

Aquí `cm[i, j]` es el número de tickets cuya `class` verdadera es `i` pero que fueron predichos como `class` `j`.
Al inspeccionar una matriz de confusión (o su mapa de calor), busca:

*   **Celdas fuera de la diagonal** – indican clasificaciones erróneas (qué `classes` se confunden con mayor
    frecuencia).
*   **Falsos positivos vs. falsos negativos** – p. ej., una suma alta en una fila fuera de la diagonal significa que el `model`
    omitió frecuentemente esa `class` real (muchos FN); una suma alta en una columna fuera de la diagonal significa muchas
    predicciones incorrectas de esa `class` (muchos FP).
*   **Clases subrepresentadas** – las `classes` con pocos ejemplos pueden aparecer como filas/columnas casi vacías,
    lo que indica que el `model` rara vez las predice correctamente.

Analizar adecuadamente la matriz de confusión ayuda a dirigir la limpieza de datos o los ajustes del `model` para tipos de tickets específicos.

## Estrategia de Evaluación para Sistemas de Tickets Reales

Construir un pipeline de evaluación fiable requiere más que solo elegir métricas:

*   **Datos limpios y etiquetados**: Asegúrate de que tu conjunto de prueba sea representativo y esté etiquetado con precisión. Elimina
    duplicados o tickets mal etiquetados antes de evaluar.
*   **Línea base vs. Ajuste fino**: Compara siempre tu `model` de IA con líneas base simples (p. ej., un
    predictor de la `class` mayoritaria o sistemas de reglas por palabras clave). Mide las mejoras relativas utilizando las métricas elegidas.
*   **Reevaluación periódica**: Las tendencias de los tickets cambian con el tiempo (problemas estacionales, nuevos productos). Planifica
    reentrenar y reevaluar el `model` regularmente o activarlo ante un desvío de los datos (data drift).
*   **Comunicación con las partes interesadas**: Traduce las métricas en información procesable para las partes interesadas no técnicas.
    Por ejemplo, "El recall para tickets urgentes aumentó del 75% al 85%, lo que significa que detectamos un 10%
    más de problemas de alta prioridad automáticamente". Usa gráficos (p. ej., gráficos de barras de precisión/recall por `class`)
    y enfatiza el impacto en el negocio (respuesta más rápida, reducción de trabajo acumulado).

## Conclusión

En resumen, **no puedes mejorar lo que no mides**. La exactitud por sí sola no es suficiente para
datos de tickets complejos y desbalanceados. En su lugar, haz un seguimiento de la precisión, el recall y el F1 por `class` (usando
promedios macro/micro según corresponda), y considera métricas multietiqueta si tus tickets tienen múltiples
anotaciones. Comienza a rastrear las métricas desde el principio en cualquier integración de IA para que las ganancias (o los problemas) sean
visibles. Al centrarse en las métricas correctas desde el primer día, los equipos de soporte pueden mejorar iterativamente sus
clasificadores de tickets y ofrecer una automatización más fiable.

¿Quieres probar estas ideas con tus propios datos? Echa un vistazo a la plataforma
[Softoft’s Ticket Classification](https://ticket-classification.softoft.de) para
experimentar con conjuntos de datos de tickets reales y herramientas de evaluación integradas.