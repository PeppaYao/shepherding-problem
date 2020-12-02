import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

fig, ax = plt.subplots()

data = {}
labels = np.arange(1, 70)

x70 = [1994.000, 1947.000, 1870.000, 2001.000, 2001.000, 1786.000, 2001.000, 2001.000, 2001.000, 2001.000, 2001.000, 2001.000, 2001.000, 2001.000, 2001.000, 1274.000, 992.000, 2001.000, 1102.000, 990.000, 1347.000, 915.000, 1144.000, 589.000, 1214.000, 587.000, 1057.000, 1031.000, 568.000, 555.000, 951.000, 553.000, 543.000, 539.000, 541.000, 540.000, 538.000, 537.000, 550.000, 550.000, 547.000, 543.000, 533.000, 534.000, 509.000, 513.000, 544.000, 541.000, 531.000, 514.000, 523.000, 515.000, 517.000, 517.000, 500.000, 519.000, 500.000, 504.000, 509.000, 505.000, 496.000, 490.000, 523.000, 511.000, 518.000, 493.000, 491.000, 500.000, 481.000]

data['70'] = x70

df = pd.DataFrame(data, index=labels)


sns.heatmap(df, vmin=0, vmax=2001, cmap="YlGnBu")

ax.set_ylabel('k neighbors')
ax.set_xlabel('the number of sheep')
plt.show()

fig.savefig("E:\\我的坚果云\\latex\\doubleDistSum\\pics\\heatmap70.pdf", dpi=600, format='pdf')