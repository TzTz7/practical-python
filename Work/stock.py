class Stock:
    def __init__(self,name,shares,price):
        self.name = name
        self.shares = shares
        self.price = price
    def cost(self):
        return self.price*self.shares
    
    def sell(self, nshares):
        self.shares -= nshares

    def __repr__(self):
        return f'Stock({self.name},{self.shares},{self.price})'

class MyStock(Stock):
    def __init__(self,name,shares,price,factor):
        super().__init__(name,shares,price)
        self.factor = factor

    def panic(self):
        self.sell(self.shares)

    def cost(self):
        return self.factor * super().cost()
    
    def __repr__(self):
        return f'MyStock({self.name},{self.shares},{self.price},{self.factor})'

def ChangeStock(Stock):
    def __init__(self,name,shares,price,change):
        super().__init(name,shares,price)
        self.change=change

        
def main():
    b = Stock('AAPL', 50, 122.34)
    a = Stock('GOOG',100,490.10)
    c = Stock('IBM', 75, 91.75)
    s = MyStock('GOOG', 100, 490.10, 1.25)
    print(a)
    print(s)
    cols = ['name','shares']
    for col in cols:
        print(col+'='+str(getattr(a,col)))
    
if __name__ == '__main__':
    import sys
    main()