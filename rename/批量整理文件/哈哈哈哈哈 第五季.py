import os
import re
import shutil
from pathlib import Path

def rename_hnls_files(directory):
    """
    重新编号命名文件
    格式：01_YYYYMMDD期.mp4, 02_YYYYMMDD期.mp4, ...
    未匹配的文件移动到 '未识别' 子文件夹中
    """
    # pattern = re.compile(r'^(\d{2})_(\d{8})(期)?\.mp4$', re.IGNORECASE)
    pattern = re.compile(r'^(\d{2})_(\d{4}-\d{2}-\d{2}) 第\d+期[上下中]?\.mp4$', re.IGNORECASE)

    # 创建未识别目录
    unknown_dir = os.path.join(directory, "未识别")
    os.makedirs(unknown_dir, exist_ok=True)

    all_files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    matched_files = []
    unmatched_files = []

    # 分类匹配与未匹配
    for f in all_files:
        if pattern.match(f):
            matched_files.append(f)
        else:
            unmatched_files.append(f)

    # 按日期排序
    matched_files.sort(key=lambda x: pattern.match(x).group(2))

    # 重命名
    for idx, filename in enumerate(matched_files, 1):
        match = pattern.match(filename)
        new_name = f"{idx:02d}_{match.group(2)}期.mp4"
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_name)

        if os.path.exists(new_path):
            print(f"警告：{new_name} 已存在，跳过重命名")
            continue

        # 实际重命名操作
        os.rename(old_path, new_path)
        print(f"重命名: {old_path} -> {new_name}")

    # 移动未匹配的文件
    for filename in unmatched_files:
        src = os.path.join(directory, filename)
        dst = os.path.join(unknown_dir, filename)
        shutil.move(src, dst)  # 取消注释执行移动
        print(f"移动未识别文件: {filename} -> 未识别/")

    print(f"\n已完成 {len(matched_files)} 个文件的重命名，{len(unmatched_files)} 个未识别文件已移动")

def main():
    # target_dir = r"Z:\download\综艺\哈哈哈哈哈 第五季"
    target_dir = r"X:\天翼\nas\综艺\哈哈哈哈哈 第五季"
    
    if not os.path.exists(target_dir):
        print(f"目录不存在: {target_dir}")
        return

    print(f"开始处理目录: {target_dir}")
    rename_hnls_files(target_dir)

if __name__ == "__main__":
    main()
