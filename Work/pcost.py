# pcost.py
#读取 portfolio.csv 文件（列对应股票名称、持股数量、买入价）
# 计算购买这些股票的总花费。

# Hint: to convert a string to an integer, use int(s)
# To convert a string to a floating point, use float(s).

# Your program should print output such as the following:

# Total cost 44671.15
# Exercise 1.27
f = open('Data/portfolio.csv','rt')
total : float = 0
head = next(f)
for line in f:
    row = line.split(',')
    shares : int = int(row[1])
    price  : float = float(row[2].strip())
    total += shares * price

print(f'Total cost {total:0.2f}',)
f.close()