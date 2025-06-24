---
title: Getting Started
description: Install Open Ticket AI and integrate it with your ticket system.
---

# Installation

Open Ticket AI can be deployed quickly using Docker. Run the following command on your server to start the container:

```bash
docker run -d -p 8080:80 your-docker-repo/atc:latest
```

This community edition does **not** provide a public REST API. Instead, all communication happens via your ticket system's Web Services.

# Ticket System Integration

Currently integrations are available for **OTRS**, **OTOBO**, and **Znuny**. The setup is identical for all three systems:

1. Configure the necessary Web Services in your ticket system.
2. Create a dedicated user or agent for Open Ticket AI access.
3. Point the integration to the URL and credentials of that Web Service user.

For detailed instructions, consult the corresponding getting started guides for your ticket system.

