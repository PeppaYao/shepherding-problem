# 股票K线图绘制
# 如果当天的收盘价高于开盘价，即当天的价格上涨，称为阳线，通常绘制成红色
# 如果当天的收盘价低于开盘价，即当天的价格下跌，则称为阴线，通常绘制成绿色
# 在美国的股票市场上，反而是用红色代表跌，用绿色代表涨。

# 最高价
# 收盘价
# 开盘价
# 最低价

import datetime
import tushare as ts
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # 设置tushare pro的token并获取连接
    ts.set_token('4fb9440af1ccf9c852aa83287ba891ee9af26ffcc4272fbb0918f396')
    pro = ts.pro_api()
    # 设定获取日线行情的初始日期和终止日期
    start_dt = '20200101'
    end_dt = '20210101'

    # 循环获取单个股票的日线行情
    df = pro.daily(ts_code='000002.SZ', start_date=start_dt, end_date=end_dt)
    df = df.iloc[::-1]
    df.set_index('trade_date', inplace=True)
    plt.rcParams['font.sans-serif'] = ['SimHei']

    df['close'].plot(title='万科股价走势图')
    plt.show()