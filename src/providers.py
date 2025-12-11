import time
import os
from openai import OpenAI
import anthropic
import google.generativeai as genai

class LLMProvider:
    def generate(self, prompt, model):
        """Returns dict: {'model': str, 'input_tokens': int, 'output_tokens': int, 'latency': float}"""
        raise NotImplementedError

class OpenAIProvider(LLMProvider):
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def generate(self, prompt, model):
        start = time.time()
        response = self.client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}]
        )
        duration = time.time() - start
        
        usage = response.usage
        return {
            "provider": "OpenAI",
            "model": model,
            "input_tokens": usage.prompt_tokens,
            "output_tokens": usage.completion_tokens,
            "latency": round(duration, 4)
        }

class AnthropicProvider(LLMProvider):
    def __init__(self):
        self.client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

    def generate(self, prompt, model):
        start = time.time()
        response = self.client.messages.create(
            model=model,
            max_tokens=1024,
            messages=[{"role": "user", "content": prompt}]
        )
        duration = time.time() - start
        
        return {
            "provider": "Anthropic",
            "model": model,
            "input_tokens": response.usage.input_tokens,
            "output_tokens": response.usage.output_tokens,
            "latency": round(duration, 4)
        }

class GoogleProvider(LLMProvider):
    def __init__(self):
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

    def generate(self, prompt, model):
        start = time.time()
        gemini_model = genai.GenerativeModel(model)
        response = gemini_model.generate_content(prompt)
        duration = time.time() - start
        
        # Gemini requires a separate call or specific field access for token counts 
        # Note: usage_metadata is available in recent SDK versions
        usage = response.usage_metadata
        return {
            "provider": "Google",
            "model": model,
            "input_tokens": usage.prompt_token_count,
            "output_tokens": usage.candidates_token_count,
            "latency": round(duration, 4)
            }
