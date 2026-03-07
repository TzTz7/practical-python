# pcost.py
#读取 portfolio.csv 文件（列对应股票名称、持股数量、买入价）
# 计算购买这些股票的总花费。

# Hint: to convert a string to an integer, use int(s)
# To convert a string to a floating point, use float(s).

# Your program should print output such as the following:

# Total cost 44671.15
# Exercise 1.27
import csv
import sys
def portfolio_cost(filename:str)->float:
    total : float = 0.0
    f = None # 关键：提前初始化f为None，确保变量始终被定义
    try:
        f = open(filename,'rt')
        rows = csv.reader(f)
        headers=next(rows)
        for index,row in enumerate(rows,start=1):
            record = dict(zip(headers,row))
            try:
                shares:int = int(record['shares'])
                price:float = float(record['price'])
                total += shares * price
            except ValueError:
                print('Row',index,': Couldn\'t convert:',row)
    except FileNotFoundError:
        print('No such file or directory: ',filename)
    finally:
        if f:
            f.close()
    return total

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

total = portfolio_cost(filename)
print(f'Total cost {total:0.2f}',)