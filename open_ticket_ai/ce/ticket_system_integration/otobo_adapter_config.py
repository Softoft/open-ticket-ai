import os

from pydantic import BaseModel


class OTOBOAdapterConfig(BaseModel):
    """
    Configuration model for OTOBO adapter.

    Attributes:
        server_address (str): The base URL of the OTOBO server.
        webservice_name (str): The name of the web service to use.
        search_operation_url (str): The URL for the search operation.
        update_operation_url (str): The URL for the update operation.
        get_operation_url (str): The URL for the get operation.
        username (str): The username for authentication.
        password_env_var (str): The environment variable that contains the password.
    """

    server_address: str
    webservice_name: str
    search_operation_url: str
    update_operation_url: str
    get_operation_url: str
    username: str
    password_env_var: str

    def __str__(self):
        """Return a string representation of the configuration."""

        return (
            f"OTOBOServerConfig(server_address={self.server_address}, "
            f"webservice_name={self.webservice_name}, "
            f"search_operation_url={self.search_operation_url}, "
            f"update_operation_url={self.update_operation_url}, "
            f"get_operation_url={self.get_operation_url}, "
            f"username={self.username})"
        )

    @property
    def password(self) -> str:
        """
        Retrieves the password from the environment variable specified in the configuration.

        Returns:
            str: The password for authentication.
        """
        password = os.getenv(self.password_env_var)
        if not password:
            raise ValueError(f"Environment variable '{self.password_env_var}' is not set.")
        return password
