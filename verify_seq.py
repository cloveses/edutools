from myxl import *

datas = get_data_cols('./szsum/resfilea.xlsx')
data_col = datas[1]
res = []
for i in range(173222500001,173222507853):
    if str(i) not in data_col:
        res.append(str(i))
print(res)