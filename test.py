import os
from openpyxl import *

file_path=os.path.join(os.getcwd(),'data')
wb=load_workbook('{0}/onlineretail.xlsx'.format(file_path))
workbench=wb.get_sheet_by_name('Sheet1')



# product=wb.get_sheet_by_name('StockCode')
# customer=wb.get_sheet_by_name('CustomerID')

result=[]
B=[]
G=[]
for i in workbench['B']:
    B.append(i.value)
for j in workbench['G']:
    G.append(j.value)
for index in range(len(B)):
    result.append([B[index],G[index]])
del B
del G
print(result[0:8])

del result[0]

data={}

for m in result:
    if m[1] in data.keys():
        data[m[1]].append(m[0])
    else:
        data[m[1]]=[m[0]]
del result
print(data)

with open('online.dat','a') as f:
    for n in data.keys():
        string=" ".join(str(s) for s in data[n])
        f.writelines(string+'\n')

print('done')









