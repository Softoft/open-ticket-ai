import { resolveComponent, useSSRContext } from "vue";
import { ssrRenderAttrs, ssrRenderStyle, ssrRenderComponent } from "vue/server-renderer";
import { _ as _export_sfc } from "./plugin-vue_export-helper.1tPrXgE0.js";
const __pageData = JSON.parse('{"title":"Dokumentation für **/ce/ticket_system_integration/*.py","description":"","frontmatter":{},"headers":[],"relativePath":"de/api/run/ticket_system_integration.md","filePath":"de/api/run/ticket_system_integration.md"}');
const _sfc_main = { name: "de/api/run/ticket_system_integration.md" };
function _sfc_ssrRender(_ctx, _push, _parent, _attrs, $props, $setup, $data, $options) {
  const _component_Badge = resolveComponent("Badge");
  _push(`<div${ssrRenderAttrs(_attrs)}><h1 id="dokumentation-fur-ce-ticket-system-integration-py" tabindex="-1">Dokumentation für <code>**/ce/ticket_system_integration/*.py</code> <a class="header-anchor" href="#dokumentation-fur-ce-ticket-system-integration-py" aria-label="Permalink to &quot;Dokumentation für \`**/ce/ticket_system_integration/*.py\`&quot;">​</a></h1><h2 id="modul-open-ticket-ai-src-ce-ticket-system-integration-otobo-adapter-py" tabindex="-1">Modul: <code>open_ticket_ai\\src\\ce\\ticket_system_integration\\otobo_adapter.py</code> <a class="header-anchor" href="#modul-open-ticket-ai-src-ce-ticket-system-integration-otobo-adapter-py" aria-label="Permalink to &quot;Modul: \`open_ticket_ai\\src\\ce\\ticket_system_integration\\otobo_adapter.py\`&quot;">​</a></h2><hr><h2 id="modul-open-ticket-ai-src-ce-ticket-system-integration-otobo-adapter-config-py" tabindex="-1">Modul: <code>open_ticket_ai\\src\\ce\\ticket_system_integration\\otobo_adapter_config.py</code> <a class="header-anchor" href="#modul-open-ticket-ai-src-ce-ticket-system-integration-otobo-adapter-config-py" aria-label="Permalink to &quot;Modul: \`open_ticket_ai\\src\\ce\\ticket_system_integration\\otobo_adapter_config.py\`&quot;">​</a></h2><hr><h2 id="modul-open-ticket-ai-src-ce-ticket-system-integration-ticket-system-adapter-py" tabindex="-1">Modul: <code>open_ticket_ai\\src\\ce\\ticket_system_integration\\ticket_system_adapter.py</code> <a class="header-anchor" href="#modul-open-ticket-ai-src-ce-ticket-system-integration-ticket-system-adapter-py" aria-label="Permalink to &quot;Modul: \`open_ticket_ai\\src\\ce\\ticket_system_integration\\ticket_system_adapter.py\`&quot;">​</a></h2><h3 id="class-ticketsystemadapter" tabindex="-1"><span style="${ssrRenderStyle({})}">class</span> <code>TicketSystemAdapter</code> <a class="header-anchor" href="#class-ticketsystemadapter" aria-label="Permalink to &quot;&lt;span style=&#39;text-info&#39;&gt;class&lt;/span&gt; \`TicketSystemAdapter\`&quot;">​</a></h3><p>Eine abstrakte Basisklasse für Ticket-System-Adapter. Diese Klasse definiert die Schnittstelle, die alle konkreten Ticket-System-Adapter implementieren müssen, um mit verschiedenen Ticket-Systemen zu interagieren. Sie bietet eine gemeinsame Konfigurationsbehandlung durch Dependency Injection und erfordert, dass Unterklassen die Kernoperationen für Tickets implementieren.</p><p><strong>Parameter:</strong></p><ul><li><strong><code>config</code></strong> (<code>SystemConfig</code>) - Systemkonfigurationsobjekt, das die Adapter-Einstellungen enthält.</li></ul><details class="details custom-block"><summary>#### `);
  _push(ssrRenderComponent(_component_Badge, {
    type: "info",
    text: "method"
  }, null, _parent));
  _push(` <span class="text-warning">def</span> <code>__init__(self, config: SystemConfig)</code></summary><p>Initialisiert den Adapter mit der Systemkonfiguration. Diesem Konstruktor wird die Systemkonfiguration automatisch über das Dependency-Injection-Framework injiziert. Er initialisiert den Adapter mit der bereitgestellten Konfiguration und stellt die ordnungsgemäße Einrichtung der geerbten Komponenten sicher.</p><p><strong>Parameter:</strong></p><ul><li><strong><code>config</code></strong> (<code>SystemConfig</code>) - Das Systemkonfigurationsobjekt, das alle notwendigen Einstellungen und Parameter für den Adapter enthält.</li></ul></details><details class="details custom-block"><summary>#### `);
  _push(ssrRenderComponent(_component_Badge, {
    type: "info",
    text: "method"
  }, null, _parent));
  _push(` <span class="text-warning">async def</span> <code>update_ticket(self, ticket_id: str, data: dict) -&gt; dict | None</code></summary><p>Aktualisiert ein Ticket im System. Diese Methode muss von konkreten Adaptern implementiert werden, um die Aktualisierung von Ticket-Attributen im Ziel-Ticket-System zu handhaben. Sie sollte Teilaktualisierungen unterstützen und die aktualisierte Ticket-Darstellung zurückgeben.</p><p><strong>Parameter:</strong></p><ul><li><strong><code>ticket_id</code></strong> () - Eindeutiger Bezeichner des zu aktualisierenden Tickets.</li><li><strong><code>data</code></strong> () - Dictionary mit Attributen, die am Ticket aktualisiert werden sollen.</li></ul><p><strong>Rückgabe:</strong> (<code>Optional[dict]</code>) - Das aktualisierte Ticket-Objekt als Dictionary bei Erfolg, oder None, wenn die Aktualisierung fehlschlug oder das Ticket nicht gefunden wurde.</p></details><details class="details custom-block"><summary>#### `);
  _push(ssrRenderComponent(_component_Badge, {
    type: "info",
    text: "method"
  }, null, _parent));
  _push(` <span class="text-warning">async def</span> <code>find_tickets(self, query: dict) -&gt; list[dict]</code></summary><p>Sucht nach Tickets, die auf <code>query</code> passen. Diese Methode muss von konkreten Adaptern implementiert werden, um komplexe Suchen im Ziel-Ticket-System durchzuführen. Die Abfragestruktur ist adapterspezifisch, sollte aber gängige Filter- und Suchoperationen unterstützen.</p><p><strong>Parameter:</strong></p><ul><li><strong><code>query</code></strong> () - Dictionary, das die Suchparameter und Filter repräsentiert.</li></ul><p><strong>Rückgabe:</strong> (<code>list[dict]</code>) - Eine Liste von Ticket-Objekten (als Dictionaries), die der Abfrage entsprechen. Gibt eine leere Liste zurück, wenn keine Übereinstimmungen gefunden werden.</p></details><details class="details custom-block"><summary>#### `);
  _push(ssrRenderComponent(_component_Badge, {
    type: "info",
    text: "method"
  }, null, _parent));
  _push(` <span class="text-warning">async def</span> <code>find_first_ticket(self, query: dict) -&gt; dict | None</code></summary><p>Gibt das erste Ticket zurück, das auf <code>query</code> passt, falls vorhanden. Dies ist eine Hilfsmethode, die das erste passende Ticket aus einer Suchoperation zurückgeben sollte. Sie sollte die Leistung optimieren, indem sie die Ergebnisse intern begrenzt.</p><p><strong>Parameter:</strong></p><ul><li><strong><code>query</code></strong> () - Dictionary, das die Suchparameter und Filter repräsentiert.</li></ul><p><strong>Rückgabe:</strong> (<code>Optional[dict]</code>) - Das erste passende Ticket-Objekt als Dictionary, oder None, wenn keine Tickets der Abfrage entsprechen.</p></details><hr></div>`);
}
const _sfc_setup = _sfc_main.setup;
_sfc_main.setup = (props, ctx) => {
  const ssrContext = useSSRContext();
  (ssrContext.modules || (ssrContext.modules = /* @__PURE__ */ new Set())).add("de/api/run/ticket_system_integration.md");
  return _sfc_setup ? _sfc_setup(props, ctx) : void 0;
};
const ticket_system_integration = /* @__PURE__ */ _export_sfc(_sfc_main, [["ssrRender", _sfc_ssrRender]]);
export {
  __pageData,
  ticket_system_integration as default
};
