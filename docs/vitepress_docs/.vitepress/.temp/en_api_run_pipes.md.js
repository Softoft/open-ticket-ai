import { resolveComponent, useSSRContext } from "vue";
import { ssrRenderAttrs, ssrRenderStyle, ssrRenderComponent } from "vue/server-renderer";
import { _ as _export_sfc } from "./plugin-vue_export-helper.1tPrXgE0.js";
const __pageData = JSON.parse('{"title":"Documentation for **/ce/run/pipe_implementations/*.py","description":"","frontmatter":{},"headers":[],"relativePath":"en/api/run/pipes.md","filePath":"en/api/run/pipes.md"}');
const _sfc_main = { name: "en/api/run/pipes.md" };
function _sfc_ssrRender(_ctx, _push, _parent, _attrs, $props, $setup, $data, $options) {
  const _component_Badge = resolveComponent("Badge");
  _push(`<div${ssrRenderAttrs(_attrs)}><h1 id="documentation-for-ce-run-pipe-implementations-py" tabindex="-1">Documentation for <code>**/ce/run/pipe_implementations/*.py</code> <a class="header-anchor" href="#documentation-for-ce-run-pipe-implementations-py" aria-label="Permalink to &quot;Documentation for \`**/ce/run/pipe_implementations/*.py\`&quot;">​</a></h1><h2 id="module-open-ticket-ai-src-ce-run-pipe-implementations-basic-ticket-fetcher-py" tabindex="-1">Module: <code>open_ticket_ai\\src\\ce\\run\\pipe_implementations\\basic_ticket_fetcher.py</code> <a class="header-anchor" href="#module-open-ticket-ai-src-ce-run-pipe-implementations-basic-ticket-fetcher-py" aria-label="Permalink to &quot;Module: \`open_ticket_ai\\src\\ce\\run\\pipe_implementations\\basic_ticket_fetcher.py\`&quot;">​</a></h2><h3 id="class-basicticketfetcher" tabindex="-1"><span style="${ssrRenderStyle({})}">class</span> <code>BasicTicketFetcher</code> <a class="header-anchor" href="#class-basicticketfetcher" aria-label="Permalink to &quot;&lt;span style=&#39;text-info&#39;&gt;class&lt;/span&gt; \`BasicTicketFetcher\`&quot;">​</a></h3><p>Simple fetcher that loads ticket data using the ticket system adapter. This pipe retrieves ticket information from an external ticket system using the provided adapter. It serves as a placeholder for more complex fetching implementations.</p><p><strong>Parameters:</strong></p><ul><li><strong><code>fetcher_config</code></strong> (<code>RegistryInstanceConfig</code>) - Configuration instance for the fetcher.</li><li><strong><code>ticket_system</code></strong> (<code>TicketSystemAdapter</code>) - Adapter for interacting with the ticket system.</li></ul><details class="details custom-block"><summary>#### `);
  _push(ssrRenderComponent(_component_Badge, {
    type: "info",
    text: "method"
  }, null, _parent));
  _push(` <span class="text-warning">def</span> <code>__init__(self, config: RegistryInstanceConfig, ticket_system: TicketSystemAdapter)</code></summary><p>Initializes the BasicTicketFetcher with configuration and ticket system adapter.</p><p><strong>Parameters:</strong></p><ul><li><strong><code>config</code></strong> (<code>RegistryInstanceConfig</code>) - The configuration instance for the fetcher.</li><li><strong><code>ticket_system</code></strong> (<code>TicketSystemAdapter</code>) - The adapter for interacting with the ticket system.</li></ul></details><details class="details custom-block"><summary>#### `);
  _push(ssrRenderComponent(_component_Badge, {
    type: "info",
    text: "method"
  }, null, _parent));
  _push(` <span class="text-warning">def</span> <code>process(self, context: PipelineContext) -&gt; PipelineContext</code></summary><p>Fetches ticket data and updates the pipeline context. Retrieves the ticket using the ticket ID from the context. If found, updates the context&#39;s data dictionary with the ticket information. If no ticket is found, the context remains unchanged.</p><p><strong>Parameters:</strong></p><ul><li><strong><code>context</code></strong> (<code>PipelineContext</code>) - The pipeline context containing the <code>ticket_id</code>.</li></ul><p><strong>Returns:</strong> (<code>PipelineContext</code>) - The context object. If a ticket was found, its <code>data</code> dictionary contains the ticket information. Otherwise, returns the original context.</p></details><details class="details custom-block"><summary>#### `);
  _push(ssrRenderComponent(_component_Badge, {
    type: "info",
    text: "method"
  }, null, _parent));
  _push(` <span class="text-warning">def</span> <code>get_description() -&gt; str</code></summary><p>Provides a static description of this pipe&#39;s functionality.</p><p><strong>Returns:</strong> (<code>str</code>) - A static description of the pipe&#39;s purpose and behavior.</p></details><hr><h2 id="module-open-ticket-ai-src-ce-run-pipe-implementations-generic-ticket-updater-py" tabindex="-1">Module: <code>open_ticket_ai\\src\\ce\\run\\pipe_implementations\\generic_ticket_updater.py</code> <a class="header-anchor" href="#module-open-ticket-ai-src-ce-run-pipe-implementations-generic-ticket-updater-py" aria-label="Permalink to &quot;Module: \`open_ticket_ai\\src\\ce\\run\\pipe_implementations\\generic_ticket_updater.py\`&quot;">​</a></h2><h3 id="class-genericticketupdater" tabindex="-1"><span style="${ssrRenderStyle({})}">class</span> <code>GenericTicketUpdater</code> <a class="header-anchor" href="#class-genericticketupdater" aria-label="Permalink to &quot;&lt;span style=&#39;text-info&#39;&gt;class&lt;/span&gt; \`GenericTicketUpdater\`&quot;">​</a></h3><p>Update a ticket in the ticket system using data from the context. This pipe component is responsible for updating tickets in an external ticket tracking system (like Jira, ServiceNow, etc.) using data generated during the pipeline execution. It checks the pipeline context for update instructions and delegates the actual update operation to the configured ticket system adapter.</p><p><strong>Parameters:</strong></p><ul><li><strong><code>modifier_config</code></strong> () - Configuration settings for the ticket updater.</li><li><strong><code>ticket_system</code></strong> () - Adapter instance for interacting with the external ticket system.</li></ul><details class="details custom-block"><summary>#### `);
  _push(ssrRenderComponent(_component_Badge, {
    type: "info",
    text: "method"
  }, null, _parent));
  _push(` <span class="text-warning">def</span> <code>__init__(self, config: RegistryInstanceConfig, ticket_system: TicketSystemAdapter)</code></summary><p>Initializes the <code>GenericTicketUpdater</code> with configuration and ticket system adapter.</p><p><strong>Parameters:</strong></p><ul><li><strong><code>config</code></strong> () - Configuration instance containing settings for the pipeline component.</li><li><strong><code>ticket_system</code></strong> () - Adapter object that handles communication with the external ticket system.</li></ul></details><details class="details custom-block"><summary>#### `);
  _push(ssrRenderComponent(_component_Badge, {
    type: "info",
    text: "method"
  }, null, _parent));
  _push(` <span class="text-warning">def</span> <code>process(self, context: PipelineContext) -&gt; PipelineContext</code></summary><p>Processes the pipeline context to update the ticket if update data exists. Retrieves update data from the context (specifically from the key <code>&quot;update_data&quot;</code> in <code>context.data</code>) and updates the ticket in the ticket system if update data is present. Returns the context unchanged.</p><p><strong>Parameters:</strong></p><ul><li><strong><code>context</code></strong> () - The pipeline context containing data and ticket information.</li></ul><p><strong>Returns:</strong> () - The original pipeline context after processing (unchanged).</p></details><details class="details custom-block"><summary>#### `);
  _push(ssrRenderComponent(_component_Badge, {
    type: "info",
    text: "method"
  }, null, _parent));
  _push(` <span class="text-warning">def</span> <code>get_description() -&gt; str</code></summary><p>Provides a description of the pipe&#39;s purpose.</p><p><strong>Returns:</strong> () - A string describing the pipe&#39;s functionality.</p></details><hr><h2 id="module-open-ticket-ai-src-ce-run-pipe-implementations-hf-local-ai-inference-service-py" tabindex="-1">Module: <code>open_ticket_ai\\src\\ce\\run\\pipe_implementations\\hf_local_ai_inference_service.py</code> <a class="header-anchor" href="#module-open-ticket-ai-src-ce-run-pipe-implementations-hf-local-ai-inference-service-py" aria-label="Permalink to &quot;Module: \`open_ticket_ai\\src\\ce\\run\\pipe_implementations\\hf_local_ai_inference_service.py\`&quot;">​</a></h2><h3 id="class-hfaiinferenceservice" tabindex="-1"><span style="${ssrRenderStyle({})}">class</span> <code>HFAIInferenceService</code> <a class="header-anchor" href="#class-hfaiinferenceservice" aria-label="Permalink to &quot;&lt;span style=&#39;text-info&#39;&gt;class&lt;/span&gt; \`HFAIInferenceService\`&quot;">​</a></h3><p>A class representing a Hugging Face AI model. This class is a placeholder for future implementation of Hugging Face AI model functionalities. Currently, it does not contain any methods or properties.</p><details class="details custom-block"><summary>#### `);
  _push(ssrRenderComponent(_component_Badge, {
    type: "info",
    text: "method"
  }, null, _parent));
  _push(` <span class="text-warning">def</span> <code>__init__(self, config: RegistryInstanceConfig)</code></summary><p>Initializes the HFAIInferenceService with configuration.</p><p><strong>Parameters:</strong></p><ul><li><strong><code>config</code></strong> (<code>RegistryInstanceConfig</code>) - Configuration instance for the service.</li></ul></details><details class="details custom-block"><summary>#### `);
  _push(ssrRenderComponent(_component_Badge, {
    type: "info",
    text: "method"
  }, null, _parent));
  _push(` <span class="text-warning">def</span> <code>process(self, context: PipelineContext) -&gt; PipelineContext</code></summary><p>Processes pipeline context by storing prepared data as model result. This method acts as a placeholder for actual model inference logic. Currently, it simply copies the &#39;prepared_data&#39; from the context to &#39;model_result&#39;.</p><p><strong>Parameters:</strong></p><ul><li><strong><code>context</code></strong> (<code>PipelineContext</code>) - The pipeline context containing data to process.</li></ul><p><strong>Returns:</strong> (<code>PipelineContext</code>) - The updated pipeline context with model result stored.</p></details><details class="details custom-block"><summary>#### `);
  _push(ssrRenderComponent(_component_Badge, {
    type: "info",
    text: "method"
  }, null, _parent));
  _push(` <span class="text-warning">def</span> <code>get_description() -&gt; str</code></summary><p>Provides a description of the service.</p><p><strong>Returns:</strong> (<code>str</code>) - Description text for the Hugging Face AI model service.</p></details><hr><h2 id="module-open-ticket-ai-src-ce-run-pipe-implementations-subject-body-preparer-py" tabindex="-1">Module: <code>open_ticket_ai\\src\\ce\\run\\pipe_implementations\\subject_body_preparer.py</code> <a class="header-anchor" href="#module-open-ticket-ai-src-ce-run-pipe-implementations-subject-body-preparer-py" aria-label="Permalink to &quot;Module: \`open_ticket_ai\\src\\ce\\run\\pipe_implementations\\subject_body_preparer.py\`&quot;">​</a></h2><h3 id="class-subjectbodypreparer" tabindex="-1"><span style="${ssrRenderStyle({})}">class</span> <code>SubjectBodyPreparer</code> <a class="header-anchor" href="#class-subjectbodypreparer" aria-label="Permalink to &quot;&lt;span style=&#39;text-info&#39;&gt;class&lt;/span&gt; \`SubjectBodyPreparer\`&quot;">​</a></h3><p>A pipeline component that prepares ticket subject and body content for processing. This pipe extracts the subject and body fields from ticket data, repeats the subject a configurable number of times, and concatenates it with the body content. The prepared data is stored in the pipeline context for downstream processing.</p><p><strong>Parameters:</strong></p><ul><li><strong><code>preparer_config</code></strong> (<code>RegistryInstanceConfig</code>) - Configuration parameters for the preparer.</li></ul><details class="details custom-block"><summary>#### `);
  _push(ssrRenderComponent(_component_Badge, {
    type: "info",
    text: "method"
  }, null, _parent));
  _push(` <span class="text-warning">def</span> <code>__init__(self, config: RegistryInstanceConfig)</code></summary><p>Initializes the SubjectBodyPreparer with configuration.</p><p><strong>Parameters:</strong></p><ul><li><strong><code>config</code></strong> (<code>RegistryInstanceConfig</code>) - Configuration parameters for the preparer.</li></ul></details><details class="details custom-block"><summary>#### `);
  _push(ssrRenderComponent(_component_Badge, {
    type: "info",
    text: "method"
  }, null, _parent));
  _push(` <span class="text-warning">def</span> <code>process(self, context: PipelineContext) -&gt; PipelineContext</code></summary><p>Processes ticket data to prepare subject and body content. Extracts subject and body fields from context data, repeats the subject as specified in configuration, and concatenates with the body. Stores the result in context under &#39;prepared_data&#39; key.</p><p><strong>Parameters:</strong></p><ul><li><strong><code>context</code></strong> (<code>PipelineContext</code>) - Pipeline context containing ticket data.</li></ul><p><strong>Returns:</strong> (<code>PipelineContext</code>) - Updated context with prepared data.</p></details><details class="details custom-block"><summary>#### `);
  _push(ssrRenderComponent(_component_Badge, {
    type: "info",
    text: "method"
  }, null, _parent));
  _push(` <span class="text-warning">def</span> <code>get_description() -&gt; str</code></summary><p>Provides a description of the pipe&#39;s functionality.</p><p><strong>Returns:</strong> (<code>str</code>) - Description of the pipe&#39;s purpose.</p></details><hr></div>`);
}
const _sfc_setup = _sfc_main.setup;
_sfc_main.setup = (props, ctx) => {
  const ssrContext = useSSRContext();
  (ssrContext.modules || (ssrContext.modules = /* @__PURE__ */ new Set())).add("en/api/run/pipes.md");
  return _sfc_setup ? _sfc_setup(props, ctx) : void 0;
};
const pipes = /* @__PURE__ */ _export_sfc(_sfc_main, [["ssrRender", _sfc_ssrRender]]);
export {
  __pageData,
  pipes as default
};
