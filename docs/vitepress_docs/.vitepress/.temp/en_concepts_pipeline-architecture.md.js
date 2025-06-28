import { ssrRenderAttrs } from "vue/server-renderer";
import { useSSRContext } from "vue";
import { _ as _export_sfc } from "./plugin-vue_export-helper.1tPrXgE0.js";
const __pageData = JSON.parse('{"title":"Open Ticket AI Architecture","description":"Learn about the architecture of Open Ticket AI.","frontmatter":{"title":"Open Ticket AI Architecture","description":"Learn about the architecture of Open Ticket AI."},"headers":[],"relativePath":"en/concepts/pipeline-architecture.md","filePath":"en/concepts/pipeline-architecture.md"}');
const _sfc_main = { name: "en/concepts/pipeline-architecture.md" };
function _sfc_ssrRender(_ctx, _push, _parent, _attrs, $props, $setup, $data, $options) {
  _push(`<div${ssrRenderAttrs(_attrs)}><h1 id="architecture" tabindex="-1">Architecture <a class="header-anchor" href="#architecture" aria-label="Permalink to &quot;Architecture&quot;">​</a></h1><h2 id="pipeline-value-objects" tabindex="-1">Pipeline &amp; Value Objects <a class="header-anchor" href="#pipeline-value-objects" aria-label="Permalink to &quot;Pipeline &amp; Value Objects&quot;">​</a></h2><p>The core of Open Ticket AI is its processing pipeline:</p><div class="language- vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang"></span><pre class="shiki shiki-themes github-light github-dark vp-code" tabindex="0"><code><span class="line"><span>[ Incoming Ticket ]</span></span>
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
<span class="line"><span>[ Ticket System Adapter ] — updates ticket via REST API</span></span></code></pre></div><p>Each stage in this pipeline consumes and produces <strong>Value Objects</strong> (e.g., <code>subject</code>, <code>body</code>, <code>queue_id</code>, <code>priority</code>). This design makes the pipeline modular and easy to extend with custom processing steps or new value objects.</p><h2 id="system-diagrams" tabindex="-1">System Diagrams <a class="header-anchor" href="#system-diagrams" aria-label="Permalink to &quot;System Diagrams&quot;">​</a></h2><h3 id="application-class-diagram" tabindex="-1">Application Class Diagram <a class="header-anchor" href="#application-class-diagram" aria-label="Permalink to &quot;Application Class Diagram&quot;">​</a></h3><h3 id="overview-diagram" tabindex="-1">Overview Diagram <a class="header-anchor" href="#overview-diagram" aria-label="Permalink to &quot;Overview Diagram&quot;">​</a></h3></div>`);
}
const _sfc_setup = _sfc_main.setup;
_sfc_main.setup = (props, ctx) => {
  const ssrContext = useSSRContext();
  (ssrContext.modules || (ssrContext.modules = /* @__PURE__ */ new Set())).add("en/concepts/pipeline-architecture.md");
  return _sfc_setup ? _sfc_setup(props, ctx) : void 0;
};
const pipelineArchitecture = /* @__PURE__ */ _export_sfc(_sfc_main, [["ssrRender", _sfc_ssrRender]]);
export {
  __pageData,
  pipelineArchitecture as default
};
