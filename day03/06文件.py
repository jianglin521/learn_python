# 打开文件
f = open('测试文本.txt', 'w', encoding="utf-8")
#print(list(f)) # 转换为列表
f.seek(0, 0) # 文件起始位置
#print(list(f))

f.write('添加测试文件')
f.close()



