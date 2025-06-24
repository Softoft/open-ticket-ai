from open_ticket_ai.ce.core.config_models import FetcherConfig
from open_ticket_ai.ce.run.fetchers.data_fetcher import DataFetcher


class BasicTicketFetcher(DataFetcher):
    """BasicTicketFetcher is a data fetcher that retrieves ticket data from a source.
    It is a placeholder for a more complex implementation that would typically
    involve fetching data from a database or an API.
    """

    @staticmethod
    def get_description() -> str:
        return "Basic ticket fetcher that retrieves ticket data from a source. It is a placeholder for a more complex implementation."




    def fetch_data(self, *args, **kwargs):
        """Retrieve ticket data from the configured source."""
        pass
