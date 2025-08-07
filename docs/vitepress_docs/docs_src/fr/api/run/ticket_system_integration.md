---
description: Découvrez notre bibliothèque Python pour une intégration transparente des systèmes de tickets. Cette
  documentation détaille le `TicketSystemAdapter`, une classe de base abstraite pour construire
  des connecteurs personnalisés, et fournit un `OTOBOAdapter` prêt à l'emploi. Apprenez à
  gérer les tickets sur différentes plateformes en utilisant des modèles unifiés comme `UnifiedTicket`, `UnifiedNote`,
  et `SearchCriteria` pour créer, mettre à jour et rechercher des tickets de support.
---
# Documentation pour `**/ce/ticket_system_integration/*.py`

## Module : `open_ticket_ai\src\ce\ticket_system_integration\otobo_adapter.py`

Paquet pour l'intégration avec les systèmes OTOBO.
Ce module fournit l'interface principale pour l'intégration OTOBO en exposant
la classe `OTOBOAdapter`. Il sert de point d'entrée public de l'API pour
interagir avec les services OTOBO.



---

## Module : `open_ticket_ai\src\ce\ticket_system_integration\otobo_adapter_config.py`



---

## Module : `open_ticket_ai\src\ce\ticket_system_integration\ticket_system_adapter.py`


### <span style='text-info'>class</span> `TicketSystemAdapter`

Une classe de base abstraite pour les adaptateurs de système de tickets.
Cette classe définit l'interface que tous les adaptateurs de système de tickets concrets doivent
implémenter pour interagir avec différents systèmes de billetterie. Elle fournit une gestion
de configuration commune par injection de dépendances et exige que les sous-classes
implémentent les opérations de base sur les tickets.

**Paramètres :**

- **`config`** (`SystemConfig`) - Objet de configuration système contenant les paramètres de l'adaptateur.


::: details #### <Badge type="info" text="method"/> <span class='text-warning'>def</span> `__init__(self, config: SystemConfig)`
Initialise l'adaptateur avec la configuration système.
Ce constructeur est automatiquement injecté avec la configuration système
en utilisant le framework d'injection de dépendances. Il initialise l'adaptateur
avec la configuration fournie et assure la configuration correcte des
composants hérités.

**Paramètres :**

- **`config`** (`SystemConfig`) - L'objet de configuration système contenant
tous les réglages et paramètres nécessaires pour l'adaptateur.

:::


::: details #### <Badge type="info" text="method"/> <span class="text-warning">async def</span> `update_ticket(self, ticket_id: str, updates: dict) -> bool`
Met à jour un ticket dans le système.
Cette méthode doit être implémentée par les adaptateurs concrets pour gérer la mise à jour
des attributs de ticket dans le système de billetterie cible. Elle doit prendre en charge les mises à jour
partielles et retourner la représentation du ticket mis à jour.

**Paramètres :**

- **`ticket_id`** () - Identifiant unique du ticket à mettre à jour.
- **`updates`** () - Dictionnaire des attributs à mettre à jour sur le ticket.

**Retourne :** (`bool`) - ``True`` si la mise à jour a réussi, sinon ``False``.

:::


::: details #### <Badge type="info" text="method"/> <span class="text-warning">async def</span> `find_tickets(self, criteria: SearchCriteria) -> list[UnifiedTicket]`
Recherche les tickets correspondant aux ``criteria``.
Cette méthode doit être implémentée par les adaptateurs concrets pour effectuer
des recherches complexes dans le système de billetterie cible. La structure de la
requête est spécifique à l'adaptateur mais doit prendre en charge les opérations de filtrage
et de recherche courantes.

**Paramètres :**

- **`criteria`** () - Paramètres définissant les tickets à rechercher.

**Retourne :** (`list[UnifiedTicket]`) - Une liste de tickets qui correspondent aux critères.
Retourne une liste vide si aucune correspondance n'est trouvée.

:::


::: details #### <Badge type="info" text="method"/> <span class="text-warning">async def</span> `find_first_ticket(self, criteria: SearchCriteria) -> UnifiedTicket | None`
Retourne le premier ticket qui correspond aux ``criteria``, s'il y en a.
Ceci est une méthode de commodité qui doit retourner le premier ticket correspondant
d'une opération de recherche. Elle doit optimiser les performances
en limitant les résultats en interne.

**Paramètres :**

- **`criteria`** () - Paramètres définissant le ticket à rechercher.

**Retourne :** (`Optional[UnifiedTicket]`) - Le premier ticket correspondant ou ``None`` si aucun ticket ne correspond.

:::


::: details #### <Badge type="info" text="method"/> <span class="text-warning">async def</span> `create_ticket(self, ticket_data: UnifiedTicket) -> UnifiedTicket`
Crée un nouveau ticket dans le système.
Cette méthode doit être implémentée par les adaptateurs concrets pour gérer la création de tickets
dans le système de billetterie cible. Les données du ticket sont fournies dans un format unifié.

**Paramètres :**

- **`ticket_data`** (`UnifiedTicket`) - Les données du ticket à créer. Contient tous les champs nécessaires dans un
format indépendant du système.

**Retourne :** (`UnifiedTicket`) - L'objet ticket créé avec les identifiants et les champs générés par le système.

:::


::: details #### <Badge type="info" text="method"/> <span class="text-warning">async def</span> `add_note(self, ticket_id: str, note: UnifiedNote) -> UnifiedNote`
Ajoute une note à un ticket existant.
Cette méthode doit être implémentée par les adaptateurs concrets pour joindre des notes/commentaires
aux tickets dans le système cible. Le contenu de la note est fourni dans un format unifié.

**Paramètres :**

- **`ticket_id`** (`str`) - Identifiant unique du ticket cible.
- **`note`** (`UnifiedNote`) - Le contenu et les métadonnées de la note à ajouter.

**Retourne :** (`UnifiedNote`) - L'objet note ajouté avec les métadonnées générées par le système (par ex., horodatage, ID).

:::


---

## Module : `open_ticket_ai\src\ce\ticket_system_integration\unified_models.py`


### <span style='text-info'>class</span> `UnifiedEntity`

Entité de base avec ID et nom optionnels.

**Paramètres :**

- **`id`** (`Optional[int]`) (default: `None`) - Identifiant unique pour l'entité. Par défaut à None.
- **`name`** (`Optional[str]`) (default: `None`) - Nom d'affichage de l'entité. Par défaut à None.

### <span style='text-info'>class</span> `UnifiedUser`

Représente un utilisateur dans le système.
Hérite des attributs de `UnifiedEntity` et ajoute :

**Paramètres :**

- **`email`** (`Optional[str]`) (default: `None`) - Adresse e-mail de l'utilisateur. Par défaut à None.

### <span style='text-info'>class</span> `UnifiedQueue`

Représente une file d'attente de tickets.
Hérite des attributs de `UnifiedEntity`.

### <span style='text-info'>class</span> `UnifiedPriority`

Représente un niveau de priorité de ticket.
Hérite des attributs de `UnifiedEntity`.

### <span style='text-info'>class</span> `UnifiedStatus`

Représente un statut de ticket.
Hérite des attributs de `UnifiedEntity`.

### <span style='text-info'>class</span> `UnifiedNote`

Représente une note attachée à un ticket.

**Paramètres :**

- **`id`** (`Optional[str]`) (default: `None`) - Identifiant unique pour la note. Par défaut à None.
- **`body`** (`str`) - Contenu de la note.
- **`created_at`** (`datetime`) - Horodatage de la création de la note.
- **`is_internal`** (`bool`) - Indique si la note est interne (non visible par les clients).
- **`author`** (`UnifiedUser`) - Utilisateur qui a créé la note.

### <span style='text-info'>class</span> `UnifiedTicket`

Représentation unifiée d'un ticket de support.

**Paramètres :**

- **`id`** (`str`) - Identifiant unique pour le ticket.
- **`subject`** (`str`) - Ligne d'objet du ticket.
- **`body`** (`str`) - Contenu/description principal du ticket.
- **`custom_fields`** (`Dict`) - Données de champs personnalisés supplémentaires associées au ticket.
- **`queue`** (`UnifiedQueue`) - File d'attente à laquelle le ticket appartient.
- **`priority`** (`UnifiedPriority`) - Niveau de priorité du ticket.
- **`status`** (`UnifiedStatus`) - Statut actuel du ticket.
- **`owner`** (`UnifiedUser`) - Utilisateur actuellement assigné au ticket.
- **`notes`** (`List[UnifiedNote]`) (default: `liste vide`) - Liste des notes attachées au ticket. Par défaut à une liste vide.

### <span style='text-info'>class</span> `SearchCriteria`

Critères pour la recherche/le filtrage des tickets.

**Paramètres :**

- **`id`** (`Optional[str]`) (default: `None`) - ID du ticket à rechercher. Par défaut à None.
- **`subject`** (`Optional[str]`) (default: `None`) - Texte à rechercher dans les objets des tickets. Par défaut à None.
- **`queue`** (`Optional[UnifiedQueue]`) (default: `None`) - File d'attente par laquelle filtrer. Par défaut à None.
- **`user`** (`Optional[UnifiedUser]`) (default: `None`) - Utilisateur par lequel filtrer (par ex., propriétaire). Par défaut à None.


---