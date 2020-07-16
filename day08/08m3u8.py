#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import os
from concurrent.futures import ThreadPoolExecutor, wait
import sys

finishedNum = 0
allNum = 0
fileList = []
headers = {
  'Referer': 'https://video.bosum.com.cn/',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0'
}


def download(downloadLink, name):
    global finishedNum
    global allNum
    for _ in range(1):
        try:
            req = requests.get(downloadLink, headers=headers, timeout=15).content
            with open(f"{name}", "wb") as f:
                f.write(req)
                f.flush()
            finishedNum += 1
            print(f"{name}下载成功, 总进度{round(finishedNum / allNum * 100, 2)}% ({finishedNum}/{allNum})")
            break
        except:
            if _ == 9:
                print(f"{name}下载失败")
            else:
                print(f"{name}正在进行第{_}次重试")


def merge_file(path, name):
    global fileList
    cmd = "copy /b "
    for i in fileList:
        if i != fileList[-1]:
            cmd += f"{i} + "
        else:
            cmd += f"{i} {name}"
    os.chdir(path)
    with open('combine.cmd', 'w') as f:
        f.write(cmd)
    os.system("combine.cmd")
    os.system('del /Q *.ts')
    os.system('del /Q *.cmd')


def downloader(url, name, threadNum):
    global allNum
    global fileList
    print("读取文件信息中...")
    downloadPath = 'Download'
    if not os.path.exists(downloadPath):
        os.mkdir(downloadPath)
    # 查看是否存在
    if os.path.exists(f"{downloadPath}/{name}"):
        print(f"视频文件已经存在，如需重新下载请先删除之前的视频文件")
        return
    content = requests.get(url, headers=headers).text.split('\n')
    if "#EXTM3U" not in content[0]:
        raise BaseException(f"非M3U8链接")
    # .m3u8 跳转
    for video in content:
        if ".m3u8" in video:
            if video[0] == '/':
                url = url.split('//')[0] + "//" + url.split('//')[1].split('/')[0] + video
            elif video[:4] == 'http':
                url = video
            else:
                url = url.replace(url.split('/')[-1], video)
            content = requests.get(url, headers=headers).text.split('\n')
    urls = []
    for index, video in enumerate(content):
        if '#EXTINF' in video:
            if content[index + 1][0] == '/':
                downloadLink = url.split('//')[0] + "//" + url.split('//')[1].split('/')[0] + content[index + 1]
            elif content[index + 1][:4] == 'http':
                downloadLink = content[index + 1]
            else:
                downloadLink = url.replace(url.split('/')[-1], content[index + 1])
            urls.append(downloadLink)
    allNum = len(urls)

    
    pool = ThreadPoolExecutor(max_workers=threadNum)
    futures = []
    for index, downloadLink in enumerate(urls):
        # fileList.append(os.path.basename(downloadLink))
        fileList.append(os.path.basename(str(index) + '.ts'))
        futures.append(pool.submit(download, downloadLink, f"{downloadPath}/{os.path.basename(str(index) + '.ts')}"))
    wait(futures)
    print(f"运行完成")
    merge_file(downloadPath, name)
    print(f"合并完成")
    print(f"文件下载成功，尽情享用吧")


if __name__ == '__main__':
    threadNum = 20
    videoUrl = str(sys.argv[1])
    name = str(sys.argv[2])
    # threadNum = int(sys.argv[3])
    downloader(videoUrl, name, threadNum)
