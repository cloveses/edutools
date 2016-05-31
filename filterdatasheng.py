from myxl import *

#过滤应届从外省、市、县中途转学生参加中考的应届考生定向学生


# 获取所有转学名单
data_srcs = get_data('source.xls')

# #第2列为身份证号，6列为转入学校，7列为转学类型（确定是否外省、市、县转入）
# 第8列为操作日期 
# 个别学生多次转学，既有其外省、市、县中途转学又有县内转学
# 本程序依据最后一次转学情况判定

data_dict = {}
for d in data_srcs:
    if d[2] not in data_dict:
        data_dict[d[2]] = [d[7],d[6],d[8]]
    else:
        if d[8] > data_dict[d[2]][2]:
            data_dict[d[2]] = [d[7],d[6],d[8]]

# 获取应届生名单
data_yingjie = get_data('yingjie.xls')

resdata = []

for row in data_yingjie:
    if row[2] in data_dict and not data_dict[row[2]][0].startswith('县区内'):
        row.append(data_dict[row[2]][1])
        resdata.append(row)

#写入过滤后的数据        
save_datas_xlsx('rightdata.xlsx',resdata)
