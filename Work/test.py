def countdown(n):
    while n > 0:
        print("Counting down from ",n)
        yield n
        n -= 1


def filematch(filename, substr):
    with open(filename, 'r') as f:
        for line in f:
            if substr in line:
                yield line

def avg(x, *more):
    return ((x+sum(more))/(1+len(more)))
def func(s):
    return s['name']
def test():
    # Check how the dictionaries are sorted by the `name` key
    l = [
    {'name': 'AA', 'price': 32.2, 'shares': 100},
    {'name': 'CAT', 'price': 83.44, 'shares': 150},
    {'name': 'GE', 'price': 40.37, 'shares': 95},
    {'name': 'IBM', 'price': 91.1, 'shares': 50},
    {'name': 'IBM', 'price': 70.44, 'shares': 100},
    {'name': 'MSFT', 'price': 51.23, 'shares': 200},
    {'name': 'MSFT', 'price': 65.1, 'shares': 50}
    ]

    l.sort(key=lambda s:s['name'])
    print(l)

def add(x, y):
    def do_add():
        # `x` and `y` are defined above `add(x, y)`
        print('Adding', x, y)
        return x + y
    return do_add
def main():
    # import report
    # portfolio = list(report.read_portfolio('Data/portfolio.csv'))
    # portfolio.sort(key=lambda s:s.price)
    # for s in portfolio:
    #     print(s)
    a=add(1,32)
    a()
    print(a)
if __name__ == '__main__':
    main()