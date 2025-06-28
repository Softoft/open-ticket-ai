import { resolveComponent, useSSRContext } from "vue";
import { ssrRenderAttrs, ssrRenderStyle, ssrRenderComponent } from "vue/server-renderer";
import { _ as _export_sfc } from "./plugin-vue_export-helper.1tPrXgE0.js";
const __pageData = JSON.parse('{"title":"Documentation for **/ce/core/mixins/**/*.py","description":"","frontmatter":{},"headers":[],"relativePath":"en/api/core/mixins.md","filePath":"en/api/core/mixins.md"}');
const _sfc_main = { name: "en/api/core/mixins.md" };
function _sfc_ssrRender(_ctx, _push, _parent, _attrs, $props, $setup, $data, $options) {
  const _component_Badge = resolveComponent("Badge");
  _push(`<div${ssrRenderAttrs(_attrs)}><h1 id="documentation-for-ce-core-mixins-py" tabindex="-1">Documentation for <code>**/ce/core/mixins/**/*.py</code> <a class="header-anchor" href="#documentation-for-ce-core-mixins-py" aria-label="Permalink to &quot;Documentation for \`**/ce/core/mixins/**/*.py\`&quot;">​</a></h1><h2 id="module-open-ticket-ai-src-ce-core-mixins-registry-instance-config-py" tabindex="-1">Module: <code>open_ticket_ai\\src\\ce\\core\\mixins\\registry_instance_config.py</code> <a class="header-anchor" href="#module-open-ticket-ai-src-ce-core-mixins-registry-instance-config-py" aria-label="Permalink to &quot;Module: \`open_ticket_ai\\src\\ce\\core\\mixins\\registry_instance_config.py\`&quot;">​</a></h2><h3 id="class-registryinstanceconfig" tabindex="-1"><span style="${ssrRenderStyle({})}">class</span> <code>RegistryInstanceConfig</code> <a class="header-anchor" href="#class-registryinstanceconfig" aria-label="Permalink to &quot;&lt;span style=&#39;text-info&#39;&gt;class&lt;/span&gt; \`RegistryInstanceConfig\`&quot;">​</a></h3><p>Base configuration for registry instances. This class defines the core configuration structure required for initializing and managing registry instances. Each registry instance must have a unique identifier, a provider key, and can include additional provider-specific parameters.</p><p><strong>Parameters:</strong></p><ul><li><strong><code>id</code></strong> () - A unique string identifier for the registry instance. Must be at least 1 character long.</li><li><strong><code>params</code></strong> () - A dictionary of additional configuration parameters specific to the registry provider. Defaults to an empty dictionary.</li><li><strong><code>provider_key</code></strong> () - A string key identifying the provider implementation for this registry instance. Must be at least 1 character long.</li></ul><hr><h2 id="module-open-ticket-ai-src-ce-core-mixins-registry-providable-instance-py" tabindex="-1">Module: <code>open_ticket_ai\\src\\ce\\core\\mixins\\registry_providable_instance.py</code> <a class="header-anchor" href="#module-open-ticket-ai-src-ce-core-mixins-registry-providable-instance-py" aria-label="Permalink to &quot;Module: \`open_ticket_ai\\src\\ce\\core\\mixins\\registry_providable_instance.py\`&quot;">​</a></h2><h3 id="class-registryprovidableinstance" tabindex="-1"><span style="${ssrRenderStyle({})}">class</span> <code>RegistryProvidableInstance</code> <a class="header-anchor" href="#class-registryprovidableinstance" aria-label="Permalink to &quot;&lt;span style=&#39;text-info&#39;&gt;class&lt;/span&gt; \`RegistryProvidableInstance\`&quot;">​</a></h3><p>Base class for objects that can be provided by a registry. This class provides common functionality for registry-managed objects including configuration storage, pretty printing of configuration, and provider registration.</p><p><strong>Parameters:</strong></p><ul><li><strong><code>console</code></strong> (<code>Console</code>) - Rich console instance for output formatting.</li><li><strong><code>config</code></strong> (<code>RegistryInstanceConfig</code>) - Configuration object for this instance.</li></ul><details class="details custom-block"><summary>#### `);
  _push(ssrRenderComponent(_component_Badge, {
    type: "info",
    text: "method"
  }, null, _parent));
  _push(` <span class="text-warning">def</span> <code>__init__(self, config: RegistryInstanceConfig, console: Console | None)</code></summary><p>Initializes the instance with configuration and console. Stores the provided configuration and initializes a Rich Console instance if not provided. Logs the initialization event and pretty-prints the configuration.</p><p><strong>Parameters:</strong></p><ul><li><strong><code>config</code></strong> () - Configuration object for this instance.</li><li><strong><code>console</code></strong> () - Optional Rich Console instance for output formatting. If not provided, a new Console instance will be created.</li></ul></details><details class="details custom-block"><summary>#### `);
  _push(ssrRenderComponent(_component_Badge, {
    type: "info",
    text: "method"
  }, null, _parent));
  _push(` <span class="text-warning">def</span> <code>get_provider_key(cls) -&gt; str</code></summary><p>Return the provider key for the class. This key is used to register and retrieve instances from the registry.</p><p><strong>Returns:</strong> (<code>str</code>) - The class name used as the registry key.</p></details><details class="details custom-block"><summary>#### `);
  _push(ssrRenderComponent(_component_Badge, {
    type: "info",
    text: "method"
  }, null, _parent));
  _push(` <span class="text-warning">def</span> <code>get_description() -&gt; str</code></summary><p>Return a human readable description for the class. This method should be overridden by subclasses to provide specific descriptions. The base implementation returns a default placeholder message.</p><p><strong>Returns:</strong> (<code>str</code>) - Human-readable description of the class.</p></details><hr></div>`);
}
const _sfc_setup = _sfc_main.setup;
_sfc_main.setup = (props, ctx) => {
  const ssrContext = useSSRContext();
  (ssrContext.modules || (ssrContext.modules = /* @__PURE__ */ new Set())).add("en/api/core/mixins.md");
  return _sfc_setup ? _sfc_setup(props, ctx) : void 0;
};
const mixins = /* @__PURE__ */ _export_sfc(_sfc_main, [["ssrRender", _sfc_ssrRender]]);
export {
  __pageData,
  mixins as default
};
