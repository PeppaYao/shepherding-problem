import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

fig, ax = plt.subplots()

data = {}


x60 = [1604.000, 1234.000, 2001.000, 2001.000, 2001.000, 1769.000, 2001.000, 2001.000, 2001.000, 2001.000, 2001.000, 2001.000, 2001.000, 2001.000, 2001.000, 2001.000, 2001.000, 1836.000, 2001.000, 2001.000, 2001.000, 2001.000, 2001.000, 2001.000, 724.000, 774.000, 723.000, 747.000, 721.000, 701.000, 727.000, 693.000, 704.000, 732.000, 645.000, 662.000, 621.000, 622.000, 594.000, 609.000, 574.000, 578.000, 589.000, 550.000, 564.000, 642.000, 546.000, 549.000, 597.000, 478.000, 613.000, 472.000, 501.000, 571.000, 506.000, 512.000, 523.000, 525.000, 515.000, ]
labels = np.arange(1, 60)

data['60'] = x60
df = pd.DataFrame(data, index=labels)


sns.heatmap(df, vmin=0, vmax=2001, cmap="YlGnBu")

ax.set_ylabel('k neighbors')
ax.set_xlabel('the number of sheep')
plt.show()

fig.savefig("E:\\我的坚果云\\latex\\doubleDistSum\\pics\\heatmap60.pdf", dpi=600, format='pdf')