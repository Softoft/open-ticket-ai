---
description: Aprenda a hacer un ajuste fino de un modelo de IA con sus propios datos de tickets para una clasificación de tickets precisa y automatizada. Esta guía proporciona instrucciones paso a paso para preparar conjuntos de datos y entrenar modelos usando Hugging Face Transformers o una REST API on-premise.
---
# Cómo Hacer un Ajuste Fino de un Modelo de IA con sus Propios Datos de Tickets

Hacer un ajuste fino (fine-tuning) de un modelo de IA con sus propios datos de tickets es una forma poderosa de personalizar la clasificación de tickets para su organización. Al entrenar un modelo con tickets de soporte etiquetados, le enseña el lenguaje y las categorías específicas de su dominio. Este proceso generalmente implica preparar un conjunto de datos (a menudo un archivo CSV o JSON de tickets y etiquetas), elegir o crear etiquetas (como departamentos o niveles de prioridad) y luego entrenar un modelo, como un clasificador basado en Transformer, con esos datos. Puede usar herramientas como la librería Transformer de Hugging Face para entrenar modelos localmente, o usar una solución dedicada como **Open Ticket AI (ATC)**, que proporciona una REST API on-premise para la clasificación de tickets. En cualquier caso, se beneficia del aprendizaje por transferencia (transfer learning): un modelo preentrenado (p. ej., BERT, DistilBERT o RoBERTa) se adapta a las categorías de sus tickets, mejorando enormemente la precisión en comparación con un modelo genérico.

Los flujos de trabajo modernos de clasificación de texto siguen estos pasos de alto nivel:

* **Recopilar y Etiquetar Datos:** Reúna tickets históricos y asígneles las categorías (colas) o prioridades correctas. Cada ticket debe tener un campo de texto y al menos una etiqueta.
* **Formatear el Conjunto de Datos:** Guarde estos datos etiquetados en un formato estructurado (CSV o JSON). Por ejemplo, un CSV podría tener las columnas `"text","label"`.
* **Dividir en Entrenamiento/Prueba:** Reserve una parte para validación/prueba para evaluar el rendimiento.
* **Hacer Ajuste Fino del Modelo:** Use una librería como Hugging Face Transformers, o nuestra API de Open Ticket AI, para entrenar un modelo de clasificación con los datos.
* **Evaluar y Desplegar:** Verifique la precisión (o F1) con los datos de prueba, luego use el modelo entrenado para clasificar nuevos tickets.

Los lectores con conocimientos técnicos pueden seguir estos pasos en detalle. Los ejemplos a continuación ilustran cómo preparar datos de tickets y hacer un ajuste fino de un modelo usando **Hugging Face Transformers**, así como la forma en que nuestra solución Open Ticket AI soporta este flujo de trabajo a través de llamadas a la API. A lo largo del texto, asumimos categorías de tickets comunes (p. ej., “Facturación”, “Soporte Técnico”) y etiquetas de prioridad, pero sus etiquetas pueden ser cualquier cosa relevante para su sistema.

## Preparando sus Datos de Tickets

Primero, reúna un conjunto representativo de tickets pasados y etiquételos de acuerdo con su esquema de clasificación. Las etiquetas podrían ser departamentos (como **Soporte Técnico**, **Servicio al Cliente**, **Facturación**, etc.) o niveles de prioridad (p. ej., **Baja**, **Media**, **Alta**). Por ejemplo, el conjunto de datos de tickets de Softoft incluye categorías como *Soporte Técnico*, *Facturación y Pagos*, *Soporte de TI* e *Información General*. Un modelo de ejemplo de Hugging Face usa etiquetas como *Pregunta de Facturación*, *Solicitud de Característica*, *Consulta General* y *Problema Técnico*. Defina las categorías que tengan sentido para su flujo de trabajo.

Organice los datos en formato CSV o JSON. Cada registro debe contener el texto del ticket y su etiqueta. Por ejemplo, un CSV podría verse así:

```
text,label
"My printer will not connect to WiFi",Hardware,  # Texto de ticket de ejemplo y su categoría
"I need help accessing my account",Account
```

Si incluye prioridades o múltiples etiquetas, podría agregar más columnas (p. ej., `priority`). La estructura exacta es flexible, siempre que mapee claramente cada texto de ticket a su(s) etiqueta(s). Es común tener una columna para el contenido del ticket (p. ej., `"text"` o `"ticket_text"`) y una columna para la etiqueta.

Es posible que necesite limpiar y preprocesar el texto ligeramente (p. ej., eliminar firmas, etiquetas HTML o anonimizar datos), pero en muchos casos el texto crudo del ticket funciona bien como entrada para los modelos de NLP modernos. Finalmente, divida los datos etiquetados en un conjunto de entrenamiento y un conjunto de validación/prueba (por ejemplo, 80% entrenamiento / 20% prueba). Esta división le permite medir qué tan bien generaliza el modelo afinado.

## Etiquetado de Tickets

Es crucial tener etiquetas consistentes y precisas. Asegúrese de que cada ticket esté asignado correctamente a una de sus categorías elegidas. Esto puede hacerse manualmente por el personal de soporte o utilizando metadatos de tickets existentes si están disponibles. A menudo, las organizaciones etiquetan los tickets por *cola* o departamento, y a veces también por *prioridad*. Por ejemplo, el conjunto de datos de tickets de correo electrónico de Softoft categoriza los tickets tanto por departamento (cola) como por prioridad. La prioridad puede ser útil si desea entrenar un modelo para predecir la urgencia: p. ej., `Baja`, `Media`, `Crítica`. En muchas configuraciones, podría entrenar un modelo para la clasificación de departamentos y otro para la clasificación de prioridades.

Cualquiera que sea su esquema, asegúrese de tener un conjunto finito de valores de etiqueta. En un CSV, podría tener:

```
text,label,priority
"System crash when saving file","Technical Support","High"
"Request to change billing address","Billing","Low"
```

Este ejemplo tiene dos columnas de etiqueta: una para la categoría y otra para la prioridad. Para simplificar, en los siguientes ejemplos asumimos una tarea de clasificación de etiqueta única (una columna de etiqueta).

**Consejos clave para el etiquetado:**

* Defina los nombres de sus etiquetas claramente. Por ejemplo, *Soporte Técnico* vs *Soporte de TI* vs *Problema de Hardware* – evite superposiciones ambiguas.
* Si los tickets a menudo pertenecen a múltiples categorías, podría considerar la clasificación multietiqueta (asignar múltiples etiquetas) o dividirlo en modelos separados.
* Use un formato consistente (misma ortografía, mayúsculas/minúsculas) para las etiquetas en su conjunto de datos.

Al final de este paso, debería tener un archivo de conjunto de datos etiquetado (CSV o JSON) con los textos de los tickets y sus etiquetas, listo para el modelo.

## Ajuste Fino con Hugging Face Transformers

Una de las formas más flexibles de hacer un ajuste fino de un clasificador de texto es usando la librería [Hugging Face Transformers](https://huggingface.co/transformers/). Esto le permite comenzar desde un modelo de lenguaje preentrenado (como BERT o RoBERTa) y entrenarlo más a fondo con su conjunto de datos de tickets específico. Los pasos principales son: tokenizar el texto, configurar un `Trainer` y llamar a `train()`.

1. **Cargar el Conjunto de Datos:** Use `datasets` o `pandas` para cargar su CSV/JSON. Por ejemplo, la librería `datasets` de Hugging Face puede leer un CSV directamente:

   ```python
   from datasets import load_dataset
   dataset = load_dataset("csv", data_files={
       "train": "tickets_train.csv",
       "validation": "tickets_val.csv"
   })
   # Asumiendo que 'text' es la columna con el contenido del ticket, y 'label' es la columna de la categoría.
   ```

2. **Tokenizar el Texto:** Los transformers preentrenados requieren una entrada tokenizada. Cargue un tokenizador (p. ej., DistilBERT) y aplíquelo a su texto:

   ```python
   from transformers import AutoTokenizer
   tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")

   def preprocess_function(examples):
       # Tokenizar los textos (esto producirá input_ids, attention_mask, etc.)
       return tokenizer(examples["text"], truncation=True, padding="max_length")

   tokenized_datasets = dataset.map(preprocess_function, batched=True)
   ```

   Esto sigue el ejemplo de Hugging Face: primero cargue el tokenizador DistilBERT, luego use `Dataset.map` para tokenizar todos los textos en lotes. El resultado (`tokenized_datasets`) contiene los IDs de entrada y las máscaras de atención, listos para el modelo.

3. **Cargar el Modelo:** Elija un modelo preentrenado y especifique el número de etiquetas. Por ejemplo, para hacer un ajuste fino de DistilBERT para clasificación:

   ```python
   from transformers import AutoModelForSequenceClassification
   num_labels = 4  # establezca esto al número de sus categorías
   model = AutoModelForSequenceClassification.from_pretrained(
       "distilbert-base-uncased", num_labels=num_labels
   )
   ```

   Esto coincide con el ejemplo de clasificación de secuencias de Hugging Face, donde el modelo se carga con `num_labels` igual al número de clases en su conjunto de datos.

4. **Establecer Argumentos de Entrenamiento y Trainer:** Defina los hiperparámetros con `TrainingArguments`, luego cree un `Trainer` con su modelo y los datos tokenizados:

   ```python
   from transformers import TrainingArguments, Trainer
   training_args = TrainingArguments(
       output_dir="./ticket_model",
       num_train_epochs=3,
       per_device_train_batch_size=8,
       per_device_eval_batch_size=8,
       learning_rate=2e-5,
       evaluation_strategy="epoch"
   )
   trainer = Trainer(
       model=model,
       args=training_args,
       train_dataset=tokenized_datasets["train"],
       eval_dataset=tokenized_datasets["validation"],
       tokenizer=tokenizer
   )
   ```

   Esto refleja la guía de Hugging Face: después de configurar `TrainingArguments` (para el directorio de salida, épocas, tamaño de lote, etc.), instanciamos `Trainer` con el modelo, los conjuntos de datos, el tokenizador y los argumentos de entrenamiento.

5. **Entrenar el Modelo:** Llame a `trainer.train()` para iniciar el ajuste fino. Esto se ejecutará durante el número de épocas especificado, evaluando periódicamente en el conjunto de validación si se proporciona.

   ```python
   trainer.train()
   ```

   Según la documentación, este único comando inicia el ajuste fino. El entrenamiento puede tardar de minutos a horas dependiendo del tamaño de los datos y del hardware (se recomienda una GPU para conjuntos de datos grandes).

6. **Evaluar y Guardar:** Después del entrenamiento, evalúe el modelo en su conjunto de prueba para verificar la precisión u otras métricas. Luego guarde el modelo afinado y el tokenizador:

   ```python
   trainer.evaluate()
   model.save_pretrained("fine_tuned_ticket_model")
   tokenizer.save_pretrained("fine_tuned_ticket_model")
   ```

   Más tarde puede recargar este modelo con `AutoModelForSequenceClassification.from_pretrained("fine_tuned_ticket_model")`.

Una vez entrenado, puede usar el modelo para inferencia. Por ejemplo, la API `pipeline` de Hugging Face lo hace fácil:

```python
from transformers import pipeline

classifier = pipeline("text-classification", model="fine_tuned_ticket_model")
results = classifier("Please reset my password and clear my cache.")
print(results)
```

Esto mostrará la etiqueta predicha y la confianza para el nuevo texto del ticket. Como demuestran los ejemplos de Hugging Face, la abstracción `pipeline("text-classification")` le permite clasificar rápidamente nuevos textos de tickets con el modelo afinado.

## Usando Open Ticket AI (ATC de Softoft) para Entrenamiento e Inferencia

Nuestro sistema **Open Ticket AI** (también conocido como ATC – AI Ticket Classification) proporciona una solución on-premise, en contenedores Docker, con una REST API que puede ingerir sus datos de tickets etiquetados y entrenar modelos automáticamente. Esto significa que puede mantener todos los datos localmente y aun así aprovechar el potente ML. La API de ATC tiene endpoints para cargar datos, iniciar el entrenamiento y clasificar tickets.

* **Cargar Datos de Entrenamiento:** Envíe su CSV de tickets etiquetados al endpoint `/api/v1/train-data`. La API espera un payload CSV (`Content-Type: text/csv`) que contenga sus datos de entrenamiento. Por ejemplo, usando `requests` de Python:

  ```python
  import requests
  url = "http://localhost:8080/api/v1/train-data"
  headers = {"Content-Type": "text/csv"}
  with open("tickets_labeled.csv", "rb") as f:
      res = requests.post(url, headers=headers, data=f)
  print(res.status_code, res.text)
  ```

  Esto corresponde a la API “Train Data” en la documentación de ATC. Una respuesta exitosa significa que los datos han sido recibidos.

* **Iniciar Entrenamiento del Modelo:** Después de cargar los datos, inicie el entrenamiento llamando a `/api/v1/train` (no se necesita cuerpo de solicitud). En la práctica:

  ```bash
  curl -X POST http://localhost:8080/api/v1/train
  ```

  O en Python:

  ```python
  train_res = requests.post("http://localhost:8080/api/v1/train")
  print(train_res.status_code, train_res.text)
  ```

  Esto coincide con el ejemplo de la documentación para desarrolladores, que muestra que un simple POST inicia el entrenamiento. El servicio entrenará el modelo con los datos cargados (utiliza su propio pipeline de entrenamiento internamente, posiblemente basado en modelos Transformer similares). El entrenamiento se ejecuta en su servidor, y el modelo se guarda localmente cuando termina.

* **Clasificar Nuevos Tickets:** Una vez que el entrenamiento está completo, use el endpoint `/api/v1/classify` para obtener predicciones para nuevos textos de tickets. Envíe un payload JSON con el campo `"ticket_data"` que contenga el texto del ticket. Por ejemplo:

  ```python
  ticket_text = "My laptop overheats when I launch the app"
  res = requests.post(
      "http://localhost:8080/api/v1/classify",
      json={"ticket_data": ticket_text}
  )
  print(res.json())  # p. ej. {"predicted_label": "Hardware Issue", "confidence": 0.95}
  ```

  La documentación de ATC muestra un ejemplo similar con `curl` para la clasificación. La respuesta típicamente incluirá la categoría predicha (y posiblemente la confianza).

Usar la REST API de Open Ticket AI integra el flujo de entrenamiento en sus propios sistemas. Puede automatizar las cargas y las ejecuciones de entrenamiento (p. ej., entrenamiento nocturno o entrenamiento con datos nuevos), y luego usar el endpoint de clasificación en su flujo de trabajo de tickets. Como todo se ejecuta on-premise, el contenido sensible de los tickets nunca sale de sus servidores.

## Ejemplo de Código Python

A continuación se muestra un ejemplo consolidado que ilustra ambos flujos de trabajo:

```python
# Ejemplo: Ajuste fino con Hugging Face
from transformers import AutoTokenizer,
    AutoModelForSequenceClassification,
    Trainer,
    TrainingArguments
from datasets import load_dataset

# Cargar y dividir su conjunto de datos CSV
dataset = load_dataset("csv", data_files={"train": "train.csv", "validation": "val.csv"})
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")


# Tokenizar
def preprocess(examples):
    return tokenizer(examples["text"], truncation=True, padding="max_length")


tokenized = dataset.map(preprocess, batched=True)

# Cargar modelo
num_labels = 5  # p. ej., número de categorías de tickets
model = AutoModelForSequenceClassification.from_pretrained(
    "distilbert-base-uncased",
    num_labels=num_labels
    )

# Configurar Trainer
training_args = TrainingArguments(
    output_dir="./model_out", num_train_epochs=3, per_device_train_batch_size=8
)
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized["train"],
    eval_dataset=tokenized["validation"],
    tokenizer=tokenizer
)
trainer.train()
trainer.evaluate()
model.save_pretrained("fine_tuned_ticket_model")
tokenizer.save_pretrained("fine_tuned_ticket_model")

# Usar el modelo para clasificación
from transformers import pipeline

classifier = pipeline("text-classification", model="fine_tuned_ticket_model")
print(classifier("Example: The app crashes when I try to open it"))

# Ejemplo: Usando la API de Open Ticket AI
import requests

# Cargar datos (CSV)
with open("tickets_labeled.csv", "rb") as data_file:
    res = requests.post(
        "http://localhost:8080/api/v1/train-data",
        headers={"Content-Type": "text/csv"},
        data=data_file
        )
    print("Upload status:", res.status_code)
# Iniciar entrenamiento
train_res = requests.post("http://localhost:8080/api/v1/train")
print("Training status:", train_res.status_code)
# Clasificar nuevo ticket
res = requests.post(
    "http://localhost:8080/api/v1/classify",
    json={"ticket_data": "Cannot log into account"}
    )
print("Prediction:", res.json())
```

Este script demuestra ambos métodos: el pipeline de ajuste fino de Hugging Face y las llamadas REST a Open Ticket AI. Carga y tokeniza un conjunto de datos CSV, hace un ajuste fino de un clasificador DistilBERT y luego lo utiliza a través de un pipeline. También muestra cómo hacer POST de los mismos datos a la API de ATC e iniciar el entrenamiento/clasificación.

## Conclusión

Hacer un ajuste fino de un modelo de IA con sus propios datos de tickets permite una clasificación de tickets personalizada y de alta precisión. Al etiquetar tickets pasados y entrenar un modelo como un Transformer, aprovecha el aprendizaje por transferencia y el conocimiento del dominio. Ya sea que use las APIs de Python de Hugging Face o una solución llave en mano como Open Ticket AI (el servicio de clasificación on-premise de Softoft), el flujo de trabajo es similar: prepare datos etiquetados, entrene con ellos y luego use el modelo entrenado para hacer predicciones.

Hemos mostrado cómo estructurar su conjunto de datos CSV/JSON, usar la API `Trainer` de Hugging Face para el ajuste fino, y usar la REST API de Open Ticket AI para entrenamiento e inferencia on-premise. La documentación de Hugging Face proporciona una guía detallada sobre el uso de tokenizadores y el `Trainer`, y las tarjetas de modelo de ejemplo ilustran cómo se aplican los modelos de clasificación al enrutamiento de tickets. Con estas herramientas, puede iterar rápidamente: pruebe diferentes modelos preentrenados (p. ej., BERT, RoBERTa, o incluso modelos específicos del dominio), experimente con hiperparámetros y mida el rendimiento en su conjunto de prueba.

Siguiendo estos pasos, su sistema de soporte puede enrutar automáticamente los tickets al equipo correcto, marcar problemas urgentes y ahorrar a su personal innumerables horas de clasificación manual. Esta profunda integración de NLP en su flujo de trabajo de tickets ahora es accesible con librerías y APIs modernas – solo necesita proporcionar sus datos y etiquetas.