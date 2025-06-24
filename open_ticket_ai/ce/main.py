import logging

import typer
from pyfiglet import Figlet

from open_ticket_ai.ce.app import App
from open_ticket_ai.ce.core.container import DIContainer

cli = typer.Typer()


@cli.callback()
def main(
    verbose: bool = typer.Option(False, "-v", "--verbose", help="INFO-level logging"),
    debug: bool = typer.Option(False, "-d", "--debug", help="DEBUG-level logging"),
):
    """Configure logging based on CLI options."""
    # determine log level
    if debug:
        level = logging.DEBUG
    elif verbose:
        level = logging.INFO
    else:
        level = logging.WARNING

    # configure root logger
    logging.basicConfig(
        level=level,
        format="%(asctime)s %(levelname)-8s %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    logging.getLogger("urllib3").setLevel(logging.WARNING)  # example: quiet noisy libraries


@cli.command()
def start():
    """Initialize the container and start the application."""
    logger = logging.getLogger(__name__)
    f = Figlet(font="slant")
    logger.info("Starting Open Ticket AI")
    print(f.renderText("Open Ticket AI"))
    container = DIContainer()
    app: App = container.get(App)
    app.run()


if __name__ == "__main__":
    cli()
