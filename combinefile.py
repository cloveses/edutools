import os
from myxl import merge_files_data

# 参数中指定目录:python3 combinefile.py .

if __name__ == '__main__':
    if len(sys.argv) > 1:
        mdir = sys.argv[1]
        res_file = os.path.join(mdir,'resfile.xlsx')
        merge_files_data(mdir,res_file)