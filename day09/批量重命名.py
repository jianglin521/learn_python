import os
# path = input('请输入文件路径(结尾加上/)')       
path = r'E:/共享文件/乡村爱情13/'
#获取该目录下所有文件，存入列表中
fileList = os.listdir(path)
print(fileList, '00000')
n = 0
for i in fileList:
    
    #设置旧文件名（就是路径+文件名）
    oldname = path + os.sep + fileList[n]   # os.sep添加系统分隔符
    
    #设置新文件名
    newname = path + os.sep + fileList[n].split('.HD1080P')[0] + '.mp4'
    
    os.rename(oldname,newname)   #用os模块中的rename方法对文件改名
    print(oldname,'======>',newname)
    
    n+=1