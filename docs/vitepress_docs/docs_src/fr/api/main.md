---
description: Documentation officielle pour le point d'entrée de l'interface de ligne de commande (CLI) d'Open Ticket AI. Ce guide couvre main.py, détaillant comment configurer les niveaux de journalisation et lancer l'application.
---
# Documentation pour `**/ce/*.py`

## Module : `open_ticket_ai\src\ce\app.py`



---

## Module : `open_ticket_ai\src\ce\main.py`

Point d'entrée de la CLI d'Open Ticket AI.
Ce module fournit l'interface de ligne de commande pour l'application Open Ticket AI.
Il configure les niveaux de journalisation et lance l'application principale.


### <span class='text-warning'>def</span> `main(verbose: bool, debug: bool)`

Configure la journalisation en fonction des options de la CLI.
Cette fonction définit le niveau de journalisation pour l'application en fonction des indicateurs de ligne de commande fournis.
Elle prend en charge deux niveaux de verbosité :
- `--verbose` pour la journalisation de niveau INFO
- `--debug` pour la journalisation de niveau DEBUG

Si aucun indicateur n'est fourni, le niveau de journalisation par défaut est WARNING. La fonction configure également le formatage des journaux et supprime les bibliothèques bruyantes (par ex., urllib3).

**Paramètres :**

- **`verbose`** (`bool`) - Active la journalisation de niveau INFO lorsque la valeur est True.
- **`debug`** (`bool`) - Active la journalisation de niveau DEBUG lorsque la valeur est True.



### <span class='text-warning'>def</span> `start()`

Initialise le conteneur et démarre l'application.
Cette commande effectue les actions suivantes :
1. Configure le conteneur d'injection de dépendances
2. Récupère l'instance de l'application principale depuis le conteneur
3. Exécute l'application
4. Affiche une bannière de démarrage stylisée à l'aide de `pyfiglet`

L'application suit un modèle d'injection de dépendances où toutes les dépendances requises sont résolues via le `DIContainer`.



---