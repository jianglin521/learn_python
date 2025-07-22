import os

# 原始地址
path = r'Z:\download\综艺\城市捉迷藏'
# 移动地址      
newPath = r'Z:\download\综艺\城市捉迷藏'  
#图片重命名
#获取该目录下所有文件，存入列表中
fileList = os.listdir(path)
# fileList.sort(key = lambda x: int(x[:-4]))

for index, name in enumerate(fileList):
    #设置旧文件名（就是路径+文件名）
    oldname= path + os.sep + name   # os.sep添加系统分隔符
   
    #设置新文件名
    tempList = name.split('.mp4')
    # print(tempList)
    newname = tempList[0].replace('.', '-') + '.mp4'
    # newname = f'{tempList[0]}.mp4'
    # newname = newname.replace('集', '')
    newname = newPath + os.sep + newname
    print(newname)

    os.rename(oldname, newname)   #用os模块中的rename方法对文件改名
    print(oldname,'==>',newname, index + 1)
