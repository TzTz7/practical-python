class Stock:
    def __init__(self,name,shares,price):
        self.name = name
        self.shares = shares
        self.price = price
    def cost(self):
        return self.price*self.shares
    
    def sell(self, nshares):
        self.shares -= nshares

class MyStock(Stock):
    def __init__(self,name,shares,price,factor):
        super().__init__(name,shares,price)
        self.factor = factor

    def panic(self):
        self.sell(self.shares)

    def cost(self):
        return self.factor * super().cost()

def main():
    b = Stock('AAPL', 50, 122.34)
    a = Stock('GOOG',100,490.10)
    c = Stock('IBM', 75, 91.75)
    s = MyStock('GOOG', 100, 490.10, 1.25)
    print(s.cost())
    s.sell(25)
    print(s.shares)
    s.panic()
    print(s.shares)

if __name__ == '__main__':
    import sys
    main()