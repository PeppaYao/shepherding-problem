import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

fig, ax = plt.subplots()

data = {}


x50 = [1411.000, 1462.000, 2001.000, 1989.000, 2001.000, 2001.000, 2001.000, 2001.000, 2001.000, 2001.000, 1924.000, 2001.000, 2001.000, 2001.000, 2001.000, 2001.000, 2001.000, 611.000, 630.000, 573.000, 597.000, 589.000, 616.000, 605.000, 578.000, 710.000, 507.000, 605.000, 532.000, 501.000, 510.000, 525.000, 523.000, 488.000, 516.000, 477.000, 479.000, 502.000, 453.000, 454.000, 445.000, 460.000, 445.000, 428.000, 419.000, 416.000, 412.000, 413.000, 428.000]
labels = np.arange(1, 50)

data['50'] = x50


df = pd.DataFrame(data, index=labels)


sns.heatmap(df, vmin=0, vmax=2001, cmap="YlGnBu")

ax.set_ylabel('k neighbors')
ax.set_xlabel('the number of sheep')
plt.show()

fig.savefig("E:\\我的坚果云\\latex\\doubleDistSum\\pics\\heatmap50.pdf", dpi=600, format='pdf')