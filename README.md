这是自己工作中处理数据用到的代码

myxl.py 预定义用来引用的模块文件
mycount.py 对电子表格中数据进行分类统计的代码
dataclear.py 对电子表格中的数据进行清理的代码（验证成绩等级必须为A/B/C之中一种）

将操作归结为三种类型：
1.验证操作：python3 verify.py
  验证配置文件名默认为：mylimits.py
2.合并操作：python3 combinefile.py .
  合并当前目录下所有xls文件
3.统计操作：python3 summary.py resfile.xlsx 0
  统计第0列

依赖第三方模块：xlrd,xlwt,xlsxwriter
