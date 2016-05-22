import os
import sys
from myxl import merge_files_data

# 参数中指定目录和列标题行数:python3 combinefile.py . 0

if __name__ == '__main__':
    headline_rows = 0
    if len(sys.argv) > 1:
        mdir = sys.argv[1]
        if len(sys.argv) >2:
            headline_rows = int(sys[2])
        res_file = os.path.join(mdir,'resfile.xlsx')
        merge_files_data(mdir,res_file,headline_rows)
        print('Combine files had finished!')
        print('File name is :',res_file)