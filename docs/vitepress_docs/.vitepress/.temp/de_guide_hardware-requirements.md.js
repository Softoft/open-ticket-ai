import { ssrRenderAttrs } from "vue/server-renderer";
import { useSSRContext } from "vue";
import { _ as _export_sfc } from "./plugin-vue_export-helper.1tPrXgE0.js";
const __pageData = JSON.parse('{"title":"Hardware-Empfehlungen für Open Ticket AI","description":"Leitfaden zur Hardware für den Betrieb von Open Ticket AI.","frontmatter":{"title":"Hardware-Empfehlungen für Open Ticket AI","description":"Leitfaden zur Hardware für den Betrieb von Open Ticket AI."},"headers":[],"relativePath":"de/guide/hardware-requirements.md","filePath":"de/guide/hardware-requirements.md"}');
const _sfc_main = { name: "de/guide/hardware-requirements.md" };
function _sfc_ssrRender(_ctx, _push, _parent, _attrs, $props, $setup, $data, $options) {
  _push(`<div${ssrRenderAttrs(_attrs)}><h1 id="hardware-empfehlungen" tabindex="-1">Hardware-Empfehlungen <a class="header-anchor" href="#hardware-empfehlungen" aria-label="Permalink to &quot;Hardware-Empfehlungen&quot;">​</a></h1><p>Die Wahl der richtigen Hardware ist wichtig für die Leistung von Open Ticket AI, insbesondere bei einem großen Ticketaufkommen oder bei der Verwendung komplexerer Modelle.</p><ul><li><strong>Nur CPU</strong>: Ausreichend für geringe Ticketvolumen (z. B. &lt; 50 Tickets pro Minute). Die meisten modernen Server-CPUs sollten diese Arbeitslast bewältigen können.</li><li><strong>GPU (Graphics Processing Unit)</strong>: Empfohlen für höhere Volumen (z. B. &gt; 100 Tickets pro Minute) oder bei der Verwendung größerer, rechenintensiverer Modelle. GPUs der NVIDIA RTX-Serie sind eine gängige Wahl. <ul><li><strong>Beispiele</strong>: <ul><li>Hetzner Matrix GPU (die typischerweise mit reichlich vRAM ausgestattet ist)</li><li>AWS <code>g4ad.xlarge</code>-Instanz oder ähnliche Cloud-GPU-Instanzen.</li></ul></li></ul></li></ul><h2 id="arbeitsspeicher-ram" tabindex="-1">Arbeitsspeicher (RAM) <a class="header-anchor" href="#arbeitsspeicher-ram" aria-label="Permalink to &quot;Arbeitsspeicher (RAM)&quot;">​</a></h2><p>Stellen Sie sicher, dass Sie genügend RAM für die Modelle zur Verfügung haben, die Sie verwenden möchten. Beispiele für RAM-Anforderungen für bestimmte Modelle finden Sie im Abschnitt <a href="./training-models.html#4-model-selection-hardware">Training des Modells</a>.</p><ul><li>Für die standardmäßigen BERT-Modelle benötigen Sie in der Regel mindestens 4 GB RAM für das Modell, plus zusätzlichen RAM für das Betriebssystem und das Ticketsystem selbst, wenn diese auf demselben Host laufen.</li></ul><h2 id="uberlegungen-zur-bereitstellung" tabindex="-1">Überlegungen zur Bereitstellung <a class="header-anchor" href="#uberlegungen-zur-bereitstellung" aria-label="Permalink to &quot;Überlegungen zur Bereitstellung&quot;">​</a></h2><ul><li><strong>Co-Location vs. separate Geräte</strong>: Sie können Open Ticket AI auf demselben Server wie Ihr Ticketsystem oder auf einer separaten Maschine ausführen.</li><li><strong>Netzwerkkonfiguration</strong>: Wenn Sie die Anwendung auf separaten Geräten ausführen, stellen Sie sicher, dass Ihre Netzwerkkonfiguration die Kommunikation zwischen Open Ticket AI und Ihrem Ticketsystem ermöglicht. Sie müssen die <code>rest_settings</code> (insbesondere die <code>base_url</code>) in Ihrer <code>config.yml</code> anpassen, damit sie auf die korrekte Netzwerkadresse der API Ihres Ticketsystems verweist.</li></ul></div>`);
}
const _sfc_setup = _sfc_main.setup;
_sfc_main.setup = (props, ctx) => {
  const ssrContext = useSSRContext();
  (ssrContext.modules || (ssrContext.modules = /* @__PURE__ */ new Set())).add("de/guide/hardware-requirements.md");
  return _sfc_setup ? _sfc_setup(props, ctx) : void 0;
};
const hardwareRequirements = /* @__PURE__ */ _export_sfc(_sfc_main, [["ssrRender", _sfc_ssrRender]]);
export {
  __pageData,
  hardwareRequirements as default
};
