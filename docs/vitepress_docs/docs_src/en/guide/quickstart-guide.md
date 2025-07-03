---
description: Quickly install and run Open Ticket AI with Docker Compose. This step-by-step
  guide shows you how to configure and start the default workers for automated ticket
  processing.
title: Open Ticket AI Quickstart
---
# Quickstart

Follow these steps to get Open Ticket AI running with the sample configuration.

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-org/open-ticket-ai.git
   cd open-ticket-ai
   ```
2. **Copy the sample configuration**
   ```bash
   cp docs/original_source/_config_examples/queue_priority_local_config.yml config.yml
   ```
   Adjust `config.yml` with the URL and credentials of your ticket system.
3. **Start the services**
   ```bash
   docker-compose up -d --build
   ```
4. **Monitor the logs (optional)**
   ```bash
   docker-compose logs -f
   ```

The queue and priority workers will automatically begin processing tickets based on your configuration.
