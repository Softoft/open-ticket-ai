---
description: Guide du développeur pour l'ATC Community Edition, un outil de classification de tickets sur site. Apprenez à configurer le système avec YAML, à l'exécuter depuis la CLI et à étendre son architecture en utilisant des composants Python personnalisés, des pipe_ids et des adaptateurs de système de tickets.
title: Informations pour les développeurs
---

# Informations pour les développeurs sur l'ATC Community Edition

## Aperçu

L'ATC Community Edition est une solution sur site pour la classification automatisée des tickets de support. La version MVP actuelle est contrôlée via un fichier de configuration YAML et démarrée via la CLI. Il n'y a pas d'API REST pour téléverser des données d'entraînement ou déclencher une session d'entraînement.

## Architecture logicielle

L'application se compose essentiellement des packages suivants :

*   **core** – classes de base, modèles de configuration et fonctions utilitaires.
*   **run** – contient le pipeline pour la classification des tickets.
*   **ticket\_system\_integration** – adaptateurs pour différents systèmes de tickets.
*   **main.py** – point d'entrée de la CLI qui démarre le planificateur et l'orchestrateur.

L'orchestrateur exécute des `AttributePredictors` configurables, qui sont composés de `DataFetcher`, `DataPreparer`, `AIInferenceService` et `Modifier`. Tous les composants sont définis dans `config.yml` et validés au démarrage du programme.

Un exemple de commande pour démarrer l'application :

```bash
python -m open_ticket_ai.src.ce.main start
```

## Entraînement de modèles personnalisés

L'entraînement direct via l'application n'est pas fourni dans le MVP. Des modèles pré-entraînés peuvent être spécifiés et utilisés dans la configuration. Si un modèle doit être ajusté ou nouvellement créé, cela doit être fait en dehors de l'application.

## Extension

Des fetchers, preparers, services d'IA ou modifiers personnalisés peuvent être implémentés en tant que classes Python et enregistrés via la configuration. Grâce à l'injection de dépendances, de nouveaux composants peuvent être facilement intégrés.

## Comment ajouter un pipe personnalisé

Le pipeline de traitement peut être étendu avec vos propres classes de pipe. Un pipe est une
unité de travail qui reçoit un `PipelineContext`, le modifie et le retourne. Tous les
pipes héritent de la classe de base `Pipe` qui déjà
implémente le mixin `Providable`.

1.  **Créez un modèle de configuration** pour votre pipe s'il nécessite des paramètres.
2.  **Créez une sous-classe de `Pipe`** et implémentez la méthode `process`.
3.  **Redéfinissez `get_provider_key()`** si vous souhaitez une clé personnalisée.

L'exemple simplifié suivant, tiré de `AI_README`, montre un pipe d'analyse de sentiment :

```python
class SentimentPipeConfig(BaseModel):
    model_name: str = "distilbert/distilbert-base-uncased-finetuned-sst-2-english"


class SentimentAnalysisPipe(Pipe, Providable):
    def __init__(self, config: SentimentPipeConfig):
        super().__init__(config)
        self.classifier = pipeline("sentiment-analysis", model=config.model_name)

    def process(self, context: PipelineContext) -> PipelineContext:
        ticket_text = context.data.get("combined_text")
        if not ticket_text:
            context.stop_pipeline()
            return context

        sentiment = self.classifier(ticket_text)[0]
        context.data["sentiment"] = sentiment["label"]
        context.data["sentiment_confidence"] = sentiment["score"]
        return context

    @classmethod
    def get_provider_key(cls) -> str:
        return "SentimentAnalysisPipe"
```

Après avoir implémenté la classe, enregistrez-la dans votre registre d'injection de dépendances
et référencez-la dans `config.yml` en utilisant la clé de fournisseur retournée par
`get_provider_key()`.

## Comment intégrer un nouveau système de tickets

Pour connecter un autre système de help desk, implémentez un nouvel adaptateur qui hérite de
`TicketSystemAdapter`. L'adaptateur effectue la conversion entre l'API externe et les
modèles unifiés du projet.

1.  **Créez une classe d'adaptateur**, par ex. `FreshdeskAdapter(TicketSystemAdapter)`.
2.  **Implémentez toutes les méthodes abstraites** :
    - `find_tickets`
    - `find_first_ticket`
    - `create_ticket`
    - `update_ticket`
    - `add_note`
3.  **Traduisez les données** vers et depuis les modèles `UnifiedTicket` et `UnifiedNote`.
4.  **Fournissez un modèle de configuration** pour les identifiants ou les paramètres de l'API.
5.  **Enregistrez l'adaptateur** dans `create_registry.py` afin qu'il puisse être instancié
    à partir de la configuration YAML.

Une fois enregistré, spécifiez l'adaptateur dans la section `system` de `config.yml` et
l'orchestrateur l'utilisera pour communiquer avec le système de tickets.

## Résumé

L'ATC Community Edition offre un flux de travail exécuté localement pour la classification automatique de tickets dans sa version MVP. Tous les paramètres sont gérés via des fichiers YAML ; aucune API REST n'est disponible. Des processus ou des scripts externes doivent être utilisés pour l'entraînement.