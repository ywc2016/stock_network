setwd('D:\\workspace_new\\pyhton\\stock_network\\Rscript')

# 画相关系数矩阵图
library(corrplot)



M = read.csv('../coef_matrix_pearson.csv')
corrplot(M)


data(mtcars)
M <- cor(mtcars)
corrplot(M, addCoef.col = "grey")