def f1(x):
    return x > 50


data = [66, 15, 77, 88, 23, 90]
filtered = filter(f1, data)  # function中返回true保留
data2 = list(filtered)
print(data2)

# 使用lambda表达式
# filter
data3 = filter(lambda x: x > 50, data)
print(list(data3))
# map
data4 = map(lambda x: x**2, data)
print(list(data4))
# 函数
print((lambda a, b: a*b)(5, 6))
# 统计文章中单词的频率
wordString = """
    it was the best of times it was the worst of times.
    it was the age of wisdom it was the age of foolishness.
"""
wordString = wordString.replace('.', '')
wordList = wordString.split()
wordFreq = dict()
for w in wordList:
    wordFreq[w] = wordFreq.get(w, 0)+1  # 使用dict的get(key, default)
for key, value in wordFreq.items():
    print("{}: {}".format(key, value))
