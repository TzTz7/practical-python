# fileparse.py
#
# Exercise 3.3
import csv
import io
import sys
def parse_csv(rows, 
              select:list=None, 
              types:list=None,
              has_headers:bool=True,
              delimiter:str=',',
              silence_errors=False)->list:
    '''
    Parse a CSV file into a list of records
    '''

    if not has_headers and select:
        raise RuntimeError('select argument requires column headers')
    
    if isinstance(rows, io.IOBase):
        print('io')
        headers = next(rows) if has_headers else []
    elif isinstance(rows, list):
        if has_headers:
            headers = rows[0]
            rows = rows[1:]
    else:
        sys.exit()

    if isinstance(headers, str):
        headers = headers.strip().split(',')

    # with open(filename,'rt') as f:
    # rows = csv.reader(f,delimiter=delimiter)
    
    if select:
        indices = [ headers.index(name) for name in select ]
        headers = select
    
    
    records = []
    for index,row in enumerate(rows,start=1):
        # 跳不过['']
        if not row:
            continue

        # handle row
        row = row.strip().split(delimiter)
        # 跳过['']
        if all(field == '' for field in row):
            continue
        row = [ x.strip('"') for x in row ]
        
        if select: 
            row = [row[index] for index in indices]
        try:
            if types:                        
                row = [ func(val) for func,val in zip(types,row)]

            if has_headers:
                record = dict(zip(headers,row))
            else:
                record = tuple(row)

            records.append(record)
        except Exception as e:
            if not silence_errors:
                print(f'Row {index}: Couldn\'t convert {row}')
                print(f'Row {index}: Reason {e}')

    return records
        

import gzip
if __name__ == '__main__':
    # with gzip.open('Data/portfolio.csv.gz', 'rt') as file:
    #     port = parse_csv(file, types=[str,int,float])
    
    lines = ['name,shares,price', 'AA,100,34.23', 'IBM,50,91.1', 'HPE,75,45.1']
    port = parse_csv(lines, types=[str,int,float])

    # port = parse_csv('Data/portfolio.csv', types=[str,int,float])
    print(port)