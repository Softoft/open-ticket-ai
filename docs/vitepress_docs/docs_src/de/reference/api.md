# Open Ticket AI - Referenz

## Modul: `open_ticket_ai\experimental\anonymize_data.py`

### <span style='color: #2980B9;'>def</span> `anonymize_text(text)`

Anonymisiert sensible Informationen in einem gegebenen Text.

**Parameter:**

- **`text`** (`str`) - Der Eingabetext zur Anonymisierung.

**Rückgabe:** (`str`) - Der anonymisierte Text mit ersetzten benannten Entitäten, E-Mail-Adressen, Telefonnummern, IBANs und Adressen.

---

## Modul: `open_ticket_ai\experimental\email_extraction.py`

### ⚠️ Fehler beim Parsen von `open_ticket_ai\experimental\email_extraction.py`

```
erwartete einen eingerückten Block nach Funktionsdefinition in Zeile 14 (<unknown>, Zeile 15)
```

---

## Modul: `open_ticket_ai\scripts\doc_generation\add_docstrings.py`

### <span style='color: #2980B9;'>def</span> `find_python_files(path: Path) -> list[Path]`

Findet rekursiv alle Python-Dateien in einem gegebenen Pfad unter Beachtung von Ausschlussregeln.

**Parameter:**

- **`path`** () - Der Wurzelverzeichnispfad für die Suche.

**Rückgabe:** () - Eine Liste von Path-Objekten, die zu verarbeitende Python-Dateien repräsentieren.

### <span style='color: #2980B9;'>def</span> `clean_ai_response(response_text: str) -> str`

Bereinigt die KI-Antwort, um nur gültigen Python-Code zu erhalten.
Entfernt Markdown-Code-Umrandungen und führenden/abschließenden Text.

**Parameter:**

- **`response_text`** () - Der Rohtext der KI-Modellantwort.

**Rückgabe:** () - Bereinigter Python-Code-String aus der Antwort.

### <span style='color: #2980B9;'>async def</span> `add_docstrings_to_file_content(file_content: str) -> str | None`

Sendet den gesamten Dateiinhalt an ein KI-Modell, um fehlende Docstrings hinzuzufügen.

**Parameter:**

- **`file_content`** () - Ein String mit dem gesamten Quellcode einer Python-Datei.

**Rückgabe:** () - Der aktualisierte Dateiinhalt mit Docstrings oder None bei Fehlschlag.

### <span style='color: #2980B9;'>async def</span> `process_file(file_path: Path)`

Verarbeitet eine einzelne Python-Datei, indem sie zur Docstring-Hinzufügung an die KI gesendet und mit dem Ergebnis überschrieben wird.

**Parameter:**

- **`file_path`** () - Der Pfad zur zu verarbeitenden Python-Datei.

### <span style='color: #2980B9;'>async def</span> `main()`

Haupt-asynchrone Funktion zur Steuerung des Docstring-Generierungsprozesses.

---

## Modul: `open_ticket_ai\scripts\doc_generation\example_package\main_module.py`

### ⚠️ Fehler beim Parsen von `open_ticket_ai\scripts\doc_generation\example_package\main_module.py`

```
'DocstringRaises' Objekt hat kein Attribut 'default'
```

---

## Modul: `open_ticket_ai\scripts\doc_generation\generate_docs.py`

Ein Skript zur Generierung schöner Markdown-Dokumentation aus Python-Quellcode.
Verwendet das `ast`-Modul von Python, um den Quellcode zu durchlaufen,
Klassen, Funktionen und ihre Docstrings zu extrahieren. Parst die
Docstrings (unterstützt Google-, reStructuredText- und Numpydoc-Stile) und
formatiert die Ausgabe in eine saubere, moderne Markdown-Datei.

Funktionen:
-   Klassen- und funktionsbasierte Struktur.
-   Umfangreiches Parsing von Docstrings für Parameter-, Rückgabe- und Raises-Abschnitte.
-   Einbindung von Type Hints in Signaturen.
-   Modernes Markdown-Styling mit Badges und aufklappbaren Abschnitten.
-   Vollständig konfigurierbar über Befehlszeilenargumente.

### <span style='color: #8E44AD;'>class</span> `DocstringStyler`

Stellt Methoden zur Formatierung geparster Docstring-Komponenten in Markdown bereit.

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `style_params(params: List[dict], title: str) -> str`</summary>

Formatiert eine Parameterliste in eine Markdown-Liste.

</details>

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `style_returns(returns: Optional[dict]) -> str`</summary>

Formatiert den Rückgabeabschnitt in Markdown.

</details>

### <span style='color: #8E44AD;'>class</span> `MarkdownVisitor`

Ein AST-Besucher, der eine Python-Datei durchläuft und einen Markdown-Dokumentationsstring aufbaut.

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `__init__(self, file_path: Path)`</summary>

</details>

<details>
<summary>#### <span style='font-size: 极客时间; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `visit_ClassDef(self, node: ast.ClassDef)`</summary>

Verarbeitet eine Klassendefinition.

</details>

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `visit_FunctionDef(self, node: ast.FunctionDef)`</summary>

Verarbeitet eine Funktions- oder Methodendefinition.

</details>

<details>
<极客时间>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef)`</summary>

Verarbeitet eine asynchrone Funktions- oder Methodendefinition.

</details>

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `get_markdown(self) -> str`</summary>

Gibt den akkumulierten Markdown-Inhalt zurück.

</details>

### <span style='color: #2980B9;'>def</span> `parse_python_file(file_path: Path) -> str`

Parst eine Python-Datei und gibt ihre Dokumentation in Markdown zurück.

### <span style='color: #2980B9;'>def</span> `main()`

Hauptfunktion zur Ausführung des Dokumentationsgenerators.

---

## Modul: `open_ticket_ai\scripts\doc_generation\translate_docs.py`

### <span style='color: #2980B9;'>def</span> `translate_text(content: str, target_lang: str, model: str, api_key: str) -> str`

Übersetzt Markdown-*Inhalt* in *target_lang* mit OpenRouter.

**Parameter:**

- **`content`** () - Der zu übersetzende Markdown-Inhalt.
- **`target_lang`** () - Zielsprachcode (z.B. 'de', 'en').
- **`model`** () - OpenRouter-Modellkennung.
- **`api_key`** () - OpenRouter-API-Schlüssel.

**Rückgabe:** () - Übersetzter Markdown-Inhalt.

### <span style='color: #2980B9;'>def</span> `process_file(path: Path, root: Path, languages: List[str], model: str, api_key: str, out_dir: Path) -> None`

Übersetzt eine einzelne Markdown-*Datei* und schreibt Ergebnisse unter *out_dir*.

**Parameter:**

- **`path`** () - Pfad zur zu übersetzenden Markdown-Datei.
- **`root`** () - Wurzelverzeichnis der Dokumentation.
- **`languages`** () - Liste der Zielsprachcodes.
- **`model`** () - OpenRouter-Modellkennung.
- **`api_key`** () - OpenRouter-API-Schlüssel.
- **`out_dir`** () - Basisausgabeverzeichnis für Übersetzungen.

### <span style='color: #2980B9;'>def</span> `main() -> None`

Haupteinstiegspunkt für die Übersetzung von Markdown-Dokumentation mit OpenRouter.
Parst Befehlszeilenargumente für den Übersetzungsprozess, einschließlich Eingabeverzeichnis
der Markdown-Dokumente, Zielsprachen, OpenRouter-Modell und Ausgabeverzeichnis.
Durchläuft dann das Eingabeverzeichnis und verarbeitet jede Markdown-Datei
mit den bereitgestellten Argumenten.

**Rückgabe:** () - None

---

## Modul: `open_ticket_ai\scripts\license_script.py`

### <span style='color: #2980B9;'>def</span> `find_start_of_code(lines)`

Gibt den Index der ersten Nicht-Kommentarzeile zurück.

**Parameter:**

- **`lines`** (`list`) - Liste von Strings, die Zeilen in einer Datei repräsentieren.

**Rückgabe:** (`int`) - Index der ersten Zeile, die kein Kommentar oder Leerzeichen ist.

### <span style='color: #2980B9;'>def</span> `read_file(filepath)`

Liest alle Zeilen aus ``filepath``.

**Parameter:**

- **`filepath`** (`str`) - Pfad zur zu lesenden Datei.

**Rückgabe:** (`list`) - Liste von Strings, die Zeilen in der Datei repräsentieren.

### <span style='color: #2980B9;'>def</span> `write_file(filepath, lines)`

Schreibt ``lines`` in ``filepath``.

**Parameter:**

- **`filepath`** (`str`) - Pfad zur zu schreibenden Datei.
- **`lines`** (`list`) - Liste von Strings, die in die Datei geschrieben werden sollen.

### <span style='color: #2980B9;'>极客时间</span> `update_license_in_files(directory)`

Fügt den Lizenzhinweis oben in alle ``.py``-Dateien ein.
Durchläuft alle Python-Dateien im angegebenen Verzeichnis und ersetzt
bestehende Lizenzhinweise durch den neuen Lizenzhinweis. Behandelt leere
Dateien und Dateien, die nur Kommentare enthalten, entsprechend.

**Parameter:**

- **`directory`** (`str`) - Pfad zum Verzeichnis mit zu aktualisierenden Dateien.

---

## Modul: `open_ticket_ai\src\ce\app.py`

### <span style='color: #8E44AD;'>class</span> `App`

Haupteinstiegspunkt der Anwendung.

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `__init__(self, config: OpenTicketAIConfig, validator: OpenTicketAIConfigValidator, orchestrator: Orchestrator)`</summary>

Initialisiert die Anwendung.

**Parameter:**

- **`config`** () - Geladene Konfiguration für die Anwendung.
- **`validator`** () - Validator zur Überprüfung der Konfiguration.
- **`orchestrator`** () - Orchestrator zur Ausführung von Attribut-Vorhersagen.

</details>

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `run(self)`</summary>

Validiert Konfiguration und startet die Scheduler-Schleife.
Diese Methode:
1. Validiert die Anwendungskonfiguration
2. Richtet geplante Jobs mit dem Orchestrator ein
3. Tritt in eine Endlosschleife ein, um anstehende geplante Aufgaben auszuführen

</details>

---

## Modul: `open_ticket_ai\src\ce\core\config\config_models.py`

### <span style='color: #8E44AD;'>class</span> `SystemConfig`

Konfiguration für den Ticket-System-Adapter.

### <span style='color: #8E44AD;'>class</span> `FetcherConfig`

Konfiguration für Data Fetcher.

### <span style='color: #8E44AD;'>class</span> `PreparerConfig`

Konfiguration für Data Preparers.

### <span style='color: #8E44AD;'>class</span> `ModifierConfig`

Konfiguration für Modifier.

### <span style='color: #8E44AD;'>class</span> `AIInferenceServiceConfig`

Konfiguration für KI-Inferenzdienste.

### <span style='color: #8E44AD;'>class</span> `SchedulerConfig`

Konfiguration für die Planung wiederkehrender Aufgaben.

### <span style='color: #8E44AD;'>class</span> `PipelineConfig`

Konfiguration für einen einzelnen Pipeline-Workflow.

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `validate_pipe_ids_are_registered(self, all_pipe_ids: set[str]) -> None`</summary>

Validiert, dass alle Pipe-IDs in dieser Pipeline existieren.

</details>

### <span style='color: #8E44AD;'>class</span> `OpenTicketAIConfig`

Hauptkonfigurationsmodell für Open Ticket AI.

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495极客时间; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `cross_validate_references(self) -> Self`</summary>

Validiert, dass alle Pipeline-Referenzen auf Komponenten existieren.

</details>

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `get_all_register_instance_configs(self) -> list[RegistryInstanceConfig]`</summary>

Gibt alle registrierten Instanzen in der Konfiguration zurück.

</details>

### <span style='color: #2980B9;'>def</span> `load_config(path: str) -> OpenTicketAIConfig`

Lädt eine YAML-Konfigurationsdatei von ``path``.

---

## Modul: `open_ticket_ai\src\ce\core\config\config_validator.py`

### <span style='color: #8E44AD;'>class</span> `OpenTicketAIConfigValidator`

Validiert Konfigurationswerte gegen die Registry.

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `__init__(self, config: OpenTicketAIConfig, registry: Registry)`</summary>

Erstellt einen neuen Validator.

**Parameter:**

- **`config`** () - Geladene ``OpenTicketAIConfig``-Instanz.
- **`registry`** () - Registry mit verfügbaren Klassen.

</details>

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `validate_registry(self) -> None`</summary>

Stellt sicher, dass alle konfigurierten Provider registriert sind.

</details>

---

## Modul: `open_ticket_ai\src\ce\core\dependency_injection\abstract_container.py`

### <span style='color: #8E44AD;'>class</span> `AbstractContainer`

Abstrakte Schnittstelle für Dependency-Container.

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `get_instance(self, provider_key: str, subclass_of: type[T]) -> T`</summary>

Ruft eine Instanz aus dem Container ab.
Die Instanz wird basierend auf dem Provider-Schlüssel abgerufen und muss eine Unterklasse des angegebenen Typs sein.

**Parameter:**

- **`provider_key`** () - Der Schlüssel, der den Provider für die Instanz identifiziert.
- **`subclass_of`** () - Die Klasse (oder der Typ) der abzurufenden Instanz. Der Typ T muss eine Unterklasse von
`RegistryProvidableInstance` sein.

**Rückgabe:** () - Eine Instanz des durch `subclass_of` angegebenen Typs (oder einer Unterklasse).

</details>

---

## Modul: `open_ticket_ai\src\ce\core\dependency_injection\container.py`

### ⚠️ Fehler beim Parsen von `open_ticket_ai\src\ce\core\dependency_injection\container.py`

```
'DocstringRaises' Objekt hat kein Attribut 'default'
```

---

## Modul: `open_ticket_ai\src\ce\core\dependency_injection\create_registry.py`

### <span style='color: #2980B9;'>def</span> `create_registry() -> Registry`

Erstellt die Standard-Klassenregistry.

---

## Modul: `open_ticket_ai\src\ce\core\dependency_injection\registry.py`

### <span style='color: #8E44AD;'>class</span> `Registry`

Einfache Klassenregistry für Dependency-Lookup.

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `__init__(self)`</summary>

Erstellt eine leere Registry.

</details>

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `register_all(self, instance_classes: list[Type[RegistryProvidableInstance]]) -> None`</summary>

Registriert mehrere Klassen auf einmal.

</details>

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `register(self, instance_class: type[T]) -> None`</summary>

Registriert eine einzelne Klasse mit optionalem Schlüssel.

</details>

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `get(self, registry_instance_key: str, instance_class: type[T]) -> type[T]`</summary>

Ruft eine registrierte Klasse ab und validiert ihren Typ.

</details>

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='极客时间'>def</span> `contains(self, registry_instance_key: str) -> bool`</summary>

Überprüft, ob ein Schlüssel unter einem kompatiblen Typ registriert ist.

</details>

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `get_registry_types_descriptions(self) -> str`</summary>

Gibt eine Liste aller registrierten Typen und Beschreibungen zurück.

</details>

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2极客时间; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `get_all_registry_keys(self) -> list[str]`</summary>

Gibt eine Liste aller registrierten Schlüssel zurück.

</details>

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `get_type_from_key(self, registry_instance_key: str) -> type[RegistryProvidableInstance]`</summary>

Ruft den Typ einer registrierten Instanz anhand ihres Schlüssels ab.

</details>

---

## Modul: `open_ticket_ai\src\ce\core\mixins\registry_instance_config.py`

### <span style='color: #8E44AD;'>class</span> `RegistryInstanceConfig`

Basis-Konfiguration für Registry-Instanzen.

---

## Modul: `open_ticket_ai\src\ce\core\mixins\registry_providable_instance.py`

### <span style='color: #8E44AD;'>class</span> `RegistryProvidableInstance`

Basisklasse für Objekte, die von einer Registry bereitgestellt werden können.
Stellt gemeinsame Funktionalität für registry-verwaltete Objekte bereit, einschließlich
Konfigurationsspeicherung, formatierter Konfigurationsausgabe und Provider-Registrierung.

**Parameter:**

- **`console`** (`Console`) - Rich-Konsoleninstanz für die Ausgabeformatierung.
- **`config`** (`RegistryInstanceConfig`) - Konfigurationsobjekt für diese Instanz.

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `__init__(self, config: RegistryInstanceConfig, console: Console | None)`</summary>

Speichert die Konfiguration und gibt sie formatiert aus.

</details>

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `get_provider_key(cls) -> str`</summary>

Gibt den Provider-Schlüssel für die Klasse zurück.
Dieser Schlüssel wird verwendet, um Instanzen aus der Registry zu registrieren und abzurufen.

</details>

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `get_description() -> str`</summary>

Gibt eine menschenlesbare Beschreibung für die Klasse zurück.

</details>

---

## Modul: `open_ticket_ai\src\ce\core\util\create_json_config_schema.py`

### <span style='color: #8E44AD;'>class</span> `RootConfig`

Wrapper-Modell für die Schema-Generierung.

---

## Modul: `open_ticket_ai\src\ce\core\util\path_util.py`

### ⚠️ Fehler beim Parsen von `open_ticket_ai\src\ce\core\util\path_util.py`

```
'DocstringRaises' Objekt hat kein Attribut 'default'
```

---

## Modul: `open_ticket_ai\src\ce\core\util\pretty_print_config.py`

### <span style='color: #2980B9;'>def</span> `pretty_print_config(config: BaseModel, console: Console)`

Gibt ein Pydantic-Modell formatiert mit ``rich`` aus.
Konvertiert ein Pydantic BaseModel in ein Wörterbuch, serialisiert es zu YAML,
und gibt es mit der Syntaxhervorhebung von rich auf der Konsole aus.

**Parameter:**

- **`config`** (`BaseModel`) - Das anzuzeigende Pydantic-Modellkonfiguration.
- **`console`** (`Console`) - Die rich-Konsoleninstanz für die Ausgaberenderung.

---

## Modul: `open_ticket_ai\src\ce\main.py`

Open Ticket AI CLI-Einstiegspunkt.
Konfiguriert Logging-Levels und startet die Hauptanwendung.

### <span style='color: #2980B9;'>def</span> `main(verbose: bool, debug: bool)`

Konfiguriert Logging basierend auf CLI-Optionen.

**Parameter:**

- **`verbose`** (`bool`) - Aktiviert INFO-Level-Logging, wenn True.
- **`debug`** (`bool`) - Aktiviert DEBUG-Level-Logging, wenn True.

### <span style='color: #2980B9;'>def</span> `start()`

Initialisiert den Container und startet die Anwendung.

---

## Modul: `open_ticket_ai\src\ce\run\ai_models\hf_local_ai_inference_service.py`

### <span style='color: #8E44AD;'>class</span> `HFAIInferenceService`

Eine Klasse, die ein Hugging Face KI-Modell repräsentiert.
Platzhalter für zukünftige Implementierung von Hugging Face KI-Modellfunktionalitäten.
Enthält derzeit keine Methoden oder Eigenschaften.

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `__init__(self, config: RegistryInstanceConfig)`</summary>

Initialisiert den HFAIInferenceService mit Konfiguration.

**Parameter:**

- **`config`** (`RegistryInstanceConfig`) - Konfigurationsinstanz für den Dienst.

</details>

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `process(self, context: PipelineContext) -> PipelineContext`</summary>

Verarbeitet den Pipeline-Kontext, indem vorbereitete Daten als Modellergebnis gespeichert werden.

**Parameter:**

- **`context`** (`PipelineContext`) - Der Pipeline-Kontext mit zu verarbeitenden Daten.

**Rückgabe:** (`PipelineContext`) - Der aktualisierte Pipeline-Kontext mit gespeichertem Modellergebnis.

</details>

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `get_description() -> str`</summary>

Liefert eine Beschreibung des Dienstes.

**Rückgabe:** (`str`) - Beschreibungstext für den Hugging Face KI-Modelldienst.

</details>

---

## Modul: `open_ticket_ai\src\ce\run\fetchers\basic_ticket_fetcher.py`

### <span style='color: #8E44AD;'>class</span> `BasicTicketFetcher`

Einfacher Fetcher, der Ticketdaten mit dem Ticket-System-Adapter lädt.

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `__init__(self, config: RegistryInstanceConfig, ticket_system: TicketSystemAdapter)`</summary>

Initialisiert den BasicTicketFetcher mit Konfiguration und Ticket-System-Adapter.

**Parameter:**

- **`config`** () - Die Konfigurationsinstanz für den Fetcher.
- **`ticket_system`** () - Der Adapter für die Interaktion mit dem Ticket-System.

</details>

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `process(self, context: PipelineContext) -> PipelineContext`</summary>

Ruft Ticketdaten ab und aktualisiert den Pipeline-Kontext.
Ruft das Ticket mit der Ticket-ID aus dem Kontext ab und aktualisiert
das Datenwörterbuch des Kontexts mit den Ticketinformationen.

**Parameter:**

- **`context`** () - Der Pipeline-Kontext mit der Ticket-ID.

**Rückgabe:** (`PipelineContext`) - Der aktualisierte Pipeline-Kontext mit Ticketdaten.

</details>

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `get_description() -> str`</summary>

Liefert eine Beschreibung der Funktionalität dieser Pipe.

**Rückgabe:** (`str`) - Eine Beschreibung der Pipe.

</details>

---

## Modul: `open_ticket_ai\src\ce\run\modifiers\generic_ticket_updater.py`

### <span style='color: #8E44AD;'>class</span> `GenericTicketUpdater`

Aktualisiert ein Ticket im Ticket-System mit Daten aus dem Kontext.

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `__init__(self, config: RegistryInstanceConfig, ticket_system: TicketSystemAdapter)`</summary>

Initialisiert den GenericTicketUpdater mit Konfiguration und Ticket-System-Adapter.

**Parameter:**

- **`config`** () - Konfigurationsinstanz für die Pipeline-Komponente.
- **`ticket_system`** () - Adapter für die Interaktion mit dem Ticket-System.

</details>

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `process(self, context: PipelineContext) -> PipelineContext`</summary>

Verarbeitet den Pipeline-Kontext, um das Ticket zu aktualisieren, wenn Updatedaten existieren.
Ruft Updatedaten aus dem Kontext ab und aktualisiert das Ticket im Ticket-System,
wenn Updatedaten vorhanden sind. Gibt den Kontext unverändert zurück.

**Parameter:**

- **`context`** () - Der Pipeline-Kontext mit Daten und Ticketinformationen.

**Rückgabe:** () - Der ursprüngliche Pipeline-Kontext nach der Verarbeitung.

</details>

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `get_description() -> str`</summary>

</details>

---

## Modul: `open_ticket_ai\src\ce\run\orchestrator.py`

Top-Level-Orchestrierungs-Hilfsmittel.

### <span style='color: #8E44AD;'>class</span> `Orchestrator`

Führt Ticket-Verarbeitungspipelines aus.

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `__init__(self, config: OpenTicketAIConfig, container: AbstractContainer)`</summary>

Initialisiert den Orchestrator mit Konfiguration und DI-Container.

**Parameter:**

- **`config`** () - Konfigurationseinstellungen für den Orchestrator.
- **`container`** () - Dependency-Injection-Container, der Pipeline-Instanzen bereitstellt.

</details>

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `process_ticket(self, ticket_id: str, pipeline: Pipeline) -> PipelineContext`</summary>

Ruft Daten ab und führt ``pipeline`` für ``ticket_id`` aus.

</details>

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `build_pipelines(self) -> None`</summary>

Instanziiert Pipeline-Objekte mit dem DI-Container.

</details>

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `set_schedules(self) -> None`</summary>

Plant die Pipeline-Ausführung gemäß Konfiguration.

</details>

---

## Modul: `open_ticket_ai\src\ce\run\pipeline\context.py`

### <span style='color: #8E44AD;'>class</span> `PipelineContext`

Kontextobjekt, das zwischen Pipeline-Stufen übergeben wird.

**Parameter:**

- **`ticket_id`** (`str`) - Die ID des zu verarbeitenden Tickets.
- **`data`** (`dict[str, Any]`) (default: `ein leeres Wörterbuch`) - Ein Wörterbuch zum Halten beliebiger Daten für die Pipeline-Stufen. Standardmäßig ein leeres Wörterbuch.

---

## Modul: `open_ticket_ai\src\ce\run\pipeline\pipe.py`

### <span style='color: #8E44AD;'>class</span> `Pipe`

Schnittstelle für alle Pipeline-Komponenten.

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `process(self, context: PipelineContext) -> PipelineContext`</summary>

Verarbeitet ``context`` und gibt ihn zurück.

</details>

---

## Modul: `open_ticket_ai\src\ce\run\pipeline\pipeline.py`

### <span style='color: #8E44AD;'>class</span> `Pipeline`

Zusammengesetzte Pipe, die eine Sequenz von Pipes ausführt.

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `__init__(self, config: PipelineConfig, pipes: List[Pipe])`</summary>

Initialisiert die Pipeline mit Konfiguration und Komponenten-Pipes.

**Parameter:**

- **`config`** () - Konfigurationseinstellungen für die Pipeline.
- **`p极客时间`** () - Geordnete Liste von Pipe-Instanzen zur sequentiellen Ausführung.

</details>

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `execute(self, context: PipelineContext) -> PipelineContext`</summary>

Führt alle Pipes in der Pipeline sequentiell aus.
Verarbeitet den Kontext durch jede Pipe in der definierten Reihenfolge und übergibt
die Ausgabe einer Pipe als Eingabe an die nächste.

**Parameter:**

- **`context`** () - Der initiale Pipeline-Kontext mit zu verarbeitenden Daten.

**Rückgabe:** () - Der endgültige Kontext nach der Verarbeitung durch alle Pipes.

</details>

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `process(self, context: PipelineContext) -> PipelineContext`</summary>

Verarbeitet den Kontext durch die gesamte Pipeline.
Diese Methode implementiert die Pipe-Schnittstelle durch Delegation an execute().

**Parameter:**

- **`context`** () - Der zu verarbeitende Pipeline-Kontext.

**Rückgabe:** () - Der modifizierte Kontext nach der Pipeline-Ausführung.

</details>

---

## Modul: `open_ticket_ai\src\ce\run\preparers\subject_body_preparer.py`

### <span style='color: #8E44AD;'>class</span> `SubjectBodyPreparer`

Extrahiert und verkettet den Ticket-Betreff und -Text.

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `__init__(self, config: RegistryInstanceConfig)`</summary>

Initialisiert den SubjectBodyPreparer mit Konfiguration.

**Parameter:**

- **`config`** (`RegistryInstanceConfig`) - Konfigurationsparameter für den Preparer.

</details>

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `process(self, context: PipelineContext) -> PipelineContext`</summary>

Verarbeitet Ticketdaten, um Betreff- und Textinhalte vorzubereiten.
Extrahiert die Felder 'subject' und 'body' aus den Kontextdaten, wiederholt den Betreff
gemäß Konfiguration und verkettet ihn mit dem Text. Speichert
das Ergebnis im Kontext unter dem Schlüssel 'prepared_data'.

**Parameter:**

- **`context`** (`PipelineContext`) - Pipeline-Kontext mit Ticketdaten.

**Rückgabe:** (`PipelineContext`) - Aktualisierter Kontext mit vorbereiteten Daten.

</details>

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def极客时间`get_description() -> str`</summary>

Liefert eine Beschreibung der Funktionalität der Pipe.

**Rückgabe:** (`str`) - Beschreibung des Zwecks der Pipe.

</details>

---

## Modul: `open_ticket_ai\src\ce\ticket_system_integration\otobo_adapter.py`

### <span style='color: #8E44AD;'>class</span> `OTOBOAdapter`

Adapter für die OTOBO-Ticket-System-Integration.
Stellt Methoden zur Interaktion mit der OTOBO-API bereit.

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6极客时间; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `get_description() -> str`</summary>

Gibt eine Beschreibung der Funktionalität des Adapters zurück.

**Rückgabe:** (`str`) - Eine Beschreibung des OTOBO-Adapters.

</details>

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `__init__(self, config: SystemConfig, otobo_client: OTOBOClient)`</summary>

Initialisiert den OTOBO-Adapter mit Konfiguration und Client.

**Parameter:**

- **`config`** (`SystemConfig`) - Systemkonfigurationsobjekt.
- **`otobo_client`** (`OTOBOClient`) - Client zur Interaktion mit der OTOBO-API.

</details>

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>async def</span> `find_tickets(self, query: dict) -> list[dict]`</summary>

Gibt alle Tickets zurück, die ``query`` entsprechen.

**Parameter:**

- **`query`** (`dict`) - Suchparameter für Tickets.

**Rückgabe:** (`list[dict]`) - Liste der zur Abfrage passenden Tickets.

</details>

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>async def</span> `find_first_ticket(self, query: dict) -> dict | None`</summary>

Gibt das erste für ``query`` gefundene Ticket zurück, falls verfügbar.

**Parameter:**

- **`query`** (`dict`) - Suchparameter für Tickets.

**Rückgabe:** () - dict | None: Erstes passendes Ticket-Wörterbuch oder None, wenn keins gefunden wurde.

</details>

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>async def</span> `update_ticket(self, ticket_id: str, data: dict) -> dict`</summary>

Aktualisiert ``ticket_id`` mit ``data`` und gibt den aktualisierten Datensatz zurück.

**Parameter:**

- **`ticket_id`** (`str`) - ID des zu aktualisierenden Tickets.
- **`data`** (`dict`) - Aktualisierungsparameter für das Ticket.

**Rückgabe:** (`dict`) - Aktualisierter Ticket-Datensatz.

</details>

---

## Modul: `open_ticket_ai\src\ce\ticket_system_integration\otobo_adapter_config.py`

### <span style='color: #8E44AD;'>class</span> `OTOBOAdapterConfig`

Konfigurationsmodell für den OTOBO-Adapter.

**Parameter:**

- **`server_address`** (`str`) - Die Basis-URL des OTOBO-Servers.
- **`webservice_name`** (`str`) - Der Name des zu verwendenden Webdienstes.
- **`search_operation_url`** (`str`) - Die URL für die Suchoperation.
- **`update_operation_url`** (`str`) - Die URL für die Aktualisierungsoperation.
- **`get_operation_url`** (`str`) - Die URL für die Get-Operation.
- **`username`** (`str`) - Der Benutzername zur Authentifizierung.
- **`password_env_var`** (`str`) - Die Umgebungsvariable, die das Passwort enthält.

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `__str__(self)`</summary>

Gibt eine String-Repräsentation der Konfiguration zurück.

</details>

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `password(self) -> str`</summary>

Ruft das Passwort aus der in der Konfiguration angegebenen Umgebungsvariablen ab.

**Rückgabe:** (`str`) - Das Passwort zur Authentifizierung.

</details>

---

## Modul: `open_ticket_ai\src\ce\ticket_system_integration\otobo_adapter_test.py`

### <span style='color: #2980B9;'>def</span> `adapter_and_client()`

Fixture, die eine Instanz von OTOBOAdapter und einen gemockten OTOBOClient bereitstellt.

**Rückgabe:** (`tuple`) - Ein Tupel bestehend aus:
adapter (OTOBOAdapter): Konfigurierte OTOBOAdapter-Instanz
client (AsyncMock): Gemockte OTOBOClient-Instanz

### <span style='color: #2980B9;'>def</span> `test_config_str_and_password(monkeypatch)`

Testet die String-Repräsentation von OTOBOAdapterConfig und die Passwortabfrage aus der Umgebung.
Überprüft:
    1. Die __str__-Methode schließt den Passwortwert aus
    2. Das Passwort wird korrekt aus der Umgebungsvariablen abgerufen

### <span style='color: #2980B9;'>def</span> `test_config_password_missing_env(monkeypatch)`

Testet, dass OTOBOAdapterConfig einen Fehler auslöst, wenn die Passwort-Umgebungsvariable fehlt.
Überprüft:
    Der Zugriff auf die password-Eigenschaft löst einen ValueError aus, wenn die Umgebungsvariable nicht existiert

### <span style='color: #2980B9;'>def</span> `test_find_tickets(adapter_and_client)`

Testet, dass find_tickets Suchanfragen korrekt verarbeitet und Ergebnisse zurückgibt.
Überprüft:
    1. Suchparameter werden korrekt an den OTOBO-Client übergeben
    2. Ergebnisse werden ordnungsgemäß in Wörterbücher konvertiert

### <span style='color: #2980B9;'>def</span> `test_find_first_ticket(adapter_and_client)`

Testet, dass find_first_ticket den ersten Treffer oder None zurückgibt, wenn keine Tickets gefunden werden.
Überprüft:
    1. Gibt das erste Ticket zurück, wenn Treffer existieren
    2. Gibt None zurück, wenn keine Tickets der Abfrage entsprechen

### <span style='color: #2980B9;'>def</span> `test_update_ticket(adapter_and_client)`

Testet, dass update_ticket das Payload korrekt formatiert und die Antwort verarbeitet.
Überprüft:
    1. Aktualisierungsparameter werden korrekt in OTOBO-Format konvertiert
    2. Antwortdaten werden ordnungsgemäß zurückgegeben

---

## Modul: `open_ticket_ai\src\ce\ticket_system_integration\ticket_system_adapter.py`

### <span style='color: #8E44AD;'>class</span> `TicketSystemAdapter`

Eine abstrakte Basisklasse für Ticket-System-Adapter.
Definiert die Schnittstelle, die alle Ticket-System-Adapter implementieren müssen.

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `__init__(self, config: SystemConfig)`</summary>

Initialisiert den Adapter mit Systemkonfiguration.

</details>

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>async def</span> `update_ticket(self, ticket_id: str, data: dict) -> dict | None`</summary>

Aktualisiert ein Ticket im System.

**Parameter:**

- **`ticket_id`** () - Ticket-Identifikator.
- **`data`** () - Zu aktualisierende Attribute.

**Rückgabe:** (`Optional[dict]`) - Aktualisierte Ticketinformationen.

</details>

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>async def</span> `find_tickets(self, query: dict) -> list[dict]`</summary>

Sucht nach Tickets, die ``query`` entsprechen.

**Parameter:**

- **`query`** () - Suchparameter für das Ticket-System.

**Rückgabe:** (`list[dict]`) - Passende Tickets.

</details>

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>async def</span> `find_first_ticket(self, query: dict) -> dict | None`</summary>

Gibt das erste Ticket zurück, das ``query`` entspricht, falls vorhanden.

**Parameter:**

- **`query`** () - Suchparameter für das Ticket-System.

**Rückgabe:** (`Optional[dict]`) - Das erste passende Ticket oder None, wenn kein Ticket gefunden wurde.

</details>

---

## Modul: `open_ticket_ai\tests\experimental\test_anonymize_data.py`

### <span style='color: #2980B9;'>def</span> `test_remove_personal_info(text)`

Testet, dass die anonymize_text-Funktion alle angegebenen persönlichen Informationen entfernt.
Dieser Test ist mit verschiedenen Textexempeln parametrisiert, die persönliche Daten wie Namen,
Adressen, E-Mail-Adressen, Telefonnummern, IBANs und Kreditkartendetails enthalten. Überprüft, dass
nach der Verarbeitung durch anonymize_text keine der verbotenen persönlichen Informationsstrings verbleiben.

**Parameter:**

- **`text`** (`str`) - Eingabetext mit zu anonymisierenden persönlichen Informationen.

---

## Modul: `open_ticket_ai\tests\scripts\test_doc_generation\test_plantuml_compile.py`

### <span style='color: #2980B9;'>def</span> `test_compile_plantuml_diagrams_missing_dir(tmp_path: Path)`

Testet das Verhalten von compile_plantuml_diagrams bei einem nicht existierenden Verzeichnis.
Überprüft, dass die Funktion fehlende Verzeichnisse elegant behandelt durch:
1. Keine Ausnahmen auslöst, wenn mit einem nicht existierenden Pfad aufgerufen
2. Sicherstellt, dass das Verzeichnis nach dem Funktionsaufruf nicht existent bleibt

**Parameter:**

- **`tmp_path`** () - Ein Pytest-Fixture, das ein temporäres Verzeichnis-Pfadobjekt bereitstellt.

---

## Modul: `open_ticket_ai\tests\scripts\test_license_script.py`

### <span style='color: #2980B9;'>def</span> `setup_test_directory(tmp_path)`

Richtet ein temporäres Verzeichnis mit verschiedenen Dateien für Tests ein.

### <span style='color: #2980B9;'>def</span> `test_find_start_of_code(lines, expected_index)`

Testet die find_start_of_code-Funktion mit verschiedenen Zeileneingaben.

**Parameter:**

- **`lines`** () - Liste von Strings, die Zeilen einer Datei repräsentieren.
- **`expected_index`** () - Der erwartete Index, an dem der Code beginnt.

### <span style='color: #2980B9;'>def</span> `test_update_license_in_files(setup_test_directory)`

Testet die update_license_in_files-Funktion durch Aktualisieren von Dateien in einem Testverzeichnis.
Überprüft, dass:
  - Python-Dateien den neuen Lizenzhinweis oben erhalten und ihren ursprünglichen Inhalt behalten
  - Bereits lizenzierte Dateien ohne Lizenzduplizierung aktualisiert werden
  - Nicht-Python-Dateien nicht modifiziert werden

**Parameter:**

- **`setup_test_directory`** () - Pytest-Fixture, die ein temporäres Testverzeichnis einrichtet.

---

## Modul: `open_ticket_ai\tests\src\core\config_test.py`

### <span style='color: #2980B9;'>def</span> `minimal_config_dict()`

Baut das kleinste gültige Wörterbuch für ``OpenTicketAIConfig``.
Die Konfiguration folgt jetzt der neuen Pipes-and-Filters-Struktur mit
``pipelines`` anstelle von ``attribute_predictors``.

### <span style='color: #8E44AD;'>class</span> `TestSchedulerConfig`

Testfälle zur Validierung des SchedulerConfig-Modells.

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `test_valid_scheduler_config(self)`</summary>

Testet, dass eine gültige Scheduler-Konfiguration korrekt geparst wird.

</details>

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `test_scheduler_config_invalid_interval_raises_validation_error(self, interval)`</summary>

Testet, dass ungültige Intervallwerte einen ValidationError auslösen.

</details>

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `test_scheduler_config_invalid_unit_raises_validation_error(self)`</summary>

Testet, dass eine ungültige Zeiteinheit einen ValidationError auslöst.

</details>

### <span style='color: #8E44AD;'>class</span> `TestOpenTicketAIConfig`

Testfälle zur Validierung des OpenTicketAIConfig-Modells.

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `test_empty_list_for_core_components_raises_validation_error(self, list_name, minimal_config_dict)`</summary>

Testet, dass leere Listen für erforderliche Komponenten einen ValidationError auslösen.

</details>

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `test_valid_open_ticket_ai_config_parses_correctly(self, minimal_config_dict)`</summary>

Testet, dass eine gültige Konfiguration korrekt mit allen Komponenten geparst wird.

</details>

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `test_invalid_cross_reference_raises_value_error(self, list_name_to_alter, pipe_index, expected_error_message_part, minimal_config_dict)`</summary>

Testet, dass ungültige Komponentenreferenzen in Pipelines einen ValueError auslösen.

</details>

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `test_duplicate_ids_in_component_list_allowed_by_basemodel_but_picked_by_set_logic(self, minimal_config_dict)`</summary>

Testet das Verhalten bei doppelten Komponenten-IDs und Cross-Reference-Auflösung.

</details>

### <span style='color: #8E44AD;'>class</span> `TestLoadConfig`

Testfälle für die load_config-Funktion.

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `test_load_config_missing_root_key_raises_key_error(self, tmp_path)`</summary>

Testet, dass ein fehlender Root-Schlüssel 'open_ticket_ai' einen KeyError auslöst.

</details>

---

## Modul: `open_ticket_ai\tests\src\core\test_di_container.py`

---

## Modul: `open_ticket_ai\tests\src\core\util_test.py`

### <span style='color: #8E44AD;'>class</span> `DummyModel`

Ein Dummy-Pydantic-Modell für Testzwecke.

**Parameter:**

- **`foo`** (`int`) - Ein Integer-Attribut für Tests.
- **`bar`** (`str`) - Ein String-Attribut für Tests.

### <span style='color: #2980B9;'>def</span> `test_find_project_root_returns_project_directory()`

Testet, dass find_project_root das Projektstammverzeichnis korrekt identifiziert.
Überprüft:
    - Das gefundene Verzeichnis hat den erwarteten Namen
    - Die aktuelle Testdatei befindet sich innerhalb des gefundenen Verzeichnisses
    - Die erwartete Konfigurationsdatei existiert im Stammverzeichnis

### <span style='color: #2980B9;'>def</span> `test_find_project_root_invalid_name_raises()`

Testet, dass find_project_root einen FileNotFoundError mit ungültigem Projektnamen auslöst.

### <span style='color: #2980B9;'>def</span> `test_pretty_print_config_outputs_yaml()`

Testet, dass pretty_print_config die Konfiguration wie erwartet als YAML ausgibt.
Überprüft:
    - Die Ausgabe enthält genau ein Element
    - Das Ausgabeelement ist ein Syntax-Objekt
    - Das ausgegebene YAML entspricht der erwarteten serialisierten Konfiguration

### <span style='color: #2980B9;'>def</span> `test_root_config_schema_contains_open_ticket_ai()`

Testet, dass das generierte JSON-Schema die erwartete 'open_ticket_ai'-Eigenschaft enthält.

### <span style='color: #2980B9;'>def</span> `test_schema_file_written(tmp_path, monkeypatch)`

Testet, dass die JSON-Schemadatei korrekt generiert und geschrieben wird.

**Parameter:**

- **`tmp_path`** () - Pytest-Fixture für temporäres Verzeichnis
- **`monkeypatch`** () - Pytest-Fixture zur Modifikation der Umgebung

---

## Modul: `open_ticket_ai\tests\src\run\fetchers\test_fetchers.py`

### <span style='color: #8E44AD;'>class</span> `DummyFetcher`

Ein Dummy-Fetcher für Testzwecke.
Ruft keine echten Daten ab, sondern setzt nur ein Dummy-Flag im Kontext.

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `__init__(self, cfg, ticket_system)`</summary>

Initialisiert den DummyFetcher.

**Parameter:**

- **`cfg`** () - Die Konfiguration für den Fetcher.
- **`ticket_system`** () - Ein Mock-Ticket-System-Objekt für Tests.

</details>

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `process(self, context: PipelineContext) -> PipelineContext`</summary>

Verarbeitet den Pipeline-Kontext durch Setzen eines Dummy-Flags.

**Parameter:**

- **`context`** () - Der Pipeline-Kontext.

**Rückgabe:** (`PipelineContext`) - Der aktualisierte Pipeline-Kontext mit auf True gesetztem Dummy-Flag.

</details>

### <span style='color: #2980B9;'>def</span> `test_dummy_fetcher_process_populates_context()`

Testet, dass der DummyFetcher process-Methode den Kontext mit einem Dummy-Flag füllt.

### <span style='color: #2980B9;'>def</span> `test_basic_ticket_fetcher_fetches_ticket()`

Testet, dass der BasicTicketFetcher ein Ticket abruft und den Kontext füllt.

### <span style='color: #2980B9;'>def</span> `test_basic_ticket_fetcher_description()`

Testet die Beschreibung des BasicTicketFetchers.

---

## Modul: `open_ticket_ai\tests\src\run\pipeline\test_pipeline.py`

---

## Modul: `open_ticket_ai\tests\src\run\test_ai_models.py`

### <span style='color: #8E44AD;'>class</span> `DummyService`

Ein Dummy-Dienst für Tests, der einen KI-Inferenzdienst simuliert.
Erweitert die abstrakte Basisklasse Pipe und implementiert eine einfache
process-Methode, die ein Dummy-Ergebnis basierend auf dem Eingabekontext generiert.

**Parameter:**

- **`ai_inference_config`** () - Konfiguration für den Dummy-Dienst.

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `__init__(self, cfg)`</summary>

Initialisiert den DummyService mit gegebener Konfiguration.

**Parameter:**

- **`cfg`** () - Konfigurationsobjekt für den Dienst.

</details>

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `process(self, context: PipelineContext) -> PipelineContext`</summary>

Verarbeitet den Eingabekontext durch Generierung eines Dummy-Modellergebnisses.

**Parameter:**

- **`context`** () - Der Pipeline-Kontext mit Eingabedaten.

**Rückgabe:** (`PipelineContext`) - Aktualisierter Kontext mit hinzugefügtem Dummy-Modellergebnis.

</details>

### <span style='color: #2980B9;'>def</span> `example_config()`

Fixture, das eine Dummy-KI-Inferenzdienstkonfiguration bereitstellt.

**Rückgabe:** (`AIInferenceServiceConfig`) - Konfigurationsinstanz für Tests.

### <span style='color: #2980B9;'>def</span> `test_service_process_sets_result(example_config)`

Testet, dass DummyService model_result korrekt im Kontext setzt.

### <span style='color: #2980B9;'>def</span> `test_hf_service_description()`

Testet, dass die Hugging Face-Dienstbeschreibung erwarteten Text enthält.

### <span style='color: #2980B9;'>def</span> `test_hf_service_process_returns_context(example_config)`

Testet, dass der Hugging Face-Dienst den Kontext mit Modellergebnis zurückgibt.

---

## Modul: `open_ticket_ai\tests\src\run\test_modifiers.py`

### <span style='color: #8E44AD;'>class</span> `DummyModifier`

Eine Dummy-Modifier-Klasse für Testzwecke.
Setzt ein Flag im Pipeline-Kontext, um Modifikation anzuzeigen.

**Parameter:**

- **`modifier_config`** () - Konfiguration für den Modifier.
- **`ticket_system`** () - Die Ticket-System-Schnittstelle.

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `__init__(self, cfg, ticket_system)`</summary>

Initialisiert die DummyModifier-Instanz.

**Parameter:**

- **`cfg`** () - Konfigurationsobjekt für den Modifier.
- **`ticket_system`** () - Die zu verwendende Ticket-System-Schnittstelle.

</details>

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `process(self, context: PipelineContext) -> PipelineContext`</summary>

Verarbeitet den Pipeline-Kontext durch Setzen eines Modifikationsflags.

**Parameter:**

- **`context`** () - Der Pipeline-Kontext mit Ticketdaten.

**Rückgabe:** () - Der modifizierte Pipeline-Kontext.

</details>

### <span style='color: #2980B9;'>def</span> `test_modifier_initialization_calls_pretty_print()`

Testet, dass die Modifier-Initialisierung die Pretty-Print-Funktion aufruft.
Überprüft, dass während der Initialisierung eines Modifiers die Konfigurations-
Pretty-Print-Funktion genau einmal mit der korrekten Konfiguration aufgerufen wird.

### <span style='color: #2980B9;'>def</span> `test_generic_ticket_updater_calls_update()`

Testet, dass GenericTicketUpdater die update-Methode des Adapters korrekt aufruft.
Überprüft, dass bei der Verarbeitung eines Kontexts mit Updatedaten die
update_ticket-Methode des Adapters mit der korrekten Ticket-ID und Daten aufgerufen wird.

---

## Modul: `open_ticket_ai\tests\src\run\test_pipeline.py`

### <span style='color: #8E44AD;'>class</span> `DummyPreparer`

Eine Dummy-Implementierung eines Data Preparers für Testzwecke.
Wendet eine einfache Transformation auf Eingabedaten an.

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `prepare(self, data)`</summary>

Transformiert Eingabedaten, indem ein spezifischer Wert in einen String eingebettet wird.

**Parameter:**

- **`data`** (`dict`) - Eingabedatenwörterbuch, das einen Schlüssel 'v' erwartet.

**Rückgabe:** (`str`) - Ein formatierter String, der den Wert aus data['v'] enthält.

</details>

### <span style='color: #8E44AD;'>class</span> `DummyAI`

Eine Dummy-Implementierung eines KI-Modells für Testzwecke.
Simuliert das Generieren von Antworten aus Prompts durch Rückgabe einer formatierten Version des Eingabe-Prompts.

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `generate_response(self, prompt)`</summary>

Generiert eine simulierte KI-Antwort basierend auf dem Eingabe-Prompt.

**Parameter:**

- **`prompt`** (`str`) - Der Eingabe-Prompt für das KI-Modell.

**Rückgabe:** (`str`) - Ein formatierter String, der den Eingabe-Prompt enthält.

</details>

### <span style='color: #8E44AD;'>class</span> `DummyModifier`

Eine Dummy-Implementierung eines Ergebnis-Modifiers für Testzwecke.
Simuliert das Modifizieren von Modellergebnissen und verfolgt die letzten Argumente,
die an die modify-Methode übergeben wurden.

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method极客时间</span> <span style='color: #2980B9;'>def</span> `__init__(self)`</summary>

Initialisiert die DummyModifier-Instanz.
Richtet eine Instanzvariable ein, um die letzten in modify-Aufrufen verwendeten Argumente zu verfolgen.

</details>

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `modify(self, ticket_id: str, model_result)`</summary>

Simuliert das Modifizieren eines Modellergebnisses und speichert die Eingabeargumente.

**Parameter:**

- **`ticket_id`** (`str`) - Identifikator für das zu verarbeitende Ticket.
- **`model_result`** () - Das Ergebnis des Modells, das modifiziert würde.

**Rückgabe:** (`str`) - Ein fester String, der den Abschluss anzeigt.

</details>

---

## Modul: `open_ticket_ai\tests\src\run\test_preparers\test_data_preparer.py`

### <span style='color: #8E44AD;'>class</span> `DummyPreparer`

Eine Dummy-Implementierung einer Pipe zum Testen der Preparer-Funktionalität.
Kopiert einen Wert aus den Kontextdaten unter einem spezifischen Schlüssel.

**Parameter:**

- **`preparer_config`** (`PreparerConfig`) - Konfigurationseinstellungen für den Preparer.

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `__init__(self, cfg)`</summary>

Initialisiert den DummyPreparer mit der gegebenen Konfiguration.

**Parameter:**

- **`cfg`** (`PreparerConfig`) - Konfigurationsobjekt für den Preparer.

</details>

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `process(self, context: PipelineContext) -> PipelineContext`</summary>

Verarbeitet den Pipeline-Kontext durch Kopieren von Daten in das Feld 'prepared_data'.
Kopiert den Wert von context.data['key'] nach context.data['prepared_data'].

**Parameter:**

- **`context`** (`PipelineContext`) - Der Pipeline-Kontext mit Ticketdaten.

**Rückgabe:** (`PipelineContext`) - Der aktualisierte Kontext mit hinzugefügtem 'prepared_data'.

</details>

### <span style='color: #2980B9;'>def</span> `test_preparer_process_updates_context()`

Testet, dass DummyPreparer Kontextdaten korrekt aktualisiert.
Überprüft:
    1. Die Konfiguration des Preparers wird während der Initialisierung korrekt ausgegeben
    2. Die process-Methode kopiert den 'key'-Wert korrekt nach 'prepared_data'

---

## Modul: `open_ticket_ai\tests\src\run\test_preparers\test_subject_body_preparer.py`

### <span style='color: #2980B9;'>def</span> `test_subject_body_preparer_process_concatenates_fields()`

Testet die process-Methode des SubjectBodyPreparers.
Dieser Test überprüft, dass:
1. Während der Initialisierung der Preparer pretty_print_config mit seiner Konfiguration aufruft
2. Die process-Methode die Felder 'subject' und 'body' aus den Kontextdaten korrekt verkettet

---

## Modul: `open_ticket_ai\tests\src\test_app_main.py`

### <span style='color: #8E44AD;'>class</span> `TestAppRun`

Testsuite für die Funktionalität der App.run()-Methode.

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `test_run_validation_passes(self, monkeypatch)`</summary>

Testet, dass App.run() Validierung und Planung ausführt, wenn die Validierung erfolgreich ist.
Stellt sicher:
    - Validator wird genau einmal aufgerufen
    - Orchestrator plant Zeitpläne genau einmal ein
    - Konsolenausgabe erfolgt wie erwartet

</details>

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `test_run_validation_error_logs(self, monkeypatch, caplog)`</summary>

Testet, dass App.run() Validierungsfehler angemessen protokolliert.
Stellt sicher:
    - Validierungsfehler werden auf ERROR-Level protokolliert
    - Orchestrator versucht weiterhin, Zeitpläne nach Validierungsfehler einzurichten

</details>

### <span style='color: #8E44AD;'>class</span> `TestMainModule`

Testsuite für die Funktionalität des Hauptmoduls.

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `test_main_sets_logging_level(self, monkeypatch)`</summary>

Testet, dass main() die Logging-Verbositätslevel korrekt setzt.
Überprüft:
    - Logging-Level wird auf INFO gesetzt, wenn verbose=True

</details>

<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `test_start_creates_container_and_runs_app(self, monkeypatch, capsys)`</summary>

Testet die vollständige Anwendungsstartsequenz.
Stellt sicher:
    - Dependency-Container wird initialisiert
    - App-Instanz wird abgerufen und ausgeführt
    - Erwartete Konsolenausgabe (figlet art) ist vorhanden

</details>