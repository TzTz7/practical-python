# fileparse.py
#
# Exercise 3.3
import csv
def parse_csv(filename:str, selected:list=None, 
              types:list=None,has_header:bool=True,
              delimiter:str=',')->list:
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename,'rt') as f:
        rows = csv.reader(f,delimiter=delimiter)
        headers = next(rows) if has_header else []
        if selected:
            indices = [ headers.index(name) for name in selected ]
            headers = selected

        records = []
        for row in rows:
            if not row:
                continue
            if selected:
                row = [row[index] for index in indices]
            if types:
                row = [ func(val) for func,val in zip(type,row)]
            if has_header:
                record = dict(zip(headers,row))
            else:
                record = tuple(row)
  
            records.append(record)
    return records
