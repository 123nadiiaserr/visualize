import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Generate random data
np.random.seed(42)
data_1 = {}
data = pd.DataFrame({
    "X": np.arange(1, 11, 2),
    "Y": np.random.randint(10, 100, 10)
})

# Create plots
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
sns.lineplot(x="X", y="Y", data=data, marker="o")
plt.title("Line Plot")

plt.subplot(1, 2, 2)
sns.barplot(x="X", y="Y", data=data)
plt.title("Bar Chart")

plt.show()
