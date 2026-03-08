import csv
# name shares price
# "AA" 100 32.20
# "IBM" 50 91.10
# "CAT" 150 83.44
# "MSFT" 200 51.23
# "GE" 95 40.37
# "MSFT" 50 65.10
# "IBM" 100 70.44
def toturple(data:str)->tuple:
    '''
        turn '2/2/12' to (2,2,12) 
    '''
    data = data.split('/')
    data = [int(x) for x in data]
    return tuple(data)

with open('Data/dowstocks.csv') as f:
    rows = csv.reader(f) 
    header = next(rows)
    row = next(rows)
    types = [str, float,toturple, str, float, float, float, float, int]
    record =  { name:func(val) for name,func,val in zip(header,types,row)}
    print(record)