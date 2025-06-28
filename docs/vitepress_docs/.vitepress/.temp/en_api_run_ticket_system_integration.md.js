import { resolveComponent, useSSRContext } from "vue";
import { ssrRenderAttrs, ssrRenderStyle, ssrRenderComponent } from "vue/server-renderer";
import { _ as _export_sfc } from "./plugin-vue_export-helper.1tPrXgE0.js";
const __pageData = JSON.parse('{"title":"Documentation for **/ce/ticket_system_integration/*.py","description":"","frontmatter":{},"headers":[],"relativePath":"en/api/run/ticket_system_integration.md","filePath":"en/api/run/ticket_system_integration.md"}');
const _sfc_main = { name: "en/api/run/ticket_system_integration.md" };
function _sfc_ssrRender(_ctx, _push, _parent, _attrs, $props, $setup, $data, $options) {
  const _component_Badge = resolveComponent("Badge");
  _push(`<div${ssrRenderAttrs(_attrs)}><h1 id="documentation-for-ce-ticket-system-integration-py" tabindex="-1">Documentation for <code>**/ce/ticket_system_integration/*.py</code> <a class="header-anchor" href="#documentation-for-ce-ticket-system-integration-py" aria-label="Permalink to &quot;Documentation for \`**/ce/ticket_system_integration/*.py\`&quot;">​</a></h1><h2 id="module-open-ticket-ai-src-ce-ticket-system-integration-otobo-adapter-py" tabindex="-1">Module: <code>open_ticket_ai\\src\\ce\\ticket_system_integration\\otobo_adapter.py</code> <a class="header-anchor" href="#module-open-ticket-ai-src-ce-ticket-system-integration-otobo-adapter-py" aria-label="Permalink to &quot;Module: \`open_ticket_ai\\src\\ce\\ticket_system_integration\\otobo_adapter.py\`&quot;">​</a></h2><hr><h2 id="module-open-ticket-ai-src-ce-ticket-system-integration-otobo-adapter-config-py" tabindex="-1">Module: <code>open_ticket_ai\\src\\ce\\ticket_system_integration\\otobo_adapter_config.py</code> <a class="header-anchor" href="#module-open-ticket-ai-src-ce-ticket-system-integration-otobo-adapter-config-py" aria-label="Permalink to &quot;Module: \`open_ticket_ai\\src\\ce\\ticket_system_integration\\otobo_adapter_config.py\`&quot;">​</a></h2><hr><h2 id="module-open-ticket-ai-src-ce-ticket-system-integration-ticket-system-adapter-py" tabindex="-1">Module: <code>open_ticket_ai\\src\\ce\\ticket_system_integration\\ticket_system_adapter.py</code> <a class="header-anchor" href="#module-open-ticket-ai-src-ce-ticket-system-integration-ticket-system-adapter-py" aria-label="Permalink to &quot;Module: \`open_ticket_ai\\src\\ce\\ticket_system_integration\\ticket_system_adapter.py\`&quot;">​</a></h2><h3 id="class-ticketsystemadapter" tabindex="-1"><span style="${ssrRenderStyle({})}">class</span> <code>TicketSystemAdapter</code> <a class="header-anchor" href="#class-ticketsystemadapter" aria-label="Permalink to &quot;&lt;span style=&#39;text-info&#39;&gt;class&lt;/span&gt; \`TicketSystemAdapter\`&quot;">​</a></h3><p>An abstract base class for ticket system adapters. This class defines the interface that all concrete ticket system adapters must implement to interact with different ticketing systems. It provides common configuration handling through dependency injection and requires subclasses to implement core ticket operations.</p><p><strong>Parameters:</strong></p><ul><li><strong><code>config</code></strong> (<code>SystemConfig</code>) - System configuration object containing adapter settings.</li></ul><details class="details custom-block"><summary>#### `);
  _push(ssrRenderComponent(_component_Badge, {
    type: "info",
    text: "method"
  }, null, _parent));
  _push(` <span class="text-warning">def</span> <code>__init__(self, config: SystemConfig)</code></summary><p>Initialize the adapter with system configuration. This constructor is automatically injected with the system configuration using the dependency injection framework. It initializes the adapter with the provided configuration and ensures proper setup of inherited components.</p><p><strong>Parameters:</strong></p><ul><li><strong><code>config</code></strong> (<code>SystemConfig</code>) - The system configuration object containing all necessary settings and parameters for the adapter.</li></ul></details><details class="details custom-block"><summary>#### `);
  _push(ssrRenderComponent(_component_Badge, {
    type: "info",
    text: "method"
  }, null, _parent));
  _push(` <span class="text-warning">async def</span> <code>update_ticket(self, ticket_id: str, data: dict) -&gt; dict | None</code></summary><p>Update a ticket in the system. This method must be implemented by concrete adapters to handle updating ticket attributes in the target ticketing system. It should support partial updates and return the updated ticket representation.</p><p><strong>Parameters:</strong></p><ul><li><strong><code>ticket_id</code></strong> () - Unique identifier of the ticket to update.</li><li><strong><code>data</code></strong> () - Dictionary of attributes to update on the ticket.</li></ul><p><strong>Returns:</strong> (<code>Optional[dict]</code>) - The updated ticket object as a dictionary if successful, or None if the update failed or the ticket wasn&#39;t found.</p></details><details class="details custom-block"><summary>#### `);
  _push(ssrRenderComponent(_component_Badge, {
    type: "info",
    text: "method"
  }, null, _parent));
  _push(` <span class="text-warning">async def</span> <code>find_tickets(self, query: dict) -&gt; list[dict]</code></summary><p>Search for tickets matching <code>query</code>. This method must be implemented by concrete adapters to perform complex searches against the target ticketing system. The query structure is adapter-specific but should support common filtering and search operations.</p><p><strong>Parameters:</strong></p><ul><li><strong><code>query</code></strong> () - Dictionary representing the search parameters and filters.</li></ul><p><strong>Returns:</strong> (<code>list[dict]</code>) - A list of ticket objects (as dictionaries) that match the query. Returns an empty list if no matches are found.</p></details><details class="details custom-block"><summary>#### `);
  _push(ssrRenderComponent(_component_Badge, {
    type: "info",
    text: "method"
  }, null, _parent));
  _push(` <span class="text-warning">async def</span> <code>find_first_ticket(self, query: dict) -&gt; dict | None</code></summary><p>Return the first ticket that matches <code>query</code> if any. This is a convenience method that should return the first matching ticket from a search operation. It should optimize for performance by limiting results internally.</p><p><strong>Parameters:</strong></p><ul><li><strong><code>query</code></strong> () - Dictionary representing the search parameters and filters.</li></ul><p><strong>Returns:</strong> (<code>Optional[dict]</code>) - The first matching ticket object as a dictionary, or None if no tickets match the query.</p></details><hr></div>`);
}
const _sfc_setup = _sfc_main.setup;
_sfc_main.setup = (props, ctx) => {
  const ssrContext = useSSRContext();
  (ssrContext.modules || (ssrContext.modules = /* @__PURE__ */ new Set())).add("en/api/run/ticket_system_integration.md");
  return _sfc_setup ? _sfc_setup(props, ctx) : void 0;
};
const ticket_system_integration = /* @__PURE__ */ _export_sfc(_sfc_main, [["ssrRender", _sfc_ssrRender]]);
export {
  __pageData,
  ticket_system_integration as default
};
