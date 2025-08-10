---
description: 'Découvrez un framework de pipeline Python modulaire pour construire des flux de traitement de données robustes. Cette documentation couvre les composants principaux : l''orchestrateur `Pipeline`, les étapes individuelles `Pipe`, et le `PipelineContext` pour la gestion de l''état. Apprenez à implémenter un traitement séquentiel, à gérer les erreurs avec élégance, à administrer le statut d''exécution (RUNNING, SUCCESS, FAILED, STOPPED), et à garantir la sécurité des types avec Pydantic.'
---
# Documentation pour `**/ce/run/pipeline/*.py`

## Module : `open_ticket_ai\src\ce\run\pipeline\context.py`


### <span style='text-info'>class</span> `PipelineContext`

Objet de contexte passé entre les étapes du pipeline.
Cette classe générique sert de conteneur pour partager l'état et les données entre les
différentes étapes d'un pipeline de traitement. Elle s'appuie sur Pydantic pour la validation
et la sérialisation des données.

Le paramètre de type générique `DataT` doit être une sous-classe de `BaseModel`,
garantissant la sécurité des types pour la charge utile principale des données.

**Paramètres :**

- **`data`** (`DataT`) - La charge utile principale des données en cours de traitement dans le pipeline.
Doit être une instance de modèle Pydantic correspondant au type générique.
- **`meta_info`** (`MetaInfo`) - Métadonnées sur l'exécution du pipeline, incluant
les informations de statut et les détails opérationnels.


::: details #### <Badge type="info" text="méthode"/> <span class='text-warning'>def</span> `stop_pipeline(self)`
Signale au pipeline d'arrêter le traitement.
Cette méthode fournit un moyen contrôlé pour les étapes du pipeline d'indiquer
que le traitement doit s'arrêter. Elle met à jour les métadonnées de statut du contexte
à `STOPPED`, que les étapes suivantes peuvent vérifier pour terminer prématurément.

Note :
    Cette méthode modifie l'état du contexte mais ne retourne aucune valeur.

:::


---

## Module : `open_ticket_ai\src\ce\run\pipeline\meta_info.py`


### <span style='text-info'>class</span> `MetaInfo`

Stocke les métadonnées sur l'état d'exécution du pipeline.
Ce modèle capture le statut actuel d'un pipeline ainsi que toute information
d'erreur en cas d'échec.

**Paramètres :**

- **`status`** () (par défaut : `RUNNING`) - Statut d'exécution actuel du pipeline. La valeur par défaut est RUNNING.
- **`error_message`** () - Message d'erreur détaillé si le pipeline a échoué. None si réussi.
- **`failed_pipe`** () - Identifiant du pipe spécifique qui a causé l'échec. None si réussi.


---

## Module : `open_ticket_ai\src\ce\run\pipeline\pipe.py`


### <span style='text-info'>class</span> `Pipe`

Interface pour tous les composants du pipeline.
Cette classe de base abstraite définit l'interface commune que tous les composants
du pipeline doivent implémenter. Elle hérite de `Providable`
pour permettre l'enregistrement automatique dans un registre de composants et de `ABC`
pour forcer l'implémentation des méthodes abstraites.

Les sous-classes doivent implémenter la méthode `process` pour définir leur logique
de transformation de données spécifique au sein du pipeline.

Attributs :
    Hérite des attributs de `Providable` pour la gestion du registre.
    InputDataType (type[InputDataT]) : Le type du modèle de données d'entrée 
        attendu par ce composant de pipe.
    OutputDataType (type[OutputDataT]) : Le type du modèle de données de sortie 
        produit par ce composant de pipe.


::: details #### <Badge type="info" text="méthode"/> <span class='text-warning'>def</span> `process(self, context: PipelineContext[InputDataT]) -> PipelineContext[OutputDataT]`
Traite un objet de contexte de pipeline et retourne le contexte modifié.
Cette méthode définit la logique de traitement principale pour un composant de pipeline.
Elle prend un objet `PipelineContext` contenant l'état partagé du pipeline,
effectue des transformations ou des opérations sur ce contexte, et retourne le
contexte mis à jour pour le composant suivant dans le pipeline.

Args :
    context : Le contexte de pipeline actuel contenant les données d'état partagées.

Retourne :
    L'objet `PipelineContext` mis à jour après le traitement.

Lève :
    Des exceptions spécifiques à l'implémentation peuvent être levées par les sous-classes pour
    indiquer des erreurs de traitement ou des états invalides.

:::


---

## Module : `open_ticket_ai\src\ce\run\pipeline\pipeline.py`

Définit la classe Pipeline pour exécuter une séquence de pipes.
Le Pipeline est un Pipe spécialisé qui exécute plusieurs pipes en séquence. Il gère le contexte
et le statut tout au long de l'exécution, traitant les erreurs et les demandes d'arrêt de manière appropriée.

### <span style='text-info'>class</span> `Pipeline`

Un pipeline qui exécute une séquence de pipes de manière séquentielle.
Cette classe gère le flux d'exécution de plusieurs pipes, en s'occupant des transitions de statut,
de la propagation des erreurs et des demandes d'arrêt pendant le traitement.

**Paramètres :**

- **`pipes`** () - Liste d'objets Pipe à exécuter en séquence.


::: details #### <Badge type="info" text="méthode"/> <span class='text-warning'>def</span> `__init__(self, config: PipelineConfig, pipes: List[Pipe])`
Initialise le Pipeline avec la configuration et la séquence de pipes.

**Paramètres :**

- **`config`** () - Paramètres de configuration pour le pipeline.
- **`pipes`** () - Liste ordonnée d'instances de Pipe à exécuter.

:::


::: details #### <Badge type="info" text="méthode"/> <span class='text-warning'>def</span> `execute(self, context: PipelineContext) -> PipelineContext`
Exécute tous les pipes séquentiellement avec gestion des erreurs et propagation du statut.
Traite chaque pipe en séquence tout en :
- Validant les données d'entrée à l'aide du modèle d'entrée de chaque pipe
- Gérant les demandes de statut STOPPED provenant des pipes
- Capturant et journalisant les exceptions pendant l'exécution des pipes
- Mettant à jour le statut du contexte de manière appropriée (RUNNING, SUCCESS, FAILED, STOPPED)

**Paramètres :**

- **`context`** () - Le contexte du pipeline contenant l'état d'exécution et les données.

**Retourne :** () - Le PipelineContext mis à jour reflétant l'état d'exécution final après le traitement.

:::


::: details #### <Badge type="info" text="méthode"/> <span class='text-warning'>def</span> `process(self, context: PipelineContext) -> PipelineContext`
Traite le contexte à travers toute la séquence du pipeline.
Implémente la méthode abstraite de la classe de base Pipe. Délègue à
la méthode `execute()` pour le traitement réel du pipeline.

**Paramètres :**

- **`context`** () - Le contexte du pipeline contenant l'état d'exécution et les données.

**Retourne :** () - Le PipelineContext mis à jour après le traitement à travers tous les pipes.

:::


---

## Module : `open_ticket_ai\src\ce\run\pipeline\status.py`


### <span style='text-info'>class</span> `PipelineStatus`

Représente les états possibles de l'exécution d'un pipeline.
Cette énumération définit les différents statuts qu'un pipeline peut avoir au cours de son cycle de vie.

**Paramètres :**

- **`RUNNING`** () - Indique que le pipeline est en cours d'exécution.
- **`SUCCESS`** () - Indique que le pipeline s'est terminé avec succès sans erreurs.
- **`STOPPED`** () - Indique que le pipeline a été délibérément arrêté (arrêt contrôlé).
- **`FAILED`** () - Indique que le pipeline s'est terminé en raison d'une erreur inattendue.


---