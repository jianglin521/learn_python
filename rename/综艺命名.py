import os

# 指定要处理的根目录
root_directory = r"X:\天翼\nas\综艺\灿烂的花园"  # 修改为你的根目录路径

def revert_renamed_files(target_dir):
    # 遍历目标目录及其子目录
    for current_dir, _, files in os.walk(target_dir):
        # 获取当前目录名作为参考前缀
        parent_dir_name = os.path.basename(current_dir.rstrip("/\\"))

        for filename in files:
            # 检查文件名中是否包含上级目录名
            if f"_{parent_dir_name}_" in filename:
                # 去除上级目录名，重命名回原始格式
                new_filename = filename.replace(f"_{parent_dir_name}_", "_", 1)
                file_path = os.path.join(current_dir, filename)
                new_file_path = os.path.join(current_dir, new_filename)
                # 重命名文件
                os.rename(file_path, new_file_path)
                print(f"Reverted: {file_path} -> {new_file_path}")

# 运行函数处理指定目录及其子目录
if os.path.isdir(root_directory):
    revert_renamed_files(root_directory)
else:
    print("指定的目录路径无效，请检查路径。")