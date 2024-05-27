# pcost.py
#
# Exercise 1.27
import csv
import os
dirname = os.path.dirname(__file__)

def find_cost(fileName):
    total_cost = 0.0

    with open(fileName, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:

            try:
                nshares = int(row[1])
                price = float(row[2])
                total_cost += nshares * price
            except ValueError:
                print("couldn't parse", row)

    print('Total cost', total_cost)
    return total_cost

cost = find_cost(dirname + '\\Data\\missing.csv')

with open(dirname + '\\Data\\missing.csv', 'wt') as f:
    print(cost,file = f)