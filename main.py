import os
import pandas as pd
from dotenv import load_dotenv
from src.providers import OpenAIProvider, AnthropicProvider, GoogleProvider
from src.config import PRICING, PROMPTS
from termcolor import colored

load_dotenv()

def calculate_cost(model, input_tok, output_tok):
    if model not in PRICING:
        return 0.0
    rates = PRICING[model]
    input_cost = (input_tok / 1_000_000) * rates['input']
    output_cost = (output_tok / 1_000_000) * rates['output']
    return round(input_cost + output_cost, 6)

def main():
    providers = {
        "gpt-4o-mini": OpenAIProvider(),
        "claude-3-5-sonnet-20240620": AnthropicProvider(),
        "gemini-1.5-flash": GoogleProvider()
    }

    results = []

    print(colored("Starting Benchmark...", "green", attrs=["bold"]))
    
    for prompt_id, prompt in enumerate(PROMPTS):
        print(f"\nProcessing Prompt {prompt_id+1}: {prompt[:30]}...")
        
        for model_name, provider in providers.items():
            try:
                data = provider.generate(prompt, model_name)
                cost = calculate_cost(model_name, data['input_tokens'], data['output_tokens'])
                
                data['cost_usd'] = cost
                data['prompt_snippet'] = prompt[:30]
                results.append(data)
                
                print(f"  ✅ {model_name}: {data['input_tokens']}+{data['output_tokens']} toks | ${cost} | {data['latency']}s")
            except Exception as e:
                print(f"  ❌ {model_name} failed: {e}")

    # Save Results
    df = pd.DataFrame(results)
    os.makedirs("data", exist_ok=True)
    df.to_csv("data/benchmark_results.csv", index=False)
    print(colored("\nResults saved to data/benchmark_results.csv", "cyan"))

if __name__ == "__main__":
    main()
