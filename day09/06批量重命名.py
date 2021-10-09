import os

path = r'C:\Users\92536\Downloads\电影\航拍中国 第一季'      

#获取该目录下所有文件，存入列表中
fileList = os.listdir(path)

for name in fileList:
    #设置旧文件名（就是路径+文件名）
    oldname= path + os.sep + name   # os.sep添加系统分隔符
    
    #设置新文件名
    # newname = '图片{}'.format(int(name[2:]) + 100)
    # newname = path + os.sep + newname
    # print(newname)
    value = oldname.split('.')
    newname = '航拍中国第一季-{}.mp4'.format(value[5][-2:])
    newname = path + os.sep + newname
    print(newname)

    os.rename(oldname,newname)   #用os模块中的rename方法对文件改名
    print(oldname,'==>',newname)
