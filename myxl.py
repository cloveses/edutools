import os
import xlrd
import xlwt

def get_data(filename):
     #既可以打开xls类型的文件，也可以打开xlsx类型的文件
    #w = xlrd.open_workbook('text.xls')
    #w = xlrd.open_workbook('acs.xlsx')
    datas = []
    w = xlrd.open_workbook(filename)
    ws = w.sheets()[0]
    nrows = ws.nrows
    for i in range(nrows):
        data = ws.row_values(i)
        datas.append(ws.row_values(i))
    #    print(datas)
    return datas

def get_files(directory):
    files = []
    files = os.listdir(directory)
    files = [f for f in files if f.endswith('.xls') or f.endswith('.xlsx')]
    return files
    
def save_datas(filename,datas):
    #将一张表的信息写入电子表格中
    #文件内容不能太大，否则输出文件会出错。
    w = xlwt.Workbook(encoding='utf-8')
    ws = w.add_sheet('sheet1')
    for rowi,row in enumerate(datas):
        rr = ws.row(rowi)
        for coli,celld in enumerate(row):
            if isinstance(celld,int):
                rr.set_cell_number(coli,celld)
            else:
                rr.set_cell_text(coli,celld)
    #rr = ws.row(4)
    w.save(filename)

def save_data_sheets(filename,datass,sheetnames):
    #将对应表中的信息列表写入对应的work_sheet中
    #例：datass=[sheet1表的信息列表，sheet2表的信息列表],sheetnames=['sheet1','sheet2']
    #文件内容不能太大，否则输出文件会出错。
    w = xlwt.Workbook(encoding='utf-8')
    sheets = [w.add_sheet(sheetname) for sheetname in sheetnames]
    for ws,datas in zip(sheets,datass):
        for rowi,row in enumerate(datas):
            rr = ws.row(rowi)
            for coli,celld in enumerate(row):
                if isinstance(celld,int):
                    rr.set_cell_number(coli,celld)
                else:
                    rr.set_cell_text(coli,celld)
    w.save(filename)

def test():
    print(get_data('text.xls'))
    print(get_files('.'))
    datas = [(1,'22345433225467755','降解','abc'),
                 (2,'34333333332345345','顺中','cde'),
            (3,'354634324234343566','dddgd','efd')]
    save_datas('ttt.xls',datas)
    datass = [[(1,'22345433225467755','降解','abc'),
                 (2,'34333333332345345','顺中','cde')],[
            (3,'354634324234343566','dddgd','efd'),]]
    save_data_sheets('tttt.xls',datass,['sheet1','sheet2'])
    
def countit(datas):
    from collections import Counter
    c = Counter(datas)
    for k,v in c.items():
        print(k,v,sep='\t')

def save_datas_xlsx(filename,datas):
    #将一张表的信息写入电子表格中XLSX文件格式
    import xlsxwriter
    w = xlsxwriter.Workbook(filename)
    w_sheet = w.add_worksheet('sheet1')
    for rowi,row in enumerate(datas):
        for coli,celld in enumerate(row):
            w_sheet.write(rowi,coli,celld)
    w.close()

def save_data_sheets_xlsx(filename,datass,sheetnames):
    #将对应表中的信息列表写入对应的work_sheet中
    #例：datass=[sheet1表的信息列表，sheet2表的信息列表],sheetnames=['sheet1','sheet2']
    #文件内容不能太大，否则输出文件会出错。
    import xlsxwriter
    w = xlsxwriter.Workbook(filename)

    w = xlwt.Workbook(encoding='utf-8')
    sheets = [w.add_sheet(sheetname) for sheetname in sheetnames]
    for ws,datas in zip(sheets,datass):
        for rowi,row in enumerate(datas):
            for coli,celld in enumerate(row):
                ws.write(rowi,coli,celld)
    w.close()

if __name__ == '__main__':
    # test()
    pass
