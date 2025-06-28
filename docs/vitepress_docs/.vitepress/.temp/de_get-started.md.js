import { ssrRenderAttrs, ssrRenderStyle } from "vue/server-renderer";
import { useSSRContext } from "vue";
import { _ as _export_sfc } from "./plugin-vue_export-helper.1tPrXgE0.js";
const __pageData = JSON.parse('{"title":"Erste Schritte","description":"Installieren Sie Open Ticket AI und integrieren Sie es in Ihr Ticketsystem.","frontmatter":{"title":"Erste Schritte","description":"Installieren Sie Open Ticket AI und integrieren Sie es in Ihr Ticketsystem."},"headers":[],"relativePath":"de/get-started.md","filePath":"de/get-started.md"}');
const _sfc_main = { name: "de/get-started.md" };
function _sfc_ssrRender(_ctx, _push, _parent, _attrs, $props, $setup, $data, $options) {
  _push(`<div${ssrRenderAttrs(_attrs)}><h1 id="installation" tabindex="-1">Installation <a class="header-anchor" href="#installation" aria-label="Permalink to &quot;Installation&quot;">​</a></h1><p>Open Ticket AI kann schnell mit Docker bereitgestellt werden. Führen Sie den folgenden Befehl auf Ihrem Server aus, um den Container zu starten:</p><div class="language-bash vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">bash</span><pre class="shiki shiki-themes github-light github-dark vp-code" tabindex="0"><code><span class="line"><span style="${ssrRenderStyle({ "--shiki-light": "#6F42C1", "--shiki-dark": "#B392F0" })}">docker</span><span style="${ssrRenderStyle({ "--shiki-light": "#032F62", "--shiki-dark": "#9ECBFF" })}"> run</span><span style="${ssrRenderStyle({ "--shiki-light": "#005CC5", "--shiki-dark": "#79B8FF" })}"> -d</span><span style="${ssrRenderStyle({ "--shiki-light": "#032F62", "--shiki-dark": "#9ECBFF" })}"> your-docker-repo/atc:latest</span></span></code></pre></div><p>Diese Community-Edition stellt <strong>keine</strong> öffentliche REST-API zur Verfügung. Stattdessen findet die gesamte Kommunikation über die Web Services Ihres Ticketsystems statt.</p><h1 id="ticketsystem-integration" tabindex="-1">Ticketsystem-Integration <a class="header-anchor" href="#ticketsystem-integration" aria-label="Permalink to &quot;Ticketsystem-Integration&quot;">​</a></h1><p>Derzeit sind Integrationen für <strong>OTRS</strong>, <strong>OTOBO</strong> und <strong>Znuny</strong> verfügbar. Die Einrichtung ist für alle drei Systeme identisch:</p><ol><li>Konfigurieren Sie die erforderlichen Web Services in Ihrem Ticketsystem.</li><li>Erstellen Sie einen dedizierten Benutzer oder Agenten für den Zugriff durch Open Ticket AI.</li><li>Richten Sie die Integration auf die URL und die Anmeldedaten dieses Web-Service-Benutzers aus.</li></ol><p>Detaillierte Anweisungen finden Sie in den entsprechenden Anleitungen für die ersten Schritte für Ihr Ticketsystem.</p></div>`);
}
const _sfc_setup = _sfc_main.setup;
_sfc_main.setup = (props, ctx) => {
  const ssrContext = useSSRContext();
  (ssrContext.modules || (ssrContext.modules = /* @__PURE__ */ new Set())).add("de/get-started.md");
  return _sfc_setup ? _sfc_setup(props, ctx) : void 0;
};
const getStarted = /* @__PURE__ */ _export_sfc(_sfc_main, [["ssrRender", _sfc_ssrRender]]);
export {
  __pageData,
  getStarted as default
};
