import os
from openpyxl import *


def pre_deal(file_name,sheet_name, column1, column2, out_file_name):
    # 导入文件的路径
    file_path = os.path.join(os.getcwd(), 'data')
    # 加载文件并读取工作表
    wb = load_workbook('{0}/{1}'.format(file_path, file_name))
    workbench = wb.get_sheet_by_name(sheet_name)
    print("读取文件成功")

    print("开始读取数据")
    result = []  # 结果列表
    B = []       # column1列表
    G = []       # column2列表
    # 读取column1 的数据
    for i in workbench[column1]:
        B.append(i.value)

    # 读取column2数据
    for j in workbench[column2]:
        G.append(j.value)

    # 合并column1和column2的数据，存入result
    for index in range(len(B)):
        result.append([B[index], G[index]])

    # 释放空间，清除不合格的数据（result[0]为列名）
    del B
    del G
    # print(result[0:8])
    del result[0]

    # 扫描result，将其转变为dict
    data = {}
    for m in result:
        if m[1] in data.keys():
            data[m[1]].append(m[0])
        else:
            data[m[1]] = [m[0]]
    del result
    # print(data)

    #
    print("开始存储数据")
    with open(out_file_name, 'a') as f:
        for n in data.keys():
            string = " ".join(str(s) for s in data[n])
            f.writelines(string + '\n')

    print('转换数据成功')


if __name__=='__main__':
    filename='onlineretail.xlsx'
    sheetname='Sheet1'
    column1='B'
    column2='G'
    outfilename='online.dat'
    print("resource file:{0} sheet:{1} column:{2} {3}".format(filename,sheetname,column1,column2))
    print("out file:{0}".format(outfilename))
    # print("input 'Y' to continue:")
    i=input("input 'Y' to continue,'n' to exit:")
    if i=='Y' or i=='y':
        pre_deal(filename,sheetname,column1,column2,outfilename)
    else:print("exiting")
