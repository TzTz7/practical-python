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
from fileparse import parse_csv
def read_portfolio(filename)->list:
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    with open(filename) as f:
        
        portfolio_list = parse_csv(f,
                                select=['name','shares','price'],
                                types=[str,int,float],
                                has_headers=True,
                                delimiter=',',
                                silence_errors=False)
        return portfolio_list
    # dictionarise = dict(portfolio)
    # with open(filename, 'rt') as f:
    #     rows = csv.reader(f)
    #     headers = next(rows)
    #     for row in rows:
    #         record = dict(zip(headers,row))
    #         try:
    #             dictionary = {
    #                 'name': record['name'],
    #                 'shares': int(record['shares']),
    #                 'price': float(record['price'])
    #             }
    #             dictionarise.append(dictionary)
    #         except ValueError:
    #             print('coudld not parse', row)
    #return dictionarise

def read_prices(filename)->list:

    with open(filename) as f:

        prices_list = parse_csv(f,
                                types=[str,float],
                                has_headers=False,
                                delimiter=',',
                                silence_errors=False)
        return { x[0]:x[1] for x in prices_list }
    # dictionary = {}
    # headers=['name','price']
    # with open(filename, 'rt') as f:
    #     rows = csv.reader(f)
    #     for row in rows:
    #         if not row:
    #             continue
    #         try:
    #             record = dict(zip(headers,row))
    #             price:float = float(record['price'])
    #             name:str = str(record['name'])
    #             dictionary[name] = price
    #         except ValueError:
    #             print('coudld not parse', row)
    # return dictionary

def make_report(portfolio,prices):
    tuples = []
    for dict in portfolio:
        new_tuple = (dict['name'], 
                     dict['shares'], 
                     prices[dict['name']], 
                     float(prices[dict['name']]-dict['price']))
        tuples.append(new_tuple)    
    return tuples

def print_report(data)->None:
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s'  % headers)
    print(('-' * 10 + ' ') * len(headers))
    for row in data:
        print('%10s %10d %10.2f %10.2f' % row)

def main(argv):
    portfolio = read_portfolio(argv[1])
    prices = read_prices(argv[2])
    report = make_report(portfolio,prices)
    print_report(report)
    print(prices)
if __name__ == '__main__':
    import sys
    main(sys.argv)