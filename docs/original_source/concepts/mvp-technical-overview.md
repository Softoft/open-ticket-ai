---
title: Technical Overview (MVP)
description: A technical look at the Minimum Viable Product of ATC.
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

The core of the MVP architecture is straightforward:

*   **`QueueClassifier` and `PriorityClassifier`:** These components load the specified Hugging Face models and execute them to predict queue and priority.
*   **Mapping to Local Queues/Priorities:** The predictions from the models are then mapped to your local system's queues and priorities. This mapping is defined as a dictionary in the configuration file. You can use a wildcard character (`*`) to match any queue. It's common practice to have a "Miscellaneous" or "Junk" queue where wildcard matches are routed. The same wildcard logic applies to priorities, though it's less frequently needed given the typical 5-level priority scale.
*   **`TicketClassifier`:** This component orchestrates the process by calling both the `QueueClassifier` and `PriorityClassifier` simultaneously and returning their combined results.
*   **`TicketProcessor`:** This component is responsible for the overall workflow. It:
    1.  Fetches the next ticket from the integrated ticket system (via the `TicketSystemAdapter`).
    2.  Calls the `TicketClassifier` to get predictions.
    3.  Calls the `updateTicket` method of its injected `TicketSystemAdapter` to apply the classification results to the ticket in the external system.
    The `TicketProcessor` runs in a continuous loop, polling for new tickets at a configurable interval (defaulting to 10 seconds).

Below are some diagrams illustrating parts of the system design:

### MVP Software Design
![MVP Software Design](/images/mvp-software-design.png)

### MVP Design Diagram
![MVP Design](/images/mvp-design.png)

### Data Collection Flow (MVP)
![No Data Collection in MVP](/images/mv-no-data-collection.png)


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
