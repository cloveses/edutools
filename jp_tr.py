# -*- coding:utf-8 -*- 

from myxl import get_data

datas = get_data('jpx.xls')

addr_b = [i for i in datas if int(i[1]) <= 99]
addr_a = [i for i in datas if int(i[1]) > 99]
# print(addr_a)
seats = [
0,0,0,1,0,0,0,
1,0,1,0,1,0,0,
0,1,0,1,0,1,0,1,
0,0,1,0,0,1,0,0
]

head = 0
tail = -1
for i in range(1,len(addr_a) // 30 + 1):
    for j,flag in enumerate(seats):
        seat = "%03d%02d" % (i,j+1)
        if flag:
            addr_a[tail].append(seat)
            tail = tail - 1
        else:
            addr_a[head].append(seat)
            head += 1
start = head
end = len(addr_a) + tail + 1
print(start,end)
for j,addr in enumerate(range(start,end)):
    print(j,addr)
    seat = "%03d%02d" % (i+1,j+1)
    addr_a[addr].append(seat)

for a in addr_a:
    for l in a:
        print(l,end='\t')
    print()

