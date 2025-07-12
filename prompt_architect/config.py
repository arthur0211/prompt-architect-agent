# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Configuration module for the Prompt Architect Agent."""

import os
from dataclasses import dataclass
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

@dataclass
class PromptArchitectConfiguration:
    """Configuration for the Prompt Architect Agent."""
    
    # Model configuration
    agent_model: str = "gemini-2.5-pro"
    fallback_model: str = "gemini-2.5-flash"
    
    # Agent configuration
    agent_name: str = "PromptArchitect"
    agent_description: str = "Especialista em arquitetura de prompts que conduz entrevistas estruturadas para criar prompts profissionais de alta qualidade."
    
    # Tool configuration
    max_search_results: int = 10
    request_timeout: int = 10
    
    # API configuration
    gemini_api_key: str = None
    
    def __post_init__(self):
        """Validate configuration after initialization."""
        # Get API key from environment
        self.gemini_api_key = os.getenv('GEMINI_API_KEY')
        
        # Validate required settings
        if not self.gemini_api_key or self.gemini_api_key == 'your_api_key_here':
            raise ValueError(
                "Por favor, configure sua GEMINI_API_KEY no arquivo .env. "
                "A chave API é necessária para o funcionamento do agente."
            )
    
    def to_env_vars(self) -> dict:
        """Convert configuration to environment variables format."""
        return {
            'GEMINI_API_KEY': self.gemini_api_key,
        }

# Set environment variables dynamically (following Google sample pattern)
def configure_environment():
    """Configure environment variables for the ADK."""
    try:
        config = PromptArchitectConfiguration()
        env_vars = config.to_env_vars()
        
        for key, value in env_vars.items():
            if value:
                os.environ.setdefault(key, value)
        
        return config
    except Exception as e:
        raise RuntimeError(f"Erro na configuração do ambiente: {e}")

# Global configuration instance
config = configure_environment()