---
description: Learn how to quickly install and run Open Ticket AI using Docker Compose. This guide provides easy setup instructions for integrating with your OTRS, OTOBO, or Znuny helpdesk via Web Services.
title: Getting Started
---

# Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-org/open-ticket-ai.git
   cd open-ticket-ai
   ```

2. **Copy the sample configuration**
   ```bash
   cp docs/original_source/_config_examples/queue_priority_local_config.yml config.yml
   ```

3. **Build and start the services**
   ```bash
   docker-compose up -d --build
   ```

Open Ticket AI communicates with your ticket system via Web Services; there is no external API.

# Ticket System Integration

Currently integrations are available for **OTRS**, **OTOBO**, and **Znuny**. The setup is identical for all three systems:

1. Configure the necessary Web Services in your ticket system.
2. Create a dedicated user or agent for Open Ticket AI access.
3. Point the integration to the URL and credentials of that Web Service user.

For detailed instructions, consult the corresponding getting started guides for your ticket system.
