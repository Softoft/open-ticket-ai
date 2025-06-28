import { ssrRenderAttrs } from "vue/server-renderer";
import { useSSRContext } from "vue";
import { _ as _export_sfc } from "./plugin-vue_export-helper.1tPrXgE0.js";
const __pageData = JSON.parse('{"title":"Hardware Recommendations for Open Ticket AI","description":"Guidance on hardware for running Open Ticket AI.","frontmatter":{"title":"Hardware Recommendations for Open Ticket AI","description":"Guidance on hardware for running Open Ticket AI."},"headers":[],"relativePath":"en/guide/hardware-requirements.md","filePath":"en/guide/hardware-requirements.md"}');
const _sfc_main = { name: "en/guide/hardware-requirements.md" };
function _sfc_ssrRender(_ctx, _push, _parent, _attrs, $props, $setup, $data, $options) {
  _push(`<div${ssrRenderAttrs(_attrs)}><h1 id="hardware-recommendations" tabindex="-1">Hardware Recommendations <a class="header-anchor" href="#hardware-recommendations" aria-label="Permalink to &quot;Hardware Recommendations&quot;">​</a></h1><p>Choosing the right hardware is important for the performance of Open Ticket AI, especially when dealing with a large volume of tickets or using more complex models.</p><ul><li><strong>CPU-only</strong>: Sufficient for small volumes of tickets (e.g., &lt; 50 tickets per minute). Most modern server CPUs should handle this workload.</li><li><strong>GPU (Graphics Processing Unit)</strong>: Recommended for higher volumes (e.g., &gt; 100 tickets per minute) or when using larger, more computationally intensive models. NVIDIA RTX series GPUs are a common choice. <ul><li><strong>Examples</strong>: <ul><li>Hetzner Matrix GPU (which typically comes with ample vRAM)</li><li>AWS <code>g4ad.xlarge</code> instance or similar cloud GPU instances.</li></ul></li></ul></li></ul><h2 id="memory-ram" tabindex="-1">Memory (RAM) <a class="header-anchor" href="#memory-ram" aria-label="Permalink to &quot;Memory (RAM)&quot;">​</a></h2><p>Ensure you have enough RAM available for the models you intend to use. Refer to the <a href="./training-models.html#4-model-selection-hardware">Training the Model</a> section for examples of RAM requirements for specific models.</p><ul><li>For the default BERT models, you will generally need at least 4GB of RAM dedicated to the model, plus additional RAM for the operating system and the ticket system itself if they are running on the same host.</li></ul><h2 id="deployment-considerations" tabindex="-1">Deployment Considerations <a class="header-anchor" href="#deployment-considerations" aria-label="Permalink to &quot;Deployment Considerations&quot;">​</a></h2><ul><li><strong>Co-location vs. Separate Devices</strong>: You can run Open Ticket AI on the same server as your ticket system or on a separate machine.</li><li><strong>Network Configuration</strong>: If running on separate devices, ensure your network configuration allows communication between Open Ticket AI and your ticket system. You will need to adjust the <code>rest_settings</code> (specifically the <code>base_url</code>) in your <code>config.yml</code> to point to the correct network address of your ticket system&#39;s API.</li></ul></div>`);
}
const _sfc_setup = _sfc_main.setup;
_sfc_main.setup = (props, ctx) => {
  const ssrContext = useSSRContext();
  (ssrContext.modules || (ssrContext.modules = /* @__PURE__ */ new Set())).add("en/guide/hardware-requirements.md");
  return _sfc_setup ? _sfc_setup(props, ctx) : void 0;
};
const hardwareRequirements = /* @__PURE__ */ _export_sfc(_sfc_main, [["ssrRender", _sfc_ssrRender]]);
export {
  __pageData,
  hardwareRequirements as default
};
