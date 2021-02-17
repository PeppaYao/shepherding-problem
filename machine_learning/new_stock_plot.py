import datetime
import tushare as ts
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # 设置tushare pro的token并获取连接
    ts.set_token('4fb9440af1ccf9c852aa83287ba891ee9af26ffcc4272fbb0918f396')
    pro = ts.pro_api()
    # 设定获取日线行情的初始日期和终止日期
    start_dt = '20200101'
    end_dt = '20210125'

    # 循环获取单个股票的日线行情
    df = pro.daily(ts_code='600519.SH', start_date=start_dt, end_date=end_dt)
    df = df.iloc[::-1]
    df.set_index('trade_date', inplace=True)
    plt.rcParams['font.sans-serif'] = ['SimHei']

    df['close'].plot(title='贵州茅台股价走势图')
    plt.show()
