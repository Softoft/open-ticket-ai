---
title: Training AI Models for Open Ticket AI
description: Guide on how to train or fine-tune models for Open Ticket AI.
---

# Training the Model

:::note
You only need to train your own model if you want to use a custom model or fine-tune the default models. To achieve good results, a significant amount of training data is necessary—ideally, at least 1000 tickets per queue and priority. Data cleaning, normalization, tokenization, and experimentation with different models and hyperparameters are often required.
:::

Training or fine-tuning a model for Open Ticket AI involves several key steps:

### 1. Data Collection

*   **Export Historical Data**: Gather historical ticket data (including subject and body) from your existing ticket system.
*   **Label Data**: Accurately label each ticket with the correct queue and priority. This labeled dataset will be the foundation for training your model.

### 2. Data Cleaning

*   **Remove Noise**: Eliminate irrelevant information such as email signatures, Personally Identifiable Information (PII), and spam.
*   **Normalize Text**: Standardize whitespace and ensure consistent character encodings.

### 3. Data Transformation & Tokenization

*   **Combine Fields**: Concatenate the subject and body of the tickets to form a single input text for the model.
*   **Set `max_length`**: Choose an appropriate `max_length` for tokenization (e.g., 256–512 tokens) based on the median length of your tickets. This prevents truncation of important information while managing computational resources.
*   **Use Tokenizer**: Utilize the provided `ticket_combined_email_tokenizer` or a tokenizer compatible with your chosen model.

### 4. Model Selection & Hardware

Consider the following when selecting a model and the required hardware:

| Model                          | RAM Required | Notes                         |
| ------------------------------ | ------------ | ----------------------------- |
| `distilbert-base-german-cased` | 2 GB         | Lightweight, German text      |
| `bert-base-german-cased`       | 4 GB         | Higher accuracy, German text  |
| `deberta-large-mnli`           | 8 GB         | Multilingual / large contexts |

(*Note: The table above provides examples; actual requirements may vary.*)

### 5. Training & Fine-Tuning

*   **Hyperparameter Tuning**: Use the built-in hyperparameter tuner to experiment with settings like `learning_rate`, `batch_size`, and `epochs` to find the optimal configuration for your dataset.
*   **Monitor Performance**: The training script will output a summary of the model's performance and resource usage, helping you track progress and make adjustments.

### 6. Evaluation

*   **Measure Accuracy**: Evaluate the model's performance based on its accuracy in predicting queue and priority.
*   **Analyze Confidence**: Examine the relationship between the model's confidence scores and the correctness of its predictions. This analysis is crucial for setting an optimal `confidence_threshold` in the configuration.
*   **Confidence-Weighted Accuracy Score (CWAS)** (Optional): You might consider using a metric like CWAS to get a more nuanced view of performance:
    ```math
    \text{CWAS} = \text{percent_predicted} \times (\text{percent_correct}^2)
    ```
    This score rewards models that are both accurate and make a high percentage of predictions (i.e., are not overly reliant on falling back to a default for low-confidence cases).
