---
description: "Plan your Ticket Automation project: multiple starting points (labeled data, unlabeled data, or no data) and clear flows to training, deployment, and support. Includes quick-start via hosted Prediction API."
pageClass: "full-page"
aside: false
---

# Ticket Automation Planner (Flows)

Not every team starts from the same place. Pick the flow that matches your situation.
Each diagram links to the relevant part of the docs and ends in a clear **service package**.
## 0) One-screen overview

```mermaid
---
config:
  theme: 'dark'
---
flowchart TD
  S((Start)) --> Q1{Labeled?}
  Q1 -- Yes --> A0[Flow A]
  Q1 -- No --> Q2{Unlabeled?}
  Q2 -- Yes --> B0[Flow B]
  Q2 -- No --> Q3{Fast?}
  Q3 -- Yes --> D0[Flow D]
  Q3 -- No --> C0[Flow C]

click A0 "#flow-a-many-labeled" "Flow A"
click B0 "#flow-b-many-unlabeled" "Flow B"
click C0 "#flow-c-few-or-no-tickets" "Flow C"
click D0 "#flow-d-quick-start-hosted-api" "Flow D"
```

---

## <a id="flow-a-many-labeled"></a> A) Many labeled

```mermaid
---
config:
  theme: 'dark'
---
flowchart TD
  A[Audit/Tax] --> B[Train]
  B --> C[Eval]
  C --> D[On-Prem]
  D --> E[Pilot]
  E --> F[Support]
```

---

## <a id="flow-b-many-unlabeled"></a> B) Many unlabeled

```mermaid
---
config:
  theme: 'dark'
---
flowchart TD
  A[Ingest] --> B[Auto-Label]
  B --> C[QC]
  C --> D{OK?}
  D -- No --> B
  D -- Yes --> E[Train]
  E --> F[Eval]
  F --> G[On-Prem]
  G --> H[Support]
```

---

## <a id="flow-c-few-or-no-tickets"></a> C) Few / no tickets

```mermaid
---
config:
  theme: 'dark'
---
flowchart TD
  A[Define Tax] --> B[Synth Data]
  B --> C[Baseline]
  C --> D[Eval]
  D --> E{Pilot}
  E -- API --> H[Hosted DE]
  E -- Local --> I[On-Prem]
  H --> J[Collect]
  I --> J
  J --> K[Fine-Tune]
  K --> L[Prod/Support]
```

---

## <a id="flow-d-quick-start-hosted-api"></a> D) Quick start (API)

```mermaid
---
config:
  theme: 'dark'
---
flowchart TD
  A[Use API DE] --> B[Measure]
  B --> C{Tax OK?}
  C -- Yes --> D[Scale/Support]
  C -- No --> E[Auto/Synth - Train]
  E --> F[On-Prem]
```

---

## Optional add-ons

### Multilingual

```mermaid
---
config:
  theme: 'dark'
---
flowchart TD
  A[More langs?] --> B{Hist per lang?}
  B -- Yes --> C[Auto-Label]
  B -- No --> D[Synth]
  C --> E[Train Multi]
  D --> E
  E --> F[Pilot/Eval]
```

### Extra attributes

```mermaid
---
config:
  theme: 'dark'
---
flowchart TD
  A[Add tags/assignee/FAA] --> B[Extend labels/gen]
  B --> C[Multi-task/Chain]
  C --> D[Deploy]
```

