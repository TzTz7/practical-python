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

def main():
    for line in open('Data/portfolio.csv'):
        print(line, end='')
    print("-"*10)
    for line in filematch('Data/portfolio.csv','IBM'):
        print(line, end='')

if __name__ == '__main__':
    main()