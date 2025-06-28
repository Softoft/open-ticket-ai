import { ssrRenderAttrs } from "vue/server-renderer";
import { useSSRContext } from "vue";
import { _ as _export_sfc } from "./plugin-vue_export-helper.1tPrXgE0.js";
const __pageData = JSON.parse('{"title":"Open Ticket AI Architektur","description":"Erfahren Sie mehr über die Architektur von Open Ticket AI.","frontmatter":{"title":"Open Ticket AI Architektur","description":"Erfahren Sie mehr über die Architektur von Open Ticket AI."},"headers":[],"relativePath":"de/concepts/pipeline-architecture.md","filePath":"de/concepts/pipeline-architecture.md"}');
const _sfc_main = { name: "de/concepts/pipeline-architecture.md" };
function _sfc_ssrRender(_ctx, _push, _parent, _attrs, $props, $setup, $data, $options) {
  _push(`<div${ssrRenderAttrs(_attrs)}><h1 id="architektur" tabindex="-1">Architektur <a class="header-anchor" href="#architektur" aria-label="Permalink to &quot;Architektur&quot;">​</a></h1><h2 id="pipeline-value-objects" tabindex="-1">Pipeline &amp; Value Objects <a class="header-anchor" href="#pipeline-value-objects" aria-label="Permalink to &quot;Pipeline &amp; Value Objects&quot;">​</a></h2><p>Der Kern von Open Ticket AI ist seine Verarbeitungspipeline:</p><div class="language- vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang"></span><pre class="shiki shiki-themes github-light github-dark vp-code" tabindex="0"><code><span class="line"><span>[ Eingehendes Ticket ]</span></span>
<span class="line"><span>       ↓</span></span>
<span class="line"><span>[ Preprocessor ] — bereinigt &amp; führt Betreff+Text zusammen</span></span>
<span class="line"><span>       ↓</span></span>
<span class="line"><span>[ Transformer Tokenizer ]</span></span>
<span class="line"><span>       ↓</span></span>
<span class="line"><span>[ Queue Classifier ] → Queue-ID + Konfidenz</span></span>
<span class="line"><span>       ↓</span></span>
<span class="line"><span>[ Priority Classifier ] → Prioritäts-Score + Konfidenz</span></span>
<span class="line"><span>       ↓</span></span>
<span class="line"><span>[ Postprocessor ] — wendet Schwellenwerte an, leitet weiter oder markiert</span></span>
<span class="line"><span>       ↓</span></span>
<span class="line"><span>[ Ticket System Adapter ] — aktualisiert Ticket über REST API</span></span></code></pre></div><p>Jede Stufe in dieser Pipeline konsumiert und produziert <strong>Value Objects</strong> (z. B. <code>subject</code>, <code>body</code>, <code>queue_id</code>, <code>priority</code>). Dieses Design macht die Pipeline modular und einfach durch benutzerdefinierte Verarbeitungsschritte oder neue Value Objects erweiterbar.</p><h2 id="systemdiagramme" tabindex="-1">Systemdiagramme <a class="header-anchor" href="#systemdiagramme" aria-label="Permalink to &quot;Systemdiagramme&quot;">​</a></h2></div>`);
}
const _sfc_setup = _sfc_main.setup;
_sfc_main.setup = (props, ctx) => {
  const ssrContext = useSSRContext();
  (ssrContext.modules || (ssrContext.modules = /* @__PURE__ */ new Set())).add("de/concepts/pipeline-architecture.md");
  return _sfc_setup ? _sfc_setup(props, ctx) : void 0;
};
const pipelineArchitecture = /* @__PURE__ */ _export_sfc(_sfc_main, [["ssrRender", _sfc_ssrRender]]);
export {
  __pageData,
  pipelineArchitecture as default
};
