---
description: Discover the technical architecture of the Automated Ticket Classification
  (ATC) MVP, detailing its use of Hugging Face models for automatic queue and priority
  classification and the specific steps for integration with the OTOBO ticket system.
title: Technical Overview (MVP)
---
# Technical Overview (MVP)

This document outlines the core technical aspects of the Minimum Viable Product (MVP) for the Automated Ticket Classification (ATC) system.

## MVP Features

The MVP focuses on the fundamental capabilities of:

*   **Queue Classification:** Automatically assigning tickets to the correct team or department.
*   **Priority Classification:** Automatically determining the urgency of a ticket.

Users can leverage their own Hugging Face models or utilize the default ATC models. The default queue model can differentiate between 42 different classes, and the default priority model can distinguish between 5 priority levels.

These predicted queues and priorities can be mapped to your organization's specific queues and priorities. Configuration options also allow you to define:
*   The queue for incoming tickets.
*   The queue for tickets that could not be confidently classified.
*   The confidence threshold for the queue model.

## Architecture Implementation

The MVP uses the same pipeline architecture as the rest of Open Ticket AI.  A
pipeline is defined in `config.yml` and lists the components that should run in
order. Typical stages include a fetcher, data preparers, AI inference services
and modifiers that write results back to the help desk.

Pipelines are executed by the `Orchestrator`, which schedules them at the
interval specified in the configuration. Each pipeline polls the ticket system
for new tickets and processes them through the configured pipes.

Start the service with:

```bash
python -m open_ticket_ai.src.ce.main start
```

This command launches the CLI, loads `config.yml`, builds the dependency
injection container and begins executing the pipelines.

Below are some diagrams illustrating parts of the system design:

### MVP Software Design

### MVP Design Diagram

### Data Collection Flow (MVP)


## OTOBO Specifics

The application runs as a Docker Compose service, ideally within the same network as the OTOBO web server.

For OTOBO integration, the following setup is required:

*   **OTOBO Webservices:** Configure the necessary web services in OTOBO.
*   **Dedicated ATC User:** Create a special user account in OTOBO for ATC with the appropriate permissions:
    *   Read access to the incoming tickets queue.
    *   "Move into" permissions for all queues that ATC should be able to assign tickets to.
    *   Write and/or priority update permissions for the incoming ticket queue.
    *   *(Note: Priority is typically updated first, then the queue.)*
*   **OTOBO as REST Provider:** Ensure OTOBO is correctly set up to act as a REST provider.

The URLs for the OTOBO REST API and the ticket system identifier ("otobo") are then specified in the ATC YAML configuration file.
