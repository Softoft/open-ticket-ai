import { ssrRenderAttrs } from "vue/server-renderer";
import { useSSRContext } from "vue";
import { _ as _export_sfc } from "./plugin-vue_export-helper.1tPrXgE0.js";
const __pageData = JSON.parse('{"title":"Documentation for **/ce/core/config/**/*.py","description":"","frontmatter":{},"headers":[],"relativePath":"en/api/core/ce_core_config.md","filePath":"en/api/core/ce_core_config.md"}');
const _sfc_main = { name: "en/api/core/ce_core_config.md" };
function _sfc_ssrRender(_ctx, _push, _parent, _attrs, $props, $setup, $data, $options) {
  _push(`<div${ssrRenderAttrs(_attrs)}><h1 id="documentation-for-ce-core-config-py" tabindex="-1">Documentation for <code>**/ce/core/config/**/*.py</code> <a class="header-anchor" href="#documentation-for-ce-core-config-py" aria-label="Permalink to &quot;Documentation for \`**/ce/core/config/**/*.py\`&quot;">​</a></h1><h2 id="module-open-ticket-ai-src-ce-core-config-config-models-py" tabindex="-1">Module: <code>open_ticket_ai\\src\\ce\\core\\config\\config_models.py</code> <a class="header-anchor" href="#module-open-ticket-ai-src-ce-core-config-config-models-py" aria-label="Permalink to &quot;Module: \`open_ticket_ai\\src\\ce\\core\\config\\config_models.py\`&quot;">​</a></h2><hr><h2 id="module-open-ticket-ai-src-ce-core-config-config-validator-py" tabindex="-1">Module: <code>open_ticket_ai\\src\\ce\\core\\config\\config_validator.py</code> <a class="header-anchor" href="#module-open-ticket-ai-src-ce-core-config-config-validator-py" aria-label="Permalink to &quot;Module: \`open_ticket_ai\\src\\ce\\core\\config\\config_validator.py\`&quot;">​</a></h2><hr></div>`);
}
const _sfc_setup = _sfc_main.setup;
_sfc_main.setup = (props, ctx) => {
  const ssrContext = useSSRContext();
  (ssrContext.modules || (ssrContext.modules = /* @__PURE__ */ new Set())).add("en/api/core/ce_core_config.md");
  return _sfc_setup ? _sfc_setup(props, ctx) : void 0;
};
const ce_core_config = /* @__PURE__ */ _export_sfc(_sfc_main, [["ssrRender", _sfc_ssrRender]]);
export {
  __pageData,
  ce_core_config as default
};
