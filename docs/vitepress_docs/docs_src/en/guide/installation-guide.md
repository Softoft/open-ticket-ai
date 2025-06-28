---
title: Installing Open Ticket AI
description: Step-by-step guide to install Open Ticket AI.
---

# Installation

Follow these steps to install Open Ticket AI:

1.  **Clone the repository**
    ```bash
    git clone https://github.com/your-org/open-ticket-ai.git
    cd open-ticket-ai
    ```

2.  **Create a `config.yml`**
    Refer to the  documentation for details on setting up this file.

3.  **Start with Docker Compose**
    This command will build the necessary Docker images and start the application services in detached mode.
    ```bash
    docker-compose up -d --build
    ```

4.  **Monitor logs**
    You can monitor the logs of the running services to ensure everything is starting up correctly.
    ```bash
    docker-compose logs -f
    ```
