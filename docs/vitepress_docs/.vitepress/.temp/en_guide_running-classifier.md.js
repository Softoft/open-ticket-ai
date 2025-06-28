import { ssrRenderAttrs, ssrRenderStyle } from "vue/server-renderer";
import { useSSRContext } from "vue";
import { _ as _export_sfc } from "./plugin-vue_export-helper.1tPrXgE0.js";
const __pageData = JSON.parse('{"title":"Using Open Ticket AI","description":"How to run and use Open Ticket AI for ticket classification.","frontmatter":{"title":"Using Open Ticket AI","description":"How to run and use Open Ticket AI for ticket classification."},"headers":[],"relativePath":"en/guide/running-classifier.md","filePath":"en/guide/running-classifier.md"}');
const _sfc_main = { name: "en/guide/running-classifier.md" };
function _sfc_ssrRender(_ctx, _push, _parent, _attrs, $props, $setup, $data, $options) {
  _push(`<div${ssrRenderAttrs(_attrs)}><h1 id="usage" tabindex="-1">Usage <a class="header-anchor" href="#usage" aria-label="Permalink to &quot;Usage&quot;">​</a></h1><p>This section describes how to run Open Ticket AI for its primary function: classifying tickets.</p><h2 id="run-inference" tabindex="-1">Run Inference <a class="header-anchor" href="#run-inference" aria-label="Permalink to &quot;Run Inference&quot;">​</a></h2><p>Once Open Ticket AI is installed and configured, you can start the classification process using Docker Compose:</p><div class="language-bash vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">bash</span><pre class="shiki shiki-themes github-light github-dark vp-code" tabindex="0"><code><span class="line"><span style="${ssrRenderStyle({ "--shiki-light": "#6F42C1", "--shiki-dark": "#B392F0" })}">docker-compose</span><span style="${ssrRenderStyle({ "--shiki-light": "#032F62", "--shiki-dark": "#9ECBFF" })}"> up</span><span style="${ssrRenderStyle({ "--shiki-light": "#032F62", "--shiki-dark": "#9ECBFF" })}"> classifier</span></span></code></pre></div><p>This command starts the necessary services, typically including:</p><ul><li><strong>Queue Worker</strong>: Fetches tickets, uses the configured model to predict the appropriate queue, and then updates the ticket in your system (e.g., moves it to the predicted queue or flags it based on confidence levels).</li><li><strong>Priority Worker</strong>: Similar to the Queue Worker, but focuses on predicting and assigning ticket priority.</li></ul><p>These workers will continuously monitor the incoming queue (as defined in your <code>config.yml</code>) and process new tickets as they arrive.</p><p><em>(Note: The exact service names and behavior might vary based on your specific configuration and version of Open Ticket AI.)</em></p></div>`);
}
const _sfc_setup = _sfc_main.setup;
_sfc_main.setup = (props, ctx) => {
  const ssrContext = useSSRContext();
  (ssrContext.modules || (ssrContext.modules = /* @__PURE__ */ new Set())).add("en/guide/running-classifier.md");
  return _sfc_setup ? _sfc_setup(props, ctx) : void 0;
};
const runningClassifier = /* @__PURE__ */ _export_sfc(_sfc_main, [["ssrRender", _sfc_ssrRender]]);
export {
  __pageData,
  runningClassifier as default
};
