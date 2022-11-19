import os

path = r'Z:\其它\临时文件'      

#图片重命名
#获取该目录下所有文件，存入列表中
fileList = os.listdir(path)
fileList.sort(key = lambda x: int(x[:-4]))

for index, name in enumerate(fileList):
    #设置旧文件名（就是路径+文件名）
    oldname= path + os.sep + name   # os.sep添加系统分隔符
   
    #设置新文件名
    # newname = '{}.mp4'.format(index + 1 + 13282)
    newname = '{}.mp4'.format(int(name[:-4]) - 10000)
    newname = path + os.sep + newname

    # newname = '{}.jpeg'.format(index)
    # newname = path + os.sep + newname

    os.rename(oldname,newname)   #用os模块中的rename方法对文件改名
    print(oldname,'==>',newname, index + 1)
