import os
import pandas as pd

def merge_files_in_directory(input_dir, output_file):
    # 获取目录中所有 CSV 文件的文件名列表
    csv_files = [f for f in os.listdir(input_dir) if f.endswith('.csv')]

    # 按照文件名后缀的数字顺序排序文件列表
    csv_files.sort(key=lambda x: int(x.split('_')[-1].split('.')[0]))

    # 初始化一个空的 DataFrame，用于存储合并后的结果
    merged_df = pd.DataFrame()

    # 逐个读取 CSV 文件并合并
    for csv_file in csv_files:
        file_path = os.path.join(input_dir, csv_file)
        df = pd.read_csv(file_path, sep='\t')
        merged_df = pd.concat([merged_df, df], ignore_index=True)

    # 保存合并后的结果到新文件
    merged_df.to_csv(output_file, sep='\t', index=False)

    print(f'Merged data saved to {output_file}')

# 用户输入目录和输出文件名
input_dir = input('Enter the directory containing CSV files: ')
output_file = input('Enter the name of the output file: ')

# 调用函数进行合并
merge_files_in_directory(input_dir, output_file)
