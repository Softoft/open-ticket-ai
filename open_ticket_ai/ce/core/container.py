from injector import Injector, Module, provider, singleton, inject, BoundKey

class AppModule(Module):
    def __init__(self, cfg: Config):
        self.cfg = cfg

    def configure(self, binder: Binder):
        missing = [f.key for f in self.cfg.fetchers if f.key not in _FETCHER_REGISTRY]
        if missing:
            raise RuntimeError(f"Unbekannte Fetcher-Keys in config: {missing}")
        binder.bind(Config, to=self.cfg, scope=singleton)
        binder.bind(Injector, to=binder.injector, scope=singleton)
        for fc in self.cfg.fetchers:
            cls = _FETCHER_REGISTRY[fc.key]
            binder.bind(DataFetcher, to=cls, annotated_with=fc.key, scope=singleton)