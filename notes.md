### python总结
- python中函数传入的是基本类型，就直接覆盖。如果传入的是引用类型，就会直接修改。
- 字典使用`dicts.get("name", "Jack")`可以防止该key不存在的时候抛出异常。
- map调用后需要使用list转换一下。`res = list(map(lambda x: x*2, data))`
- `for sheep in all_sheep`这样调用是无序的，跟从下标遍历是有区别的。