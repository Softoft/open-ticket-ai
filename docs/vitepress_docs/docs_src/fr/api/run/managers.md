---
description: Explorez la classe `Orchestrator` d'OpenTicketAI, un composant essentiel pour
  automatiser les flux de travail de traitement des tickets. Ce module Python gère
  le cycle de vie complet des pipelines, y compris l'instanciation via l'injection
  de dépendances, le traitement individuel des tickets et l'exécution planifiée pour
  une automatisation continue.
---
# Documentation pour `**/ce/run/managers/*.py`

## Module : `open_ticket_ai\src\ce\run\managers\orchestrator.py`

Utilitaires d'orchestration de haut niveau.

### <span style='text-info'>class</span> `Orchestrator`

Orchestre l'exécution des pipelines de traitement de tickets.
Cette classe gère le cycle de vie des pipelines, y compris :
- L'instanciation des pipelines via l'injection de dépendances
- Le traitement individuel des tickets
- L'exécution planifiée des pipelines

**Paramètres :**

- **`config`** () - Paramètres de configuration pour l'orchestrateur
- **`container`** () - Conteneur d'injection de dépendances fournissant les instances de pipeline
- **`_logger`** () - Instance de logger pour les opérations d'orchestration
- **`_pipelines`** () - Dictionnaire associant les identifiants de pipeline aux instances de pipeline


::: details #### <Badge type="info" text="méthode"/> <span class='text-warning'>def</span> `__init__(self, config: OpenTicketAIConfig, container: AbstractContainer)`
Initialise l'Orchestrator avec la configuration et le conteneur d'injection de dépendances.

**Paramètres :**

- **`config`** () - Paramètres de configuration pour l'orchestrateur.
- **`container`** () - Conteneur d'injection de dépendances fournissant les instances de pipeline.

:::


::: details #### <Badge type="info" text="méthode"/> <span class='text-warning'>def</span> `process_ticket(self, ticket_id: str, pipeline: Pipeline) -> PipelineContext`
Exécute un pipeline pour un ticket spécifique.
Crée un contexte de traitement et exécute le pipeline spécifié pour traiter
le ticket donné. C'est la méthode principale pour le traitement individuel des tickets.

**Paramètres :**

- **`ticket_id`** () - Identifiant unique du ticket à traiter.
- **`pipeline`** () - Instance de pipeline à exécuter.

**Retourne :** (`PipelineContext`) - Le contexte d'exécution contenant les résultats et l'état
après l'exécution du pipeline.

:::


::: details #### <Badge type="info" text="méthode"/> <span class='text-warning'>def</span> `build_pipelines(self) -> None`
Instancie tous les objets pipeline configurés.
Utilise le conteneur d'injection de dépendances pour créer des instances de pipeline
basées sur la configuration. Remplit le registre interne des pipelines
avec les correspondances entre les identifiants de pipeline et les instances.

:::


::: details #### <Badge type="info" text="méthode"/> <span class='text-warning'>def</span> `set_schedules(self) -> None`
Configure l'exécution planifiée pour tous les pipelines.
Effectue les opérations suivantes :
1. Construit les pipelines s'ils ne sont pas déjà instanciés
2. Configure l'exécution périodique pour chaque pipeline selon sa
   configuration de planification en utilisant la bibliothèque `schedule`

La planification utilise les paramètres de configuration suivants :
- interval : Valeur de l'intervalle numérique
- unit : Unité de temps (par ex., minutes, heures, jours)

Note :
- Utilise le modèle `schedule.every(interval).unit` pour la planification
- Passe un contexte `ticket_id` vide lors des exécutions planifiées

:::


---