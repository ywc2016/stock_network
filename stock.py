# coding:utf-8
import tushare as ts
import pandas as pd
import random
import time
import numpy as np
import math


def read_data():
    sh_stocks = pd.read_csv('sh.csv')
    # 删除第2,3行
    sh_stocks = sh_stocks.drop([0, 1])
    # 删除3以后的奇数列
    col = sh_stocks.columns
    cols_to_remove = []
    for i in range(1, len(col)):
        if i % 2 == 0:
            cols_to_remove.append(col[i])

    sh_stocks = sh_stocks.drop(cols_to_remove, axis=1)
    sh_stocks.to_csv("sh_stocks.csv",
                     index=False, sep=',', encoding="UTF-8")


def preprocessing():
    sh_stocks = pd.read_csv('sh_stocks.csv')
    # 0替换成nan
    sh_stocks = sh_stocks.replace(0, np.nan)
    sh_stocks.to_csv("sh_stocks.csv",
                     index=False, sep=',', encoding="UTF-8")


def relation_coefficient(cor_type='pearson'):
    sh_stocks = pd.read_csv('sh_stocks.csv')
    sh_stocks = sh_stocks.drop(['日期'], axis=1)
    coef_matrix = np.zeros((sh_stocks.shape[1], sh_stocks.shape[1]))
    for i in range(0, sh_stocks.shape[1]):
        for j in range(0, sh_stocks.shape[1]):
            if i == j:
                coef_matrix[i][j] = 1
            elif i < j:
                continue
            else:
                d1 = sh_stocks[sh_stocks.columns[i]]
                d2 = sh_stocks[sh_stocks.columns[j]]
                if (len(d1) != len(d2)):
                    coef_matrix[i][j] = np.nan
                else:
                    D = pd.DataFrame([d1, d2])
                    D = D.dropna(axis=1, how='any')  # 删除有nan的列
                    D = D.transpose()
                    CORR = D.corr(method=cor_type)
                    coef_matrix[j][i] = coef_matrix[i][j] = CORR[CORR.index[0]][1]
    pd.DataFrame(coef_matrix).to_csv("coef_matrix_" + cor_type + ".csv",
                                     index=False, sep=',', encoding="UTF-8")


if __name__ == '__main__':
    print(1)
    # relation_coefficient('spearman')
