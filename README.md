# LLM Token Bench

A Python toolkit to benchmark, audit, and compare the real-world performance of major Large Language Models (LLMs).

**LLM Token Bench** goes beyond simple "price per million tokens" sheets. It measures the actual cost of tasks by analyzing **token verbosity** (how chatty a model is), **latency** (time to first byte/total time), and **final cost** across providers like OpenAI, Anthropic, and Google.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

## Key Features

*   **Multi-Provider Support:** Unified wrappers for OpenAI (GPT-4o), Anthropic (Claude 3.5 Sonnet), and Google (Gemini 1.5 Flash).
*   **Real-World Cost Analysis:** Calculates costs based on dynamic pricing configurations.
*   **Latency Tracking:** Measures exactly how long each model takes to respond.
*   **Visualization:** Automatically generates charts to compare Cost vs. Verbosity.
*   **Modular Design:** Easy to add new providers (Groq, Mistral, Azure) in `src/providers.py`.

## Installation

1.  **Clone the repository**
    ```bash
    git clone https://github.com/MastafaF/llm-token-bench.git
    cd llm-token-bench
    ```

2.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure API Keys**
    Create a `.env` file in the root directory:
    ```bash
    cp .env.example .env
    ```
    Open `.env` and add your keys:
    ```text
    OPENAI_API_KEY=sk-...
    ANTHROPIC_API_KEY=sk-ant-...
    GEMINI_API_KEY=...
    ```


##  Visualize Results
Generate comparison charts based on the saved data.
code
Bash
python src/visualize.py
This will generate two images in the data/ folder:
cost_comparison.png
token_efficiency.png


## Project Structure
code
Text
llm-token-bench/
├── data/                  # Stores CSV results and generated PNG charts
├── src/
│   ├── config.py          # Pricing models and test prompts
│   ├── providers.py       # API wrappers (OpenAI, Anthropic, Google)
│   └── visualize.py       # Matplotlib/Seaborn charting scripts
├── main.py                # Entry point for the benchmark
├── requirements.txt       # Project dependencies
└── README.md

## Example Insights
Gemini 1.5 Flash is often the cheapest but can be more verbose (uses more output tokens) than GPT-4o.
Claude 3.5 Sonnet typically offers high-quality reasoning but comes at higher latency and cost.
GPT-4o-mini offers a strong middle ground for speed and conciseness.


## Roadmap

Add Groq integration for ultra-low latency testing.

Implement Github Actions to run daily benchmarks automatically.

Add response quality evaluation using an "LLM-as-a-Judge".


##  Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License
MIT