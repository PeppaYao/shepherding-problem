from datetime import datetime

now = datetime.now()
print(now)
date = datetime(2021, 1, 3, 9, 30)
print(date)
print(date.year)
print(date.month)
print(date.day)
print(date.hour)
print(date.minute)
print(date.second)
# 我们把1970年1月1日称为epoch time记为0
print(date.timestamp())
print(now.strftime("%Y"))
