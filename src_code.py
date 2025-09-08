import pandas as pd
import matplotlib.pyplot as plt

# Data for Solutions by stc (Six-Month Period Ended 30 June 2025)
data = {
    "Metric": ["Current Ratio", "Debt Ratio", "Profit Margin", "ROE", "ROA"],
    "Value": [1.54, 0.67, 0.154, 0.223, 0.073]  # corrected values
}

df = pd.DataFrame(data)

# Metrics that should be shown as percentages
percent_metrics = ["Debt Ratio", "Profit Margin", "ROE", "ROA"]
df["DisplayValue"] = df.apply(
    lambda x: x["Value"]*100 if x["Metric"] in percent_metrics else x["Value"], axis=1
)

# Plot
fig, ax = plt.subplots(figsize=(10,6))
bars = ax.barh(df["Metric"], df["DisplayValue"], color="steelblue")

# Annotate values
for bar, val, metric in zip(bars, df["DisplayValue"], df["Metric"]):
    if metric in percent_metrics:
        ax.text(bar.get_width()+0.5, bar.get_y()+bar.get_height()/2,
                f"{val:.1f}%", va="center", fontsize=11)
    else:
        ax.text(bar.get_width()+0.05, bar.get_y()+bar.get_height()/2,
                f"{val:.2f}", va="center", fontsize=11)

# Title
ax.set_title("Key Financial Ratios – By stc\nSix-Month Period Ended 30 June 2025",
             fontsize=14, weight="bold")
ax.set_xlabel("Value")
plt.tight_layout()

# Save as PNG
plt.savefig("C:/Users/Dell/Desktop/financial_kpis.png", dpi=300, bbox_inches="tight")
plt.show()
