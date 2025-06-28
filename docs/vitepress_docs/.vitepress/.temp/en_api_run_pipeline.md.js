import { resolveComponent, useSSRContext } from "vue";
import { ssrRenderAttrs, ssrRenderStyle, ssrRenderComponent } from "vue/server-renderer";
import { _ as _export_sfc } from "./plugin-vue_export-helper.1tPrXgE0.js";
const __pageData = JSON.parse('{"title":"Documentation for **/ce/run/pipeline/*.py","description":"","frontmatter":{},"headers":[],"relativePath":"en/api/run/pipeline.md","filePath":"en/api/run/pipeline.md"}');
const _sfc_main = { name: "en/api/run/pipeline.md" };
function _sfc_ssrRender(_ctx, _push, _parent, _attrs, $props, $setup, $data, $options) {
  const _component_Badge = resolveComponent("Badge");
  _push(`<div${ssrRenderAttrs(_attrs)}><h1 id="documentation-for-ce-run-pipeline-py" tabindex="-1">Documentation for <code>**/ce/run/pipeline/*.py</code> <a class="header-anchor" href="#documentation-for-ce-run-pipeline-py" aria-label="Permalink to &quot;Documentation for \`**/ce/run/pipeline/*.py\`&quot;">​</a></h1><h2 id="module-open-ticket-ai-src-ce-run-pipeline-context-py" tabindex="-1">Module: <code>open_ticket_ai\\src\\ce\\run\\pipeline\\context.py</code> <a class="header-anchor" href="#module-open-ticket-ai-src-ce-run-pipeline-context-py" aria-label="Permalink to &quot;Module: \`open_ticket_ai\\src\\ce\\run\\pipeline\\context.py\`&quot;">​</a></h2><h3 id="class-pipelinecontext" tabindex="-1"><span style="${ssrRenderStyle({})}">class</span> <code>PipelineContext</code> <a class="header-anchor" href="#class-pipelinecontext" aria-label="Permalink to &quot;&lt;span style=&#39;text-info&#39;&gt;class&lt;/span&gt; \`PipelineContext\`&quot;">​</a></h3><p>Context object passed between pipeline stages. This class serves as a container for sharing state and data across different stages of a processing pipeline. It uses Pydantic for data validation and serialization.</p><p><strong>Parameters:</strong></p><ul><li><strong><code>ticket_id</code></strong> (<code>str</code>) - The unique identifier of the ticket being processed through the pipeline stages.</li><li><strong><code>data</code></strong> (<code>dict[str, Any]</code>) - A flexible dictionary for storing arbitrary data exchanged between pipeline stages. Defaults to an empty dictionary.</li></ul><hr><h2 id="module-open-ticket-ai-src-ce-run-pipeline-pipe-py" tabindex="-1">Module: <code>open_ticket_ai\\src\\ce\\run\\pipeline\\pipe.py</code> <a class="header-anchor" href="#module-open-ticket-ai-src-ce-run-pipeline-pipe-py" aria-label="Permalink to &quot;Module: \`open_ticket_ai\\src\\ce\\run\\pipeline\\pipe.py\`&quot;">​</a></h2><h3 id="class-pipe" tabindex="-1"><span style="${ssrRenderStyle({})}">class</span> <code>Pipe</code> <a class="header-anchor" href="#class-pipe" aria-label="Permalink to &quot;&lt;span style=&#39;text-info&#39;&gt;class&lt;/span&gt; \`Pipe\`&quot;">​</a></h3><p>Interface for all pipeline components. This abstract base class defines the common interface that all pipeline components must implement. It inherits from <code>RegistryProvidableInstance</code> to enable automatic registration in a component registry and from <code>ABC</code> to enforce abstract method implementation.</p><p>Subclasses must implement the <code>process</code> method to define their specific data transformation logic within the pipeline.</p><p>Attributes: Inherits attributes from <code>RegistryProvidableInstance</code> for registry management.</p><details class="details custom-block"><summary>#### `);
  _push(ssrRenderComponent(_component_Badge, {
    type: "info",
    text: "method"
  }, null, _parent));
  _push(` <span class="text-warning">def</span> <code>process(self, context: PipelineContext) -&gt; PipelineContext</code></summary><p>Process a pipeline context object and return the modified context. This method defines the core processing logic for a pipeline component. It takes a <code>PipelineContext</code> object containing shared pipeline state, performs transformations or operations on this context, and returns the updated context for the next component in the pipeline.</p><p>Args: context: The current pipeline context containing shared state data.</p><p>Returns: The updated <code>PipelineContext</code> object after processing.</p><p>Raises: Implementation-specific exceptions may be raised by subclasses to indicate processing errors or invalid states.</p></details><hr><h2 id="module-open-ticket-ai-src-ce-run-pipeline-pipeline-py" tabindex="-1">Module: <code>open_ticket_ai\\src\\ce\\run\\pipeline\\pipeline.py</code> <a class="header-anchor" href="#module-open-ticket-ai-src-ce-run-pipeline-pipeline-py" aria-label="Permalink to &quot;Module: \`open_ticket_ai\\src\\ce\\run\\pipeline\\pipeline.py\`&quot;">​</a></h2><h3 id="class-pipeline" tabindex="-1"><span style="${ssrRenderStyle({})}">class</span> <code>Pipeline</code> <a class="header-anchor" href="#class-pipeline" aria-label="Permalink to &quot;&lt;span style=&#39;text-info&#39;&gt;class&lt;/span&gt; \`Pipeline\`&quot;">​</a></h3><p>Composite pipe executing a sequence of pipes. The Pipeline class represents a composite pipe that executes a sequence of individual pipes in a defined order. It implements the Pipe interface and processes data by sequentially passing a context object through each component pipe.</p><p><strong>Parameters:</strong></p><ul><li><strong><code>pipes</code></strong> () - An ordered list of Pipe instances to execute sequentially.</li></ul><details class="details custom-block"><summary>#### `);
  _push(ssrRenderComponent(_component_Badge, {
    type: "info",
    text: "method"
  }, null, _parent));
  _push(` <span class="text-warning">def</span> <code>__init__(self, config: PipelineConfig, pipes: List[Pipe])</code></summary><p>Initializes the Pipeline with configuration and component pipes.</p><p><strong>Parameters:</strong></p><ul><li><strong><code>config</code></strong> () - Configuration settings for the pipeline.</li><li><strong><code>pipes</code></strong> () - Ordered list of Pipe instances to execute sequentially.</li></ul></details><details class="details custom-block"><summary>#### `);
  _push(ssrRenderComponent(_component_Badge, {
    type: "info",
    text: "method"
  }, null, _parent));
  _push(` <span class="text-warning">def</span> <code>execute(self, context: PipelineContext) -&gt; PipelineContext</code></summary><p>Executes all pipes in the pipeline sequentially. Processes the context through each pipe in the defined order, passing the output of one pipe as input to the next.</p><p><strong>Parameters:</strong></p><ul><li><strong><code>context</code></strong> () - The initial pipeline context containing data to process.</li></ul><p><strong>Returns:</strong> () - The final context after processing through all pipes.</p></details><details class="details custom-block"><summary>#### `);
  _push(ssrRenderComponent(_component_Badge, {
    type: "info",
    text: "method"
  }, null, _parent));
  _push(` <span class="text-warning">def</span> <code>process(self, context: PipelineContext) -&gt; PipelineContext</code></summary><p>Processes context through the entire pipeline. This method implements the Pipe interface by delegating to execute().</p><p><strong>Parameters:</strong></p><ul><li><strong><code>context</code></strong> () - The pipeline context to process.</li></ul><p><strong>Returns:</strong> () - The modified context after pipeline execution.</p></details><hr></div>`);
}
const _sfc_setup = _sfc_main.setup;
_sfc_main.setup = (props, ctx) => {
  const ssrContext = useSSRContext();
  (ssrContext.modules || (ssrContext.modules = /* @__PURE__ */ new Set())).add("en/api/run/pipeline.md");
  return _sfc_setup ? _sfc_setup(props, ctx) : void 0;
};
const pipeline = /* @__PURE__ */ _export_sfc(_sfc_main, [["ssrRender", _sfc_ssrRender]]);
export {
  __pageData,
  pipeline as default
};
