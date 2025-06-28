import { ssrRenderAttrs, ssrRenderAttr } from "vue/server-renderer";
import { _ as _imports_0, a as _imports_1 } from "./overview.tojtMu7F.js";
import { useSSRContext } from "vue";
import { _ as _export_sfc } from "./plugin-vue_export-helper.1tPrXgE0.js";
const __pageData = JSON.parse('{"title":"Architekturübersicht von Open Ticket AI","description":"Ein allgemeiner Überblick über die Komponenten und den Datenfluss in Open Ticket AI.","frontmatter":{"title":"Architekturübersicht von Open Ticket AI","description":"Ein allgemeiner Überblick über die Komponenten und den Datenfluss in Open Ticket AI."},"headers":[],"relativePath":"de/architecture.md","filePath":"de/architecture.md"}');
const _sfc_main = { name: "de/architecture.md" };
function _sfc_ssrRender(_ctx, _push, _parent, _attrs, $props, $setup, $data, $options) {
  _push(`<div${ssrRenderAttrs(_attrs)}><h1 id="architekturubersicht" tabindex="-1">Architekturübersicht <a class="header-anchor" href="#architekturubersicht" aria-label="Permalink to &quot;Architekturübersicht&quot;">​</a></h1><p>Open Ticket AI basiert auf einer modularen Pipeline, die jedes Ticket in einer Reihe von klar definierten Stufen verarbeitet. Das System nutzt Dependency Injection und Konfigurationsdateien, um diese Stufen zusammenzusetzen, was die Erweiterung oder den Austausch einzelner Teile erleichtert.</p><h2 id="verarbeitungs-pipeline" tabindex="-1">Verarbeitungs-Pipeline <a class="header-anchor" href="#verarbeitungs-pipeline" aria-label="Permalink to &quot;Verarbeitungs-Pipeline&quot;">​</a></h2><p>Die Pipeline zur Ticketverarbeitung sieht wie folgt aus:</p><div class="language- vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang"></span><pre class="shiki shiki-themes github-light github-dark vp-code" tabindex="0"><code><span class="line"><span>[ Eingehendes Ticket ]</span></span>
<span class="line"><span>       ↓</span></span>
<span class="line"><span>[ Preprocessor ] — bereinigt &amp; führt Betreff+Text zusammen</span></span>
<span class="line"><span>       ↓</span></span>
<span class="line"><span>[ Transformer Tokenizer ]</span></span>
<span class="line"><span>       ↓</span></span>
<span class="line"><span>[ Queue Classifier ] → Queue-ID + Konfidenz</span></span>
<span class="line"><span>       ↓</span></span>
<span class="line"><span>[ Priority Classifier ] → Prioritätswert + Konfidenz</span></span>
<span class="line"><span>       ↓</span></span>
<span class="line"><span>[ Postprocessor ] — wendet Schwellenwerte an, leitet weiter oder markiert</span></span>
<span class="line"><span>       ↓</span></span>
<span class="line"><span>[ Ticket System Adapter ] — aktualisiert Ticket über REST API</span></span></code></pre></div><p>Jeder Schritt konsumiert und produziert <strong>Werteobjekte</strong> (Value Objects) wie <code>subject</code>, <code>body</code>, <code>queue_id</code> und <code>priority</code>. Dieser Ansatz hält die Pipeline modular und ermöglicht das Hinzufügen neuer Schritte oder Werteobjekte mit minimalen Änderungen am restlichen System.</p><h2 id="hauptkomponenten" tabindex="-1">Hauptkomponenten <a class="header-anchor" href="#hauptkomponenten" aria-label="Permalink to &quot;Hauptkomponenten&quot;">​</a></h2><ul><li><strong>App &amp; Orchestrator</strong> – Validieren die Konfiguration, planen Jobs und verwalten die Gesamtschleife.</li><li><strong>Fetchers</strong> – Rufen neue Tickets von externen Systemen ab.</li><li><strong>Preparers</strong> – Wandeln rohe Ticketdaten in eine für KI-Modelle geeignete Form um.</li><li><strong>AI Inference Services</strong> – Laden Hugging Face-Modelle und erzeugen Vorhersagen für Queue oder Priorität.</li><li><strong>Modifiers</strong> – Übertragen die Vorhersagen über Adapter zurück in das Ticketsystem.</li><li><strong>Ticket System Adapters</strong> – Stellen REST-Integrationen mit Systemen wie OTOBO bereit.</li></ul><p>Alle Komponenten werden in einem zentralen Dependency-Injection-Container registriert und über <code>config.yml</code> konfiguriert.</p><h2 id="diagramme" tabindex="-1">Diagramme <a class="header-anchor" href="#diagramme" aria-label="Permalink to &quot;Diagramme&quot;">​</a></h2><h3 id="anwendungs-klassendiagramm" tabindex="-1">Anwendungs-Klassendiagramm <a class="header-anchor" href="#anwendungs-klassendiagramm" aria-label="Permalink to &quot;Anwendungs-Klassendiagramm&quot;">​</a></h3><p><img${ssrRenderAttr("src", _imports_0)} alt="Anwendungs-Klassendiagramm"></p><h3 id="ubersichtsdiagramm" tabindex="-1">Übersichtsdiagramm <a class="header-anchor" href="#ubersichtsdiagramm" aria-label="Permalink to &quot;Übersichtsdiagramm&quot;">​</a></h3><p><img${ssrRenderAttr("src", _imports_1)} alt="Übersichtsdiagramm"></p><p>Diese Diagramme veranschaulichen, wie die Pipeline orchestriert wird und wie die einzelnen Komponenten miteinander interagieren.</p></div>`);
}
const _sfc_setup = _sfc_main.setup;
_sfc_main.setup = (props, ctx) => {
  const ssrContext = useSSRContext();
  (ssrContext.modules || (ssrContext.modules = /* @__PURE__ */ new Set())).add("de/architecture.md");
  return _sfc_setup ? _sfc_setup(props, ctx) : void 0;
};
const architecture = /* @__PURE__ */ _export_sfc(_sfc_main, [["ssrRender", _sfc_ssrRender]]);
export {
  __pageData,
  architecture as default
};
