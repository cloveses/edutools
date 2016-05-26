from myxl import *

# 体育成绩分析程序
# 学生体育成绩保存在scores.xls中无(标题行)；
# 第7，9，11，13，15，17列分别为跳远，体前屈，800米，1000米，实心球，跳绳项目成绩
# 其中11，13列满分为20分，其余满分为15分
# 分析要求：总平均分，优，良，及格，不及格的人数及百分比
# 优 90以上 良 80－90 及格 60－80 不及格 60以下
# 过滤掉成绩全为空，（有个别单元格为注释残疾等）
# 输出为：
# 满分为20分的11，13列统计
# 满分为15分的7，9，15，17列统计
# 总评统计最后输出

datacols = get_data_cols('scores.xls')

run_pro = [datacols[11],datacols[13]]
not_run_pro = [datacols[7],datacols[9],datacols[15],datacols[17]]

def switch(cols):
    cols = [d for d in cols if (isinstance(d,str) and d.strip().strip('\n')) or isinstance(d,float)]
    cols = [int(d) for d in cols if (isinstance(d,str) and d.isdigit()) or isinstance(d,float)]
    return cols

run_pro = [switch(ds) for ds in run_pro]
not_run_pro = [switch(ds) for ds in not_run_pro]

def per(total,studs):
    print(studs,studs/total*100,end='\t',sep='\t')

def summary_item(projs,full_score):
    aclass = full_score * 0.9
    bclass = full_score * 0.8
    cclass = full_score * 0.6
    for coldatas in projs:
        all_stus = len(coldatas)
        print(sum(coldatas)/all_stus,end='\t',sep='\t')
        a_data = [d for d in coldatas if d >= aclass]
        b_data = [d for d in coldatas if d < aclass and d >= bclass]
        c_data = [d for d in coldatas if d < bclass and d >= cclass]
        d_data = [d for d in coldatas if d < cclass]
        per(all_stus,len(a_data))
        per(all_stus,len(b_data))
        per(all_stus,len(c_data))
        per(all_stus,len(d_data))
        print()

summary_item(run_pro,20)
summary_item(not_run_pro,15)

datarows = get_data('scores.xls')

def get_score_cells(datarows,colnums):
    res = []
    for rows in datarows:
        datarow = []
        for i in colnums:
            cell_data = rows[i]
            if isinstance(cell_data,str):
                cell_data = cell_data.strip().strip('\n')
                if not cell_data.isdigit():
                    cell_data = ''
            elif isinstance(cell_data,float):
                cell_data = str(cell_data)[:str(cell_data).index('.')]
            else:
                cell_data = ''
            datarow.append(cell_data)
        datarow = [int(d) for d in datarow if d]
        if datarow:
            res.append(datarow)
    return res

scores_row = get_score_cells(datarows,[7,9,11,13,15,17])
scores_everyone = [sum(d) for d in scores_row]

full_score = 50
aclass = full_score * 0.9
bclass = full_score * 0.8
cclass = full_score * 0.6

print(sum(scores_everyone)/len(scores_everyone),end='\t',sep='\t')

a_data = [d for d in scores_everyone if d >= aclass]
b_data = [d for d in scores_everyone if d < aclass and d >= bclass]
c_data = [d for d in scores_everyone if d < bclass and d >= cclass]
d_data = [d for d in scores_everyone if d < cclass]

total = len(scores_everyone)

a_data_ones = len(a_data)
b_data_ones = len(b_data)
c_data_ones = len(c_data)
d_data_ones = len(d_data)

print(a_data_ones,a_data_ones/total*100,end='\t',sep='\t')
print(b_data_ones,b_data_ones/total*100,end='\t',sep='\t')
print(c_data_ones,c_data_ones/total*100,end='\t',sep='\t')
print(d_data_ones,d_data_ones/total*100,sep='\t')
