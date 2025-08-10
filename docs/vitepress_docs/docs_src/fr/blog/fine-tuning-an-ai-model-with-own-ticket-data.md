---
description: Apprenez à affiner un modèle d'IA avec vos propres données de tickets pour une classification de tickets précise et automatisée. Ce guide fournit des instructions étape par étape pour préparer des jeux de données et entraîner des modèles en utilisant Hugging Face Transformers ou une API REST sur site (on-premise).
---
# Comment affiner un modèle d'IA avec vos propres données de tickets

L'affinage d'un modèle d'IA sur vos propres données de tickets est un moyen puissant de personnaliser la classification des tickets pour votre organisation. En entraînant un modèle sur des tickets de support étiquetés, vous lui apprenez votre langage et vos catégories spécifiques à votre domaine. Ce processus implique généralement la préparation d'un jeu de données (souvent un fichier CSV ou JSON de tickets et d'étiquettes), le choix ou la création d'étiquettes (telles que les départements ou les niveaux de priorité), puis l'entraînement d'un modèle comme un classifieur basé sur les Transformers sur ces données. Vous pouvez utiliser des outils comme la bibliothèque Transformer de Hugging Face pour entraîner des modèles localement, ou utiliser une solution dédiée comme **Open Ticket AI (ATC)**, qui fournit une API REST sur site (on-premise) pour la classification de tickets. Dans les deux cas, vous bénéficiez de l'apprentissage par transfert (transfer learning) : un modèle pré-entraîné (par ex. BERT, DistilBERT ou RoBERTa) est adapté à vos catégories de tickets, améliorant considérablement la précision par rapport à un modèle générique.

Les flux de travail modernes de classification de texte suivent ces étapes de haut niveau :

* **Collecter et étiqueter les données :** Rassemblez les tickets historiques et attribuez-leur les bonnes catégories (files d'attente) ou priorités. Chaque ticket doit avoir un champ de texte et au moins une étiquette.
* **Formater le jeu de données :** Enregistrez ces données étiquetées dans un format structuré (CSV ou JSON). Par exemple, un CSV pourrait avoir les colonnes `"text","label"`.
* **Diviser en ensembles d'entraînement/test :** Réservez une partie pour la validation/test afin d'évaluer la performance.
* **Affiner le modèle :** Utilisez une bibliothèque comme Hugging Face Transformers, ou notre API Open Ticket AI, pour entraîner un modèle de classification sur les données.
* **Évaluer et déployer :** Vérifiez la précision (ou le score F1) sur les données non vues, puis utilisez le modèle entraîné pour classifier de nouveaux tickets.

Les lecteurs avertis sur le plan technique peuvent suivre ces étapes en détail. Les exemples ci-dessous illustrent comment préparer les données de tickets et affiner un modèle en utilisant **Hugging Face Transformers**, ainsi que la manière dont notre solution Open Ticket AI prend en charge ce flux de travail via des appels API. Tout au long de ce guide, nous supposons des catégories de tickets courantes (par ex. « Facturation », « Support Technique ») et des étiquettes de priorité, mais vos étiquettes peuvent être tout ce qui est pertinent pour votre système.

## Préparer vos données de tickets

Tout d'abord, rassemblez un ensemble représentatif de tickets passés et étiquetez-les selon votre schéma de classification. Les étiquettes peuvent être des départements (comme **Support Technique**, **Service Client**, **Facturation**, etc.) ou des niveaux de priorité (par ex. **Faible**, **Moyen**, **Élevé**). Par exemple, le jeu de données de tickets Softoft inclut des catégories telles que *Support Technique*, *Facturation et Paiements*, *Support Informatique* et *Demande Générale*. Un modèle d'exemple de Hugging Face utilise des étiquettes comme *Question de facturation*, *Demande de fonctionnalité*, *Demande générale* et *Problème technique*. Définissez les catégories qui ont du sens pour votre flux de travail.

Organisez les données au format CSV ou JSON. Chaque enregistrement doit contenir le texte du ticket et son étiquette. Par exemple, un CSV pourrait ressembler à ceci :

```
text,label
"Mon imprimante ne se connecte pas au WiFi",Matériel,  # Exemple de texte de ticket et sa catégorie
"J'ai besoin d'aide pour accéder à mon compte",Compte
```

Si vous incluez des priorités ou plusieurs étiquettes, vous pouvez ajouter d'autres colonnes (par ex. `priority`). La structure exacte est flexible, tant que vous associez clairement chaque texte de ticket à sa ou ses étiquettes. Il est courant d'avoir une colonne pour le contenu du ticket (par ex. `"text"` ou `"ticket_text"`) et une colonne pour l'étiquette.

Vous devrez peut-être nettoyer et prétraiter légèrement le texte (par ex. supprimer les signatures, les balises HTML ou anonymiser les données), mais dans de nombreux cas, le texte brut du ticket fonctionne bien comme entrée pour les modèles NLP modernes. Enfin, divisez les données étiquetées en un ensemble d'entraînement et un ensemble de validation/test (par exemple, 80 % entraînement / 20 % test). Cette division vous permet de mesurer à quel point le modèle affiné généralise.

## Étiquetage des tickets

Des étiquettes cohérentes et précises sont cruciales. Assurez-vous que chaque ticket est correctement assigné à l'une de vos catégories choisies. Cela peut être fait manuellement par le personnel de support ou en utilisant les métadonnées de ticket existantes si elles sont disponibles. Souvent, les organisations étiquettent les tickets par *file d'attente* ou département, et parfois aussi par *priorité*. Par exemple, le jeu de données de tickets par e-mail de Softoft catégorise les tickets à la fois par département (file d'attente) et par priorité. La priorité peut être utile si vous voulez entraîner un modèle à prédire l'urgence : par ex., `Faible`, `Moyen`, `Critique`. Dans de nombreuses configurations, vous pourriez entraîner un modèle pour la classification par département et un autre pour la classification par priorité.

Quel que soit votre schéma, assurez-vous d'avoir un ensemble fini de valeurs d'étiquettes. Dans un CSV, vous pourriez avoir :

```
text,label,priority
"Le système plante lors de la sauvegarde du fichier","Support Technique","Élevée"
"Demande de changement d'adresse de facturation","Facturation","Faible"
```

Cet exemple a deux colonnes d'étiquettes : une pour la catégorie et une pour la priorité. Pour des raisons de simplicité, dans les exemples suivants, nous supposons une tâche de classification à étiquette unique (une seule colonne d'étiquette).

**Conseils clés pour l'étiquetage :**

* Définissez clairement les noms de vos étiquettes. Par exemple, *Support Technique* vs *Support Informatique* vs *Problème Matériel* – évitez les chevauchements ambigus.
* Si les tickets appartiennent souvent à plusieurs catégories, vous pourriez envisager une classification multi-étiquettes (assigner plusieurs étiquettes) ou la diviser en modèles distincts.
* Utilisez un formatage cohérent (même orthographe, même casse) pour les étiquettes dans votre jeu de données.

À la fin de cette étape, vous devriez avoir un fichier de jeu de données étiqueté (CSV ou JSON) avec les textes des tickets et leurs étiquettes, prêt pour le modèle.

## Affinage avec Hugging Face Transformers

L'une des manières les plus flexibles d'affiner un classifieur de texte est d'utiliser la bibliothèque [Hugging Face Transformers](https://huggingface.co/transformers/). Cela vous permet de partir d'un modèle de langage pré-entraîné (comme BERT ou RoBERTa) et de l'entraîner davantage sur votre jeu de données de tickets spécifique. Les étapes principales sont : tokeniser le texte, configurer un `Trainer`, et appeler `train()`.

1. **Charger le jeu de données :** Utilisez `datasets` ou `pandas` pour charger votre CSV/JSON. Par exemple, la bibliothèque `datasets` de Hugging Face peut lire un CSV directement :

   ```python
   from datasets import load_dataset
   dataset = load_dataset("csv", data_files={
       "train": "tickets_train.csv",
       "validation": "tickets_val.csv"
   })
   # En supposant que 'text' est la colonne avec le contenu du ticket, et 'label' est la colonne de catégorie.
   ```

2. **Tokeniser le texte :** Les transformers pré-entraînés nécessitent une entrée tokenisée. Chargez un tokenizer (par ex. DistilBERT) et appliquez-le à votre texte :

   ```python
   from transformers import AutoTokenizer
   tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")

   def preprocess_function(examples):
       # Tokeniser les textes (cela produira input_ids, attention_mask, etc.)
       return tokenizer(examples["text"], truncation=True, padding="max_length")

   tokenized_datasets = dataset.map(preprocess_function, batched=True)
   ```

   Ceci suit l'exemple de Hugging Face : d'abord charger le tokenizer DistilBERT, puis utiliser `Dataset.map` pour tokeniser tous les textes par lots. Le résultat (`tokenized_datasets`) contient les ID d'entrée et les masques d'attention, prêts pour le modèle.

3. **Charger le modèle :** Choisissez un modèle pré-entraîné et spécifiez le nombre d'étiquettes. Par exemple, pour affiner DistilBERT pour la classification :

   ```python
   from transformers import AutoModelForSequenceClassification
   num_labels = 4  # définissez ceci sur le nombre de vos catégories
   model = AutoModelForSequenceClassification.from_pretrained(
       "distilbert-base-uncased", num_labels=num_labels
   )
   ```

   Cela correspond à l'exemple de classification de séquence de Hugging Face, où le modèle est chargé avec `num_labels` égal au nombre de classes dans votre jeu de données.

4. **Définir les arguments d'entraînement et le Trainer :** Définissez les hyperparamètres avec `TrainingArguments`, puis créez un `Trainer` avec votre modèle et vos données tokenisées :

   ```python
   from transformers import TrainingArguments, Trainer
   training_args = TrainingArguments(
       output_dir="./ticket_model",
       num_train_epochs=3,
       per_device_train_batch_size=8,
       per_device_eval_batch_size=8,
       learning_rate=2e-5,
       evaluation_strategy="epoch"
   )
   trainer = Trainer(
       model=model,
       args=training_args,
       train_dataset=tokenized_datasets["train"],
       eval_dataset=tokenized_datasets["validation"],
       tokenizer=tokenizer
   )
   ```

   Cela reflète le guide de Hugging Face : après avoir configuré `TrainingArguments` (pour le répertoire de sortie, les époques, la taille de lot, etc.), nous instancions `Trainer` avec le modèle, les jeux de données, le tokenizer et les arguments d'entraînement.

5. **Entraîner le modèle :** Appelez `trainer.train()` pour démarrer l'affinage. Cela s'exécutera pour le nombre d'époques spécifié, en évaluant périodiquement sur l'ensemble de validation s'il est fourni.

   ```python
   trainer.train()
   ```

   Conformément à la documentation, cette seule commande lance l'affinage. L'entraînement peut prendre de quelques minutes à plusieurs heures en fonction de la taille des données et du matériel (GPU recommandé pour les grands jeux de données).

6. **Évaluer et sauvegarder :** Après l'entraînement, évaluez le modèle sur votre ensemble de test pour vérifier la précision ou d'autres métriques. Ensuite, sauvegardez le modèle affiné et le tokenizer :

   ```python
   trainer.evaluate()
   model.save_pretrained("fine_tuned_ticket_model")
   tokenizer.save_pretrained("fine_tuned_ticket_model")
   ```

   Vous pourrez recharger ce modèle plus tard avec `AutoModelForSequenceClassification.from_pretrained("fine_tuned_ticket_model")`.

Une fois entraîné, vous pouvez utiliser le modèle pour l'inférence. Par exemple, l'API pipeline de Hugging Face le rend facile :

```python
from transformers import pipeline

classifier = pipeline("text-classification", model="fine_tuned_ticket_model")
results = classifier("Veuillez réinitialiser mon mot de passe et vider mon cache.")
print(results)
```

Ceci affichera l'étiquette prédite et le score de confiance pour le nouveau texte de ticket. Comme le montrent les exemples de Hugging Face, l'abstraction `pipeline("text-classification")` vous permet de classifier rapidement de nouveaux textes de tickets avec le modèle affiné.

## Utiliser Open Ticket AI (ATC de Softoft) pour l'entraînement et l'inférence

Notre système **Open Ticket AI** (aussi connu sous le nom d'ATC – AI Ticket Classification) fournit une solution sur site (on-premise), conteneurisée avec Docker et dotée d'une API REST qui peut ingérer vos données de tickets étiquetées et entraîner des modèles automatiquement. Cela signifie que vous pouvez conserver toutes les données localement tout en tirant parti d'un ML puissant. L'API ATC a des points de terminaison pour téléverser des données, déclencher l'entraînement et classifier des tickets.

* **Téléverser les données d'entraînement :** Envoyez votre CSV de tickets étiquetés au point de terminaison `/api/v1/train-data`. L'API attend une charge utile CSV (`Content-Type: text/csv`) contenant vos données d'entraînement. Par exemple, en utilisant `requests` en Python :

  ```python
  import requests
  url = "http://localhost:8080/api/v1/train-data"
  headers = {"Content-Type": "text/csv"}
  with open("tickets_labeled.csv", "rb") as f:
      res = requests.post(url, headers=headers, data=f)
  print(res.status_code, res.text)
  ```

  Cela correspond à l'API « Train Data » dans la documentation d'ATC. Une réponse réussie signifie que les données ont été reçues.

* **Démarrer l'entraînement du modèle :** Après avoir téléversé les données, déclenchez l'entraînement en appelant `/api/v1/train` (aucun corps de requête n'est nécessaire). En pratique :

  ```bash
  curl -X POST http://localhost:8080/api/v1/train
  ```

  Ou en Python :

  ```python
  train_res = requests.post("http://localhost:8080/api/v1/train")
  print(train_res.status_code, train_res.text)
  ```

  Cela correspond à l'exemple de la documentation pour les développeurs, qui montre qu'un simple POST lance l'entraînement. Le service entraînera le modèle sur les données téléversées (il utilise son propre pipeline d'entraînement en interne, possiblement basé sur des modèles Transformer similaires). L'entraînement s'exécute sur votre serveur, et le modèle est sauvegardé localement une fois terminé.

* **Classifier de nouveaux tickets :** Une fois l'entraînement terminé, utilisez le point de terminaison `/api/v1/classify` pour obtenir des prédictions pour de nouveaux textes de tickets. Envoyez une charge utile JSON avec le champ `"ticket_data"` contenant le texte du ticket. Par exemple :

  ```python
  ticket_text = "Mon ordinateur portable surchauffe quand je lance l'application"
  res = requests.post(
      "http://localhost:8080/api/v1/classify",
      json={"ticket_data": ticket_text}
  )
  print(res.json())  # par ex. {"predicted_label": "Problème Matériel", "confidence": 0.95}
  ```

  La documentation d'ATC montre un exemple `curl` similaire pour la classification. La réponse inclura généralement la catégorie prédite (et éventuellement le score de confiance).

L'utilisation de l'API REST d'Open Ticket AI intègre le flux d'entraînement dans vos propres systèmes. Vous pouvez automatiser les téléversements et les sessions d'entraînement (par ex. entraînement nocturne ou sur de nouvelles données), puis utiliser le point de terminaison de classification dans votre flux de travail de billetterie. Comme tout s'exécute sur site, le contenu sensible des tickets ne quitte jamais vos serveurs.

## Exemple de code Python

Voici un exemple consolidé illustrant les deux flux de travail :

```python
# Exemple : Affinage avec Hugging Face
from transformers import AutoTokenizer,
    AutoModelForSequenceClassification,
    Trainer,
    TrainingArguments
from datasets import load_dataset

# Charger et diviser votre jeu de données CSV
dataset = load_dataset("csv", data_files={"train": "train.csv", "validation": "val.csv"})
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")


# Tokeniser
def preprocess(examples):
    return tokenizer(examples["text"], truncation=True, padding="max_length")


tokenized = dataset.map(preprocess, batched=True)

# Charger le modèle
num_labels = 5  # par ex., le nombre de catégories de tickets
model = AutoModelForSequenceClassification.from_pretrained(
    "distilbert-base-uncased",
    num_labels=num_labels
    )

# Configurer le Trainer
training_args = TrainingArguments(
    output_dir="./model_out", num_train_epochs=3, per_device_train_batch_size=8
)
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized["train"],
    eval_dataset=tokenized["validation"],
    tokenizer=tokenizer
)
trainer.train()
trainer.evaluate()
model.save_pretrained("fine_tuned_ticket_model")
tokenizer.save_pretrained("fine_tuned_ticket_model")

# Utiliser le modèle pour la classification
from transformers import pipeline

classifier = pipeline("text-classification", model="fine_tuned_ticket_model")
print(classifier("Exemple : L'application plante quand j'essaie de l'ouvrir"))

# Exemple : Utilisation de l'API Open Ticket AI
import requests

# Téléverser les données (CSV)
with open("tickets_labeled.csv", "rb") as data_file:
    res = requests.post(
        "http://localhost:8080/api/v1/train-data",
        headers={"Content-Type": "text/csv"},
        data=data_file
        )
    print("Statut du téléversement :", res.status_code)
# Déclencher l'entraînement
train_res = requests.post("http://localhost:8080/api/v1/train")
print("Statut de l'entraînement :", train_res.status_code)
# Classifier un nouveau ticket
res = requests.post(
    "http://localhost:8080/api/v1/classify",
    json={"ticket_data": "Impossible de se connecter au compte"}
    )
print("Prédiction :", res.json())
```

Ce script illustre les deux méthodes : le pipeline d'affinage de Hugging Face et les appels REST à l'API Open Ticket AI. Il charge et tokenise un jeu de données CSV, affine un classifieur DistilBERT, puis l'utilise via un pipeline. Il montre également comment envoyer les mêmes données via POST à l'API d'ATC et déclencher l'entraînement/la classification.

## Conclusion

L'affinage d'un modèle d'IA sur vos propres données de tickets permet une classification de tickets personnalisée et très précise. En étiquetant les tickets passés et en entraînant un modèle comme un Transformer, vous tirez parti de l'apprentissage par transfert et de la connaissance du domaine. Que vous utilisiez les API Python de Hugging Face ou une solution clé en main comme Open Ticket AI (le service de classification sur site de Softoft), le flux de travail est similaire : préparez des données étiquetées, entraînez le modèle sur celles-ci, puis utilisez le modèle entraîné pour les prédictions.

Nous avons montré comment structurer votre jeu de données CSV/JSON, utiliser l'API `Trainer` de Hugging Face pour l'affinage, et utiliser l'API REST d'Open Ticket AI pour l'entraînement et l'inférence sur site. La documentation de Hugging Face fournit des conseils détaillés sur l'utilisation des tokenizers et du `Trainer`, et des fiches de modèle (model cards) d'exemple illustrent comment les modèles de classification sont appliqués au routage des tickets. Avec ces outils, vous pouvez itérer rapidement : essayez différents modèles pré-entraînés (par ex. BERT, RoBERTa, ou même des modèles spécifiques au domaine), expérimentez avec les hyperparamètres, et mesurez la performance sur votre ensemble de test.

En suivant ces étapes, votre système de support peut automatiquement router les tickets vers la bonne équipe, signaler les problèmes urgents, et faire gagner à votre personnel d'innombrables heures de tri manuel. Cette intégration profonde du NLP dans votre flux de travail de billetterie est désormais accessible grâce aux bibliothèques et API modernes – il vous suffit de fournir vos données et vos étiquettes.