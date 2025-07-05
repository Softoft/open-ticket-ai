---
description: Learn how to install Open Ticket AI using Docker Compose with this step-by-step
  guide. Follow instructions to clone the repository, create a configuration, and
  deploy the application.
title: Installing Open Ticket AI
---
# Installation

The recommended way to deploy Open Ticket AI is via Docker Compose.

1. **Ensure Docker and Docker Compose are installed** on your server.
2. **Clone the repository**
   ```bash
   git clone https://github.com/your-org/open-ticket-ai.git
   cd open-ticket-ai
   ```
3. **Create a configuration**
   Copy the example configuration and modify it for your environment:
   ```bash
   cp docs/original_source/_config_examples/queue_priority_local_config.yml config.yml
   ```
4. **Start the services**
   Build and launch the containers in the background:
   ```bash
   docker-compose up -d --build
   ```
5. **Monitor logs (optional)**
   ```bash
   docker-compose logs -f
   ```
