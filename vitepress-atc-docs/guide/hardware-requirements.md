---
title: Hardware Recommendations for Open Ticket AI
description: Guidance on hardware for running Open Ticket AI.
---

# Hardware Recommendations

Choosing the right hardware is important for the performance of Open Ticket AI, especially when dealing with a large volume of tickets or using more complex models.

*   **CPU-only**: Sufficient for small volumes of tickets (e.g., < 50 tickets per minute). Most modern server CPUs should handle this workload.
*   **GPU (Graphics Processing Unit)**: Recommended for higher volumes (e.g., > 100 tickets per minute) or when using larger, more computationally intensive models. NVIDIA RTX series GPUs are a common choice.
    *   **Examples**:
        *   Hetzner Matrix GPU (which typically comes with ample vRAM)
        *   AWS `g4ad.xlarge` instance or similar cloud GPU instances.

## Memory (RAM)

Ensure you have enough RAM available for the models you intend to use. Refer to the [Training the Model](./training-models.md#4-model-selection-hardware) section for examples of RAM requirements for specific models.

*   For the default BERT models, you will generally need at least 4GB of RAM dedicated to the model, plus additional RAM for the operating system and the ticket system itself if they are running on the same host.

## Deployment Considerations

*   **Co-location vs. Separate Devices**: You can run Open Ticket AI on the same server as your ticket system or on a separate machine.
*   **Network Configuration**: If running on separate devices, ensure your network configuration allows communication between Open Ticket AI and your ticket system. You will need to adjust the `rest_settings` (specifically the `base_url`) in your `run_config.yaml` to point to the correct network address of your ticket system's API.
