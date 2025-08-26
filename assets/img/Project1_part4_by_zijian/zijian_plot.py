import matplotlib.pyplot as plt
import numpy as np

# Generate synthetic data for the curve
x = np.linspace(0, 100, 500)
y = np.exp(-x/20) * 100  # exponentially decaying curve

fig, axs = plt.subplots(1, 2, figsize=(12, 5), sharey=True)

# Common settings for both plots
for ax in axs:
    ax.set_xticks([])  # remove x-axis ticks
    ax.set_yticks([])  # remove y-axis ticks

# Left plot: Data-driven perspective
axs[0].plot(x, y, color="black", linewidth=2)
axs[0].set_title("Data-driven Approach", fontsize=14)
axs[0].set_xlabel("Events", fontsize=12)
axs[0].set_ylabel("Frequency", fontsize=12)

# Add annotations
axs[0].annotate("Common cases", xy=(10, 60), xytext=(20, 80),
                arrowprops=dict(arrowstyle="->", linewidth=1.5))
axs[0].annotate("Corner cases", xy=(70, 1), xytext=(40, 0),
                arrowprops=dict(arrowstyle="->", linewidth=1.5))

# Add dashed augmentation line for corner cases
axs[0].plot([40, 100], [15, 15], "k--")
axs[0].text(60, 7, "Data augmentation",)
axs[0].plot([50, 50], [9, 15], "k--")
axs[0].plot([90, 90], [2, 15], "k--")


# Right plot: Concept-guided perspective
axs[1].plot(x, y, color="black", linewidth=2)
axs[1].set_title("Concept-guided Approach", fontsize=14)
axs[1].set_xlabel("Events", fontsize=12)

# Arrow pointing outward from the curve (concept extraction)
axs[1].annotate("Extract concepts\nfrom common cases", xy=(11, 60), xytext=(60, 70),
                arrowprops=dict(arrowstyle="<-", linewidth=1.5))
axs[1].annotate("", xy=(68,3), xytext=(68, 65),
                arrowprops=dict(arrowstyle="->", linewidth=1.5))
axs[1].text(70, 40, "Instructions\nfor corner cases", fontsize=10)

plt.tight_layout()
# plt.show()

# output到当前文件路径, 命名为concept_learning.png
current_path = __file__.rsplit("/", 1)[0]
plt.savefig(f"{current_path}/concept_learning.png", dpi=300)
plt.close()