# 列表 2020-02-27
member = ['小甲鱼', '小布丁', '黑夜', '谜途', '怡静']
print(member, 'member')

# 向末尾添加元素
member.append('福禄娃娃')
print(member, len(member), 'member') # len(member) 列表长度

# 列表扩展
member.extend(['竹林小溪', '降临'])
print(member, 'member')

# 列表插入元素
member.insert(0, '牡丹')
print(member, 'member')

# 元素交换
print(member[0], member[1])
temp = member[0]
member[0] = member[1]
member[1] = temp
print(member, 'member')

# 列表删除元素
member.remove('怡静') # remove
print(member, 'member')

del member[0] # del
# del member 
print(member, 'member')

# pop函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
name = member.pop()
print(member, name)

name = member.pop(0)
print(member, name)

# 列表分片
test1 = member[1:3]
test2 = member[:3]
test3 = member[1:]
test4 = member[:]
#print(test1, test2, test3, test4)

# 列表翻转
member.reverse()
print(member, 'member')




