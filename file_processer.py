#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# --------------------------------------------------------
# @Author : ${1:kkutysllb
# @E-mail : libing1@sn.chinamobile.com, 31468130@qq.com
# @Date   : 2024-12-29 01:53
# @Desc   : 文件名处理
# --------------------------------------------------------
"""
import os

def process_file_name(file_path):
    # 获取文件名
    file_name = os.path.basename(file_path)
    # 获取文件名和后缀
    file_name, file_extension = os.path.splitext(file_name)
    file_name = file_name.split("[")[0] + file_extension
    return file_name

def process_directory(directory_path):
    # 获取文件名
    f"""批量处理目录下的所有文件"""
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        if os.path.isfile(file_path):  # 确保是文件而不是目录
            new_file_name = process_file_name(file_path)
            new_file_path = os.path.join(directory_path, new_file_name)
            
            if file_path != new_file_path:  # 只在文件名需要更改时进行重命名
                os.rename(file_path, new_file_path)
                print(f"文件已重命名: {filename} -> {new_file_name}")


if __name__ == "__main__":
   directory_path = "/Users/libing/Downloads/8 数据结构与传统算法"
   process_directory(directory_path)