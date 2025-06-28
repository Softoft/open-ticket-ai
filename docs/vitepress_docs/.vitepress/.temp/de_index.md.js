import { resolveComponent, useSSRContext } from "vue";
import { ssrRenderAttrs, ssrRenderComponent } from "vue/server-renderer";
import { _ as _export_sfc } from "./plugin-vue_export-helper.1tPrXgE0.js";
const __pageData = JSON.parse('{"title":"","description":"","frontmatter":{"layout":"home","hero":{"name":"Open Ticket AI","text":"","tagline":"Sparen Sie Zeit und Geld durch Automatisierung","image":{"light":"https://softoft.sirv.com/Images/atc-logo-2024-blue.png?w=300&q=100","dark":"https://softoft.sirv.com/Images/atc-logo-2024-blue.png?w=300&q=100","alt":"VitePress"},"actions":[{"theme":"brand","text":"Loslegen","link":"/get-started"},{"theme":"alt","text":"Funktionsübersicht","link":"/concepts/community-edition-overview"}]},"features":[{"title":"Einfache Installation","details":"Installieren Sie ATC einfach mit Docker auf Ihrem Server.","icon":{"light":"https://softoft.sirv.com/Images/otobo/docs/custom/icons/server-solid.png?h=48&q=100","dark":"https://softoft.sirv.com/Images/otobo/docs/custom/icons/server-solid.png?h=48&q=100&colorlevel.white=0","height":48,"width":"auto","alt":"OTOBO ATC AI Icon"}},{"title":"Leistungsstarke API","details":"Nutzen Sie die HTTP REST API für die Datenübertragung und Modellverwaltung.","icon":{"light":"https://softoft.sirv.com/Images/otobo/docs/custom/icons/code-solid.png?h=48&q=100","dark":"https://softoft.sirv.com/Images/otobo/docs/custom/icons/code-solid.png?h=48&q=100&colorlevel.white=0","height":48,"width":"auto","alt":"OTOBO ATC AI Icon"}},{"title":"OTOBO Integration","details":"Verwenden Sie das ATC Add-On für nahtlose Integration in OTOBO.","icon":{"light":"https://softoft.sirv.com/Images/otobo/docs/custom/icons/plug-solid.png?h=48&q=100","dark":"https://softoft.sirv.com/Images/otobo/docs/custom/icons/plug-solid.png?h=48&q=100&colorlevel.white=0","height":48,"width":"auto","alt":"OTOBO ATC AI Icon"}},{"title":"Automatisierte Klassifizierung","details":"Automatisieren Sie die Klassifizierung von Support-Tickets.","icon":{"light":"https://softoft.sirv.com/Images/otobo/docs/custom/icons/robot-solid.png?h=48&q=100","dark":"https://softoft.sirv.com/Images/otobo/docs/custom/icons/robot-solid.png?h=48&q=100&colorlevel.white=0","height":48,"width":"auto","alt":"OTOBO ATC AI Icon"}},{"title":"Hohe Sicherheit","details":"Alle Daten werden lokal verarbeitet, um Datenschutz zu gewährleisten.","icon":{"light":"https://softoft.sirv.com/Images/otobo/docs/custom/icons/lock-solid.png?h=48&q=100","dark":"https://softoft.sirv.com/Images/otobo/docs/custom/icons/lock-solid.png?h=48&q=100&colorlevel.white=0","height":48,"width":"auto","alt":"OTOBO ATC AI Icon"}},{"title":"Flexibilität","details":"Passen Sie die Konfiguration nach Ihren Bedürfnissen an.","icon":{"light":"https://softoft.sirv.com/Images/otobo/docs/custom/icons/gear-solid.png?h=48&q=100","dark":"https://softoft.sirv.com/Images/otobo/docs/custom/icons/gear-solid.png?h=48&q=100&colorlevel.white=0","height":48,"width":"auto","alt":"OTOBO ATC AI Icon"}}]},"headers":[],"relativePath":"de/index.md","filePath":"de/index.md"}');
const _sfc_main = { name: "de/index.md" };
function _sfc_ssrRender(_ctx, _push, _parent, _attrs, $props, $setup, $data, $options) {
  const _component_OTAIPredictionDemo = resolveComponent("OTAIPredictionDemo");
  const _component_ServicePackagesComponent = resolveComponent("ServicePackagesComponent");
  const _component_SupportPlansComponent = resolveComponent("SupportPlansComponent");
  _push(`<div${ssrRenderAttrs(_attrs)}>`);
  _push(ssrRenderComponent(_component_OTAIPredictionDemo, null, null, _parent));
  _push(ssrRenderComponent(_component_ServicePackagesComponent, null, null, _parent));
  _push(ssrRenderComponent(_component_SupportPlansComponent, null, null, _parent));
  _push(`<h2 id="kontakt" tabindex="-1">Kontakt <a class="header-anchor" href="#kontakt" aria-label="Permalink to &quot;Kontakt&quot;">​</a></h2><div class="text-center mt-8"><p class="text-lg font-semibold">Interessiert an unseren Dienstleistungen?</p><p class="text-gray-600">Kontaktieren Sie uns für ein persönliches Angebot.</p><a href="mailto:sales@softoft.de" class="mt-4 inline-block bg-blue-600 text-white px-6 py-3 rounded hover:bg-blue-700 transition-colors"> Senden Sie uns eine E-Mail an sales@softoft.de </a></div></div>`);
}
const _sfc_setup = _sfc_main.setup;
_sfc_main.setup = (props, ctx) => {
  const ssrContext = useSSRContext();
  (ssrContext.modules || (ssrContext.modules = /* @__PURE__ */ new Set())).add("de/index.md");
  return _sfc_setup ? _sfc_setup(props, ctx) : void 0;
};
const index = /* @__PURE__ */ _export_sfc(_sfc_main, [["ssrRender", _sfc_ssrRender]]);
export {
  __pageData,
  index as default
};
