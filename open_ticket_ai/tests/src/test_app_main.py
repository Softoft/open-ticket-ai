import logging
from unittest.mock import MagicMock

import pytest

from open_ticket_ai.src.ce.app import App, console
from open_ticket_ai.src.ce import main as main_module
import open_ticket_ai.src.ce.app as app_module


class TestAppRun:
    def test_run_validation_passes(self, monkeypatch):
        validator = MagicMock()
        orchestrator = MagicMock()
        app = App(config=MagicMock(), validator=validator, orchestrator=orchestrator)

        # ensure loop exits immediately
        def fake_run_pending():
            raise KeyboardInterrupt()
        monkeypatch.setattr(app_module.schedule, "run_pending", fake_run_pending)
        monkeypatch.setattr(app_module.time, "sleep", lambda x: None)
        print_mock = MagicMock()
        monkeypatch.setattr(console, "print", print_mock)

        with pytest.raises(KeyboardInterrupt):
            app.run()

        validator.validate_registry.assert_called_once()
        orchestrator.set_schedules.assert_called_once()
        print_mock.assert_called_once()

    def test_run_validation_error_logs(self, monkeypatch, caplog):
        validator = MagicMock()
        validator.validate_registry.side_effect = ValueError("bad config")
        orchestrator = MagicMock()
        app = App(config=MagicMock(), validator=validator, orchestrator=orchestrator)

        def fake_run_pending():
            raise KeyboardInterrupt()
        monkeypatch.setattr(app_module.schedule, "run_pending", fake_run_pending)
        monkeypatch.setattr(app_module.time, "sleep", lambda x: None)

        with caplog.at_level(logging.ERROR):
            with pytest.raises(KeyboardInterrupt):
                app.run()

        assert "Configuration validation failed: bad config" in caplog.text
        orchestrator.set_schedules.assert_called_once()


class TestMainModule:
    def test_main_sets_logging_level(self, monkeypatch):
        basic_cfg = MagicMock()
        monkeypatch.setattr(main_module.logging, "basicConfig", basic_cfg)
        monkeypatch.setattr(main_module.logging, "getLogger", lambda name=None: MagicMock())

        main_module.main(verbose=True, debug=False)
        assert basic_cfg.call_args.kwargs["level"] == logging.INFO

    def test_start_creates_container_and_runs_app(self, monkeypatch, capsys):
        app_mock = MagicMock()
        container_mock = MagicMock(get=MagicMock(return_value=app_mock))
        monkeypatch.setattr(main_module, "DIContainer", MagicMock(return_value=container_mock))
        figlet_instance = MagicMock(renderText=MagicMock(return_value="art"))
        monkeypatch.setattr(main_module, "Figlet", MagicMock(return_value=figlet_instance))
        monkeypatch.setattr(main_module.logging, "getLogger", lambda name=None: MagicMock())

        main_module.start()

        container_mock.get.assert_called_once_with(App)
        app_mock.run.assert_called_once()
        captured = capsys.readouterr()
        assert "art" in captured.out

