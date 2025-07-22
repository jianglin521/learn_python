import os
import re
import shutil

def rename_files_by_pattern(directory, regex_pattern, sort_group_index=2, preview=True):
    """
    通用重命名脚本：只更改编号，保留后缀内容
    :param directory: 目标文件夹
    :param regex_pattern: 正则表达式（带编号 + 排序字段 + 剩余文件名）
    :param sort_group_index: 用于排序的正则 group 编号（默认第2组）
    :param preview: 是否只预览，不实际重命名
    """

    pattern = re.compile(regex_pattern, re.IGNORECASE)
    unknown_dir = os.path.join(directory, "未识别")
    os.makedirs(unknown_dir, exist_ok=True)

    all_files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

    matched_files = []
    unmatched_files = []

    for f in all_files:
        m = pattern.match(f)
        if m:
            matched_files.append((f, m))
        else:
            unmatched_files.append(f)

    # 排序：用第 sort_group_index 个 group（通常是日期）
    matched_files.sort(key=lambda x: x[1].group(sort_group_index))

    # 重命名
    for idx, (filename, match) in enumerate(matched_files, 1):
        rest = filename[filename.find('_') + 1:]  # 保留下划线后的所有内容
        new_name = f"{idx:02d}_{rest}"

        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_name)

        if os.path.exists(new_path):
            print(f"⚠️ 已存在：{new_name}，跳过")
            continue

        if preview:
            print(f"📝 [预览] 重命名: {filename} -> {new_name}")
        else:
            os.rename(old_path, new_path)
            print(f"✅ 已重命名: {filename} -> {new_name}")

    # 处理未匹配文件
    for filename in unmatched_files:
        src = os.path.join(directory, filename)
        dst = os.path.join(unknown_dir, filename)
        if preview:
            print(f"📦 [预览] 移动未识别文件: {filename} -> 未识别/")
        else:
            shutil.move(src, dst)
            print(f"📦 已移动未识别文件: {filename} -> 未识别/")

    print(f"\n📁 处理完成：{len(matched_files)} 个文件匹配，{len(unmatched_files)} 个未识别")

def main():
    # target_dir = r"X:\天翼\nas\综艺\五十公里桃花坞 第五季"
    target_dir = r"X:\天翼\nas\综艺\五十公里桃花坞 第五季"

    # ✅ 正则切换这里即可，默认group(2)是排序依据
    # 示例：01_2024-04-26 第1期
    # regex = r'^(\d{2})_(\d{4})-(\d{2})-(\d{2}) (第\d{2}期[上下中]?)[.](mp4|mkv)$'
    # 示例：05_20250110-第1期.mp4
    regex = r'^(\d{2})_(\d{8})期?-(第\d{1,2}期[上下中]?)[.](mp4|mkv)$'



    # ✅ sort_group_index=2 对应 (\d{8}) 日期
    rename_files_by_pattern(target_dir, regex_pattern=regex, sort_group_index=2, preview=True)
    # rename_files_by_pattern(target_dir, regex_pattern=regex, sort_group_index=2, preview=False)

if __name__ == "__main__":
    main()
