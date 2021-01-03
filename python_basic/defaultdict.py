from collections import defaultdict


# 使用字典时，如果所引用的键不存在，就会抛出异常-KeyError，从而导致整个程序终止执行
# defaultdict在键不存在时返回一个默认值
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])  # 不存在的key返回N/A
