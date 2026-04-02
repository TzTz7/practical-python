class Stock:
    def __init__(self,name,shares,price):
        self.name = name
        self.shares = shares
        self.price = price
    def cost(self):
        return self.price*self.shares
    
    def sell(self, num):
        self.shares -= num

def main():
    print('class[stock] test')
    b = Stock('AAPL', 50, 122.34)
    a = Stock('GOOG',100,490.10)
    c = Stock('IBM', 75, 91.75)
    s = Stock('GOOG', 100, 490.10)
    print(s.cost())
    s.sell(25)
    print(s.shares)
    print(s.cost()) 

if __name__ == '__main__':
    import sys
    main()