import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_results():
    df = pd.read_csv("data/benchmark_results.csv")
    
    # 1. Cost Comparison
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df, x='model', y='cost_usd', hue='provider')
    plt.title("Cost per Task Comparison (USD)")
    plt.ylabel("Cost ($)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("data/cost_comparison.png")
    
    # 2. Token Efficiency (Output Tokens per Prompt)
    # Does one model waffle more than others?
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df, x='model', y='output_tokens', hue='provider')
    plt.title("Verbosity Comparison (Output Tokens)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("data/token_efficiency.png")

if __name__ == "__main__":
    plot_results()

