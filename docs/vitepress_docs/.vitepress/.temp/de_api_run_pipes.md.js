import { resolveComponent, useSSRContext } from "vue";
import { ssrRenderAttrs, ssrRenderStyle, ssrRenderComponent } from "vue/server-renderer";
import { _ as _export_sfc } from "./plugin-vue_export-helper.1tPrXgE0.js";
const __pageData = JSON.parse('{"title":"Dokumentation für **/ce/run/pipe_implementations/*.py","description":"","frontmatter":{},"headers":[],"relativePath":"de/api/run/pipes.md","filePath":"de/api/run/pipes.md"}');
const _sfc_main = { name: "de/api/run/pipes.md" };
function _sfc_ssrRender(_ctx, _push, _parent, _attrs, $props, $setup, $data, $options) {
  const _component_Badge = resolveComponent("Badge");
  _push(`<div${ssrRenderAttrs(_attrs)}><h1 id="dokumentation-fur-ce-run-pipe-implementations-py" tabindex="-1">Dokumentation für <code>**/ce/run/pipe_implementations/*.py</code> <a class="header-anchor" href="#dokumentation-fur-ce-run-pipe-implementations-py" aria-label="Permalink to &quot;Dokumentation für \`**/ce/run/pipe_implementations/*.py\`&quot;">​</a></h1><h2 id="modul-open-ticket-ai-src-ce-run-pipe-implementations-basic-ticket-fetcher-py" tabindex="-1">Modul: <code>open_ticket_ai\\src\\ce\\run\\pipe_implementations\\basic_ticket_fetcher.py</code> <a class="header-anchor" href="#modul-open-ticket-ai-src-ce-run-pipe-implementations-basic-ticket-fetcher-py" aria-label="Permalink to &quot;Modul: \`open_ticket_ai\\src\\ce\\run\\pipe_implementations\\basic_ticket_fetcher.py\`&quot;">​</a></h2><h3 id="class-basicticketfetcher" tabindex="-1"><span style="${ssrRenderStyle({})}">class</span> <code>BasicTicketFetcher</code> <a class="header-anchor" href="#class-basicticketfetcher" aria-label="Permalink to &quot;&lt;span style=&#39;text-info&#39;&gt;class&lt;/span&gt; \`BasicTicketFetcher\`&quot;">​</a></h3><p>Einfacher Fetcher, der Ticketdaten mithilfe des Ticket-System-Adapters lädt. Diese Pipe ruft Ticketinformationen aus einem externen Ticketsystem mithilfe des bereitgestellten Adapters ab. Sie dient als Platzhalter für komplexere Fetching-Implementierungen.</p><p><strong>Parameter:</strong></p><ul><li><strong><code>fetcher_config</code></strong> (<code>RegistryInstanceConfig</code>) - Konfigurationsinstanz für den Fetcher.</li><li><strong><code>ticket_system</code></strong> (<code>TicketSystemAdapter</code>) - Adapter zur Interaktion mit dem Ticketsystem.</li></ul><details class="details custom-block"><summary>#### `);
  _push(ssrRenderComponent(_component_Badge, {
    type: "info",
    text: "method"
  }, null, _parent));
  _push(` <span class="text-warning">def</span> <code>__init__(self, config: RegistryInstanceConfig, ticket_system: TicketSystemAdapter)</code></summary><p>Initialisiert den BasicTicketFetcher mit Konfiguration und Ticket-System-Adapter.</p><p><strong>Parameter:</strong></p><ul><li><strong><code>config</code></strong> (<code>RegistryInstanceConfig</code>) - Die Konfigurationsinstanz für den Fetcher.</li><li><strong><code>ticket_system</code></strong> (<code>TicketSystemAdapter</code>) - Der Adapter zur Interaktion mit dem Ticketsystem.</li></ul></details><details class="details custom-block"><summary>#### `);
  _push(ssrRenderComponent(_component_Badge, {
    type: "info",
    text: "method"
  }, null, _parent));
  _push(` <span class="text-warning">def</span> <code>process(self, context: PipelineContext) -&gt; PipelineContext</code></summary><p>Ruft Ticketdaten ab und aktualisiert den Pipeline-Kontext. Ruft das Ticket mithilfe der Ticket-ID aus dem Kontext ab. Wenn es gefunden wird, wird das Daten-Dictionary des Kontexts mit den Ticketinformationen aktualisiert. Wenn kein Ticket gefunden wird, bleibt der Kontext unverändert.</p><p><strong>Parameter:</strong></p><ul><li><strong><code>context</code></strong> (<code>PipelineContext</code>) - Der Pipeline-Kontext, der die <code>ticket_id</code> enthält.</li></ul><p><strong>Rückgabe:</strong> (<code>PipelineContext</code>) - Das Kontextobjekt. Wenn ein Ticket gefunden wurde, enthält sein <code>data</code>-Dictionary die Ticketinformationen. Andernfalls wird der ursprüngliche Kontext zurückgegeben.</p></details><details class="details custom-block"><summary>#### `);
  _push(ssrRenderComponent(_component_Badge, {
    type: "info",
    text: "method"
  }, null, _parent));
  _push(` <span class="text-warning">def</span> <code>get_description() -&gt; str</code></summary><p>Liefert eine statische Beschreibung der Funktionalität dieser Pipe.</p><p><strong>Rückgabe:</strong> (<code>str</code>) - Eine statische Beschreibung des Zwecks und Verhaltens der Pipe.</p></details><hr><h2 id="modul-open-ticket-ai-src-ce-run-pipe-implementations-generic-ticket-updater-py" tabindex="-1">Modul: <code>open_ticket_ai\\src\\ce\\run\\pipe_implementations\\generic_ticket_updater.py</code> <a class="header-anchor" href="#modul-open-ticket-ai-src-ce-run-pipe-implementations-generic-ticket-updater-py" aria-label="Permalink to &quot;Modul: \`open_ticket_ai\\src\\ce\\run\\pipe_implementations\\generic_ticket_updater.py\`&quot;">​</a></h2><h3 id="class-genericticketupdater" tabindex="-1"><span style="${ssrRenderStyle({})}">class</span> <code>GenericTicketUpdater</code> <a class="header-anchor" href="#class-genericticketupdater" aria-label="Permalink to &quot;&lt;span style=&#39;text-info&#39;&gt;class&lt;/span&gt; \`GenericTicketUpdater\`&quot;">​</a></h3><p>Aktualisiert ein Ticket im Ticketsystem unter Verwendung von Daten aus dem Kontext. Diese Pipe-Komponente ist für die Aktualisierung von Tickets in einem externen Ticket-Tracking-System (wie Jira, ServiceNow usw.) verantwortlich, wobei Daten verwendet werden, die während der Pipeline-Ausführung generiert wurden. Sie prüft den Pipeline-Kontext auf Aktualisierungsanweisungen und delegiert den eigentlichen Aktualisierungsvorgang an den konfigurierten Ticket-System-Adapter.</p><p><strong>Parameter:</strong></p><ul><li><strong><code>modifier_config</code></strong> () - Konfigurationseinstellungen für den Ticket-Updater.</li><li><strong><code>ticket_system</code></strong> () - Adapter-Instanz zur Interaktion mit dem externen Ticketsystem.</li></ul><details class="details custom-block"><summary>#### `);
  _push(ssrRenderComponent(_component_Badge, {
    type: "info",
    text: "method"
  }, null, _parent));
  _push(` <span class="text-warning">def</span> <code>__init__(self, config: RegistryInstanceConfig, ticket_system: TicketSystemAdapter)</code></summary><p>Initialisiert den <code>GenericTicketUpdater</code> mit Konfiguration und Ticket-System-Adapter.</p><p><strong>Parameter:</strong></p><ul><li><strong><code>config</code></strong> () - Konfigurationsinstanz, die Einstellungen für die Pipeline-Komponente enthält.</li><li><strong><code>ticket_system</code></strong> () - Adapter-Objekt, das die Kommunikation mit dem externen Ticketsystem abwickelt.</li></ul></details><details class="details custom-block"><summary>#### `);
  _push(ssrRenderComponent(_component_Badge, {
    type: "info",
    text: "method"
  }, null, _parent));
  _push(` <span class="text-warning">def</span> <code>process(self, context: PipelineContext) -&gt; PipelineContext</code></summary><p>Verarbeitet den Pipeline-Kontext, um das Ticket zu aktualisieren, falls Aktualisierungsdaten vorhanden sind. Ruft Aktualisierungsdaten aus dem Kontext ab (insbesondere aus dem Schlüssel <code>&quot;update_data&quot;</code> in <code>context.data</code>) und aktualisiert das Ticket im Ticketsystem, wenn Aktualisierungsdaten vorhanden sind. Gibt den Kontext unverändert zurück.</p><p><strong>Parameter:</strong></p><ul><li><strong><code>context</code></strong> () - Der Pipeline-Kontext, der Daten und Ticketinformationen enthält.</li></ul><p><strong>Rückgabe:</strong> () - Der ursprüngliche Pipeline-Kontext nach der Verarbeitung (unverändert).</p></details><details class="details custom-block"><summary>#### `);
  _push(ssrRenderComponent(_component_Badge, {
    type: "info",
    text: "method"
  }, null, _parent));
  _push(` <span class="text-warning">def</span> <code>get_description() -&gt; str</code></summary><p>Liefert eine Beschreibung des Zwecks der Pipe.</p><p><strong>Rückgabe:</strong> () - Ein String, der die Funktionalität der Pipe beschreibt.</p></details><hr><h2 id="modul-open-ticket-ai-src-ce-run-pipe-implementations-hf-local-ai-inference-service-py" tabindex="-1">Modul: <code>open_ticket_ai\\src\\ce\\run\\pipe_implementations\\hf_local_ai_inference_service.py</code> <a class="header-anchor" href="#modul-open-ticket-ai-src-ce-run-pipe-implementations-hf-local-ai-inference-service-py" aria-label="Permalink to &quot;Modul: \`open_ticket_ai\\src\\ce\\run\\pipe_implementations\\hf_local_ai_inference_service.py\`&quot;">​</a></h2><h3 id="class-hfaiinferenceservice" tabindex="-1"><span style="${ssrRenderStyle({})}">class</span> <code>HFAIInferenceService</code> <a class="header-anchor" href="#class-hfaiinferenceservice" aria-label="Permalink to &quot;&lt;span style=&#39;text-info&#39;&gt;class&lt;/span&gt; \`HFAIInferenceService\`&quot;">​</a></h3><p>Eine Klasse, die ein Hugging Face AI-Modell repräsentiert. Diese Klasse ist ein Platzhalter für die zukünftige Implementierung von Funktionalitäten des Hugging Face AI-Modells. Derzeit enthält sie keine Methoden oder Eigenschaften.</p><details class="details custom-block"><summary>#### `);
  _push(ssrRenderComponent(_component_Badge, {
    type: "info",
    text: "method"
  }, null, _parent));
  _push(` <span class="text-warning">def</span> <code>__init__(self, config: RegistryInstanceConfig)</code></summary><p>Initialisiert den HFAIInferenceService mit der Konfiguration.</p><p><strong>Parameter:</strong></p><ul><li><strong><code>config</code></strong> (<code>RegistryInstanceConfig</code>) - Konfigurationsinstanz für den Dienst.</li></ul></details><details class="details custom-block"><summary>#### `);
  _push(ssrRenderComponent(_component_Badge, {
    type: "info",
    text: "method"
  }, null, _parent));
  _push(` <span class="text-warning">def</span> <code>process(self, context: PipelineContext) -&gt; PipelineContext</code></summary><p>Verarbeitet den Pipeline-Kontext, indem vorbereitete Daten als Modellergebnis gespeichert werden. Diese Methode dient als Platzhalter für die eigentliche Modell-Inferenzlogik. Derzeit kopiert sie einfach die &#39;prepared_data&#39; aus dem Kontext in &#39;model_result&#39;.</p><p><strong>Parameter:</strong></p><ul><li><strong><code>context</code></strong> (<code>PipelineContext</code>) - Der Pipeline-Kontext, der die zu verarbeitenden Daten enthält.</li></ul><p><strong>Rückgabe:</strong> (<code>PipelineContext</code>) - Der aktualisierte Pipeline-Kontext mit dem gespeicherten Modellergebnis.</p></details><details class="details custom-block"><summary>#### `);
  _push(ssrRenderComponent(_component_Badge, {
    type: "info",
    text: "method"
  }, null, _parent));
  _push(` <span class="text-warning">def</span> <code>get_description() -&gt; str</code></summary><p>Liefert eine Beschreibung des Dienstes.</p><p><strong>Rückgabe:</strong> (<code>str</code>) - Beschreibungstext für den Hugging Face AI-Modelldienst.</p></details><hr><h2 id="modul-open-ticket-ai-src-ce-run-pipe-implementations-subject-body-preparer-py" tabindex="-1">Modul: <code>open_ticket_ai\\src\\ce\\run\\pipe_implementations\\subject_body_preparer.py</code> <a class="header-anchor" href="#modul-open-ticket-ai-src-ce-run-pipe-implementations-subject-body-preparer-py" aria-label="Permalink to &quot;Modul: \`open_ticket_ai\\src\\ce\\run\\pipe_implementations\\subject_body_preparer.py\`&quot;">​</a></h2><h3 id="class-subjectbodypreparer" tabindex="-1"><span style="${ssrRenderStyle({})}">class</span> <code>SubjectBodyPreparer</code> <a class="header-anchor" href="#class-subjectbodypreparer" aria-label="Permalink to &quot;&lt;span style=&#39;text-info&#39;&gt;class&lt;/span&gt; \`SubjectBodyPreparer\`&quot;">​</a></h3><p>Eine Pipeline-Komponente, die den Betreff und den Inhalt eines Tickets für die Verarbeitung vorbereitet. Diese Pipe extrahiert die Felder für Betreff und Inhalt aus den Ticketdaten, wiederholt den Betreff eine konfigurierbare Anzahl von Malen und verkettet ihn mit dem Inhalt. Die vorbereiteten Daten werden im Pipeline-Kontext für die nachgelagerte Verarbeitung gespeichert.</p><p><strong>Parameter:</strong></p><ul><li><strong><code>preparer_config</code></strong> (<code>RegistryInstanceConfig</code>) - Konfigurationsparameter für den Preparer.</li></ul><details class="details custom-block"><summary>#### `);
  _push(ssrRenderComponent(_component_Badge, {
    type: "info",
    text: "method"
  }, null, _parent));
  _push(` <span class="text-warning">def</span> <code>__init__(self, config: RegistryInstanceConfig)</code></summary><p>Initialisiert den SubjectBodyPreparer mit der Konfiguration.</p><p><strong>Parameter:</strong></p><ul><li><strong><code>config</code></strong> (<code>RegistryInstanceConfig</code>) - Konfigurationsparameter für den Preparer.</li></ul></details><details class="details custom-block"><summary>#### `);
  _push(ssrRenderComponent(_component_Badge, {
    type: "info",
    text: "method"
  }, null, _parent));
  _push(` <span class="text-warning">def</span> <code>process(self, context: PipelineContext) -&gt; PipelineContext</code></summary><p>Verarbeitet Ticketdaten, um Betreff und Inhalt vorzubereiten. Extrahiert Betreff- und Inhaltsfelder aus den Kontextdaten, wiederholt den Betreff wie in der Konfiguration angegeben und verkettet ihn mit dem Inhalt. Speichert das Ergebnis im Kontext unter dem Schlüssel &#39;prepared_data&#39;.</p><p><strong>Parameter:</strong></p><ul><li><strong><code>context</code></strong> (<code>PipelineContext</code>) - Pipeline-Kontext, der Ticketdaten enthält.</li></ul><p><strong>Rückgabe:</strong> (<code>PipelineContext</code>) - Aktualisierter Kontext mit vorbereiteten Daten.</p></details><details class="details custom-block"><summary>#### `);
  _push(ssrRenderComponent(_component_Badge, {
    type: "info",
    text: "method"
  }, null, _parent));
  _push(` <span class="text-warning">def</span> <code>get_description() -&gt; str</code></summary><p>Liefert eine Beschreibung der Funktionalität der Pipe.</p><p><strong>Rückgabe:</strong> (<code>str</code>) - Beschreibung des Zwecks der Pipe.</p></details><hr></div>`);
}
const _sfc_setup = _sfc_main.setup;
_sfc_main.setup = (props, ctx) => {
  const ssrContext = useSSRContext();
  (ssrContext.modules || (ssrContext.modules = /* @__PURE__ */ new Set())).add("de/api/run/pipes.md");
  return _sfc_setup ? _sfc_setup(props, ctx) : void 0;
};
const pipes = /* @__PURE__ */ _export_sfc(_sfc_main, [["ssrRender", _sfc_ssrRender]]);
export {
  __pageData,
  pipes as default
};
