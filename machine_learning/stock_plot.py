# 股票数据读取与K线图绘制
import tushare as ts
df = ts.get_k_data('000002',start='2009-01-01', end='2019-01-01')
print(df.head())
