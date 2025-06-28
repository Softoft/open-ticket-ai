import { ssrRenderAttrs, ssrRenderStyle } from "vue/server-renderer";
import { useSSRContext } from "vue";
import { _ as _export_sfc } from "./plugin-vue_export-helper.1tPrXgE0.js";
const __pageData = JSON.parse('{"title":"Getting Started","description":"Install Open Ticket AI and integrate it with your ticket system.","frontmatter":{"title":"Getting Started","description":"Install Open Ticket AI and integrate it with your ticket system."},"headers":[],"relativePath":"en/get-started.md","filePath":"en/get-started.md"}');
const _sfc_main = { name: "en/get-started.md" };
function _sfc_ssrRender(_ctx, _push, _parent, _attrs, $props, $setup, $data, $options) {
  _push(`<div${ssrRenderAttrs(_attrs)}><h1 id="installation" tabindex="-1">Installation <a class="header-anchor" href="#installation" aria-label="Permalink to &quot;Installation&quot;">​</a></h1><p>Open Ticket AI can be deployed quickly using Docker. Run the following command on your server to start the container:</p><div class="language-bash vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">bash</span><pre class="shiki shiki-themes github-light github-dark vp-code" tabindex="0"><code><span class="line"><span style="${ssrRenderStyle({ "--shiki-light": "#6F42C1", "--shiki-dark": "#B392F0" })}">docker</span><span style="${ssrRenderStyle({ "--shiki-light": "#032F62", "--shiki-dark": "#9ECBFF" })}"> run</span><span style="${ssrRenderStyle({ "--shiki-light": "#005CC5", "--shiki-dark": "#79B8FF" })}"> -d</span><span style="${ssrRenderStyle({ "--shiki-light": "#032F62", "--shiki-dark": "#9ECBFF" })}"> your-docker-repo/atc:latest</span></span></code></pre></div><p>This community edition does <strong>not</strong> provide a public REST API. Instead, all communication happens via your ticket system&#39;s Web Services.</p><h1 id="ticket-system-integration" tabindex="-1">Ticket System Integration <a class="header-anchor" href="#ticket-system-integration" aria-label="Permalink to &quot;Ticket System Integration&quot;">​</a></h1><p>Currently integrations are available for <strong>OTRS</strong>, <strong>OTOBO</strong>, and <strong>Znuny</strong>. The setup is identical for all three systems:</p><ol><li>Configure the necessary Web Services in your ticket system.</li><li>Create a dedicated user or agent for Open Ticket AI access.</li><li>Point the integration to the URL and credentials of that Web Service user.</li></ol><p>For detailed instructions, consult the corresponding getting started guides for your ticket system.</p></div>`);
}
const _sfc_setup = _sfc_main.setup;
_sfc_main.setup = (props, ctx) => {
  const ssrContext = useSSRContext();
  (ssrContext.modules || (ssrContext.modules = /* @__PURE__ */ new Set())).add("en/get-started.md");
  return _sfc_setup ? _sfc_setup(props, ctx) : void 0;
};
const getStarted = /* @__PURE__ */ _export_sfc(_sfc_main, [["ssrRender", _sfc_ssrRender]]);
export {
  __pageData,
  getStarted as default
};
