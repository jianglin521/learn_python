import os
import re

def pad_filenames_recursively(directory):
    for root, _, files in os.walk(directory):
        for filename in files:
            # 匹配文件名中“_”前的数字
            match = re.match(r'(\d+)(_.+)', filename)
            if match:
                number = match.group(1)  # 提取数字部分（字符串）
                rest = match.group(2)    # 获取剩余部分
                # 仅对小于10的数字且未补零的情况进行处理
                if number.isdigit() and int(number) < 10 and not number.startswith("0"):
                    padded_number = f"0{number}"
                    new_filename = f"{padded_number}{rest}"
                    old_path = os.path.join(root, filename)
                    new_path = os.path.join(root, new_filename)

                    # 重命名文件
                    # os.rename(old_path, new_path)
                    # print(f"重命名: {old_path} -> {new_path}")

# 使用示例，替换为你想操作的根目录路径
directory_path = r"Z:\download\下载\综艺"
# directory_path = r"X:\天翼\nas\综艺"
pad_filenames_recursively(directory_path)