import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Example data
data = pd.DataFrame({
    "metrics": ["Monologue", "Dialogue", "Monologue", "Dialogue"],
    "correlation": [74.21, 59.65, 75.88, 77.83],
    "Models": ["DeepSeek-v3", "DeepSeek-v3", "GPT-4o", "GPT-4o"]
})

# Use compact style for papers
sns.set(style="whitegrid", context="paper")
sns.set_context("paper", font_scale=0.9)

plt.rcParams["pdf.fonttype"] = 42
plt.rcParams["ps.fonttype"] = 42

# Create compact bar plot
g = sns.catplot(
    x="metrics", y="correlation", hue="Models",
    data=data, kind="bar",
    palette=sns.color_palette(["#ff4b47", "#678ec4"]),
    width=0.55,
    legend=False
)

g.set_xticklabels(["Monologue", "Dialogue"], fontsize=9)
g.set(ylim=(50, 80))
g.despine(left=True)
g.fig.set_size_inches(3, 1.1)

ax = g.axes.flatten()[0]
ax.set_ylabel("CoNLL F1 score", fontsize=9)
ax.set_xlabel("")

# Custom legend on top
handles = [
    plt.Line2D([0], [0], color="#ff4b47", lw=8),
    plt.Line2D([0], [0], color="#678ec4", lw=8)
]
labels = ["DeepSeek-v3", "GPT-4o"]

g.fig.legend(
    handles, labels,
    loc="upper center",
    bbox_to_anchor=(0.5, 1.18),
    ncol=2,
    frameon=False
)

plt.savefig("genres.pdf", bbox_inches="tight", pad_inches=0.01, format="pdf")
plt.show()
