from collections import OrderedDict

od = OrderedDict()
od['c'] = 1
od['a'] = 2
od['b'] = 3
print(od)  # key是按照元素插入的顺序来排序的，而不是按照key本身
keys = ['apple', 'banana', 'cat']
values = [4, 5, 6]
od.update(zip(keys, values)) # 向老字典之中追加一个新字典，相当于合并了两个字典
print(od)
od.pop('a')  # 删除
print(od)
od.move_to_end('b')  # 将'b'元素移动到队尾
print(od)
