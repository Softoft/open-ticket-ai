---
title: Features of Open Ticket AI
description: Explore the capabilities of Open Ticket AI.
---

# Features

Open Ticket AI is designed to automate ticket classification while keeping full control over your data. The following sections provide an overview of the core capabilities that help streamline customer service workflows.

## Queue Classification
Automatically predicts the appropriate queue for each incoming ticket. Departments like IT, Accounting, or Sales receive the requests that are relevant to them without manual triage, speeding up response times.

## Priority Prediction
Evaluates the urgency of tickets and assigns a priority value. Open Ticket AI can output discrete levels from 1–5 or a continuous score between 0–100, allowing you to adapt the classification to your existing processes.

## Low-confidence Handling
Tickets that cannot be classified with high certainty are forwarded to a dedicated review queue. This mechanism avoids incorrect assignments and provides human operators with the opportunity to verify edge cases.

## Multi-language Support
Supports German and English out of the box and can be extended to additional languages. Teams operating across different regions benefit from consistent classification regardless of language.

## On-Premise Deployment
Runs entirely on your own infrastructure using Docker containers. No external services are required, ensuring that sensitive data never leaves your environment and simplifying compliance with privacy regulations.

## Extensible Pipelines
Custom Value Objects such as tags or Service-Level Agreements can be added to the classification pipeline. This extensibility means the software can grow with your needs and accommodate unique business rules.

## API Access
A comprehensive HTTP REST API exposes all key functions for training, managing models, and predicting labels. The API makes it straightforward to integrate Open Ticket AI with existing ticket systems or other applications.

## OTOBO Integration
For organizations using the OTOBO ticketing system, an add-on is available that enables seamless data exchange. Tickets created within OTOBO can be automatically enriched with AI predictions to assist your support staff.
