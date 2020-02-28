# encoding="utf-8" 设置打开文件编码
f = open('record.txt', encoding="utf-8")

boy = []
girl = []
count = 1
for each_line in f:
  if each_line[:6] != '======':
    # 我们这里进行字符串分割
    # print(each_line, '1111')
    (role, line_spoken) = each_line.split(' ', 1)
    if role == '小甲鱼':
      boy.append(line_spoken)
    if role == '小客服':
      girl.append(line_spoken)
  else:
    # 文件分别保存操作
    file_name_boy = 'boy_' + str(count) + '.txt'
    file_name_girl = 'gile_' + str(count) + '.txt'

    boy_file = open(file_name_boy, 'w', encoding='utf-8')
    girl_file = open(file_name_girl, 'w', encoding='utf-8')

    boy_file.writelines(boy)
    girl_file.writelines(girl)

    boy_file.close()
    girl_file.close()

    boy = []
    girl = []
    #count += 1

# 关闭文件
f.close()
