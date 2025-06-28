import { ssrRenderAttrs, ssrRenderStyle } from "vue/server-renderer";
import { useSSRContext } from "vue";
import { _ as _export_sfc } from "./plugin-vue_export-helper.1tPrXgE0.js";
const __pageData = JSON.parse('{"title":"Verwendung von Open Ticket AI","description":"Wie man Open Ticket AI zur Ticket-Klassifizierung ausführt und verwendet.","frontmatter":{"title":"Verwendung von Open Ticket AI","description":"Wie man Open Ticket AI zur Ticket-Klassifizierung ausführt und verwendet."},"headers":[],"relativePath":"de/guide/running-classifier.md","filePath":"de/guide/running-classifier.md"}');
const _sfc_main = { name: "de/guide/running-classifier.md" };
function _sfc_ssrRender(_ctx, _push, _parent, _attrs, $props, $setup, $data, $options) {
  _push(`<div${ssrRenderAttrs(_attrs)}><h1 id="verwendung" tabindex="-1">Verwendung <a class="header-anchor" href="#verwendung" aria-label="Permalink to &quot;Verwendung&quot;">​</a></h1><p>Dieser Abschnitt beschreibt, wie man Open Ticket AI für seine Hauptfunktion ausführt: die Klassifizierung von Tickets.</p><h2 id="inferenz-ausfuhren" tabindex="-1">Inferenz ausführen <a class="header-anchor" href="#inferenz-ausfuhren" aria-label="Permalink to &quot;Inferenz ausführen&quot;">​</a></h2><p>Sobald Open Ticket AI installiert und konfiguriert ist, können Sie den Klassifizierungsprozess mit Docker Compose starten:</p><div class="language-bash vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">bash</span><pre class="shiki shiki-themes github-light github-dark vp-code" tabindex="0"><code><span class="line"><span style="${ssrRenderStyle({ "--shiki-light": "#6F42C1", "--shiki-dark": "#B392F0" })}">docker-compose</span><span style="${ssrRenderStyle({ "--shiki-light": "#032F62", "--shiki-dark": "#9ECBFF" })}"> up</span><span style="${ssrRenderStyle({ "--shiki-light": "#032F62", "--shiki-dark": "#9ECBFF" })}"> classifier</span></span></code></pre></div><p>Dieser Befehl startet die erforderlichen Dienste, typischerweise einschließlich:</p><ul><li><strong>Queue Worker</strong>: Ruft Tickets ab, verwendet das konfigurierte Modell, um die passende Warteschlange vorherzusagen, und aktualisiert dann das Ticket in Ihrem System (z. B. verschiebt es in die vorhergesagte Warteschlange oder markiert es basierend auf Konfidenzniveaus).</li><li><strong>Priority Worker</strong>: Ähnlich wie der Queue Worker, konzentriert sich aber auf die Vorhersage und Zuweisung der Ticket-Priorität.</li></ul><p>Diese Worker überwachen kontinuierlich die eingehende Warteschlange (wie in Ihrer <code>config.yml</code> definiert) und verarbeiten neue Tickets, sobald sie eintreffen.</p><p><em>(Hinweis: Die genauen Dienstnamen und das Verhalten können je nach Ihrer spezifischen Konfiguration und Version von Open Ticket AI variieren.)</em></p></div>`);
}
const _sfc_setup = _sfc_main.setup;
_sfc_main.setup = (props, ctx) => {
  const ssrContext = useSSRContext();
  (ssrContext.modules || (ssrContext.modules = /* @__PURE__ */ new Set())).add("de/guide/running-classifier.md");
  return _sfc_setup ? _sfc_setup(props, ctx) : void 0;
};
const runningClassifier = /* @__PURE__ */ _export_sfc(_sfc_main, [["ssrRender", _sfc_ssrRender]]);
export {
  __pageData,
  runningClassifier as default
};
