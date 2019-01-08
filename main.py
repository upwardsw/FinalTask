#!usr/binpython3
#-*-coding:UTF-8-*-
import os
import models.FPGrowth as FP
import models.Apriori as A

def run_Apriori(file,minsup):
    # 将数据集导入
    parsedDat = [line.split() for line in open(file).readlines()]
    F = A.apriori(parsedDat, minsup)
    return F

def run_FG_Growth(file,times):
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

if __name__=='__main__':
    datafile=os.path.join(os.getcwd(),'data','newsread.dat')
    print(datafile)
    A_result=run_Apriori(datafile,0.17)
    FP_result=run_FG_Growth(datafile,100000)
    print(A_result)
    print(FP_result)
