import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


data = {'name': [200, 300, 400], 'pay': [400, 500, 600]}
labels = ['0.1N', '0.2N', '0.3N']
df = pd.DataFrame(data, index=labels)

sns.heatmap(df, vmin=0, vmax=600)
plt.show()