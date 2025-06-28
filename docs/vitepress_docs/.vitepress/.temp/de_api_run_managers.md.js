import { resolveComponent, useSSRContext } from "vue";
import { ssrRenderAttrs, ssrRenderStyle, ssrRenderComponent } from "vue/server-renderer";
import { _ as _export_sfc } from "./plugin-vue_export-helper.1tPrXgE0.js";
const __pageData = JSON.parse('{"title":"Dokumentation für **/ce/run/managers/*.py","description":"","frontmatter":{},"headers":[],"relativePath":"de/api/run/managers.md","filePath":"de/api/run/managers.md"}');
const _sfc_main = { name: "de/api/run/managers.md" };
function _sfc_ssrRender(_ctx, _push, _parent, _attrs, $props, $setup, $data, $options) {
  const _component_Badge = resolveComponent("Badge");
  _push(`<div${ssrRenderAttrs(_attrs)}><h1 id="dokumentation-fur-ce-run-managers-py" tabindex="-1">Dokumentation für <code>**/ce/run/managers/*.py</code> <a class="header-anchor" href="#dokumentation-fur-ce-run-managers-py" aria-label="Permalink to &quot;Dokumentation für \`**/ce/run/managers/*.py\`&quot;">​</a></h1><h2 id="modul-open-ticket-ai-src-ce-run-managers-orchestrator-py" tabindex="-1">Modul: <code>open_ticket_ai\\src\\ce\\run\\managers\\orchestrator.py</code> <a class="header-anchor" href="#modul-open-ticket-ai-src-ce-run-managers-orchestrator-py" aria-label="Permalink to &quot;Modul: \`open_ticket_ai\\src\\ce\\run\\managers\\orchestrator.py\`&quot;">​</a></h2><p>Dienstprogramme für die Top-Level-Orchestrierung.</p><h3 id="class-orchestrator" tabindex="-1"><span style="${ssrRenderStyle({})}">class</span> <code>Orchestrator</code> <a class="header-anchor" href="#class-orchestrator" aria-label="Permalink to &quot;&lt;span style=&#39;text-info&#39;&gt;class&lt;/span&gt; \`Orchestrator\`&quot;">​</a></h3><p>Orchestriert die Ausführung von Ticketverarbeitungs-Pipelines. Diese <code>class</code> verwaltet den Lebenszyklus von Pipelines, einschließlich:</p><ul><li>Instanziierung von Pipelines mittels Dependency Injection</li><li>Individuelle Ticketverarbeitung</li><li>Geplante Ausführung von Pipelines</li></ul><p><strong>Parameter:</strong></p><ul><li><strong><code>config</code></strong> () - Konfigurationseinstellungen für den Orchestrator</li><li><strong><code>container</code></strong> () - Dependency-Injection-Container, der Pipeline-Instanzen bereitstellt</li><li><strong><code>_logger</code></strong> () - Logger-Instanz für Orchestrierungsoperationen</li><li><strong><code>_pipelines</code></strong> () - Dictionary, das Pipeline-IDs auf Pipeline-Instanzen abbildet</li></ul><details class="details custom-block"><summary>#### `);
  _push(ssrRenderComponent(_component_Badge, {
    type: "info",
    text: "Methode"
  }, null, _parent));
  _push(` <span class="text-warning">def</span> <code>__init__(self, config: OpenTicketAIConfig, container: AbstractContainer)</code></summary><p>Initialisiert den Orchestrator mit Konfiguration und DI-Container.</p><p><strong>Parameter:</strong></p><ul><li><strong><code>config</code></strong> () - Konfigurationseinstellungen für den Orchestrator.</li><li><strong><code>container</code></strong> () - Dependency-Injection-Container, der Pipeline-Instanzen bereitstellt.</li></ul></details><details class="details custom-block"><summary>#### `);
  _push(ssrRenderComponent(_component_Badge, {
    type: "info",
    text: "Methode"
  }, null, _parent));
  _push(` <span class="text-warning">def</span> <code>process_ticket(self, ticket_id: str, pipeline: Pipeline) -&gt; PipelineContext</code></summary><p>Führt eine Pipeline für ein bestimmtes Ticket aus. Erstellt einen Verarbeitungskontext und führt die angegebene Pipeline aus, um das gegebene Ticket zu verarbeiten. Dies ist die Kernmethode für die individuelle Ticketverarbeitung.</p><p><strong>Parameter:</strong></p><ul><li><strong><code>ticket_id</code></strong> () - Eindeutiger Bezeichner des zu verarbeitenden Tickets</li><li><strong><code>pipeline</code></strong> () - Auszuführende Pipeline-Instanz</li></ul><p><strong>Rückgabe:</strong> (<code>PipelineContext</code>) - Der Ausführungskontext, der Ergebnisse und den Zustand nach der Pipeline-Ausführung enthält</p></details><details class="details custom-block"><summary>#### `);
  _push(ssrRenderComponent(_component_Badge, {
    type: "info",
    text: "Methode"
  }, null, _parent));
  _push(` <span class="text-warning">def</span> <code>build_pipelines(self) -&gt; None</code></summary><p>Instanziiert alle konfigurierten Pipeline-Objekte. Verwendet den Dependency-Injection-Container, um Pipeline-Instanzen basierend auf der Konfiguration zu erstellen. Füllt die interne Pipeline-Registry mit Zuordnungen von Pipeline-IDs zu Instanzen.</p></details><details class="details custom-block"><summary>#### `);
  _push(ssrRenderComponent(_component_Badge, {
    type: "info",
    text: "Methode"
  }, null, _parent));
  _push(` <span class="text-warning">def</span> <code>set_schedules(self) -&gt; None</code></summary><p>Konfiguriert die geplante Ausführung für alle Pipelines. Führt die folgenden Operationen aus:</p><ol><li>Erstellt Pipelines, falls diese noch nicht instanziiert wurden</li><li>Konfiguriert die periodische Ausführung für jede Pipeline gemäß ihrer Zeitplankonfiguration unter Verwendung der <code>schedule</code>-Bibliothek</li></ol><p>Die Zeitplanung verwendet die folgenden Konfigurationsparameter:</p><ul><li>interval: Numerischer Intervallwert</li><li>unit: Zeiteinheit (z. B. <code>minutes</code>, <code>hours</code>, <code>days</code>)</li></ul></details><hr></div>`);
}
const _sfc_setup = _sfc_main.setup;
_sfc_main.setup = (props, ctx) => {
  const ssrContext = useSSRContext();
  (ssrContext.modules || (ssrContext.modules = /* @__PURE__ */ new Set())).add("de/api/run/managers.md");
  return _sfc_setup ? _sfc_setup(props, ctx) : void 0;
};
const managers = /* @__PURE__ */ _export_sfc(_sfc_main, [["ssrRender", _sfc_ssrRender]]);
export {
  __pageData,
  managers as default
};
