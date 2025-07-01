---
description: Ensure peak performance for Open Ticket AI with the right hardware. This guide details CPU, GPU, and RAM recommendations for common deployment scenarios.
title: Hardware Recommendations for Open Ticket AI
---

# Hardware Recommendations

Selecting appropriate hardware ensures smooth operation of Open Ticket AI.

* **CPU-only**: Adequate for small ticket volumes and models such as DistilBERT.
* **GPU**: Recommended for high volumes or when using larger models. NVIDIA RTX series cards or comparable cloud instances (e.g., Hetzner Matrix GPU, AWS `g4ad.xlarge`) work well.

## Memory (RAM)

Approximate RAM requirements for the bundled models:

| Model                | RAM |
| -------------------- | --- |
| DistilBERT           | ~2 GB |
| BERT-base            | ~4 GB |

Ensure additional RAM is available for the operating system and ticket system if they run on the same host.

## Deployment Considerations

* **Co-location vs. Separate Devices**: You can run Open Ticket AI on the same server as your ticket system or on a separate machine.
* **Network Configuration**: If running on separate devices, adjust the `rest_settings.base_url` in `config.yml` so your ticket system can reach the application.
