import { ssrRenderAttrs, ssrRenderAttr } from "vue/server-renderer";
import { _ as _imports_0, a as _imports_1 } from "./overview.tojtMu7F.js";
import { useSSRContext } from "vue";
import { _ as _export_sfc } from "./plugin-vue_export-helper.1tPrXgE0.js";
const __pageData = JSON.parse('{"title":"Open Ticket AI Architecture Overview","description":"High-level look at the components and data flow in Open Ticket AI.","frontmatter":{"title":"Open Ticket AI Architecture Overview","description":"High-level look at the components and data flow in Open Ticket AI."},"headers":[],"relativePath":"en/architecture.md","filePath":"en/architecture.md"}');
const _sfc_main = { name: "en/architecture.md" };
function _sfc_ssrRender(_ctx, _push, _parent, _attrs, $props, $setup, $data, $options) {
  _push(`<div${ssrRenderAttrs(_attrs)}><h1 id="architecture-overview" tabindex="-1">Architecture Overview <a class="header-anchor" href="#architecture-overview" aria-label="Permalink to &quot;Architecture Overview&quot;">​</a></h1><p>Open Ticket AI is built around a modular pipeline that processes each ticket through a series of well-defined stages. The system relies on dependency injection and configuration files to assemble these stages, making it easy to extend or replace individual pieces.</p><h2 id="processing-pipeline" tabindex="-1">Processing Pipeline <a class="header-anchor" href="#processing-pipeline" aria-label="Permalink to &quot;Processing Pipeline&quot;">​</a></h2><p>The ticket processing pipeline looks like this:</p><div class="language- vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang"></span><pre class="shiki shiki-themes github-light github-dark vp-code" tabindex="0"><code><span class="line"><span>[ Incoming Ticket ]</span></span>
<span class="line"><span>       ↓</span></span>
<span class="line"><span>[ Preprocessor ] — cleans &amp; merges subject+body</span></span>
<span class="line"><span>       ↓</span></span>
<span class="line"><span>[ Transformer Tokenizer ]</span></span>
<span class="line"><span>       ↓</span></span>
<span class="line"><span>[ Queue Classifier ] → Queue ID + confidence</span></span>
<span class="line"><span>       ↓</span></span>
<span class="line"><span>[ Priority Classifier ] → Priority score + confidence</span></span>
<span class="line"><span>       ↓</span></span>
<span class="line"><span>[ Postprocessor ] — applies thresholds, routes or flags</span></span>
<span class="line"><span>       ↓</span></span>
<span class="line"><span>[ Ticket System Adapter ] — updates ticket via REST API</span></span></code></pre></div><p>Each step consumes and produces <strong>Value Objects</strong> such as <code>subject</code>, <code>body</code>, <code>queue_id</code> and <code>priority</code>. This approach keeps the pipeline modular and allows new steps or value objects to be added with minimal changes to the rest of the system.</p><h2 id="main-components" tabindex="-1">Main Components <a class="header-anchor" href="#main-components" aria-label="Permalink to &quot;Main Components&quot;">​</a></h2><ul><li><strong>App &amp; Orchestrator</strong> – Validate configuration, schedule jobs and manage the overall loop.</li><li><strong>Fetchers</strong> – Retrieve new tickets from external systems.</li><li><strong>Preparers</strong> – Transform raw ticket data into a form suitable for AI models.</li><li><strong>AI Inference Services</strong> – Load Hugging Face models and produce queue or priority predictions.</li><li><strong>Modifiers</strong> – Apply the predictions back to the ticket system via adapters.</li><li><strong>Ticket System Adapters</strong> – Provide REST integrations with systems such as OTOBO.</li></ul><p>All components are registered in a central dependency injection container and configured via <code>config.yml</code>.</p><h2 id="diagrams" tabindex="-1">Diagrams <a class="header-anchor" href="#diagrams" aria-label="Permalink to &quot;Diagrams&quot;">​</a></h2><h3 id="application-class-diagram" tabindex="-1">Application Class Diagram <a class="header-anchor" href="#application-class-diagram" aria-label="Permalink to &quot;Application Class Diagram&quot;">​</a></h3><p><img${ssrRenderAttr("src", _imports_0)} alt="Anwendungs-Klassendiagramm"></p><h3 id="overview-diagram" tabindex="-1">Overview Diagram <a class="header-anchor" href="#overview-diagram" aria-label="Permalink to &quot;Overview Diagram&quot;">​</a></h3><p><img${ssrRenderAttr("src", _imports_1)} alt="Übersichtsdiagramm"></p><p>These diagrams illustrate how the pipeline is orchestrated and how each component interacts with the others.</p><hr></div>`);
}
const _sfc_setup = _sfc_main.setup;
_sfc_main.setup = (props, ctx) => {
  const ssrContext = useSSRContext();
  (ssrContext.modules || (ssrContext.modules = /* @__PURE__ */ new Set())).add("en/architecture.md");
  return _sfc_setup ? _sfc_setup(props, ctx) : void 0;
};
const architecture = /* @__PURE__ */ _export_sfc(_sfc_main, [["ssrRender", _sfc_ssrRender]]);
export {
  __pageData,
  architecture as default
};
