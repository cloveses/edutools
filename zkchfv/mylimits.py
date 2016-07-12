from verify import verify_data_str,verify_data_int,verify_data_float

# 以下为可用限制条件参数示例
# {
#     'length_min':3,
#     'length_max':6,
#     'min':0,
#     'max':100,
#     're_exp':r'[ab]',
#     'choices':['A','B'],
# }


seat_number = {
    "length_min":10,
    "length_max":10,
}

subject = {
    'choices':['语文','物理','化学','数学','思想品德','历史','英语'],
}

limits = [{},{},{},{},seat_number,subject,{}]
filters = [verify_data_int,verify_data_str,verify_data_str,verify_data_str,
    verify_data_str,verify_data_str,verify_data_float]
cols_sum = 7
verify_dir = './data'
headline_row_num = 1