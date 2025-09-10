import os
from dotenv import load_dotenv
import textwrap

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

from google import genai
from google.genai.types import GenerateContentConfig

INSTRUCTIONS = textwrap.dedent(
    """
    - You are an AI chat assistant focused on answering questions
    about data science tasks and retrieving relevant information.
    - The user is an experienced data scientist who requires quick
    but accurate access to information.
    - Response format should be plain text WITHOUT ANY markdown-like
    formatting unless specified otherwise.
    - Use context and knowledge bases to provide a coherent answer.
    - Responses should NOT be verbose.
    - Minimize length but retain relevant context.
    - Cite sources wherever possible and necessary.
"""
)


class LLMWrapper:
    def __init__(
        self,
        provider="gemini",
        model_name="gemini-2.5-flash",
        api_key=GEMINI_API_KEY,
        temperature: float = 1.0,
        system_instr=INSTRUCTIONS,
    ):
        self.provider = provider.lower()
        self.model_name = model_name
        self.temperature = temperature
        self.api_key = api_key
        self.system_instructions = system_instr

        if self.provider == "gemini":
            if not self.api_key:
                raise ValueError("API key required for Gemini provider")
            self.client = genai.Client(api_key=self.api_key)
        else:
            raise NotImplementedError(
                f"Provider '{self.provider}' not implemented yet."
            )

    def prompt(self, prompt_text, context=None):
        prompt_contents = []
        if context:
            prompt_contents.append(
                f"""
Here's some context that may be useful.
---
{context}
---
Now, answer the following user query."""
            )
        prompt_contents.append(prompt_text)
        if self.provider == "gemini":
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=prompt_contents,
                config=GenerateContentConfig(
                    temperature=self.temperature,
                    system_instruction=self.system_instructions,
                ),
            )
            return response.text
        else:
            raise NotImplementedError(
                f"Provider '{self.provider}' not implemented yet."
            )
