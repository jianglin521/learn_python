import os
import zipfile
# import itchat

# 前端打包（入参work_path为项目目录）
def build(work_path):
    # 开始打包
    print('########### run build ############')
    # 打包命令
    cmd = 'npm run build'
    # 切换到需要项目目录
    os.chdir(work_path)
    # 当前项目目录下执行打包命令
    if os.system(cmd) == 0:
        # 打包完成
        print('########### build complete ############')
        zipDir( work_path + r'\dist', r'c:\Users\92536\Desktop\crm.zip')     

def zipDir(dirpath,outFullName):
    """
    压缩指定文件夹
    :param dirpath: 目标文件夹路径
    :param outFullName: 压缩文件保存路径+xxxx.zip
    :return: 无
    """
    zip = zipfile.ZipFile(outFullName,"w",zipfile.ZIP_DEFLATED)
    for path,dirnames,filenames in os.walk(dirpath):
        # 去掉目标跟路径，只对目标文件夹下边的文件及文件夹进行压缩
        fpath = path.replace(dirpath,'')

        for filename in filenames:
            zip.write(os.path.join(path,filename),os.path.join(fpath,filename))
    zip.close()
    print('--------------压缩完成-------------------！')

# 微信登录
# def chat_login():
#   # 登录并获得QR码
#   itchat.auto_login(hotReload=True)
#   # 通过手机扫描QR码登录的微信号给“文件传输助手”发送消息“您好”
#   author = itchat.search_friends(nickName='枪')[0]
#   author.send('邵老板好!我是来自程序')

if __name__ == "__main__":
  work_path = r'd:\WebstormProjects\untitled2\icfo-operation-platform-ui'
  build(work_path)     
