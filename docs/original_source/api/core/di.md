---
description: Learn how Open Ticket AI uses dependency injection to assemble its components at startup.
---
# Dependency Injection

Open Ticket AI relies on a small dependency injection (DI) container to build all
required objects. Every component derives from the `Providable` mixin. The mixin
exposes a `get_provider_key()` class method which is used to reference the
component inside `config.yml`.

During startup the CLI creates a `DIContainer`. The container loads
`config.yml`, builds a `Registry` of all available classes and then instantiates
components whose `provider_key` values appear in the configuration. Adding the
name returned by `get_provider_key()` to the config is therefore enough to make a
component available when the application starts.

The container also offers helper methods such as `get_pipeline()` which creates a
`Pipeline` instance by instantiating each listed pipe through the registry.
