# FILE_PATH: open_ticket_ai\tests\src\core\test_di_container.py
import unittest
from unittest.mock import MagicMock, patch
from dependency_injector import containers, providers
from open_ticket_ai.src.core.di_container import DIContainer


class TestDIContainer(unittest.TestCase):
    """Test suite for verifying the dependency injection container configuration.

    This class contains tests to ensure that the DI container correctly initializes
    and provides all necessary dependencies with their expected configurations.
    """

    def test_container_initialization(self):
        """Tests that the DI container initializes without errors.

        Verifies that all providers within the container can be initialized
        without raising exceptions.
        """
        container = DIContainer()
        container.config.from_dict({
            "openai_api_key": "test_key",
            "model_name": "test_model",
            "max_tokens": 100,
            "temperature": 0.7,
            "system_prompt": "test_prompt"
        })
        container.init_resources()
        container.wire(modules=[__name__])

    @patch('open_ticket_ai.src.core.di_container.OpenAI')
    def test_llm_service_provider(self, mock_openai):
        """Tests the LLM service provider configuration.

        Verifies that:
        - The provider returns an instance of the correct service class
        - The service is initialized with expected parameters from config

        Args:
            mock_openai (MagicMock): Mock for the OpenAI client class.
        """
        container = DIContainer()
        container.config.from_dict({
            "openai_api_key": "test_key",
            "model_name": "test_model",
            "max_tokens": 100,
            "temperature": 0.7,
            "system_prompt": "test_prompt"
        })

        service = container.llm_service_provider()

        mock_openai.assert_called_once_with(api_key="test_key")
        self.assertEqual(service.model_name, "test_model")
        self.assertEqual(service.max_tokens, 100)
        self.assertEqual(service.temperature, 0.7)
        self.assertEqual(service.system_prompt, "test_prompt")

    @patch('open_ticket_ai.src.core.di_container.OpenAI')
    def test_llm_service_singleton(self, mock_openai):
        """Tests that the LLM service provider returns a singleton instance.

        Verifies that multiple calls to the provider return the same instance.
        """
        container = DIContainer()
        container.config.from_dict({
            "openai_api_key": "test_key",
            "model_name": "test_model",
            "max_tokens": 100,
            "temperature": 0.7,
            "system_prompt": "test_prompt"
        })

        service1 = container.llm_service_provider()
        service2 = container.llm_service_provider()

        self.assertIs(service1, service2)