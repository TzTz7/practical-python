# report.py
#The file Data/portfolio.csv contains a list of stocks in a portfolio.
#In Exercise 1.30, you wrote a function portfolio_cost(filename)
#that read this file and performed a simple calculation.
# 把此前的这些工作整合起来 —— 
# 在你的 report.py 程序中新增几行代码，
# 用于计算投资组合的盈亏（gain/loss）。
# 新增的代码需要结合练习 2.5 中得到的股票列表，
# 以及练习 2.6 中得到的价格字典，计算出该投资组合的当前总价值，
# 以及对应的盈亏金额。
# Exercise 2.4
import csv

def read_portfolio(filename)->list:
    dictionarise = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = dict(zip(headers,row))
            try:
                # price:float = float(record['price'])
                # shares:int = int(record['shares'])
                # name:str = str(record['name'])
                # dictionary['name'] = name
                # dictionary['shares'] = shares
                # dictionary['price'] = price
                dictionary = {
                    'name': record['name'],
                    'shares': int(record['shares']),
                    'price': float(record['price'])
                }
                dictionarise.append(dictionary)
            except ValueError:
                print('coudld not parse', row)
    return dictionarise

def read_prices(filename)->dict:
    dictionary = {}
    headers=['name','price']
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            if not row:
                continue
            try:
                record = dict(zip(headers,row))
                price:float = float(record['price'])
                name:str = str(record['name'])
                dictionary[name] = price
            except ValueError:
                print('coudld not parse', row)
    return dictionary

def make_report(prices:dict,portfolio:list)->list:
    tuples = []
    labels = ['Name','Shares','Price','Change']
    for dict in portfolio:
        new_tuple = (dict['name'], dict['shares'], prices[dict['name']], float(prices[dict['name']]-dict['price']))
        print(new_tuple)
        tuples.append(new_tuple)    

    for i in range(4):
        print(f'{labels[i]:>10}', end=' ')
    print('\n')
    for i in range(4):
        value = ''
        print(f'{value:->10}', end=' ')
    print("\n")

    for name, shares, price, change in tuples:
        print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')
    return tuples

if __name__ == '__main__':
    portfolio = read_portfolio('Data/portfolio.csv') #买时的支数量和价格
    prices = read_prices('Data/prices.csv') # 现在每支股票对应的价格
    # gain:float = 0.0
    # for dict in portfolio:
    #     shares = dict['shares']
    #     name = dict['name']
    #     gain += (prices[name] - dict['price']) * dict['shares']

    # print(f'gain = {gain:0.2f}')
    make_report(prices,portfolio)