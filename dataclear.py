from myxl import *

datas = get_data('zhsz.xls')

def verifyd(datas):
    for data in datas:
        data = [d.strip('\n').strip() for d in data]
        scores = data[3:]
        for score in scores:
            if score not in ['A','B','C']:
                print(data)
                continue
verifyd(datas)

def cleard(datas):
    rightds = []
    for data in datas:
        data = [d.strip('\n').strip() for d in data]
        rightds.append(data)
    return rightds

datas = cleard(datas)
save_datas_xlsx('clear_zhsz.xlsx',datas)

