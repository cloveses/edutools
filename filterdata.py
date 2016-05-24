from myxl import *

#根据源数据过滤不符合条件的数据
#source.xls为比对的源文件（其中的包含正确的数据）
#mydata.xls为上报的需要被过滤的数据文件

#获用于取比对的源数据列：[0]表示第一列
srcs = get_data_cols('source.xls')[0]

#获取需要被过滤的数据文件
datass = get_data('mydata.xls')

# 过滤依据列序号，从0开始
filter_col_seq = 1
#过滤数据类型，防止数据格式不正确
filter_type = str


resdata = []
for datarow in datass:
    #过滤条件
    if isinstance(datarow[filter_col_seq],filter_type)\
        and datarow[filter_col_seq] in srcs:
        resdata.append(datarow)
    else:
        print(datarow)

#写入过滤后的数据        
save_datas_xlsx('rightdata.xlsx',resdata)
