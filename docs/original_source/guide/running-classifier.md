---
description: Learn how to use Open Ticket AI with Docker Compose to automate ticket
  classification. This guide explains how to run queue and priority workers to intelligently
  route and prioritize support tickets based on AI predictions.
title: Using Open Ticket AI
---
# Usage

This section describes how to run Open Ticket AI for its primary function: classifying tickets.

## Run Inference

Once Open Ticket AI is installed and configured, you can start the classification process using Docker Compose:

```bash
docker-compose up classifier
```

This command starts the necessary services, typically including:

*   **Queue Worker**: Fetches tickets, uses the configured model to predict the appropriate queue, and then updates the ticket in your system (e.g., moves it to the predicted queue or flags it based on confidence levels).
*   **Priority Worker**: Similar to the Queue Worker, but focuses on predicting and assigning ticket priority.

These workers will continuously monitor the incoming queue (as defined in your `config.yml`) and process new tickets as they arrive.

*(Note: The exact service names and behavior might vary based on your specific configuration and version of Open Ticket AI.)*
