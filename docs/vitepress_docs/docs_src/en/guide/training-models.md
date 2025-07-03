---
description: 'Learn how to train and fine-tune custom models for Open Ticket AI. This
  guide covers the external workflow: exporting data, training a model, and updating
  your config.'
title: Training Models
---
# Training Models

Open Ticket AI does not provide an in-app UI or API for model training. Instead, you train models externally and then reference them in your configuration.

## Workflow Overview

1. **Export labeled tickets**
   Export ticket texts with their queue and priority labels from your helpdesk.
2. **Fine-tune a model**
   Use a tool such as a Jupyter Notebook with the `transformers` library to train or fine-tune a language model on this data.
3. **Publish or save the model**
   Upload the resulting model to the Hugging Face Hub or save it locally so that Open Ticket AI can access it.
4. **Update the configuration**
   Edit `config.yml` and set the `model_name` (or `hf_model`) of each pipeline to the location of your new model. Restart the application to load it.
