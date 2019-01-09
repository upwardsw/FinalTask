#!usr/binpython3
# -*-coding:UTF-8-*-
import os
import models.FPGrowth as FP
import models.Apriori as A


def run_Apriori(file, minsup):
    # 将数据集导入
    parsedDat = [line.split() for line in open(file).readlines()]
    F = A.apriori(parsedDat, minsup)
    return F


def run_FG_Growth(file, times):
    # 将数据集导入
    parsedDat = [line.split() for line in open(file).readlines()]
    # 对初始集合格式化
    initSet = FP.createInitSet(parsedDat)
    # 构建FP树,并从中寻找出现times次数的项
    myFPtree, myHeaderTab = FP.createTree(initSet, times)
    # 创建一个空列表来保存这些频繁项集
    myFreqList = []
    FP.mineTree(myFPtree, myHeaderTab, times, set([]), myFreqList)
    return myFreqList


if __name__ == '__main__':
    file_path = os.path.join(os.getcwd(), 'data', 'newsread.dat')
    print("Now reading file:{0}".format(file_path))
    A_result = run_Apriori(file_path, 0.17)
    print("Apriori's result:{0}".format(A_result))
    FP_result = run_FG_Growth(file_path, 100000)
    print("FP-Growth's result:{0}".format(FP_result))
