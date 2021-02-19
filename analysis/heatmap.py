import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

fig, ax = plt.subplots()

data = {}
labels = ['0.8', '0.7', '0.6', '0.5', '0.4', '0.3', '0.2', '0.1'][::-1]

x30 = [2001.000, 1396.000, 2001.000, 464.000, 425.000, 479.000, 570.000, 581.000]
x40 = [2001.000, 1681.000, 2001.000, 450.000, 425.000, 415.000, 399.000, 401.000]
x50 = [2001.000, 2001.000, 2001.000, 573.000, 578.000, 501.000, 516.000, 454.000]
x60 = [1769.000, 2001.000, 1836.000, 2001.000, 701.000, 662.000, 578.000, 549.000]
x70 = [2001.000, 2001.000, 1347.000, 1031.000, 541.000, 543.000, 531.000, 519.000]


data['30'] = x30
data['40'] = x40
data['50'] = x50
data['60'] = x60
data['70'] = x70
df = pd.DataFrame(data, index=labels)


sns.heatmap(df, vmin=0, vmax=2001, cmap="YlGnBu")

ax.set_ylabel('k neighbors')
ax.set_xlabel('the number of sheep')
plt.show()

fig.savefig("E:\\我的坚果云\\latex\\doubleDistSum\\pics\\kneighbor30to70.pdf", dpi=600, format='pdf')