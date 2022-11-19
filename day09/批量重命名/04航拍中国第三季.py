import os

# 原始地址
path = r'Z:\download\下载'
# 移动地址      
newPath = r'Z:\download\电视剧\航拍中国\S3'  
#图片重命名
#获取该目录下所有文件，存入列表中
fileList = os.listdir(path)
# fileList.sort(key = lambda x: int(x[:-4]))

for index, name in enumerate(fileList):
    #设置旧文件名（就是路径+文件名）
    oldname = path + os.sep + name   # os.sep添加系统分隔符
  
    #设置新文件名
    tempList = name.split(' ')
    # print(tempList)
    # indexStr = '0' + str(index + 1) if index + 1 < 10 else str(index + 1)
    newname = '航拍中国第三季-{}.mp4'.format(tempList[3] + tempList[4].split('：')[0])
    # newname = newname.replace('E', '')
    newname = newPath + os.sep + newname

    os.rename(oldname, newname)   #用os模块中的rename方法对文件改名
    print(oldname,'==>',newname, index + 1)
