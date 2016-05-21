import sys
from myxl import summary_col

    # 统计指定电子表格文件中的指定序号列到指定的文件中
    # filename 指定电子表格文件
    # col_seq_num 列序号从0开始
    # w例如：统计文件my.xls,依照第3列
    # python3 summary.py my.xls 2


if len(sys.argv) >=3:
    filename = sys.argv[1]
    col_seq_num = sys.argv[2]
    if col_seq_num.isdigit():
        col_seq_num = int(col_seq_num)
        summary_col(filename,col_seq_num)