import { resolveComponent, useSSRContext } from "vue";
import { ssrRenderAttrs, ssrRenderStyle, ssrRenderComponent } from "vue/server-renderer";
import { _ as _export_sfc } from "./plugin-vue_export-helper.1tPrXgE0.js";
const __pageData = JSON.parse('{"title":"Documentation for **/ce/run/managers/*.py","description":"","frontmatter":{},"headers":[],"relativePath":"en/api/run/managers.md","filePath":"en/api/run/managers.md"}');
const _sfc_main = { name: "en/api/run/managers.md" };
function _sfc_ssrRender(_ctx, _push, _parent, _attrs, $props, $setup, $data, $options) {
  const _component_Badge = resolveComponent("Badge");
  _push(`<div${ssrRenderAttrs(_attrs)}><h1 id="documentation-for-ce-run-managers-py" tabindex="-1">Documentation for <code>**/ce/run/managers/*.py</code> <a class="header-anchor" href="#documentation-for-ce-run-managers-py" aria-label="Permalink to &quot;Documentation for \`**/ce/run/managers/*.py\`&quot;">​</a></h1><h2 id="module-open-ticket-ai-src-ce-run-managers-orchestrator-py" tabindex="-1">Module: <code>open_ticket_ai\\src\\ce\\run\\managers\\orchestrator.py</code> <a class="header-anchor" href="#module-open-ticket-ai-src-ce-run-managers-orchestrator-py" aria-label="Permalink to &quot;Module: \`open_ticket_ai\\src\\ce\\run\\managers\\orchestrator.py\`&quot;">​</a></h2><p>Top level orchestration utilities.</p><h3 id="class-orchestrator" tabindex="-1"><span style="${ssrRenderStyle({})}">class</span> <code>Orchestrator</code> <a class="header-anchor" href="#class-orchestrator" aria-label="Permalink to &quot;&lt;span style=&#39;text-info&#39;&gt;class&lt;/span&gt; \`Orchestrator\`&quot;">​</a></h3><p>Orchestrates the execution of ticket processing pipelines. This class manages the lifecycle of pipelines including:</p><ul><li>Pipeline instantiation via dependency injection</li><li>Individual ticket processing</li><li>Scheduled execution of pipelines</li></ul><p><strong>Parameters:</strong></p><ul><li><strong><code>config</code></strong> () - Configuration settings for the orchestrator</li><li><strong><code>container</code></strong> () - Dependency injection container providing pipeline instances</li><li><strong><code>_logger</code></strong> () - Logger instance for orchestration operations</li><li><strong><code>_pipelines</code></strong> () - Dictionary mapping pipeline IDs to pipeline instances</li></ul><details class="details custom-block"><summary>#### `);
  _push(ssrRenderComponent(_component_Badge, {
    type: "info",
    text: "method"
  }, null, _parent));
  _push(` <span class="text-warning">def</span> <code>__init__(self, config: OpenTicketAIConfig, container: AbstractContainer)</code></summary><p>Initialize the Orchestrator with configuration and DI container.</p><p><strong>Parameters:</strong></p><ul><li><strong><code>config</code></strong> () - Configuration settings for the orchestrator.</li><li><strong><code>container</code></strong> () - Dependency injection container providing pipeline instances.</li></ul></details><details class="details custom-block"><summary>#### `);
  _push(ssrRenderComponent(_component_Badge, {
    type: "info",
    text: "method"
  }, null, _parent));
  _push(` <span class="text-warning">def</span> <code>process_ticket(self, ticket_id: str, pipeline: Pipeline) -&gt; PipelineContext</code></summary><p>Executes a pipeline for a specific ticket. Creates a processing context and runs the specified pipeline to process the given ticket. This is the core method for individual ticket processing.</p><p><strong>Parameters:</strong></p><ul><li><strong><code>ticket_id</code></strong> () - Unique identifier of the ticket to process</li><li><strong><code>pipeline</code></strong> () - Pipeline instance to execute</li></ul><p><strong>Returns:</strong> (<code>PipelineContext</code>) - The execution context containing results and state after pipeline execution</p></details><details class="details custom-block"><summary>#### `);
  _push(ssrRenderComponent(_component_Badge, {
    type: "info",
    text: "method"
  }, null, _parent));
  _push(` <span class="text-warning">def</span> <code>build_pipelines(self) -&gt; None</code></summary><p>Instantiates all configured pipeline objects. Uses the dependency injection container to create pipeline instances based on the configuration. Populates the internal pipeline registry with pipeline ID to instance mappings.</p></details><details class="details custom-block"><summary>#### `);
  _push(ssrRenderComponent(_component_Badge, {
    type: "info",
    text: "method"
  }, null, _parent));
  _push(` <span class="text-warning">def</span> <code>set_schedules(self) -&gt; None</code></summary><p>Configures scheduled execution for all pipelines. Performs the following operations:</p><ol><li>Builds pipelines if not already instantiated</li><li>Configures periodic execution for each pipeline according to its schedule configuration using the <code>schedule</code> library</li></ol><p>The scheduling uses the following configuration parameters:</p><ul><li>interval: Numeric interval value</li><li>unit: Time unit (e.g., minutes, hours, days)</li></ul></details><hr></div>`);
}
const _sfc_setup = _sfc_main.setup;
_sfc_main.setup = (props, ctx) => {
  const ssrContext = useSSRContext();
  (ssrContext.modules || (ssrContext.modules = /* @__PURE__ */ new Set())).add("en/api/run/managers.md");
  return _sfc_setup ? _sfc_setup(props, ctx) : void 0;
};
const managers = /* @__PURE__ */ _export_sfc(_sfc_main, [["ssrRender", _sfc_ssrRender]]);
export {
  __pageData,
  managers as default
};
